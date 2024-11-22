![Return to the JTMP landing page](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/blob/main/HomePage.md)

# Charge Code Updates

The Justice partners are in the process of establishing a standardized charge code table. Values from the Uniform Charge Table are to be incorporated consistently by all JTMP endpoint systems into their native offense or statute code tables.  The UCT will provide a Charge Key that will uniquely identify each charge and provide the basis for standardizing key data elements related to each charge, as well as keeping all partner systems synchronized as legislative change and other changes result in modification, repeal or enactment of charges. 

This table will include both chargeable offenses from Louisiana state statutes and New Orleans municipal code violations.

When published, the full table of statute codes will be available online to authorized users (including Orleans Parish justice developers).

The charge code table will be fronted by an application that will enable authorized justice partner users to make updates to specific code values as legislation changes.

The application publishes to the JTMP API with a MessageType of ChargeUpdate every time a change is enacted in the charge code table. Subscribers are required to consume each ChargeUpdate message. Messages with a Charge Key that do not match an existing record should result in creation of a new record. ChargeUpdate messages that match a Charge Key in the system should update the values for that record. Existing charges are to be preserved in the table to maintain accuracy of prior cases and offenses.

## Preceding Exchange

None

## Triggering Event

An existing record is modified or a new record is saved to the Orleans Uniform Charge Table.  

## Real-World Effects

The purpose of the Charge Code Update data exchange is to ensure consistency in the definition of chargeable offenses as a case moves from initial police incident and arrest, to booking, to charging and disposition of a court case.  

##Business Rules##
...mandaory vs optional...

## Data Requirements

![XML Schemas](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/tree/main/schemas/UniformChargeTable_iepd/api)

### Key data elements include

- ChargeKey - a unique identifer that is to be stored as a Key in each endpoint system's statute code or charge table.
- Source - indicates Louisiana Revises Statutes or New Orleans Municipal Code
- Title, ChargeViolation, ChargeSubparagraph - three fields that break out the numberic portions of a title and statute reference
- ChargeMofifier1, ChargeModifier2 - two fields that indicate Inchoate modifiers that may be attached to the charge
- ChargeDescirption - short text description of the charge. Initial values are those in current use in the Jail and Court systems on the AS400 platform
- LongDescription - possible future usage for more detailed charging language
- CourtType - indicator or the Default court to which the charge is filed (State or Municipal & Traffic)
- Charge Class (Severity Level, 1 through 4 to distinguish felony from midemeanor, and level of severity)
- Effective Date - beginning date from which the charge may be used
- Inactive Date - ending date, after which the charge is not valid
- ChargeString - a Concatenation of Title, ChargeViolation, ChargeSubparagraph and Class to uniquely identify a charge with a more user-readable syntax 

## Artifacts
![Sample XML File](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/tree/main/schemas/UniformChargeTable_iepd/examples)

![Mapping Spreadsheet](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/blob/main/schemas/UniformChargeTable_iepd/artifacts/UniformChargeTable_MappingSpreadsheet.xlsx)

![Class Diagram](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/blob/main/schemas/UniformChargeTable_iepd/artifacts/UniformChargeTable_ClassDiagram.svg)

