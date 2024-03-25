
# Booking Exchange

The Jail Management System will publish a Booking and Release message each time a client is either booked  into the jail or released for any reason (ROR, Bond, No Probable Cause, Disposition, etc.)

## Preceding Exchange: 

Arrest Report (from Police Department)​

## Triggering Events:

1. Supervisor Approval in JMS of a new Booking
2. Supervisor Approval in JMS of a JMS Release

## Real-World Effects: 

Notify Subscriber systems of a new jail event. Subscribers may update existing pending case events or update previously-created events. Many Subscriber systems will opt to stage incoming events in a queue or review screen pending human action to import into the case management system. 

## Data Requirements:

[XML Schemas](schemas/booking-iepd/api/xml_schema/)

## Artifacts:

[Mapping Spreadsheet](schemas/booking-iepd/artifacts/booking mapping spreadsheet.xlsx)

[Class Diagram](schemas/booking-iepd/artifacts/booking class diagram.svg)

[Sample XML File](schemas/booking-iepd/examples/Annotated_NOLA_Booking_msg.xml)


