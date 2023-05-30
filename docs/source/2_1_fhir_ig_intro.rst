FHIR IGs: Introduction
==============================================

This document is intended to be an introduction to FHIR Implementation Guides (commonly referred to as FHIR IGs) and how they are used, as well as some examples of what an implementation guide would normally contain and links to more in-depth reading. This document is not intended to be a complete walkthrough of everything about FHIR IGs but should be a good beginning point for a user to understand what they mean and how to begin using them.

IGs contain two different kinds of resource references:

* Contents:  A set of logical statements which implementations must conform to, these are almost always conformance resources (see Definition Instances for an exception to this)
* Examples: Examples that illustrate the intent of the profiles defined in the IG

Why do IGs exist? Why doesn't FHIR cover everything?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The base FHIR specification describes a set of base resources, frameworks, and APIs that are used in many different contexts in healthcare. However, there is wide variability between jurisdictions and across the healthcare ecosystem around practices, requirements, regulations, and what actions are feasible. For this reason, the FHIR specification is a "platform specification" - it creates a common foundation on which a variety of different solutions are implemented. Because of this, the FHIR specification usually requires further adaptation to contexts of use. Typically, these adaptations specify:

* Rules about which resource elements are or are not used, as well as what additional elements are added that are not part of the base specification (using Extensions)
* Rules about which API features are used, and how
* Rules about which terminologies are used elements
* Descriptions of how the Resource elements and API features map to local requirements and/or implementations

Note that because of the nature of the healthcare ecosystem, there may be multiple overlapping sets of adaptations.

IGs versus the ImplementationGuide resource
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FHIR IGs are not to be confused with the actual ImplementationGuide resource found in the FHIR specification. A FHIR IG is a complete set of profiles, extensions, terminology, and examples that define a set of rules of how a particular interoperability or standards problem is solved using FHIR resources, while the ImplementationGuide resource is a single FHIR resource that defines the logical content of the IG, along with the important entry pages for the publication.

IG Versioning
^^^^^^^^^^^^^
FHIR IGs developed and maintained by HL7 must go through a balloting process, like how the FHIR spec evolves over time. This means that “popular” IGs often have multiple versions, culminating in a “Build” (or Continuous Integration/Continuous Development [CI/CD]) version that should be considered volatile and **can change at any time**. After passing a balloting process for the first time, the IG will be released formally as Standard for Trial Use (STU) 1. Every time the IG passes a ballot, they can formally increment the STU version. For example, the US Core IG's current publication is STU 4 (with STU 5 being a work in progress) and the eCR IG's current publication is STU 1 (with STU2 being a work in progress).

StructureDefinition Resource
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Profiles and extensions are going to take form as a FHIR StructureDefinition resource. Every FHIR resource has an underlying StructureDefinition, as this is how data elements are defined as well as their associated rules. By creating a StructureDefinition that defines a profile on a certain resource, this allows the definitions of the structures to be shared and published through repositories of structure definitions, compared with each other, and used as the basis for code, report, and UI generation. These are almost always created using a point-and-click software or by using FHIR ShortHand, more on these tools can be found in IG Creation Tools.

FHIRPath
^^^^^^^^
Please note that this document may make use of “FHIRPath” to provide a consistent reference to FHIR data structures. FHIRPath provides for a path string from a base resource through elements and nested elements within a resource, along with some accompanying functions where needed. This document will only be using the path notation itself. For an example, the Patient resource has an element called “name”. A name is a FHIR data type of “HumanName” which consists of several additional elements that you would expect to be associated with a name, such as “given”, “family”, “suffix”, and so forth. So, to reference the entire name element consisting of all these elements, the following notation is used: ``Patient.name``. To then reference a specific sub-element, it would simply take the reference chain one further: ``Patient.name.given``.

Please be aware as well that FHIR uses “0 indexing” for list items—elements that can have more than one occurrence (maximum cardinality greater than 1). In the case of the “HumanName” type, given is a list element with 0..* while “family” is not, with a 0..1 cardinality. Given the use of “0 indexing”, the first “given” of the first “name” would be referenced as: ``Patient.name[0].given[0]``. **Please be aware that usages of “[x]” are not intended to indicate indexing. “[x]” is a specific FHIR notation for choice of data type elements.**

Example FHIR IGs
^^^^^^^^^^^^^^^^
Listed below are a few sample FHIR IGs that can be browsed to see more complete examples of IGs (note that these are all linked to the most recent published STU versions, **NOT** the CI/CD versions). All examples used in this document will come from the US Core IG.

* US Core (https://www.hl7.org/fhir/us/core/)
* Electronic Case Reporting (eCR) (http://hl7.org/fhir/us/ecr/)
* Vital Records Mortality and Morbidity Reporting (a.k.a. VRDR) (http://hl7.org/fhir/us/vrdr/)
* Occupational Data for Health (ODH) (http://hl7.org/fhir/us/odh/)