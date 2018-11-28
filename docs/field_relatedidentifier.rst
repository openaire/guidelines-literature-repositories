.. _dci:relatedIdentifier:

Related Identifier (R)
======================

``datacite:relatedIdentifier``

Cardinality
~~~~~~~~~~~

*Recommended*

*Occurrence: 0-n*

Definition and Usage Instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An identifier of a related resource other than the primary Identifier applied to the resource being registered. 

**Remarks**

* adapted from `DataCite MetadataKernel`_ v4.1

Property relatedIdentifier (R, 0-n)
-----------------------------------

Use the related identifier as value. Repeat this property for each related identifier.

Attribute relatedIdentifierType (M)
-----------------------------------

The type of the RelatedIdentifier (occurrence: 1). Mandatory if *RelatedIdentifier* is used.

.. include:: vocabularies/relatedidentifiertype.rst

Attribute relationType (M)
--------------------------

Description of the relationship of the resource being registered (A) and the related resource (B) (occurrence: 1). Mandatory if *RelatedIdentifier* is used.

.. include:: vocabularies/relationtype.rst

Attribute relatedMetadataScheme (O)
-----------------------------------

The name of the scheme (occurrences: 0-1).

**Allowed values, examples, other constraints**

Use only with this relation pair: (``HasMetadata``/``IsMetadataFor``).


Attribute schemeURI (O)
-----------------------

The URI of the relatedMetadataScheme (occurrences: 0-1).

**Allowed values, examples, other constraints**

Use only with this relation pair: (``HasMetadata``/``IsMetadataFor``).


Attribute schemeType (O)
------------------------

The type of the relatedMetadataScheme, linked with the schemeURI (occurrences: 0-1).

**Allowed values, examples, other constraints**

Use only with this relation pair: (``HasMetadata``/``IsMetadataFor``).

Examples: ``XSD``, ``DDT``, ``Turtle``

Attribute resourceTypeGeneral (O)
---------------------------------

The general type of the related resource (occurrences: 0-1).

.. include:: vocabularies/resourcetypegeneral.rst

Example
~~~~~~~

.. code-block:: xml
   :linenos:

   <datacite:relatedIdentifiers>
      <datacite:relatedIdentifier relatedIdentifierType="URL" relationType="HasPart">http://someUrl</datacite:relatedIdentifier>
   </datacite:relatedIdentifiers>

.. _DataCite MetadataKernel: http://schema.datacite.org/meta/kernel-4.1/