.. _dci:creator:

Creator (M)
===========

``datacite:creator``

Cardinality
~~~~~~~~~~~

*Mandatory*

*Occurrence: 1-n*

Definition and Usage Instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The authors of the publication in priority order. May be a corporate/institutional or personal name.

**Do Not Confuse With**

* :ref:`dci:contributor`
* :ref:`dc:publisher`

**Remarks**

* adapted from `DataCite MetadataKernel`_ v4.1

Property creator (M, 1-n)
-------------------------


.. _dci:creator_creatorName:

Subproperty creatorName (M)
---------------------------

The name of the author (occurrence: 1). The format should be: family, given. Non-roman names may be transliterated according to the
`ALA-LC <http://www.loc.gov/catdir/cpso/roman.html>`_ schemas.

.. _dci:creator_nameType:

Attribute nameType (R)
**********************

The type of name (occurrence: 0-1).

.. include:: vocabularies/nametype.rst

.. _dci:creator_givenName:

Subproperty givenName (R)
-------------------------

The personal or first name of the author.

.. _dci:creator_familyName:

Subproperty familyName (R)
--------------------------

The surname or last name of the author.

.. _dci:creator_nameIdentifier:

Subproperty nameIdentifier (R)
------------------------------

Uniquely identifies an individual or legal entity, according to various schemes (occurrences: 0-n).
The format is dependent upon scheme.

.. note::
   OpenAIRE recommends including a nameIdentifier such as an ORCID or a ISNI if available.


.. _dci:creator_nameIdentifier_nameIdentifierScheme:

Attribute nameIdentifierScheme (M)
**********************************

The name of the name identifier scheme (occurrence: 1).
Mandatory if nameIdentifier is used.

.. _dci:creator_nameIdentifier_schemeURI:

Attribute schemeURI (R)
***********************

The URI of the name identifier scheme (occurrence: 0-1).

.. _dci:creator_affiliation:

Subproperty affiliation (R)
---------------------------

The organizational or institutional affiliation of the creator (occurrence: 0-n).

Example
~~~~~~~
.. code-block:: xml
   :linenos:

   <datacite:creators>
     <datacite:creator>
       <datacite:creatorName>Evans, R.J.</datacite:creatorName>
       <datacite:affiliation>Institute of Science and Technology</datacite:affiliation>
       <datacite:nameIdentifier nameIdentifierScheme="ORCID"
                       schemeURI="http://orcid.org">
         1234-1234-1234-1234
       </datacite:nameIdentifier>
     </datacite:creator>
   </datacite:creators>

.. _DataCite MetadataKernel: http://schema.datacite.org/meta/kernel-4.1/