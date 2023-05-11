Introduction
============
The Bidirectional Services eReferral (BSeR) FHIR Implementation Guide (IG) defines how to support referrals between clinical and non-clinical partners using the
FHIR specification.

This companion guide is intended to supplement the Implementation Guide, providing a linear onboarding on how to get started with and understand the nuances of the
BSeR FHIR IG. For specifics such as profile constraints, please always consult the BSeR FHIR IG directly.

Actors
------
There are two core actors involved in the data exchange, broadly described as the "initiator" and "recipient".

**Initiator** - The initiator is the entity which initiates the referral. This is intended to be a clinical healthcare provider for the majority of cases, but the
Implementation Guide does not limit this explicitly and depending on indivudal workflows others, such as intermediary services, may act as an initiator per
the way it is defined for the purposes of the BSeR FHIR IG.

**Recipient** - The recipient is the entity which receives the referral and is responsible for the the requested intervention. For the purposes of the BSeR FHIR
IG, this is a extra-clinical community partner who offers programs to meet patient needs such as chronic condition management or similar services.


Use Cases
---------

The BSeR FHIR Implementation Guide is designed for a number of uses cases, with the intent to support expansion into additional use cases. Use cases which are
currently fully defined include:

- Arthritis
- Diabetes Prevention
- Early Childhood Nutrition
- Hypertension
- Obesity
- Tobacco Use Cessation

For more information on extending into additional use cases, please see the relevant section of this document.


Social Determinants of Health
-----------------------------
Social Determinants of Health (SDoH) are considered an important area of data involved in the process of providing referrals. What constitutes Social
Determinants of Health are broad. For the BSeR FHIR IG, collection is limited to employment status, education level, and general demographic information such as
race and ethnicity.

** TODO: ADD IN A BLURB TO EXPLAIN SDOH DATA COLLECTION FOR THE CDC NEEDS HERE **

In healthcare workflows, handling standardized SDoH data is an active area of development. In the U.S., this is tied heavily with the US Core Data for
Interoperability (USCDI) requirements. For additional information, please see the profile alignment section of this document related to the Gravity SDoH for Clinical
Care Implementation Guide.