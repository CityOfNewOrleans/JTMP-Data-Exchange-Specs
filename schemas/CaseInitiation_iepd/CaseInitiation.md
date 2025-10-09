![Return to the JTMP landing page](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/blob/main/README.md)

# New Case Initiation Exchange

A Courts' Case Management (CMS) will publish a New Case Initiation message each time a Clerk creates a new Criminal case (other case types?). This data exchange serves two purposes: to provide case details and a court case number to parties that need to track or contribute to case processing; and to correlate a court case with a preceeding event sent by another publishing system, for example a Booking message published by the jail management system (JMS). 

The publisher may be the CMS of any court jurisdiction - Criminal, Juvenile, or Municipal & Traffic. 

## Preceding Exchange: 

Booking
Charge Filing (Screening Action and Bill of Information)

## Triggering Event:
A Case Initiation message will be triggered any time a new case is created in a court case management system (CMS). 
1. A new Booking message automatically generates a new Magistrate Case in Criminal District Courts’ CMS 
2. A Charge Filing message automatically generates a new Criminal Case in Criminal District Courts’ CMS

Note: The judge and court section are assigned through a process  known as Allotment. The Allotment process will trigger a Case Update message that will associate the Criminal Case Docket # with the assigned Judge and Court Section. This transactional data exchange replaces the Allotment List, in conveying new case information to all interested parties.
The processes are different in Juvenile and Municipal and Traffic Court. The triggering event will still be creation of a new case and assignment of a case ID number.

The processes are different in Juvenile and Municipal and Traffic Court. The triggering event will still be creation of a new case and assignment of a case ID number. 

## Subsequent Event:
* Case Updates convey the allotted judge and court section
* Charge Updates convey amended or disposed charges
* Entity Updates convey changes or additions to persons on the case 
* Proposed Motions and Orders filed to the Clerk by case parties

## Real-World Effects: 

The purpose of this data exchange is to enable partner justice systems to either set up a new case or to associate court proceedings with a preceeding event, such as a jail booking. This exchange should be triggered as soon as a new court case is created in order to keep partners like the jail, prosecutor, and public defender apprised and enable them to take the next actions in court in a timely manner. 

This exchange is also intended to improve efficiency and accuracy. Subscriber systems should use the incoming data in this XML payload to create a new Matter or Case (depending on the system's terminology) in time for their end users to review details and prepare filings for court. The timely exchange results in improvements in data accuracy and completeness, since data will populate automatically in the Subscriber systems. Reduction of re-keying of information saves staff time and reduces or elimiates errors.  The errors in re-keying obscure identifying numbers like SSN or court case ID reduce the types of errors that lead to case delays and ill-informed decision-making. 

This exchange will also convey the details of the one or more charges filed on the case. To the extent all partners are using values from the Uniform Charge Table, this will improve the clarity of specific charges and improve the visibility and accuracy of the please and other amendments to charges as the case proceeds. 

## Data Requirements:

![XML Schemas](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/tree/main/schemas/CaseInitiation_iepd/api/xml_schema).

### Key data elements include:
* Incident Item Number
* Booking ID (enabling the JMS to correlate a new case to a previous Booking or Charge Screening).
* Court Case ID
* Created Date (court clerk's staff will determine if this is a machine-generated date-time stamp, or the date of the judicial officer's approval)
* Current charges (either arrest charges or filed charges if the DA has filed a Screening Action Form)
* ATN-Sequence number to correlate each Charge to the value originally assigned in the State's AFIS and CCH.
* Judicial Official (the Magistrate who will hear a Magistrate case).
* Magistrate Court Section 

## Artifacts:

![Mapping Spreadsheet](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/blob/main/schemas/CaseInitiation_iepd/artifacts/CaseInitiation_MappingSpreasheet.xlsx). 

![Sample XML Files](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/tree/main/schemas/CaseInitiation_iepd/examples).

**Class Diagram:** 
![Class Diagram](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/blob/main/schemas/CaseInitiation_iepd/artifacts/CaseInitiation_ClassDiagram.svg). 


