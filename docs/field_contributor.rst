.. _dci:contributor:

3. Contributor (MA)
===================

``datacite:contributor``

Cardinality
~~~~~~~~~~~

*Mandatory if applicable*

*Occurence: 0-n*

Definition and Usage Instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The institution or person responsible for collecting, managing, distributing, or otherwise contributing to the development of the resource.

**Do Not Confuse With**

* :ref:`dc:publisher`
* :ref:`dci:creator`
* :ref:`aire:fundingReference`

**Remarks**

* adapted from `DataCite MetadataKernel`_ v4.1

.. _dci:contributor_contributorType:

Attribute contributorType (M)
-----------------------------

The type of contributor of the resource (occurence: 1). Mandatory if *Contributor* is used.

*Controlled list values*

* ContactPerson
* DataCollector
* DataCurator
* DataManager
* Distributor
* Editor
* HostingInstitution
* Producer
* ProjectLeader
* ProjectManager
* ProjectMember
* RegistrationAgency
* RegistrationAuthority
* RelatedPerson
* Researcher
* ResearchGroup
* RightsHolder
* Sponsor
* Supervisor
* WorkPackageLeader
* Other

.. _dci:contributor_contributorName:

Subproperty contributorName (M)
-------------------------------

The name of the contributor (occurence: 1). Mandatory if *Contributor* is used.

.. _dci:contributor_nameType:

Attribute nameType (R)
**********************

The type of name (occurence: 0-1).

*Controlled list values*

* Organizational
* Personal

.. _dci:contributor_familyName:

Subproperty familyName (O)
--------------------------

The surname or last name of the contributor (occurence: 0-1).

.. _dci:contributor_givenName:

Subproperty givenName (O)
-------------------------

The personal or first name of the contributor (occurence: 0-1).


.. _dci:contributor_nameIdentifier:

Subproperty nameIdentifier (R)
------------------------------

Uniquely identifies an individual or legal entity, according to various schemes (occurence: 0-n).

.. _dci:contributor_nameIdentifierScheme:

Attribute nameIdentifierScheme (M)
**********************************

The name of the name identifier scheme (occurence: 1). Mandatory if *nameIdentifier* is used.

.. _dci:contributor_schemeURI:

Attribute schemeURI (R)
***********************

The URI of the name identifier scheme (occurence: 0-1).

.. _dci:contributor_affiliation:

Subproperty affiliation (R)
---------------------------

The organisational or institutional affiliation of the contributor.

Example
~~~~~~~

.. code-block:: xml
   :linenos:

   <datacite:contributors>
	   <datacite:contributor>
	     <datacite:contributorName>Evans, R. J.</datacite:contributorName>
	   <datacite:contributor>
	   <datacite:contributor>
	     <datacite:contributorName>International Human Genome Sequencing Consortium</datacite:contributorName>
	   </datacite:contributor>
   </datacite:contributors>

.. _DataCite MetadataKernel: http://schema.datacite.org/meta/kernel-4.1/