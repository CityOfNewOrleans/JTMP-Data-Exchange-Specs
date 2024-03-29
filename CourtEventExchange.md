
# Court Event Exchange

A Courts' Case Management (CMS)) will publish a Court Event message each time a court clerk schedules a hearing or other scheduled event on a case docket. 

The publisher may be the CMS of any court jurisdiction - Criminal, Juvenile, or Municipal & Traffic. 

## Preceding Exchange: 

Charge Screening Action (new Criminal charges filed - from District Attorney)
Case Initiation (new criminal case established, Court publishes Case Number and Filed Charges)​

## Triggering Event:

1. Judge orders an event (hearing) to be scheduled
2. Court clerk addes the scheduled event to a court case docket
3. A Court Clerk updates an existing scheduled event when it is cancelled, continued or rescheduled.  


## Real-World Effects: 

The purpose of this data exchange is to keep partner justice systems in sync with the court case docket in the court clerk's CMS, which is the official system of record of court proceedings.  Publishing a scheduled event as a transaction, as soon as it is docketed in the CMS, gives the parties --the Prosecutor and Public Defender-- the assurance that their case files are up to date. 

One tangible benefit is fewer missed hearings, thus fewer Continuances. 

When hearings are continued, cancelled or rescheduled, the CMS will send an update. 

The Court Event data exchange will include a Status indicator, indicating to the Subscribing system whether the Event is New or Updated. 

Subscriber systems will match the incoming Court Event with the Court Case ID (which had previously been received in a Case Initition message). 

## Data Requirements:

XML Schemas - coming soon
### Key data elements include:
- Status indicator -- New or Updated Event
- Court Case ID
- Event Code (enumerated code list)
- Event Date
- Event Time
- Location (codelist of courtroom locations)
- Judicial Official (the Judge on the case)

## Artifacts:

Mapping Spreadsheet - coming soon

**Class Diagram:** - coming soon


Sample XML File - coming soon


