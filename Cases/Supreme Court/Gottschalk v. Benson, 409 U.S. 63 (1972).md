# Gottschalk v. Benson, 409 U.S. 63 (1972)

## Case Information

- **Citation**: 
- **Date**: 
- **Source**: [Justia Supreme Court](https://supreme.justia.com/cases/federal/us/409/63/)

## Decision

Gottschalk v. Benson, 409 U.S. 63 (1972)OverviewOpinionsMaterialsArgued:October 16, 1972Decided:November 20, 1972SyllabusU.S. Supreme CourtGottschalk v. Benson, 409 U.S. 63
(1972)Gottschalk v. BensonNo. 71-485Argued October 16,
1972Decided November 20,
1972409 U.S. 63SyllabusRespondents' method for converting numerical information from
binary-coded decimal numbers into pure binary numbers, for use in
programming conventional general purpose digital computers, is
merely a series of mathematical calculations or mental steps, and
does not constitute a patentable "process" within the meaning of
the Patent Act, 35 U.S.C. § 100(b). Pp.409 U. S.
64-73.___ C.C.P.A. (Pat.) ___, 441 F.2d 682, reversed.DOUGLAS, J., delivered the opinion of the Court, in which all
members joined except STEWART, BLACKMUN, and POWELL, JJ., who took
no part in the consideration or decision of the case.Page 409 U. S. 64Read MoreOpinionsOpinions & DissentsU.S. Supreme CourtGottschalk v. Benson,409 U.S.
63(1972)Gottschalk v. BensonNo. 71-485Argued October 16,
1972Decided November 20,
1972409 U.S.
63CERTIORARI TO THE UNITED STATES
COURTOF CUSTOMS AND PATENT
APPALSSyllabusRespondents' method for converting numerical information from
binary-coded decimal numbers into pure binary numbers, for use in
programming conventional general purpose digital computers, is
merely a series of mathematical calculations or mental steps, and
does not constitute a patentable "process" within the meaning of
the Patent Act, 35 U.S.C. § 100(b). Pp.409 U. S.
64-73.___ C.C.P.A. (Pat.) ___, 441 F.2d 682, reversed.DOUGLAS, J., delivered the opinion of the Court, in which all
members joined except STEWART, BLACKMUN, and POWELL, JJ., who took
no part in the consideration or decision of the case.Page 409 U. S. 64MR. JUSTICE DOUGLAS delivered the opinion of the Court.Respondents filed in the Patent Office an application for an
invention which was described as being related "to the processing
of data by program and more particularly to the programmed
conversion of numerical information" in general purpose digital
computers. They claimed a method for converting binary-coded
decimal (BCD) numerals into pure binary numerals. The claims were
not limited to any particular art or technology, to any particular
apparatus or machinery, or to any particular end use. They
purported to cover any use of the claimed method in a general
purpose digital computer of any type. Claims 8 and 13 [Footnote 1] were rejected by the Patent
Office but sustained by the Court of Customs and Patent Appeals,
C.C.P.A. (Pat.) , 441 F.2d 682. The case is here on a petition for
a writ of certiorari. 405 U.S. 915.The question is whether the method described and claimed is a
"process" within the meaning of the Patent Act. [Footnote 2]Page 409 U. S. 65A digital computer, as distinguished from an analog computer,
operates on data expressed in digits, solving a problem by doing
arithmetic as a person would do it by head and hand. [Footnote 3] Some of the digits are stored as
components of the computer. Others are introduced into the computer
in a form which it is designed to recognize. The computer operates
then upon both new and previously stored data. The general purpose
computer is designed to perform operations under many different
programs.The representation of numbers may be in the form of a time
series of electrical impulses, magnetized spots on the surface of
tapes, drums, or discs, charged spots on cathode-ray tube screens,
the presence or absence of punched holes on paper cards, or other
devices. The method or program is a sequence of coded instructions
for a digital computer.The patent sought is on a method of programming a general
purpose digital computer to convert signals from binary-coded
decimal form into pure binary form. A procedure for solving a given
type of mathematical problem is known as an "algorithm." The
procedures set forth in the present claims are of that kind; that
is to say, they are a generalized formulation for programs to solve
mathematical problems of converting one form of numerical
representation to another. From the generic formulation, programs
may be developed as specific applications.Page 409 U. S. 66The decimal system uses as digits the 10 symbols 0, 1, 2, 3, 4,
5, 6, 7, 8, and 9. The value represented by any digit depends, as
it does in any positional system of notation, both on its
individual value and on its relative position in the numeral.
Decimal numerals are written by placing digits in the appropriate
positions or columns of the numerical sequence,i.e.,"unit" (10^0), "tens" (10^1), "hundreds" (10^2), "thousands"
(10^3), etc. Accordingly, the numeral 1492 signifies (1 x 10^3)+(4
x 10^2)+(9 x 10^1)+(2 x 10^0).The pure binary system of positional notation uses two symbols
as digits -- 0 and 1, placed in a numerical sequence with values
based on consecutively ascending powers of 2. In pure binary
notation, what would be the tens position is the twos position;
what would be hundreds position is the fours position; what would
be the thousands position is the eights. Any decimal number from 0
to 10 can be represented in the binary system with four digits or
positions as indicated in the following table.Shown as the sum of powers of 22^3 2^2 2^1 2^0Decimal (8) (4) (2) (1) Pure Binary0 = 0 0 0 0 = 00001 = 0 0 0 2^0 = 00012 = 0 0 2^1 0 = 00103 = 0 0 2^1 2^0 = 00114 = 0 2^2 0 0 = 01005 = 0 2^2 0 2^0 = 01016 = 0 2^2 2^1 0 = 01107 = 0 2^2 2^1 2^0 = 01118 = 2^3 0 0 0 = 10009 = 2^3 0 0 2^0 = 100110 = 2^3 0 2^1 0 = 1010The BCD system using decimal numerals replaces the character for
each component decimal digit in the decimal numeral with the
corresponding four-digit binaryPage 409 U. S. 67numeral, shown in the right-hand column of the table. Thus,
decimal 53 is represented as 0101 0011 in BCD, because decimal 5 is
equal to binary 0101 and decimal 3 is equivalent to binary 0011. In
pure binary notation, however, decimal 53 equals binary 110101. The
conversion of BCD numerals to pure binary numerals can be done
mentally through use of the foregoing table. The method sought to
be patented varies the ordinary arithmetic steps a human would use
by changing the order of the steps, changing the symbolism for
writing the multiplier used in some steps, and by taking subtotals
after each successive operation. The mathematical procedures can be
carried out in existing computers long in use, no new machinery
being necessary. And, as noted, they can also be performed without
a computer.The Court stated inMackay Co. v. Radio Corp.,306 U. S. 86,306 U. S. 94,
that,"[w]hile a scientific truth, or the mathematical expression of
it, is not a patentable invention, a novel and useful structure
created with the aid of knowledge of scientific truth may be."That statement followed the longstanding rule that "[a]n idea,
of itself, is not patentable."Rubber-Tip Pencil Co. v.
Howard,20 Wall. 498,87 U. S. 507."A principle, in the abstract, is a fundamental truth; an
original cause; a motive; these cannot be patented, as no one can
claim in either of them an exclusive right."Le Roy v.
Tatham,14 How. 156,55 U. S. 175.
Phenomena of nature, though just discovered, mental processes, and
abstract intellectual concepts are not patentable, as they are the
basic tools of scientific and technological work. As we stated inFunk Bros. Seed Co. v. Kalo Co.,333 U.
S. 127,333 U. S.
130,"He who discovers a hitherto unknown phenomenon of nature has no
claim to a monopoly of it which the law recognizes. If there is to
be invention from such a discovery, it must come from the
application of the law of nature to a new and useful end."We dealt there with a "product" claim, while thePage 409 U. S. 68present case deals with a "process" claim. But we think the same
principle applies.Here the "process" claim is so abstract and sweeping as to cover
both known and unknown uses of the BCD to pure binary conversion.
The end use may (1) vary from the operation of a train to
verification of drivers' licenses to researching the law books for
precedents and (2) be performed through any existing machinery or
future-devised machinery or without any apparatus.InO'Reilly v.
Morse,15 How. 62, Morse was allowed a patent for a
process of using electromagnetism to produce distinguishable signs
for telegraphy.Id.at56 U. S. 111.
But the Court denied the eighth claim in which Morse claimed the
use of "electro magnetism, however developed for marking or
printing intelligible characters, signs, or letters, at any
distances."Id.at56 U. S. 112.
The Court, in disallowing that claim, said,"If this claim can be maintained, it matters not by what process
or machinery the result is accomplished. For aught that we now
know, some future inventor, in the onward march of science, may
discover a mode of writing or printing at a distance by means of
the electric or galvanic current, without using any part of the
process or combination set forth in the plaintiff's specification.
His invention may be less complicated -- less liable to get out of
order -- less expensive in construction, and in its operation. But
yet, if it is covered by this patent, the inventor could not use
it, nor the public have the benefit of it, without the permission
of this patentee."Id.at56 U. S.
113.InThe Telephone Cases,126 U. S.
1,126 U. S. 534,
the Court explained the Morse case as follows."The effect of that decision was, therefore, that the use of
magnetism as a motive power, without regard to the particular
process with which it was connected in the patent, could not be
claimed, but that its use in that connection could."Bell's invention was the use of electric current to transmitPage 409 U. S. 69vocal or other sounds. The claim was not"for the use of a current of electricity in its natural state as
it comes from the battery, but for putting a continuous current in
a closed circuit into a certain specified condition suited to the
transmission of vocal and other sounds, and using it in that
condition for that purpose."Ibid.The claim, in other words, was not "one for the
use of electricity distinct from the particular process with which
it is connected in his patent."Id.at126 U. S. 535.
The patent was for that use of electricity "both for the magneto
and variable resistance methods."Id.at126 U. S. 538.
Bell's claim, in other words, was not one for all telephonic use of
electricity.InCorning v.
Burden,15 How. 252,56 U. S.
267-268, the Court said,"One may discover a new and useful improvement in the process of
tanning, dyeing, etc., irrespective of any particular form of
machinery or mechanical device."The examples given were the "arts of tanning, dyeing, making
waterproof cloth, vulcanizing India rubber, smelting ores."Id.at56 U. S. 267.
Those are instances, however, where the use of chemical substances
or physical acts, such as temperature control, changes articles or
materials. The chemical process or the physical acts which
transform the raw material are, however, sufficiently definite to
confine the patent monopoly within rather definite bounds.Cochrane v. Deener,94 U. S. 780,
involved a process for manufacturing flour so as to improve its
quality. The process first separated the superfine flour and then
removed impurities from the middlings by blasts of air, reground
the middlings, and then combined the product with the superfine.Id.at94 U. S. 785.
The claim was not limited to any special arrangement of machinery.Ibid.The Court said,"That a process may be patentable, irrespective of the
particular form of the instrumentalities used,Page 409 U. S. 70cannot be disputed. If one of the steps of a process be that a
certain substance is to be reduced to a powder, it may not be at
all material what instrument or machinery is used to effect that
object, whether a hammer, a pestle and mortar, or a mill. Either
may be pointed out; but if the patent is not confined to that
particular tool or machine, the use of the others would be an
infringement, the general process being the same. A process is a
mode of treatment of certain materials to produce a given result.
It is an act, or a series of acts, performed upon the subject
matter to be transformed and reduced to a different state or
thing."Id.at94 U. S.
787-788.Transformation and reduction of an article "to a different state
or thing" is the clue to the patentability of a process claim that
does not include particular machines. So it is that a patent in the
process of "manufacturing fat acids and glycerine from fatty bodies
by the action of water at a high temperature and pressure" was
sustained inTilghman v. Proctor,102 U.
S. 707,102 U. S. 721.
The Court said,"The chemical principle or scientific fact upon which it is
founded is that the elements of neutral fat require to be severally
united with an atomic equivalent of water in order to separate from
each other and become free. This chemical fact was not discovered
by Tilghman. He only claims to have invented a particular mode of
bringing about the desired chemical union between the fatty
elements and water."Id.at102 U. S.
729.Expanded Metal Co. v. Bradford,214 U.
S. 366, sustained a patent on a "process" for expanding
metal. A process "involving mechanical operations, and producing a
new and useful result,"id.at214 U. S.
385-386, was held to be a patentable process, process
patents not being limited to chemical action.Smith v. Snow,294 U. S. 1, andTaxham v. Smith,294 U. S. 20,
involved a process for setting eggs in staged incubationPage 409 U. S. 71and applying mechanically circulated currents of air to the
eggs. The Court, in sustaining the function performed (the hatching
of eggs) and the means or process by which that is done, said:"By the use of materials in a particular manner, he secured the
performance of the function by a means which had never occurred in
nature, and had not been anticipated by the prior art; this is a
patentable method or process. . . . A method which may be patented
irrespective of the particular form of the mechanism which may be
availed of for carrying it into operation is not to be rejected as
'functional' merely because the specifications show a machine
capable of using it."294 U.S. at294 U. S.
22.It is argued that a process patent must either be tied to a
particular machine or apparatus or must operate to change articles
or materials to a "different state or thing." We do not hold that
no process patent could ever qualify if it did not meet the
requirements of our prior precedents. It is said that the decision
precludes a patent for any program servicing a computer. We do not
so hold. It is said that we have before us a program for a digital
computer but extend our holding to programs for analog computers.
We have, however, made clear from the start that we deal with a
program only for digital computers. It is said we freeze process
patents to old technologies, leaving no room for the revelations of
the new, onrushing technology. Such is not our purpose. What we
come down to, in a nutshell, is the following.It is conceded that one may not patent an idea. But, in
practical effect, that would be the result if the formula for
converting BCD numerals to pure binary numerals were patented in
this case. The mathematical formula involved here has no
substantial practical application except in connection with a
digital computer, whichPage 409 U. S. 72means that, if the judgment below is affirmed, the patent would
wholly preempt the mathematical formula and, in practical effect,
would be a patent of the algorithm itself.It may be that the patent laws should be extended to cover these
programs, a policy matter to which we are not competent to speak.
The President's Commission on the Patent System [Footnote 4] rejected the proposal that these
programs be patentable: [Footnote
5]"Uncertainty now exists as to whether the statute permits a
valid patent to be granted on programs. Direct attempts to patent
programs have been rejected on the ground of nonstatutory subject
matter. Indirect attempts to obtain patents and avoid the
rejection, by drafting claims as a process, or a machine or
components thereof programmed in a given manner, rather than as a
program itself, have confused the issue further, and should not be
permitted.""The Patent Office now cannot examine applications for programs
because of a lack of a classification technique and the requisite
search files. Even if these were available, reliable searches would
not be feasible or economic because of the tremendous volume of
prior art being generated. Without this search, the patenting of
programs would be tantamount to mere registration, and the
presumption of validity would be all but nonexistent.""It is noted that the creation of programs has undergone
substantial and satisfactory growth in the absence of patent
protection, and that copyright protection for programs is presently
available. "Page 409 U. S. 73If these programs are to be patentable, [Footnote 6] considerable problems are raised which only
committees of Congress can manage, for broad powers of
investigation are needed, including hearings which canvass the wide
variety of views which those operating in this field entertain. The
technological problems tendered in the many briefs before us
[Footnote 7] indicate to us
that considered action by the Congress is needed.Reversed.MR. JUSTICE STEWART, MR. JUSTICE BLACKMUN, and MR. JUSTICE
POWELL took no part in the consideration or decision of this
case.|409 U.S.
63app|APPENDIX TO OPINION OF THE COURTClaim 8 reads:"The method of converting signals from binary coded decimal form
into binary which comprises the steps of""(1) storing the binary coded decimal signals in a reentrant
shift register,""(2) shifting the signals to the right by at least three places,
until there is a binary '1' in the second position of said
register,""(3) masking out said binary '1' in said second position of said
register,""(4) adding a binary '1' to the first position of said
register,""(5) shifting the signals to the left by two positions, "Page 409 U. S. 74"(7) shifting the signals to the right by at least three
positions in preparation for a succeeding binary '1' in the second
position of said register."Claim 13 reads:"A data processing method for converting binary coded decimal
number representations into binary number representations,
comprising the steps of""(1) testing each binary digit position '1,' beginning with the
least significant binary digit position, of the most significant
decimal digit representation for a binary '0' or a binary '1';""(2) if a binary '0' is detected, repeating step (1) for the
next least significant binary digit position of said most
significant decimal digit representation;""(3) if a binary '1' is detected, adding a binary '1' at the
(i+1)th and (i+3)th least significant binary digit positions of the
next lesser significant decimal digit representation, and repeating
step (1) for the next least significant binary digit position of
said most significant decimal digit representation;""(4) upon exhausting the binary digit positions of said most
significant decimal digit representation, repeating steps (1)
through (3) for the next lesser significant decimal digit
representation as modified by the previous execution of steps (1)
through (3); and""(5) repeating steps (1) through (4) until the second least
significant decimal digit representation has been so
processed."[Footnote 1]They are set forth in the409 U.S.
63app|>Appendix to this opinion.[Footnote 2]Title 35 U.S.C. § 100(b) provides:"The term 'process' means process, art or method, and includes a
new use of a known process, machine, manufacture, composition of
matter, or material."Title 35 U.S.C. § 101 provides:"Whoever invents or discovers any new and useful process,
machine, manufacture, or composition of matter, or any new and
useful improvement thereof, may obtain a patent therefor, subject
to the conditions and requirements of this title."[Footnote 3]SeeR. Benrey, Understanding Digital Computers 4
(1964).[Footnote 4]"To Promote the Progress of . . . Useful Arts," Report of the
President's Commission on the Patent System (1966).[Footnote 5]Id.at 13.[Footnote 6]SeeWild, Computer Program Protection: The Need to
Legislate a Solution, 54 Corn.L.Rev. 586, 604-609 (1969); Bender,
Computer Programs: Should They Be Patentable?, 68 Col.L.Rev. 241
(1968); Buckman, Protection of Proprietary Interest in Computer
Programs, 51 J.Pat.Off.Soc. 135 (1969).[Footnote 7]Amicusbriefs of 14 interested groups have been filed
on the merits in this case.MaterialsOral ArgumentsOral Argument - October 16, 1972Search This CaseGoogle ScholarGoogle BooksGoogle WebGoogle NewsToggle buttonGet free summaries of newU.S. Supreme Courtopinions delivered to your inbox!Enter Your EmailSign Up

---
*This document was automatically generated from the Justia Supreme Court database.*
