![Return to the JTMP landing page](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/blob/main/HomePage.md)

![Return to the JTMP landing page](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/blob/main/HomePage.md)

# New Case Updates Exchanges

A Courts' Case Management (CMS) will publish a New Case Update message each time a Clerk updates a new Criminal case (other case types?). This data exchange serves two purposes: to provide case details and a court case number to parties that need to track or contribute to case processing; and to correlate a court case with a preceeding event sent by another publishing system, for example a Booking message published by the jail management system (JMS). 

The publisher may be the CMS of any court jurisdiction - Criminal, Juvenile, or Municipal & Traffic. 

## Preceding Exchange: 

Case Initiation

## Triggering Events:

1. Documents are filed and accepted into the docket
2. Charges are added, modified or removed
3. A party of entity is added or removed
4. Bond is ordered, modified or posted

## Subsequent Events:
Proposed Motions and Orders filed to the Clerk by case parties

## Real-World Effects: 

The purpose of this data exchange is to enable partner justice systems to update a case. This exchange should be triggered as soon as case is updated to keep partners like the jail, prosecutor, and public defender apprised and enable them to take the next actions in court in a timely manner. 

This exchange is also intended to improve efficiency and accuracy. Subscriber systems should use the incoming data in this XML payload to update a Matter or Case (depending on the system's terminology) in time for their end users to review details and prepare filings for court. The timely exchange results in improvements in data accuracy and completeness, since data will populate automatically in the Subscriber systems. Reduction of re-keying of information saves staff time and reduces or elimiates errors.  The errors in re-keying obscure identifying numbers like SSN or court case ID reduce the types of errors that lead to case delays and ill-informed decision-making. 

This exchange may also convey the details of the one or more charges filed on the case. To the extent all partners are using values from the Uniform Charge Table, this will improve the clarity of specific charges and improve the visibility and accuracy of the please and other amendments to charges as the case proceeds. 

## Data Requirements:

![XML Schemas](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/tree/main/schemas/CaseUpdate_iepd/api/xml_schema).

### Key data elements include:
- Arrest number (enabling the JMS to correlate a new case to a previous Booking or Charge Screening). 
- Court Case ID
- Created Date (court clerk's staff will determine if this is a machine-generated date-time stamp, or the date of the judicial officer's approval)
- Current charges (either arrest charges or filed charges if the DA has filed a Screening Action Form). 
- ATN-Sequence number to correlate each Charge to the value originally assigned in the State's AFIS and CCH. 
- Judicial Official (the Judge to whom the case has been allotted)
- Court Section

## Artifacts:

![Mapping Spreadsheet](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/blob/main/schemas/CaseUpdate_iepd/artifacts/CaseInitiation_MappingSpreasheet.xlsx). 

![Sample XML Files](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/tree/main/schemas/CaseUpdate_iepd/examples).

**Class Diagram:** 
![Class Diagram](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/blob/main/schemas/CaseUpdate_iepd/artifacts/CaseInitiation_ClassDiagram.svg). 


