![Return to the JTMP landing page](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/blob/main/HomePage.md)

# Charge Filing Exchange
This Message Specification contains the required data elements for a A Prosecutor's Case Management or Matter Management System (CMS or MMS) to either file arrest charges to intiate a criminal court case, or to file an Indictment with the Clerk of Courts for Grand Jury review. 

### New Charge Filing
A Prosecutor's Case Management or Matter Management System (CMS or MMS) will publish a New Charge Filing message each time an Assistant District Attorney, paralegal or other professional completes a charge filing document and saves or indicates it is Ready to File. 

In Orleans Parish, the charge-filing instrument is known as a Bill of Information or BOI). The BOI is normally accompanied by a Screening Action Form. The Screening Action Form contains all of the data necessary for a Court Clerk to either (a) create a new criminal court case; or (b) match a formal filing of charges to an existing Magistrate or Pre-Filing (temporary) case.  In Orleans Parish a BOI kicks off the Allotment process, whereby the new case gets assigned to a court section based on court section caseloads and case types.  

This data exchange streamlines the Criminal Distric Court Clerk's process of creating a new criminal court case by enabling the Clerk's CMS to automatically import the filed charges. The Clerk's CMS will match the new charge filing to an existing Magistrate case using one or more of the shared identifiers: 
-Police Item Number
-Sheriff Control Number (SCN) or Booking number
-Person identifiers, including the statewide identification (SID) number when available and local person identifiers as described in the Specification. 

### Indictment Filing
This Message Specification includes a GrandJuryIndictment indicator in the required XML. When a Proseutor files a charge or charges for Grand Jury deliberation, the Prosecutor CMS will set that indciator to True. 

The Criminal District Court Clerk's CMS will read that Indicator and route Grand Jury Indictments to set up a new Grand Jury case for the jury's deliberation. 

## Preceding Exchange: 

Booking
Arrest Report

## Triggering Event:

1. DA CMS user completes a charge filing document and saves or indicates it is Ready to File.
2. DA CMS user updates a previously-filed Screening Action Form and indicates it is Ready to File. 

Juvenile Court filings may use this exchange; details on the appropriate form, and routing information will be provided when the Juvenile Court CMS begins data integration. 

## Subsequent Event:
CaseInitiation from the Court Clerk CMS. Matching on one or more of the identifiers listed above, Case Initiation is intended to update the Matter or Case in each justice partner's system to include the Criminal Court Case Docket Number. 

## Real-World Effects: 

The purpose of this data exchange is to automate filing of charges and creation of the details for a new Criminal Court case. 
The Court CLerk's CMS vendor/system will need to attempt to match to an exisitng, pre-filing temporary case based on identifiers of predecessor events, such as incident, arrest or booking. 

The Clerk's CMS will create a new Grand Jury case when the GrandJuryIndictment indicator is set to True. This streamliness the process of setting up new cases for Grand Jury deliberations, and provides an efficient transition to opening a new criminal court case for those charges on which a Grand Jury returns a True Bill of Indictment. 

The timely exchange results in improvements in data accuracy and completeness, since data will populate automatically in the Subscriber systems. Reduction of re-keying of information saves staff time and reduces or elimiates errors.  The errors in re-keying obscure identifying numbers like SSN or court case ID reduce the types of errors that lead to case delays and ill-informed decision-making. 

This exchange will also leverage the UCTID from the Uniform Charge Table to improve the clarity of specific charges and improve the visibility and accuracy of charges as the case proceeds. 

## Data Requirements:

XML Schemas - coming soon. 

### Key data elements include:
- Arrest number (enabling the JMS to correlate a new case to a previous Booking or Charge Screening). 
- Magistrte Court Case ID if known
- Created Date/Filed DAte 
- Accepted charges (indicated by UCTID).
- Rejected charges
- SCN-Sequence number to correlate each Charge to the value originally assigned in the State's AFIS and CCH. 
- Prosecuting Attorney

## Artifacts: coming soon. 

**Mapping Spreadsheet** - coming soon

**Sample XML Files** - coming soon

**Class Diagram:**  - coming soon

