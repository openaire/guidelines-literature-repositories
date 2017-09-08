.. _dci:fundingReference:

4. FundingReference (MA)
========================

4.1 funderName
--------------

Name of the funding provider.

4.2 funderIdentifier
--------------------

Unique identifier of the funding entity.

4.2.1 funderIdentifiertype
^^^^^^^^^^^^^^^^^^^^^^^^^^

Type of the unique identifier of the funding entity.

4.3 fundingStream
-----------------

Name of the funding stream (optional)

4.4 awardNumber
---------------

Project grantId or awardNumber.

4.4.1 awardURI
^^^^^^^^^^^^^^

URI of the project landing page provided by the funder. 

4.5 awardTitle
--------------

Title of the project, award or grant.

**Usage Instruction**

.. include:: projectid.rst

**Since**

OpenAIRE Guidelines v1

**Modified**

adopting fundingReference elements from DataCite schema and funderId; this replaces the ``info:eu-repo/grantAgreement`` syntax.

**Example**

An example utilizing all fields:

.. code-block:: xml
   :linenos:

   <fundingReference>
     <funderName>European Commission</funderName>
     <funderIdentifier funderIdentifierType="Crossref Funder ID">http://doi.org/10.13039/100010661</funderIdentifier>
     <fundingStream>Horizon 2020 Framework Programme</fundingStream>
     <awardNumber awardURI="http://cordis.europa.eu/project/rcn/194062_en.html">643410</awardNumber>
     <awardTitle>Open Access Infrastructure for Research in Europe 2020</awardTitle>
   </fundingReference>

