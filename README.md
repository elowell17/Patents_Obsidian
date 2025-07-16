# Supreme Court Patent Cases Scraper

This Python script scrapes Supreme Court patent cases from the Justia website and saves them to your desktop in organized folders with markdown files.

## Features

- Scrapes all patent cases from https://supreme.justia.com/cases-by-topic/patents/
- Creates a folder for each case on your desktop
- Saves case information in markdown format
- Includes case title, citation, date, and full decision text
- Respectful web scraping with delays between requests
- Comprehensive error handling and logging

## Installation

1. Make sure you have Python 3.7+ installed
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Simply run the script:

```bash
python supreme_court_patent_scraper.py
```

The script will:
1. Create a folder called "Supreme_Court_Patent_Cases" on your desktop
2. Scrape all patent cases from the Justia website
3. Save each case as a markdown file named after the case
4. Each markdown file contains:
   - Case title
   - Citation
   - Date
   - Full decision text
   - Source URL

## Output Structure

```
Desktop/
└── Supreme_Court_Patent_Cases/
    ├── Case Name 1.md
    ├── Case Name 2.md
    └── ...
```

## Requirements

- Python 3.7+
- requests
- beautifulsoup4
- lxml

## Notes

- The script includes a 1-second delay between requests to be respectful to the website
- All files are saved with UTF-8 encoding
- Filenames are automatically cleaned to be filesystem-safe
- The script includes comprehensive logging to track progress and any errors

## Legal Notice

This script is for educational and research purposes. Please respect the website's terms of service and robots.txt file. The script includes reasonable delays to avoid overwhelming the server.

## Troubleshooting

If you encounter issues:

1. Check your internet connection
2. Verify the website is accessible
3. Check the console output for error messages
4. Ensure you have the required permissions to write to your desktop

## Customization

You can modify the script to:
- Change the output location by modifying the `desktop_path` parameter
- Adjust the delay between requests
- Modify the markdown template
- Add additional case information fields 