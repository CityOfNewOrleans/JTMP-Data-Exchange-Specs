![Return to the JTMP landing page](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/blob/main/README.md)

# Case Update Exchanges
A Courts' Case Management (CMS) will publish a Case Update message each time a Clerk updates pertinent details in a court case. This data exchange serves to keep all justice partners' systems synchonrized with the Court CMS as Clerks make changes to the details in the court docket. Specific types of updates are triggered, and sent with different data content. This provides both Publisher and Subscribers with greater control over which case details are updated, and how they are reflected in the Subscriber's system. 

The publisher may be the CMS of any court jurisdiction - Criminal, Juvenile, or Municipal & Traffic. 
Any justice partner agency that manages some level of court-case details in their local system may subscribe. This will include the jail, prosecutor, public defender and possibly law enforcement. 

## Preceding Exchange: 

- Case Initiation
- Court Event

## Identifying Specific Updates
This Data Exchange enables directed communication of updates, adds, or deletes and a mechanism for communicating specifically which data elements have changed. 

![Implementation Guidance](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/blob/main/schemas/CaseUpdates_iepd/artifacts/Implementation%20Guidance.md) provides implementation details on how to communicate adds, updates, or deletes. 

Further, the types of updates are predefined in this specification to include: 

- BondUpdate
- ChargeUpdate
- EntityUpdate (Parties on the case)
- CaseUpdate (Specific changes to Case Activity, including change of court, or update to case status)

If one of these messages has previously been sent and information changes, the message can be sent again. Use of MessageOperationCode attributes (add, update, delete) enable the sender to indicate which data objects have changed, and what has changed. The attributes are declared in each relevant schema set and look like this: 
image

### Example Scenarios:
A previously scheduled Court Event is rescheduled. Courts would send a Court Event message. Set the attribute MessageOperationCode to 'Update' to indicate that the CourtEventDateTime has changed. CourtEventDateTime would have the new date and time of the event.
After a delay, the State AFIS system has sent an Arrest Tracking Number (ATN) and ATN Sequence Number for a booked charge. In the original Booking message, ArrestTrackingNumber and ATNSequence were Null. A new message should be sent with the same Folder#, and a MessageOperationCode attribute set to 'Add' to for the ATN and each ATNSequence element.
An updated XML node would be preceded by the appropriate Attribute. For example, an added charge would indicated as follows:

        <j:BailBondAmount>
            <Amount>0</Amount>
        </j:BailBondAmount>
        <j:BailBondConditionDescriptionText structures:metadata="add">String</j:BailBondConditionDescriptionText>
        <j:BailBondSuretyEntity structures:metadata="update">
            <EntityPerson>
                <PersonName>
                    <PersonFullName>String</PersonFullName>
                </PersonName>
            </EntityPerson>

## Examples of Case and Charge Updates
### Adds:
 - New charge added to the case
 - Bond added
 - New party (victim, witness, attorney) added

### Updates:
 - Charge Disposition added
 - Bond updated or canceled
 - Court Event rescheduled. 
 - Lead attorney (prosecutor or defense) changed
 - Judge, Court Section or Courthouse changed

### Deletes 
Should be used in limited circumstances. Most elements once docketed on a court case are not removed. Exceptions: 
  - Entered in Error
  - Court Event canceled
  - Expunge/Seal Flag Set (Case or Charge Level)

## Triggering Events:

1. Bond is ordered, modified or posted
2. Documents are filed and accepted into the docket
3. Charges are added, modified or dismissed
4. A party or entity is added or removed
5. The expunge/seal flag is set at the case or charge level
6. One of the above items was previously entered in error and should be removed from the case docket

## Subsequent Events:
Proposed Motions and Orders filed to the Clerk by case parties

## Real-World Effects: 

The purpose of this data exchange is to enable partner justice systems to update a case. This exchange should be triggered as soon as information on a case is updated to keep partners like the jail, prosecutor, and public defender apprised and enable them to take the next actions in court in a timely manner. 

This exchange is also intended to improve efficiency and accuracy. Subscriber systems should use the incoming data in this XML payload to update a Matter or Case (depending on the system's terminology) in time for their end users to review details and prepare filings for court. The timely exchange results in improvements in data accuracy and completeness, since data will populate automatically in the Subscriber systems. Reduction of re-keying of information saves staff time and reduces or elimiates errors.  Errors, especially in re-keying identifying numbers like SSN or court case ID lead to case delays and mis-informed decision-making. 

A ChargeUpdate message will also convey the details of the one or more charges filed on the case. To the extent all partners are using values from the Uniform Charge Table, this will improve the clarity of specific charges and improve the visibility and accuracy of the please and other amendments to charges as the case proceeds. 

## Data Requirements:

![XML Schemas](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/tree/main/schemas/CaseUpdates_iepd/api/xml_schema)

### Key data elements include:
- Arrest Tracking Number and ATN-Sequence number to correlate each Charge to the value originally assigned in the State's AFIS and CCH.
- Statewide ID, or  SID. The person identifier tied to an individual's fingerprints on file in the state's automated fingerprint information system (AFIS)
- Arrest number (enabling the JMS to correlate a new case to a previous Booking or Charge Screening). 
- Court Case ID
- Created Date (court clerk's staff will determine if this is a machine-generated date-time stamp, or the date of the judicial officer's approval)
- Current charges (either arrest charges or filed charges if the DA has filed a Screening Action Form). 
- Judicial Official (the Judge to whom the case has been allotted)
- Court Section

## Artifacts:

![Mapping Spreadsheet](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/blob/main/schemas/CaseUpdates_iepd/artifacts/CourtDisposition_MappingSpreasheet.xlsx)

![Sample XML Files](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/tree/main/schemas/CaseUpdates_iepd/examples)

**Class Diagram:** 
![Class Diagram](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/blob/main/schemas/CaseUpdates_iepd/artifacts/CaseUpdates_ClassDigram.svg)


