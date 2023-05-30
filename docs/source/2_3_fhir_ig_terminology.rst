FHIR IGs: Terminology
=============================================

CodeSystems
^^^^^^^^^^^
Sometimes, a code may not exist for the domain in which an IG is being developed, or a code may need to be used that has not been fully incorporated into a published codesystem. This leads to IG developers needing to create a CodeSystem to contain these codes they may need for providing fixed values or creating a ValueSet binding (more on ValueSets below). The new codesystem needs to have a defined canonical URL that will be used whenever a code from the system is referenced, and all of the defined codes need to have the actual code, a display name, as well as a description. All these items are highly recommended for custom codesystems so an implementer can know what the code means and when it should be used.

ValueSets
^^^^^^^^^
ValueSets are created by IG developers when they would like to constrict a code element to only come from a specific set of codes. This could happen when there's not an appropriate ValueSet that already exists, when using codes from a custom codesystem that do not exist outside of the IG, or you want to limit or expand an existing ValueSet.

Instances
^^^^^^^^^
Instances are also known as examples, but for this guide, they will be referred to as instances since most IG authoring tools refer to them as such and so they do not become confused with the example type of instances. An instance will conform to a given profile (or base resource if needed) to be considered as an instance of a given profile. Most of the time, instances contain more data that one would find in the resource in a production environment as to show implementers the full use of a profile. There are two main different kinds of instances: example and definition instances. Example instances are named because they are examples of the profiles and extensions found in an IG and will be included on the Examples tab of a profile page. Definition instances are conformance items that is an instance of a resource such as a search parameter, operation definition, or questionnaire, and these items will be presented on their own IG page.

Example Instances
~~~~~~~~~~~~~~~~~
Examples instances are created just how you would create any other resource, only now they will be conforming to a certain profile or extension. To mark an example instance as conforming to a profile, there is a profile sub-element in the resource's meta element that would contain the profile's canonical URL. So for example, looking at an example that conforms to the US Core Patient, the element ``Patient.meta.profile[0]`` would have http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient to indicate that its conformant to that profile. Note the [0] at the end of that FHIRPath, this means that a resource could conform to multiple profiles.

