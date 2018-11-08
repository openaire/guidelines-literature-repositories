.. _aire:fundingReference:

4. Funding Reference (MA)
=========================

``oaire:fundingReference``

Cardinality
~~~~~~~~~~~

*Mandatory if applicable*

*Occurence: 0-n*

Definition and Usage Instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Information about financial support (funding) for the resource being registered.

**Usage Instruction**

.. include:: projectid.rst

**Remarks**

* introduced as ``info:eu-repo/grantAgreement`` in previous versions of the OpenAIRE Guidelines
* adopting fundingReference element and subproperties from DataCite MetadataKernel v4.1 which replaces the ``info:eu-repo/grantAgreement`` syntax.
* adding subproperty fundingStream to this application profile


Subproperty funderName (M)
--------------------------

Name of the funding provider (occurence: 1). Mandatory if *FundingReference* is used.

Subproperty funderIdentifier (R)
--------------------------------

Unique identifier of the funding entity (occurence: 0-1).

Attribute funderIdentifiertype (R)
**********************************

Type of the unique identifier of the funding entity (occurence: 0-1).

*Controlled list values*

* ISNI
* GRID
* Crossref Funder

see also `Open Funder Registry`_

Subproperty fundingStream (O)
-----------------------------

Name of the funding stream (optional) (occurence: 0-1).

Subproperty awardNumber (MA)
----------------------------

Project grantId or awardNumber (occurence: 1).

Attribute awardURI (R)
**********************

URI of the project landing page provided by the funder for more information about the award (grant) (occurence: 0-1). 

Subproperty awardTitle (R)
--------------------------

Title of the project, award or grant (occurence: 0-1).


Example
~~~~~~~

An example utilizing all fields:

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

.. _Open Funder Registry: http://fundref.org/fundingdata/registry.html