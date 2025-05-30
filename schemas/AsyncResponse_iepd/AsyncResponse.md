![Return to the JTMP landing page](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/blob/main/README.md)

# Asynchronous Response Messaging

The Subscriber to any message may send a response message through the service bus to convey the results of downstream message processing, after the API interaction has been closed. The asynchronous response message goes through the same process as the request message, but since it is one to one communication, the queue messaging pattern will be used. Publishing systems should provide an endpoint to receive the asynchronous response message. It is the agency’s responsibility to correlate the request message and response message by using message meta data or the message body.

The ESB will also capture async responses and can route the message to a designated recipient at the sending agency. 

![Async Response IEPD](schemas/AsyncResponse_iepd)

## Preceding Exchange: 

Any

## Triggering Event:

Receipt and subsequent processing of any JTMP message received by a Subscriber


## Real-World Effects: 

Robust response messaging gives the Publisher of a message the assurance that the critical data being shared has been received and properly processed. It also gives each Subscriber the ability to communicate back to the Publisher any time an error is encountered in processing and storing a published message. 

## Data Requirements:

### Key data elements include:
- Original TransactionID from the published message
- New, unique MessageID that identifies the response as a separate message
- Error code
- Text field to include error message encountered, or text provided by an end user (who may be rejecting a message for a business reason).

### Error Code Values and Use Cases
|Error Type|Description|XML Element used|Use Case|
|---|---|----|---|
|Endpoint Error|Failed to stage message|MessageStatus/MessageHandlingError|Error encountered  by an endpoint AFTER the processing has entered into the actual service implementation code but before the processing completes. Errors that occur in the underlying endpoint framework would respond with a fault.|
|Content Error|Validation error|MessageStatus/MessageContentError|XML content, or XML validation errors. An error that is encountered AFTER the processing has entered into the actual service implementation code but before the processing completes.|
|Received|Successfully staged|MessageStatus/SystemEventDescriptionText|This status could be sent if the receiving system sends a later message upon final processing. For example, the service could send a Received message if final acceptance is pending human review, for example clerk review of an efiling message.|
|Approved|Final Acceptance|MessageStatus/SystemEventDescriptionText|Final approval, which could be used if human review is the final stage in processing a message, for example clerk efiling review.|


## Artifacts:
**XML Schemas:** 
![XML Schemas](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/tree/main/schemas/AsyncResponse_iepd/api/xml_schema)

**Mapping Spreadsheet:**
![Mapping Spreadsheet](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/blob/main/schemas/AsyncResponse_iepd/artifacts/Async_Response_MappingSpreadsheet.xlsx)

**Sample XML:** 
![Sample XML Files](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/tree/main/schemas/AsyncResponse_iepd/examples)

**Class Diagram:** 

![Class Diagram](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/blob/main/schemas/AsyncResponse_iepd/artifacts/AsyncResponse_ClassDiagram.svg)
