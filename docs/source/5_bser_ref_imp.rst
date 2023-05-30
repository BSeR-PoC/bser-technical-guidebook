BSeR Reference Implementation
=============================

Architecture
------------
Georgia Tech Research Institute (GTRI) has developed an archteture for reference implementation of BSeR IG and implemented
initator application and recipient simulator. The architecture is designed to support various environment and intermediate
stages until the BSeR becomes mature. Figure 1 depicts the architecture.

.. image::
   images/bser_ref_imp/BSER_RI_Architecture.png
   :width: 520pt
   :alt: BSeR Reference Implementation Architecture

**Figure 1**\ : BSeR Reference Implementation Architecture


BSeR IG defines two main system roles, initiator and recipient. Initiator is a system in the clinical provider site that composes
electronic referral (e-Referral) request and sends to recipient. Recipient on the other hand is a system in the service provider
site that consumes the e-referral request(s), processes the request(s), and responds with feecbacks.

The initiator has a BSeR App that implements the following features for the clincal providers,

* Authenticating and authorization using SMART on FHIR with the EHR to access patient data.
* User interface or dashboard for providers to compose the e-Referral request and send to a service provider.
* View or import of feedback data from service provider.
* Provides an *FHIR messaging operation* endpoint for recipient to send feedbacks

.. note::
   Detail information about the *FHIR messaging operation* can be found from https://hl7.org/fhir/R4/messageheader-operation-process-message.html.

   Although *FHIR messaging operation* is not required by BSeR FHIR IG, it is recommended so that systems can have common
   standardized way of exchanging data.

Users of BSeR App in the intiator are clinical providers who refer patients to a service provider (recipient). BSeR App in the
initiator is to help users to create e-referral requests as defined in BSeR FHIR IG and send them to service providers at the
recipient side. BSeR App in the initiator is a SMART on FHIR app that complements EHR for BSeR functionality.

The recipient also has a BSeR App that implements the following features for service providers,

* Bridge between BSeR and service management.
* *FHIR messaging operation* endpoint for e-referral request messages.
* Interfaces to communicate with service management (e.g. API, Email, SFTP, etc.)
* Mapping between BSeR FHIR IG data and service management system data.

The architecture describes the BSeR App in the recicpient to support various interfaces to the service management platform.
However, not every service provider is equipped with a modern network technology for the managment tool. To support more
providers, the architecture includes not only APIs but also Emails or File Transfers for the interfaces to the service management
platform.

.. note::
   For recipients with a manual system for the service managment such as emails or sftp, BSeR App may need to provide
   a dashboard for the recipient users to maually trigger the service feedbacks.

BSeR App in the recipient, once receives the e-Referral request, parses the request, responds to the initiator with a HTTP status, and then hands the request data
over to the service management system through the interface(s).


Initiator (Clinical Provider)
-----------------------------
GTRI has developed the proof-of-concept initiator system based on the architecture. The proof-of-concept
implementation is depicted in Figure 2. As it is shown in the Figure 2, BSeR App is broken into two part, UI and engien. UI
provides a dashboard functionality to users and show data elements that need to be captured for each of BSeR use cases. Once the
user clicks on the send button, the engine takes the information, constructs BSeR FHIR IG based e-referral request, and sends
it to the selected recipient.


.. image::
   images/bser_ref_imp/BSER_RI_Initiator_App.png
   :width: 520pt
   :alt: Proof of Concept Implementation of BSeR Initiator System

**Figure 2**\ : Proof of Concept Implementation of BSeR Initiator System


Recipient (Service Provider)
----------------------------

For Recipient, GTRI has developed a recipient simulator. Recipient system needs to parse the e-Referral request messages
appropriately based on the use cases defined in the BSeR IG. The parsed data should then be delivered to the service
management application to process the request. The service management application should then send feedbacks as responses
to the initiator during the course of referred service(s).

The recipient simulator provides an api for e-Referral requests, generates feedbacks and responds with feedbacks. The
feedbacks include accept, declined, status, etc. as defined by BSeR IG. Figure 3 depicts the recipient
simulator.

.. image::
   images/bser_ref_imp/BSER_RI_Recipient_Sim.png
   :width: 460pt
   :alt: Recipient simulator

**Figure 3**\ : Recipient Simulator


Useful Links
------------

Currently, GTRI sandbox is being migrated to new infrastructure. Once this migration is finished, links will be
provided for the service instances.


.. note::
   All artifacts developed for the proof-of-concept implemenations are available in https://github.com/BSeR-PoC.
   Any issues or comments can be made using the GitHub's Issues option under each repository.

