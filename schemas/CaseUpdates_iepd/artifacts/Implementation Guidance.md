
![Return to the Case Updates IEPD](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/blob/main/schemas/CaseUpdates_iepd/CaseUpdates.md)

# Implementation Guidance for Case Update Exchanges
This document provides guidance to implementors of the [Case Update messages](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/blob/main/schemas/CaseUpdates_iepd/CaseUpdates.md) in the [New Orleans Justice Technology Modernization Program](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/tree/main) to ensure consistent and accurate processing of case update messages across systems.

## General Guidance
- Each Case Update message specification is a subset of the [Case Initiation message specification](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/blob/main/schemas/CaseInitiation_iepd/CaseInitiation.md).
- Data elements in the Case Initiation message that are not required for each specific Case Update message are removed in each Case Update pdate message specification.

### Types of Update Operations
- Each Case Update message can include any combination of data elements that are to be added, deleted or updated by the receiver.
- The value of the `<nola-ext:MessageOperationCode>` metadata element indicate which types of update operations are in the message. 
- The value of the `<nola-ext:MessageOperationCode>` metadata element must be one of the following: 
    - "add"    - Indicates the addition of new content.
    - "delete" - Indicates the removal of existing content.
    - "update" - Indicates modifications to existing content.
- The id of the `<nola-ext:MessageOperationCode>` must match its value.

For example, this [example of the Bond Update message](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/blob/main/schemas/CaseUpdates_iepd/examples/BondUpdate_example.xml) includes data to be added.

``` xml
<nola:BondUpdateExchange>
	<nola-ext:MessageOperationCode structures:id="add">add</nola-ext:MessageOperationCode>
```

- If some data is to be added, some data deleted and/or some data updated in the same message, `<nola-ext:MessageOperationCode>` may occur multiple times, ala:

``` xml
<nola:BondUpdateExchange> 
	<nola-ext:MessageOperationCode structures:id="add">add</nola-ext:MessageOperationCode>
	<nola-ext:MessageOperationCode structures:id="delete">delete</nola-ext:MessageOperationCode>
	<nola-ext:MessageOperationCode structures:id="update">update</nola-ext:MessageOperationCode>
```

### Identifying Specific Data Elements to Update
- Data elements that are to be added, deleted or updated must reference the id of the appropriate metadata element with the attribute `structures:metadata`. For instance, in the following portion of the Bond Update message example, the `<j:BailBondConditionDescriptionText>` data element is to be added.

``` xml
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
```
- Data elements that are contained within an element that is identified as added, deleted or updated are also to be updated. For instance, in the prevous example, the                     `<PersonFullName>` is contained within `<j:BailBondSuretyEntity>` and is also to be updated.

## Guidance to Implementers of Systems Sending Case Update Messages
Sending systems must:
- Include one or more `nola-ext:MessageOperationCode` elements in the message, as appropriate based on the update operation(s).
- Use the attribute `structures:metadata` to indicate the data elements to be updated and associate them with the appropriate updates operation.

## Guidance to Implementers of Systems Receiving Case Update Messages
Receiving systems must:
- Look for the `nola-ext:MessageOperationCode` element in incoming messages to indicate what update operations are contained in the message.
- Look for the attribute `structures:metadata` attributes to identify the data elements to be updated and specific update operation.
- Update each set of data elements as appropriate based on the associated update operation.
