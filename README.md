# Justice Technology Modernization Program
<p>Developers who provide these systems will interact with application programming interfaces (APIs) that JTMP will expose via Azure’s API Gateway. ​JTMP will follow a Publish/Subscribe model for the most part. ​A system or application sending data to shared with partner agencies/systems will call an API to Publish a message. ​The message metadata will indicate which Data Exchange is published in the message body. ​(Not yet available) The Service Bus will call an API hosted at the Subscriber’s system to deliver Subscribed messages. ​Alternatively, Subscribers may call a Polling Message API to Get pending messages. Alternatively, ​These interactions are illustrated below. However, this functionality is still under development. ​</p>
## Data Exchange Specifications
 A diagram of a diagram

Description automatically generated
