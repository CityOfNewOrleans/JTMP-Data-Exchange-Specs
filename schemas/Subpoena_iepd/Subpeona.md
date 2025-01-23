![Return to the JTMP landing page](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/blob/main/HomePage.md)

# Subpoena and Return of Service

Orleans Parish maintains a separate application, called CourtNotify, to manage subpoenas across all partners. Partners enter subpoena requests or information on approved subpoenas into CourtNotify. When the respondent on a subpoena is a New Orleans Police Department Officer, CourtNotify automatically notifies the officer, and the officer or a supervisor either acknowledges the request or enters information about a Conflict if the officer is unable to attend the scheduled court event. When the Respondent is a civilian, the Sheriff's Office civil process division is able to print the subpoeana for physical service. The serving deputy enters service information into CourtNotify --either successful service or an attempt. 

The purpose of this exchange is to inform the Court and other subscribers of service information. The exchange will also return an html rendering of the Subpoena document itself. 

**![Subponea-ReturnOfService IEPD](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/tree/GJS-Subpoena/schemas/Subpoena_iepd)**

## Preceding Exchange: 

The CourtNotify application maintains up-to-date court case information as a Subscriber to the Booking, Case Initiation, and Court Event data exchanges. 

## Triggering Events:

CourtNotify hosts an application programming interface (API). The exchange is executed by polling that API at regular intervals. The exchange will send one message per new or updated Subpoena Service entry that is returned by that API call. As a result subscribers will receive updated subpoena service information on regular intervals throughout a business day. 

## Real-World Effects: 

This exchange keeps the Court and subpoena requestors (district attorney or public defender) informed of subpoena service. They will know by review of their local case management system, proactively, whether a Respondent is able to attend a requested court hearing. 

## Data Requirements:
In order to properly synchronize with existing case and hearing data in the Subscribers' systems, the CourtNotify exchange must return identifiers that originated with those systems. These include: 
- Court Case ID, the case number established by the Court.
- A unique Event Identifier that the Court provided in the Court Event message for a given hearing.
- Person identifiers for law enforcement officials. The exchange will send both Badge number and Employee ID number when available. 

## Artifacts:

**![Mapping Spreadsheet](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/blob/GJS-Subpoena/schemas/Subpoena_iepd/artifacts/Subpeona_Response_MappingSpreadsheet.xlsx)** -click "view Raw" to open the spreadsheet. 

**![Sample XML File](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/blob/GJS-Subpoena/schemas/Subpoena_iepd/examples/SubpoenaSample.xml)**

**Class Diagram:**
![Class Diagram:](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/blob/GJS-Subpoena/schemas/Subpoena_iepd/artifacts/Subpoena_ClassDiagram.svg)
