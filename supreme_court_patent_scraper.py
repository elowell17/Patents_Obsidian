#!/usr/bin/env python3
"""
Supreme Court Patent Cases Scraper
Scrapes patent cases from Justia Supreme Court database and saves them to desktop
"""

import requests
from bs4 import BeautifulSoup
import os
import re
import time
import urllib.parse
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SupremeCourtPatentScraper:
    def __init__(self, desktop_path=None):
        """Initialize the scraper with desktop path"""
        if desktop_path is None:
            # Get desktop path for macOS
            self.desktop_path = Path.home() / "Desktop"
        else:
            self.desktop_path = Path(desktop_path)
        
        self.base_url = "https://supreme.justia.com"
        self.patent_cases_url = "https://supreme.justia.com/cases-by-topic/patents/"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
        # Create main folder on desktop
        self.output_folder = self.desktop_path / "Supreme_Court_Patent_Cases"
        self.output_folder.mkdir(exist_ok=True)
        
    def clean_filename(self, filename):
        """Clean filename to be filesystem safe"""
        # Remove or replace invalid characters
        filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
        # Remove extra spaces and dashes
        filename = re.sub(r'\s+', ' ', filename).strip()
        filename = re.sub(r'-+', '-', filename)
        # Limit length
        if len(filename) > 200:
            filename = filename[:200]
        return filename
    
    def get_case_links(self):
        """Get all patent case links from the main page"""
        logger.info("Fetching patent case links...")
        
        try:
            response = self.session.get(self.patent_cases_url, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find the main content area with case links
            # Look for links that contain case information
            case_links = []
            
            # Try different selectors to find case links
            selectors = [
                'a[href*="/cases/"]',
                '.case-link a',
                'a[href*="supreme.justia.com/cases/"]',
                'table a',
                '.content a'
            ]
            
            for selector in selectors:
                links = soup.select(selector)
                for link in links:
                    href = link.get('href')
                    if href and '/cases/' in href and href not in [l['href'] for l in case_links]:
                        # Make sure it's a full URL
                        if href.startswith('/'):
                            href = self.base_url + href
                        elif not href.startswith('http'):
                            href = self.base_url + '/' + href
                        
                        case_links.append({
                            'href': href,
                            'title': link.get_text(strip=True) or link.get('title', '')
                        })
            
            logger.info(f"Found {len(case_links)} potential case links")
            return case_links
            
        except Exception as e:
            logger.error(f"Error fetching case links: {e}")
            return []
    
    def extract_case_info(self, soup, url):
        """Extract case information from the case page"""
        case_info = {
            'title': '',
            'citation': '',
            'date': '',
            'decision_text': '',
            'url': url
        }
        
        try:
            # Extract case title
            title_selectors = [
                'h1',
                '.case-title',
                '.title',
                'h2',
                '.case-name'
            ]
            
            for selector in title_selectors:
                title_elem = soup.select_one(selector)
                if title_elem:
                    case_info['title'] = title_elem.get_text(strip=True)
                    break
            
            # Extract citation
            citation_selectors = [
                '.citation',
                '.case-citation',
                '.docket-number',
                '.case-number'
            ]
            
            for selector in citation_selectors:
                citation_elem = soup.select_one(selector)
                if citation_elem:
                    case_info['citation'] = citation_elem.get_text(strip=True)
                    break
            
            # Extract date
            date_selectors = [
                '.date',
                '.case-date',
                '.decision-date',
                'time'
            ]
            
            for selector in date_selectors:
                date_elem = soup.select_one(selector)
                if date_elem:
                    case_info['date'] = date_elem.get_text(strip=True)
                    break
            
            # Extract decision text - this is the main content
            decision_selectors = [
                '.decision',
                '.opinion',
                '.case-opinion',
                '.content',
                '.case-content',
                'article',
                '.main-content'
            ]
            
            for selector in decision_selectors:
                decision_elem = soup.select_one(selector)
                if decision_elem:
                    # Remove navigation, headers, footers, etc.
                    for unwanted in decision_elem.select('nav, header, footer, .navigation, .sidebar, .ads'):
                        unwanted.decompose()
                    
                    case_info['decision_text'] = decision_elem.get_text(strip=True)
                    break
            
            # If no specific decision section found, try to get main content
            if not case_info['decision_text']:
                main_content = soup.select_one('main, .main, #main, .content')
                if main_content:
                    # Remove unwanted elements
                    for unwanted in main_content.select('nav, header, footer, .navigation, .sidebar, .ads, .menu'):
                        unwanted.decompose()
                    case_info['decision_text'] = main_content.get_text(strip=True)
            
        except Exception as e:
            logger.error(f"Error extracting case info: {e}")
        
        return case_info
    
    def save_case_to_markdown(self, case_info):
        """Save case information to a markdown file"""
        if not case_info['title']:
            logger.warning("No title found for case, skipping...")
            return False
        
        # Create safe filename
        safe_title = self.clean_filename(case_info['title'])
        
        # Create markdown file directly in the output folder
        markdown_file = self.output_folder / f"{safe_title}.md"
        
        # Prepare markdown content
        markdown_content = f"""# {case_info['title']}

## Case Information

- **Citation**: {case_info['citation']}
- **Date**: {case_info['date']}
- **Source**: [Justia Supreme Court]({case_info['url']})

## Decision

{case_info['decision_text']}

---
*This document was automatically generated from the Justia Supreme Court database.*
"""
        
        try:
            with open(markdown_file, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            
            logger.info(f"Saved case: {case_info['title']}")
            return True
            
        except Exception as e:
            logger.error(f"Error saving case {case_info['title']}: {e}")
            return False
    
    def scrape_case(self, case_link):
        """Scrape individual case page"""
        try:
            logger.info(f"Scraping case: {case_link['title']}")
            
            response = self.session.get(case_link['href'], timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract case information
            case_info = self.extract_case_info(soup, case_link['href'])
            case_info['title'] = case_info['title'] or case_link['title']
            
            # Save to markdown
            success = self.save_case_to_markdown(case_info)
            
            # Be respectful with delays
            time.sleep(1)
            
            return success
            
        except Exception as e:
            logger.error(f"Error scraping case {case_link['href']}: {e}")
            return False
    
    def run(self):
        """Main method to run the scraper"""
        logger.info("Starting Supreme Court Patent Cases Scraper")
        logger.info(f"Output folder: {self.output_folder}")
        
        # Get all case links
        case_links = self.get_case_links()
        
        if not case_links:
            logger.error("No case links found. The website structure may have changed.")
            return
        
        logger.info(f"Found {len(case_links)} cases to scrape")
        
        # Scrape each case
        successful_scrapes = 0
        for i, case_link in enumerate(case_links, 1):
            logger.info(f"Processing case {i}/{len(case_links)}")
            
            if self.scrape_case(case_link):
                successful_scrapes += 1
            
            # Progress update
            if i % 10 == 0:
                logger.info(f"Progress: {i}/{len(case_links)} cases processed")
        
        logger.info(f"Scraping completed! Successfully scraped {successful_scrapes}/{len(case_links)} cases")
        logger.info(f"Files saved to: {self.output_folder}")

def main():
    """Main function"""
    scraper = SupremeCourtPatentScraper()
    scraper.run()

if __name__ == "__main__":
    main() 