.. _dci:contributor:

Contributor (MA)
================

``datacite:contributor``

Cardinality
~~~~~~~~~~~

*Mandatory if applicable*

*Occurrence: 0-n*

Definition and Usage Instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The institution or person responsible for collecting, managing, distributing, or otherwise contributing to the development of the resource.

**Do Not Confuse With**

* :ref:`dc:publisher`
* :ref:`dci:creator`
* :ref:`aire:fundingReference`

**Remarks**

* adapted from `DataCite MetadataKernel`_ v4.1

Property contributor (MA, 0-n)
------------------------------


.. _dci:contributor_contributorType:

Attribute contributorType (M)
-----------------------------

The type of contributor of the resource (occurrence: 1). Mandatory if *contributor* is used.

.. include:: vocabularies/contributortype.rst

.. _dci:contributor_contributorName:

Subproperty contributorName (M)
-------------------------------

The name of the contributor (occurrence: 1). Mandatory if *Contributor* is used.

.. _dci:contributor_nameType:

Attribute nameType (R)
**********************

The type of name (occurrence: 0-1).

.. include:: vocabularies/nametype.rst

.. _dci:contributor_familyName:

Subproperty familyName (O)
--------------------------

The surname or last name of the contributor (occurrence: 0-1).

.. _dci:contributor_givenName:

Subproperty givenName (O)
-------------------------

The personal or first name of the contributor (occurrence: 0-1).


.. _dci:contributor_nameIdentifier:

Subproperty nameIdentifier (R)
------------------------------

Uniquely identifies an individual or legal entity, according to various schemes (occurrence: 0-n).

.. _dci:contributor_nameIdentifierScheme:

Attribute nameIdentifierScheme (M)
**********************************

The name of the name identifier scheme (occurrence: 1). Mandatory if *nameIdentifier* is used.

.. _dci:contributor_schemeURI:

Attribute schemeURI (R)
***********************

The URI of the name identifier scheme (occurrence: 0-1).

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