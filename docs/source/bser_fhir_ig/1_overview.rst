Overview
========
** TODO: Add in additional BSeR Overview Information here based on what CDC would like to cover. **

The Bidirectional Services eReferral (BSeR) FHIR Implementation Guide (IG) defines how to support referrals between clinical and non-clinical partners using the FHIR specification.

This companion guide is intended to supplement the Implementation Guide, providing a linear onboarding on how to get started with and understand the nuances of the BSeR FHIR IG. For specifics such as profile constraints, please always consult the BSeR FHIR IG directly.


Implementating the BSeR FHIR IG
-------------------------------

Implementation of the BSeR FHIR IG requires the participation of diverse groups across multiple organizations. It is helpful to include everyone who may be involved in the implementation process early. This includes, but is not limited to:

* Clinical Teams - Practitioners, Administrative staff, etc. who will be sending referrals
* Non-Clinical Teams - Community organizations or others who will be receiving referrals
* Technical Teams - EMR/EHR or other tool developers, IT specialists, etc.


Use Cases
---------
The BSeR FHIR Implementation Guide is designed for a number of intervention focused use cases, with the intent to support expansion into additional use cases. Use cases which are currently fully defined include:

- Arthritis
- Diabetes Prevention
- Early Childhood Nutrition
- Hypertension
- Obesity
- Tobacco Use Cessation

For more information on extending into additional use cases, please see the relevant section of this document.


Social Determinants of Health
-----------------------------
Social Determinants of Health (SDoH) are an important area of data collection, and may be included as part of the referral process to support both program eligibility as well as public health needs. What constitutes Social Determinants of Health are broad generally, though for the BSeR FHIR IG, collection is limited to employment status, education level, and general demographic information such as race and ethnicity.

** TODO: Add in a blurb to explain SDOH data collection for the CDC needs here **

In the U.S., standardizing SDoH data with FHIR is an active area of development, which is tied in heavily with the US Core Data for Interoperability (USCDI) requirements. For additional information, please see the standards alignment section of this document, which includes discussion of U.S. Core as well as the Gravity SDoH for Clinical Care FHIR Implementation Guide.