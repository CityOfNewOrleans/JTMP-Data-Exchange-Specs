
[Return to the Case Initiation IEPD](../CaseInitiation.md)

# Implementation Guidance for Case Initiation Exchange
This document provides guidance to implementors of the [Case Initiation messages](../CaseInitiation.md) in the [New Orleans Justice Technology Modernization Program](../../../README.md) to ensure consistent and accurate processing of case update messages across systems.

## General Guidance
- The [Case Update message specification](../../CaseUpdates_iepd/CaseUpdates.md) is a subset of this [Case Initiation](../CaseInitiation.md) message specification.
- Data elements in the Case Initiation message that are not required for each specific Case Update message are removed in each Case Update message specification.

## Guidance to Implementers of Systems Sending Case Initiation Messages
Sending systems must ensure that each nc:CourtCase contains multiple `j:CaseAugmentation` elements distinguished by the `structures:id` attribute as follows:
- One `j:CaseAugmentation` with `structures:id="case"` for the case
    - Populate the following elements specific to the case: 
        - `j:CaseCourt`
        - `j:CaseCourtEvent`
        - `j:CaseExhibit`
        - `j:CaseJudge`
        - `j:CaseOfficial`
        - `j:CaseOtherEntity`
        - `j:CaseProsecutionAttorney`
        - `j:CaseWitness`
    - Leave empty (indicated with `xsi:nil="true"`) the following elements specific to a defendant:
        - `j:CaseCharge`
        - `j:CaseDefenseAttorney`
        - `j:CaseDefendantParty`
- One `j:CaseAugmentation` with `structures:id="defendant1"` (or `defendant2`, `defendant3`, etc.) for each defendant
    - Leave empty the elements specific to the case (listed above)
    - Populate the elements specific to the defendant (listed above)

For more details, see the provided [example messages](../examples).

## Guidance to Implementers of Systems Receiving Case Initiation Messages
None at this time.
