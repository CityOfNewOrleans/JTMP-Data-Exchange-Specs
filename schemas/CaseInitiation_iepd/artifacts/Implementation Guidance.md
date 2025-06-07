
[Return to the Case Initiation IEPD](../CaseInitiation.md)

# Implementation Guidance for Case Initiation Exchange
This document provides guidance to implementors of the [Case Initiation messages](../CaseInitiation.md) in the [New Orleans Justice Technology Modernization Program](../../../README.md) to ensure consistent and accurate processing of case update messages across systems.

## General Guidance
- The [Case Update message specification](../../CaseUpdates_iepd/CaseUpdates.md) is a subset of this [Case Initiation](../CaseInitiation.md) message specification.
- Data elements in the Case Initiation message that are not required for each specific Case Update message are removed in each Case Update message specification.

## Guidance to Implementers of Systems Sending Case Initiation Messages
Sending systems must:
- Ensure that each nc:CourtCase contains at most one `j:CaseDefendantParty` by including only one `j:CaseAugmentation` in each `nc:CourtCase`. Note that each `j:CaseAugmentation` includes only one `j:CaseDefendantParty`.

## Guidance to Implementers of Systems Receiving Case Initiation Messages
None at this time.
