.. _dci:alternativeIdentifier:

Alternate Identifier (R)
========================

``datacite:alternateIdentifier``

Cardinality
~~~~~~~~~~~

*Recommended*

*Occurrence: 0-n*

Definition and Usage Instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An identifier or identifiers other than the primary Identifier applied to the resource being registered. This may be any alphanumeric string which is unique within its domain of issue. May be used for local identifiers. AlternateIdentifier should be used for another identifier of the same instance (same location, same file).

**Remarks**

* adapted from `DataCite MetadataKernel`_ v4.1

Property alternateIdentifier (R, 0-n)
-------------------------------------

Value of the atlernate identifier.

Attribute alternateIdentifierType (M)
-------------------------------------

The type of the AlternateIdentifier (occurrence: 1). Mandatory if *AlternateIdentifier* is used.

The type value is *suggested* in the following list:

.. include:: vocabularies/relatedidentifiertype.rst

Example
~~~~~~~

.. code-block:: xml
   :linenos:

   <datacite:alternateIdentifiers>
      <datacite:alternateIdentifier alternateIdentifierType="URL">http://someUrl</datacite:alternateIdentifier>
   </datacite:alternateIdentifiers>

.. _DataCite MetadataKernel: http://schema.datacite.org/meta/kernel-4.1/