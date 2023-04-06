FHIR Implementation Guides (IGs)
================================

Introduction
------------
This document is intended to be an introduction to FHIR Implementation Guides (commonly referred to as FHIR IGs) and how they are used, as well as some examples of what an implementation guide would normally contain and links to more in-depth reading. This document is not intended to be a complete walkthrough of everything about FHIR IGs but should be a good beginning point for a user to understand what they mean and how to begin using them. 
 
IGs contain two different kinds of resource references:

* Contents:  A set of logical statements which implementations must conform to, these are almost always conformance resources (see Definition Instances for an exception to this) 
* Examples: Examples that illustrate the intent of the profiles defined in the IG 
 
Why do IGs exist? Why doesn’t FHIR cover everything?
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
FHIR IGs developed and maintained by HL7 must go through a balloting process, like how the FHIR spec evolves over time. This means that “popular” IGs often have multiple versions, culminating in a “Build” (or Continuous Integration/Continuous Development [CI/CD]) version that should be considered volatile and **can change at any time**. After passing a balloting process for the first time, the IG will be released formally as Standard for Trial Use (STU) 1. Every time the IG passes a ballot, they can formally increment the STU version. For example, the US Core IG’s current publication is STU 4 (with STU 5 being a work in progress) and the eCR IG’s current publication is STU 1 (with STU2 being a work in progress). 
 
StructureDefinition Resource 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Profiles and extensions are going to take form as a FHIR StructureDefinition resource. Every FHIR resource has an underlying StructureDefinition, as this is how data elements are defined as well as their associated rules. By creating a StructureDefinition that defines a profile on a certain resource, this allows the definitions of the structures to be shared and published through repositories of structure definitions, compared with each other, and used as the basis for code, report, and UI generation. These are almost always created using a point-and-click software or by using FHIR ShortHand, more on these tools can be found in IG Creation Tools. 
 
FHIRPath 
^^^^^^^^
Please note that this document may make use of “FHIRPath” to provide a consistent reference to FHIR data structures. FHIRPath provides for a path string from a base resource through elements and nested elements within a resource, along with some accompanying functions where needed. This document will only be using the path notation itself. For an example, the Patient resource has an element called “name”. A name is a FHIR data type of “HumanName” which consists of several additional elements that you would expect to be associated with a name, such as “given”, “family”, “suffix”, and so forth. So, to reference the entire name element consisting of all these elements, the following notation is used: Patient.name. To then reference a specific sub-element, it would simply take the reference chain one further: Patient.name.given.  
 
Please be aware as well that FHIR uses “0 indexing” for list items—elements that can have more than one occurrence (maximum cardinality greater than 1). In the case of the “HumanName” type, given is a list element with 0..* while “family” is not, with a 0..1 cardinality. Given the use of “0 indexing”, the first “given” of the first “name” would be referenced as: Patient.name[0].given[0]. **Please be aware that usages of “[x]” are not intended to indicate indexing. “[x]” is a specific FHIR notation for choice of data type elements.** 
 
Example FHIR IGs 
^^^^^^^^^^^^^^^^
Listed below are a few sample FHIR IGs that can be browsed to see more complete examples of IGs (note that these are all linked to the most recent published STU versions, **NOT** the CI/CD versions). All examples used in this document will come from the US Core IG. 

