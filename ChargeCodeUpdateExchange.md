# Charge Code Updates

The Justice partners have established a standardized charge code table. Values from the table, such as the statute string, description, enacted and repealed dates, and associated codes or categories are to be incorporated consistently by all JTMP endpoint systems into their native offense or statute code tables.  

This table will include both chargeable offenses from Louisiana state statutes and New Orleans municipal code violations.

The full table of statute codes is available here (Link to be provided).

The charge code table is fronted by an application that enables authorized justice partner users to make updates to specific code values as legislation changes.

The application publishes a to the JTMP API with a MessageType of ChargeUpdate every time a change is enacted in the charge code table. Subscribers are required to consume each ChargeUpdate message and store update as a new record -- existing charges are to be preserved in the table to maintain accuracy of prior cases and offenses.

## Preceding Exchange

None

## Triggering Event

A new record is saved to the Orleans Uniform Charge Table.  

## Real-World Effects

The purpose of the Charge Code Update data exchange is to ensure consistency in the definition of chargeable offenses as a case moves from initial police incident, to booking, to charging and disposition of a court case.  

## Data Requirements

XML Schemas - coming soon

### Key data elements include

- Statute String - the reference from Statute or Ordinance code books, e.g., ____
- Statute Description
- Enacted Date
- Repealed Date
-

## Artifacts

Mapping Spreadsheet - coming soon

**Class Diagram:** - coming soon

Sample XML File - coming soon
