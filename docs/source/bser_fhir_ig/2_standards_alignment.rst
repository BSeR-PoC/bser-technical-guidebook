Standards Alignment
===================

.. note::
   This page provides a discussion of alignment efforts between the BSeR FHIR IG and other major standards and implementation guides. For more information on leveraging other IGs, such as through inheritance, please refer to the general FHIR IG section of this document.

USCDI and the US Core FHIR IG
-----------------------------
The Office of the National Coordinator's United States Core Data for Interoperability standard defines the data that should be able to be handled in health data exchange. In FHIR, this is implemented using the US Core FHIR Implementation Guide. To ensure compliance, the BSeR FHIR IG profiles are built on top of relevant US Core profiles. Alternatively, some US Core profiles are referenced directly.

.. note::
   To identify the version of the underlying or referenced US Core profiles accurately, you should follow the links from the BSeR FHIR IG to the specific US Core profiles, which will take you to an statically versioned URL (e.g., https://hl7.org/fhir/us/core/STU5.0.1/StructureDefinition-us-core-practitioner.html). As USCDI and US Core have updates on a regular basis, versioning discrepancies are commonly encountered. Issues should be caught by the official HL7 FHIR Validator and similar tools, but without being aware of version based constraints it may be difficult to troubleshoot the errors reported.

Profile Inheritance
^^^^^^^^^^^^^^^^^^^
A basic example of US Core inheritance can be seen with the Referral ServiceRequest profile (Link: http://build.fhir.org/ig/HL7/bser/StructureDefinition-referral-servicerequest.html). This profile's "Type" is shown as "USCoreServiceRequestProfile". The US Core ServiceRequest Profile is then derived from the base FHIR ServiceRequest resource. This is largely for validation and more for servers to be concerned with, most implementors do not need to worry about additional handling for this sort of inheritance as conformance to the BSeR profiles ensures conformance to the underlying US Core profile.

Constrained References
^^^^^^^^^^^^^^^^^^^^^^
For implementors, the case of a constrained reference from the BSeR IG to a US Core profile is more salient. A major example in BSeR is the use of the US Core Patient profile. In the BSeR Referral Task profile, the `Task.for` element, which provides a reference to the patient who is the subject of the referral, can be seen to be constrained to explicitly `Reference(US Core Patient Profile)`.

Patient Demographics and Social Determinants of Health
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Core patient demographic information is handled directly in profiles such as the US Core Patient as defined by USCDI. This includes the patient's race and ethnicity, in alignment with the Office of Management and Budget (OMB) Standards for the Classification of Federal Data on Race and Ethnicity. Other major demographic information or some relevant observational data may vary by version of USCDI and US Core, such as Sexual Orientation and Gender Identity (SOGI) data which were not introduced as part of the core Patient data class until later versions.

In addition to demographics, USCDI defines several data elements related to SDoH data and workflows explicitly which are addressed through the Gravity SDoH for Clinical Care FHIR IG. This IG is discussed more below.

Additional Resources:
* https://www.healthit.gov/isa/united-states-core-data-interoperability-uscdi
* https://hl7.org/fhir/us/core/
* https://orwh.od.nih.gov/toolkit/other-relevant-federal-policies/OMB-standards


Gravity Social Determinants of Health for Clinical Care
-------------------------------------------------------
** TODO: Placeholder. Under active development/revision in the IG. **


Occupational Data for Health
----------------------------
The Occupational Data for Health (ODH) FHIR IG is heavily adopted for usage in standardizing data relating to occupation, such as usual work or industry. The BSeR FHIR IG leverages the ODH FHIR IG's Employment Status profile to represent the subject of the referral's current state of employment, which may impact referral criteria.

** TODO: Need feedback on CDC/YUSA/etc. on this section to determine relevance/usage of some data. **