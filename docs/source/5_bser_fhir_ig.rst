BSeR FHIR Implementation Guide
==============================

The Bidirectional Services eReferral (BSeR) FHIR Implementation Guide (IG) defines how to support referrals between clinical and non-clinical partners using the
FHIR specification.

Use Cases
---------

The guide is designed for a number of uses cases with the intent to support expansion into additional use cases. Use cases which are
currently fully defined include:

- Arthritis
- Diabetes Prevention
- Early Childhood Nutrition
- Hypertension
- Obesity
- Tobacco Use Cessation

Overview
--------
To support the BSeR workflows, the IG can be broadly broken down into three distinct areas:

- Bidirectional Data Exchange
- Workflow Management
- Patient Information

 Data models are the FHIR profiles which represent both structured artifacts through FHIR Profiles and supporting resources involved in the
act of data exchange (e.g., "message" type Bundles, MessageHeaders) as well as the way to structure the documents contained within messages (e.g.,
"document" type Bundles, individual resources like clinical Observations or the Patient).

Bidirectional Data Exchange
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The BSeR Implementation Guide documents data exchange using a messaging model, wherein a referral initiator, typically a clinical entity, will send a FHIR
Message Bundle to a recipient, typically a non clincial partner. (Historically, this would be the domain of the HL7v2 messaging standard.)

.. image::
   images/bser_fhir_ig/basic_messaging.png
   :alt: Basic Messaging Example

The bi-directionality aspect of the implementation guide then expands upon this model, laying out not just the initial messaging but iterative messaging
between the initiator and recipient. As it is part of a complete messaging cycle, the roles of "initiator" and "recipient" are defined consistently based on
the *initialization* of the exchang and the entities involved are described this way even in subsequent messages going the opposite direction. The directionality
of the messages is described as "request" (initiator to recipient) and "feedback" (recipient to feedback).

.. image:: 
   images/bser_fhir_ig/bi_messaging.png
   :alt: Bidirectional Messaging 

In the context of FHIR, the messaging is captured in the guide through FHIR resources or API expectations such as operations. This is the outermost
layer of the BSeR data structure, starting with the BSeR Referral Message Bundle profile. That profile goes together with the BSeR Referral MessageHeader profile.

Workfow Management
^^^^^^^^^^^^^^^^^
Workflow management is handled through the ServiceRequest, Task, Coverage, and a supplemental Observation resource. These capture the current state of the
referral (e.g., "Accepted"), and additional non-clinical/non-intervention related data such as insurance coverage or system specific identifiers on both the
initiator and recipient sides.

Patient Information
^^^^^^^^^^^^^^^^^^^
The majority of the BSeR FHIR IG profiles cover information directly related to the subject of the referral. This part of the IG is broken
up heavily by the individual use case, with Early Childhood Nutrition having a slightly more divergent structure as resources may refer to either the child or
guardian. In terms of clinical data the difference is usually subtle in other use cases. For example, diabetes Prevention will capture HA1C values as supporting
information, whereas other use cases do not, though most will tend to capture basic data such as the subject's weight. 

The information expected from each entity also varies. The initiation of the referral includes a limited set of clinical data from the initiator, and is the area
with the least variance. This data may be used to allow non-clinical entities to decide whether a referral meets their criteria, or provide additional context.
During an active intervention, the recipient's feedback bundle will include a different set of data captured, again based on use case. The data here may be more
observational in nature, as well as include information on scheduling or the number of missed appointments.


Social Determinants of Health/Gravity Alignment
-----------------------------------------------
Social Determinants of Health (SDoH) are considered an important area of data involved in the process of providing referrals. The standardization of SDoH data
in healthcare workflows is an active area of development, rooted in the US Core Data for Interoperability (USCDI) requirements. To this end, the BSeR FHIR IG is
being aligned with the Gravity SDoH for Clinical Care FHIR Implementation Guide. For more information on Gravity and SDoH, please see the appropriate section
of this document.

The Gravity SDoH home page can be found at https://hl7.org/fhir/us/sdoh-clinicalcare/.

Technical Structure
-------------------
(Note: As of this writing (2023-05-10) the guide is undergoing heavy revision for the 2.0.0 release. Certain details are pending the complete 2.0.0 version.)

BSeR Referral Message Bundle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The BSeR Referral Message Bundle is the wrapper for every message exchanged during the BSeR workflow. In base FHIR, a Message Bundle is a Bundle resource with a
type set to `"message"` and the first entry being a MessageHeader resource. The BSeR Referral Message Bundle profile additionally adds three slices in the list
of entries for Employment Status, Patient Consent, and Employment Level.

.. include:: examples/bser_fhir_ig/basic-message-bundle.json
    :code: json