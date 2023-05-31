Profile Breakdown and Bundle Structure
======================================
** TODO Note: As of this writing (2023-05-30) the guide is undergoing heavy revision for the 2.0.0 release. Certain details are pending the complete 2.0.0 version. **

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
** TODO: Placeholder. Under active development/revision in the IG. **


BSeR Initiator and Recipient Profiles
-------------------------------------
Relevant Profiles:

- BSeR Referral Initiator PractitionerRole
- BSeR Referral Recipient PractitionerRole
- BSeR Practitioner
- BSeR Organization
- BSeR Service Delivery Location

There are two BSeR profiles constraining PractionerRole, one for the initiator and one for the recipient. In base FHIR, the PractitionerRole is used to connect a Practitioner, as an individual, to specific organizations or services.

In BSeR, in addition to the US Core PractitionerRole constraints, the Referral Initiator PractitionerRole requires (cardinality of `1..1`) references to both a BSeR Practitioner and BSeR Organization, with an additional optional reference (cardinality of `0..1`) to the BSeR Service Delivery Location. Note that the three non-PractitionerRole profiles are generic to both the initiator and recipient. This set of profiles should capture all relevant information as determined by the referrer's system, typically in the form of the referring healthcare provider as the BSeR Practitioner profile and then the referrer's organization as the BSeR Organization profile. The BSeR Service Delivery Location may be included here if relevant, for example if it is important to represent a specific, more granular, source of the referral not addressed by the Organizatiion (e.g., "Referred by Dr. Smith at Health USA from the Atlanta office").

** TODO: Discuss the above a bit with Lantana to ensure intent. **

For the Referral Recipient, the related PractitionerRole has no explicit requirements. If the information is known at time of referral creation, it should be included, though in many cases information such as the individual provider or service delivery location might not be known by the initiator depending on the recipient organization's handling of referrals.

** TODO: Break out "required" vs "optional" a bit more to focus on onboarding with the required elements, and split up scope of concerns by initiator and recipient. **


BSeR Referral Request Document Bundle
-------------------------------------
** TODO: Placeholder. Under active development/revision in the IG. -- Need to see how the bundle nesting plays out before addressing this and the following sections. **


BSeR Referral Feedback Document Bundle
--------------------------------------
** TODO: Placeholder. Under active development/revision in the IG. **