* US Core (https://www.hl7.org/fhir/us/core/) 
* Electronic Case Reporting (eCR) (http://hl7.org/fhir/us/ecr/) 
* Vital Records Mortality and Morbidity Reporting (a.k.a. VRDR) (http://hl7.org/fhir/us/vrdr/) 
* Occupational Data for Health (ODH) (http://hl7.org/fhir/us/odh/) 

Profiles 
--------
Profiles are going to be the most common conformance resource found in a FHIR IG. A profile is a set of rules around how a FHIR resource should be used in the context of the IG, as well as any additional elements that may need to be added to support the use case of the IG. Profiles can be created for any FHIR resource needed for the context of the IG, such as Patient, Condition, or Observation. There are at least six different ways that a profile can constrict or “change” (change being a loose term since profiles are not changing the base FHIR specification) a FHIR resource: 

* Extending a data element by adding an Extension (see Extensions for more detail) 
* Changing the cardinality of an element 
* Restricting an allowed data type for a choice element 
* Fixing a value of an element 
* Constricting the value set from which a code, Coding, or CodeableConcept can come from for a data element 
* Adding a flag to a data element 
 
Changing the Cardinality 
^^^^^^^^^^^^^^^^^^^^^^^^
Every data element in a FHIR resource has a cardinality: the lower and upper bounds for how often an element can appear in a resource. This is represented in the following notation in the FHIR specification: lower .. upper. The most common cardinalities are 0..1 (not required but the element can only exist once in the instance of a resource), 0..* (not required but the element can exist infinitely many times in the instance of a resource), 1..1 (required but the element can only exist once in the instance of a resource), and 1..* (required but the element can exist infinitely many times in the instance of a resource). This cardinality can only be restricted within the bounds of the base FHIR specification; it cannot be expanded. The table below shows an example of what is and isn’t allowed: 

+------------------------+------+------+------+------+------+
| Derived (across)       | 0..0 | 0..1 | 0..n | 1..1 | 1..n |
| Base (down)            |      |      |      |      |      |
+========================+======+======+======+======+======+
|  0..1                  | Yes  | Yes  |  No  | Yes  |  No  |
+------------------------+------+------+------+------+------+
|  0..*                  | Yes  | Yes  | Yes  | Yes  | Yes  |
+------------------------+------+------+------+------+------+
|  1..1                  |  No  |  No  |  No  | Yes  |  No  |
+------------------------+------+------+------+------+------+
|  1..*                  |  No  |  No  |  No  | Yes  | Yes  |
+------------------------+------+------+------+------+------+

Restricting a Choice Element 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Within the base FHIR specification, there are elements labeled with a [x] that are called choice elements, these elements can take the form of multiple data types depending on the implementation. For example, the value[x] element in the Observation resource can take on one of 12 different data types depending on the implementation. A profile can restrict these choice elements to either a subset of the original choices or a single data type. This also applies to elements that have a type of Reference with multiple choices of other resources for the reference, it can even be restricted to be a Reference to a resource that conforms to another one of the IG’s profiles. 
 
Fixed Values and Bindings 
^^^^^^^^^^^^^^^^^^^^^^^^^
For some data elements in FHIR, there is a fixed value, which means that that element can only equal that fixed value in a data structure (if it has 1..n cardinality, it will always be in any instance of that resource but 0..n means that it’s not required to exist in any instance of the resource). For some other data elements (always elements with a code, Coding, or CodeableConcept data type), there might be a binding with a defined value set. In the FHIR specification, there are four different binding strengths that can exist for the relationship between a data element and a value set, shown in the below table (taken from the FHIR specification): 

+------------+----------------------------------------------------------------------------------------------------------------------------------+
| Strength   | Definition                                                                                                                       |
+============+==================================================================================================================================+
| Required   | To be conformant, the concept in this element SHALL be from the specified value set                                              |
+------------+----------------------------------------------------------------------------------------------------------------------------------+
| Extensible | To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can |
|            | apply to the concept being communicated. If the value set does not cover the concept (based on human review), alternate codings  |
|            | (or, data type allowing, text) may be included instead.                                                                          |
+------------+----------------------------------------------------------------------------------------------------------------------------------+
| Preferred  | Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be      |
|            | considered conformant.                                                                                                           |
+------------+----------------------------------------------------------------------------------------------------------------------------------+
| Example    | Instances are not expected or even encouraged to draw from the specified value set. The value set merely provides examples of    |
|            | the types of concepts intended to be included.                                                                                   |
+------------+----------------------------------------------------------------------------------------------------------------------------------+

Preferred is going to be the least common binding strength found both in the FHIR specification as well as any FHIR IGs, as most FHIR IGs are going to make use of the “required” binding strength since they are constricting the base specification to a specific use case. 
 
Value sets must exist somewhere for a data element to have a binding relationship with it. Most commonly they will be found within the realm of HL7 terminology, but can also exist within CDC’s PHINVADS, NIH’s VSAC, or can be defined within the FHIR IG as a ValueSet within the IG (see ValueSets for more information on custom ValueSets). 
 
The table below shows how a binding strength could be changed in a profile (note that the constraining profile can change either the strength or the value set of the bidning, but whatever the profile does, it cannot make codes valid that are invalid in the base specification): 

+------------------------+----------+------------+-----------+---------+
| Derived (across)       | required | extensible | preferred | example |
| Base (down)            |          |            |           |         |
+========================+==========+============+===========+=========+
|  requires              | Yes      | No         | No        |     No  |
+------------------------+----------+------------+-----------+---------+
|  extensible            | Yes      | Yes        | No        |     No  |
+------------------------+----------+------------+-----------+---------+
|  preferred             | Yes      | Yes        | Yes       |     No  |
+------------------------+----------+------------+-----------+---------+
|  example               | Yes      | Yes        | Yes       |    Yes  |
+------------------------+----------+------------+-----------+---------+


Flagging a Data Element 
^^^^^^^^^^^^^^^^^^^^^^^
The final way explored in this document that a profile can constrict a FHIR resource is by adding a flag to the data element. This almost always occurs with a mustSupport flag, where an IG can add this flag to indicate that systems claiming to conform to a given profile must "support" the element. This is distinct from cardinality; it is possible to have an element with a minimum cardinality of 0 but still expect systems to support the element. Note that the base FHIR specification does not define “support,” but if a profile chooses to include the flag, it must also describe what kind of “support” is expected. Examples of this include: 

* The system must be able to store and retrieve the element 
* The system must display the element to the user and/or allow the user to capture the element via the UI 
* The element must appear in an output report 
* The element must be considered when performing decision support, calculations, or other processing 

Slicing 
^^^^^^^
A common feature found in profiles in a FHIR IG is slicing. Slicing is the act of taking an element that may appear multiple times (for example, in a list) and splitting the list into a series of sub-lists, each with different restrictions on those sub-lists. This is an example taken from the FHIR specification: 

.. image:: 
   images/fhir_slicing.png
   :alt: FHIR Slicing 
   
