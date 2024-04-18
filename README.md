<h1>Justice Technology Modernization Program</h1>
<h2>Integration Architecture Overview</h2>
<p>Developers who provide these systems will interact with application programming interfaces (APIs) that JTMP will expose via Azure’s API Gateway. ​JTMP will follow a Publish/Subscribe model for the most part. ​A system or application sending data to shared with partner agencies/systems will call an API to Publish a message. ​The message metadata will indicate which Data Exchange is published in the message body. ​(Not yet available) The Service Bus will call an API hosted at the Subscriber’s system to deliver Subscribed messages. ​Alternatively, Subscribers may call a Polling Message API to Get pending messages. ​These interactions are illustrated below. However, this functionality is still under development. <br>
The following diagram provides an overview of the JTMP Service Bus. ​</p>

![AzureServiceBusIntegration_032024](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/assets/164246967/b57a533a-3345-4b62-a3b8-5c11cf4c4e98 "Azure Service Bus")

<h2>Data Exchange Specifications </h2>
<p>JTMP has identified a set of Priority Data Exchanges between these systems that drive us toward that vision.  JTMP follows the National Information Exchange Model )NIEM) in building and publishing specificaitons for each data exchange. The requirements for building each data exchange are communicated in as Information Exchange Package Documentation (IEPD). The table below lists the Publishing system or systems for each data exchange. The right-most column provides the link to the IEPD in the repository.</p>
 
|Data Exchange |Publishing System(s) |IEPD Page |API Topic-exchangeDataType name|
|-----|------|------|-----|
|Booking | Jail Management System|[Booking IEPD](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/blob/main/BookingExchange.md) |booking and release|
|New Case Initiation |Court CMS|[Case Initation IEPD](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/blob/main/CaseInitiation.md) |caseInitiation|
|Court Event|Court Case Management System (CMS)|[CourtEvent IEPD](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/blob/main/CourtEventExchange.md) |courtEvent|
|Court Order|Criminal District Court CMS/Municipal & Traffic Court CMS|[CourtOrder IEPD](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/blob/6b9667a5bcf91a051187ed3dff26fe8e4ddb0612/CourtOrderExchange.md)|courtOrder|
|Charge Code Table Updates|Centrally-hosted Uniform Charge Table|[ChargeUpdate IEPD](https://github.com/CityOfNewOrleans/JTMP-Data-Exchange-Specs/blob/main/ChargeCodeUpdateExchange.md)|chargeUpdate|
