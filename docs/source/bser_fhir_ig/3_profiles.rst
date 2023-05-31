Profile Breakdown and Bundle Structure
======================================
(Note: As of this writing (2023-05-30) the guide is undergoing heavy revision for the 2.0.0 release. Certain details are pending the complete 2.0.0 version.)

BSeR Referral Message Bundle
----------------------------
Relevant Profiles:

- BSeR Referral Message Bundle
- BSeR Referral MessageHeader
- BSeR Patient Consent
- BSeR Education Level
- Occupational Data for Health (ODH) Employment Status

The BSeR Referral Message Bundle is the wrapper for every message exchanged during the BSeR workflow. In base FHIR, a Message Bundle is a Bundle resource with a
type set to `"message"` and the first entry being a MessageHeader resource. For BSeR, this MessageHeader must be compliant to the BSeR Referral MessageHeader
profile. The BSeR Referral Message Bundle profile additionally adds three slices in the list of entries for Employment Status, Patient Consent, and Employment
Level.

.. include:: ../examples/bser_fhir_ig/basic-message-bundle.json
    :code: json


The BSeR Referral MessageHeader constrains the base resource to use references to specific BSeR profiles such as the BSeR Referral Recipient Practitioner Role,
BSeR Referral Initiator Practitioner Role, and the BSeR Referral Task.

BSeR Referral Task and Service Request Profiles
-----------------------------------------------
(Placeholder)

BSeR Initiator and Recipient Profiles
-------------------------------------
Relevant Profiles:

- BSeR Referral Initiator Practitioner Role
- BSeR Referral Recipient Practitioner Role
- BSeR Practitioner
- BSeR Organization
- BSeR Service Delivery Location

There are two BSeR profiles constraining PractionerRole, one for the initiator and one for the recipient.


BSeR Referral Request Document Bundle
-------------------------------------
(Placeholder)


BSeR Referral Feedback Document Bundle
--------------------------------------
(Placeholder)