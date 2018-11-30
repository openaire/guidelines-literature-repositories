.. _dci:title:

.. _dci:title_title:

Title (M)
=========

``datacite:title``

Cardinality
~~~~~~~~~~~

*Mandatory*

*Occurrence: 1-n*

Definition and Usage Instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A name or title by which a resource is known.

**Allowed values, examples, other constraints**

Free text.

**Remarks**

* adapted from `DataCite MetadataKernel`_ v4.1

Property title (M, 1-n)
-----------------------

Use the title name as value. Repeat this property for different title types or title languages.

Attribute lang (O)
------------------

The language of the title (occurrence: 0-1)

Use the ``xml:lang`` attribute to indicate the language of the title. The value of the attribute should be chosen from IETF BCP 47, the `IANA Language Subtag Registry <http://www.iana.org/assignments/language-subtag-registry>`_.


Attribute titleType (O)
-----------------------

The type of Title (occurrences: 0-1).

**Allowed values, examples, other constraints**

.. include:: vocabularies/titletype.rst


Example
~~~~~~~
.. code-block:: xml
   :linenos:

    <datacite:title xml:lang="en-US">
     National Institute for Environmental Studies and Center
     for Climate System Research Japan
    </datacite:title>
    <datacite:title xml:lang="en-US" titleType="Subtitle">A survey</datacite:title>

.. _DataCite MetadataKernel: http://schema.datacite.org/meta/kernel-4.1/