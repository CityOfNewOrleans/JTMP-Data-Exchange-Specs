![Return to the JTMP landing page](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/blob/main/HomePage.md)

# Uniform Commitment Order (UCO)

The Court Case Management System (CMS) will publish a UCO message when sentencing information is saved to a case in the CMS. The published Sentence data will follow the data content prescribed by the Louisiana Supreme Court (LASC) in its Uniform Commitment Order form. The CMS will include a PDF rendering of the UCO form as an attachment to the XML message. 

## Preceding Exchange: 

1. CaseChargeFiling
2. CaseInitiaion
3. One or more Motions or Proposed Orders may have been filed, that propose plea agreements or other amendments to filed charges. 

## Triggering Events:

Completion of Sentence data in the case docket.
This will be preceded by a Minutes entry that provided CMS with the details of the sentence(s), as ordered by the Presiding Judge. 

## Real-World Effects: 

The purpose of this data exchange is to enable Subscriber systems to update case disposition and sentencing when a disposition is entered and (if guilty) sentence information is imposed. 

Subscribers will be able to associate the details of the disposition and/or relevant sentences with the Court Case ID provided in the CaseInitiation data exchange. 

## Data Requirements:

### Key Booking data elements include:
- Court Case ID.
- Sheriff's Control Number
- Charge Sequence Numbers
- UCTIDs for each disposed charge
- Charge Disposition (guilty, not guilty, dismissed, pled, etc.)
- Sentence information including:
- Sentence Type (prison, probation, fines, etc.)
- Sentence Length
- Concurrent/Consecutive indicators

## Artifacts:
**XML Schema:** - Coming soon

**Mapping Spreadsheet:**
![Mapping Spreadsheet](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/blob/main/schemas/UniformCommitmentOrder_iepd/artifacts/UniformCommitmentOrder_MappingSpreadsheet.xlsx)

**Sample XML:** - Coming soon. 

**Class Diagram:**
![Class Diagram](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/blob/main/schemas/UniformCommitmentOrder_iepd/artifacts/UnformCommitmentOrder_ClassDiagram.svg)
