.. _aire:fundingReference:

Funding Reference (MA)
======================

``oaire:fundingReference``

Cardinality
~~~~~~~~~~~

*Mandatory if applicable*

*Occurrence: 0-n*

Definition and Usage Instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Information about financial support (funding) for the resource being registered.

**Usage Instruction**

.. include:: projectid.rst

**Remarks**

* introduced as ``info:eu-repo/grantAgreement`` in previous versions of the OpenAIRE Guidelines
* adopting fundingReference element and subproperties from DataCite MetadataKernel v4.1 which replaces the ``info:eu-repo/grantAgreement`` syntax.
* adding subproperty fundingStream to this application profile

Property fundingReference (MA, 0-n)
-----------------------------------

Repeat this property to indicate several different funders and projects.

Subproperty funderName (M)
--------------------------

Name of the funding provider (occurrence: 1). Mandatory if *FundingReference* is used.

Subproperty funderIdentifier (R)
--------------------------------

Unique identifier of the funding entity (occurrence: 0-1).

Attribute funderIdentifiertype (R)
**********************************

Type of the unique identifier of the funding entity (occurrence: 0-1).

.. include:: vocabularies/funderidentifiertype.rst

see also `Crossref Funder Registry`_

Subproperty fundingStream (O)
-----------------------------

Name of the funding stream (optional) (occurrence: 0-1).

Subproperty awardNumber (MA)
----------------------------

Project grantId or awardNumber (occurrence: 1).

Attribute awardURI (R)
**********************

URI of the project landing page provided by the funder for more information about the award (grant) (occurrence: 0-1). 

Subproperty awardTitle (R)
--------------------------

Title of the project, award or grant (occurrence: 0-1).


Example
~~~~~~~

Examples utilizing all fields:

.. code-block:: xml
   :linenos:

   <oaire:fundingReferences>
    <oaire:fundingReference>
     <oaire:funderName>European Commission</datacite:funderName>
     <oaire:funderIdentifier funderIdentifierType="Crossref Funder ID">http://doi.org/10.13039/100010661</oaire:funderIdentifier>
     <oaire:fundingStream>Horizon 2020 Framework Programme</oaire:fundingStream>
     <oaire:awardNumber awardURI="http://cordis.europa.eu/project/rcn/194062_en.html">643410</oaire:awardNumber>
     <oaire:awardTitle>Open Access Infrastructure for Research in Europe 2020</oaire:awardTitle>
    </oaire:fundingReference>
   </oaire:fundingReferences>
   
 .. code-block:: xml
   :linenos:
   
   <oaire:fundingReferences>
    <oaire:fundingReference>
      <oaire:funderName>Deutsche Forschungsgemeinschaft</datacite:funderName>
      <oaire:funderIdentifier funderIdentifierType="Crossref Funder ID"> http://dx.doi.org/10.13039/501100001659</oaire:funderIdentifier>
      <oaire:fundingStream>Transregios</oaire:fundingStream>
      <oaire:awardNumber awardURI="https://gepris.dfg.de/gepris/projekt/276833197">276833197</oaire:awardNumber>
      <oaire:awardTitle>Quantitative Quality Assessment of Computational Photography</oaire:awardTitle>
      </oaire:fundingReference>
    </oaire:fundingReferences>
  
.. code-block:: xml
   :linenos:
   
   <oaire:fundingReferences>
     <oaire:fundingReference>
      <oaire:funderName>SNSF</datacite:funderName>
      <oaire:funderIdentifier funderIdentifierType="ISNI">http://www.isni.org/isni/0000000106723101</oaire:funderIdentifier>
      <oaire:fundingStream>International short research visits</oaire:fundingStream>
      <oaire:awardNumber awardURI="http://p3.snf.ch/project-151094">151094</oaire:awardNumber>
      <oaire:awardTitle>Amygdala fMRI and social cognition in patients with unilateral MTLE and Urbach-Wiethe disease</oaire:awardTitle>  
     </oaire:fundingReference>
   </oaire:fundingReferences>



.. _Crossref Funder Registry: http://fundref.org/services/funder-registry
