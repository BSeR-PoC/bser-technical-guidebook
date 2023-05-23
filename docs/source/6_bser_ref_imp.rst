BSeR Reference Implementation
=============================

Architecture
------------
Georgia Tech Research Institute (GTRI) has developed an archteture for reference implementation of BSeR IG and implemented
initator application and recipient simulator. The architecture is designed to support various environment and intermediate 
stages until the BSeR becomes mature. Figure 1 depicts the architecture.   

.. image:: 
   images/BSER_RI_Architecture.png
   :width: 520pt
   :alt: BSeR Reference Implementation Architecture 

**Figure 1**\ : BSeR Reference Implementation Architecture


BSeR IG defines two main roles of systems, initiator and recipient. Initiator is a system that composes electronic referral 
(e-Referral) request and sends to recipient. Recipient on the other hand is a system that consumes the e-referral request(s) 
and process the request(s). 

In initiator, BSeR App for clinical provider is a SMART on FHIR application that can be launched from EHR's patient chart 
(EHR launch mode in SMART on FHIR framework). The App will be authorized to access EHR data by provider(s) when it is launched
from EHR. The App can provide a user interface for providers to compose the e-Referral message using patient data, 
service provider organizations, and detail referral usecase information. BSeR App should use FHIR messaging to send an 
e-Referral. HTTP 200 status code should be returned if the message was successfully received by recipients. HTTP 4xx or 5xx 
status codes can be used if error(s) occurrs. The payload should contain FHIR's OperationOutcome resource to include detail
error descriptions. 

BSeR App should asynchrously wait for feedbacks from recipient. As the feedback messages are sent by recipient asynchronously, 
BSeR App should match the incoming feedback messages to existing referral cases and update the status of the matching cases. 
The App do not response to the feedback messages as they are the messages that close the bi-directional messaging loop.


Initiator (Clinical Provider)
-----------------------------

Users of initiator are clinical providers who refer patients to a service provider (recipient) and also EHR users. 
EHR in the initiator should be FHIR enabled. Initiator system should support SMART on FHIR in order to access patient
data from EHR. 

Developers of BSeR initiator must work with IT of the clinical provider's EHR so that initiator system will comply with 
the data access policies on reading from and possibly writing to EHR. 

.. image:: 
   images/BSER_RI_Initiator_App.png
   :width: 520pt
   :alt: BSeR Reference Implementation Architecture 

**Figure 2**\ : BSeR Reference Implementation Initiator System


Recipient (Service Provider)
----------------------------

Recipient system needs to parse the e-Referral request appropriately based on the use cases defined in the
BSeR IG. The parsed data should then be delivered to the service management to process the request. The service management 
should then send feedbacks as responses to the initiator via recipient system during the referred service(s). Feedbacks
include accept, declined, status, etc. as defined by BSeR IG. 
