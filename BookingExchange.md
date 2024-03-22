# Booking Exchange
<p>The Jail Management System will publish a Booking and Release message each time a client is either booked  into the jail or released for any reason (ROR, Bond, No Probable Cause, Disposition, etc.)</p>

<p><strong>Preceding Exchange</strong>: Arrest Report (from Police Department)​</p>
<p><strong>Triggering Events</strong>:</p>
<p>1. Supervisor Approval in JMS of a new Booking<br>
2. Supervisor Approval in JMS of a JMS Release</p>
<p><strong>Real-World Effects</strong>: Notify Subscriber systems of a new jail event. Subscribers may update existing pending case events or update previously-created events. Many Subscriber systems will opt to stage incoming events in a queue or review screen pending human action to import into the case management system. ​</p>
<p><strong>Data Requirements</strong>:<br>
<em>Link to XML Schemas<em></p>
<p></p><strong>Artifacts</strong>:<br>
<p><em>Link to Mapping Spreadsheet</em></em><br>
<em>Link to Class Diagram</em><br>
<em>Link to Sample XML File</em></p>
