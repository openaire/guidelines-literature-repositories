.. _dci:publisher:

Publisher (MA)
==============

``datacite:publisher``

Cardinality
~~~~~~~~~~~

*Mandatory if applicable*

*Occurrence: 0-n*

Definition and Usage Instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**DCMI Definition**

An entity responsible for making the resource available. Examples of a Publisher include a person, an organization, or a service. Typically, the name of a Publisher should be used to indicate the entity.

**Usage Instruction**

The (commercial or non-commercial) publisher of the resource; not the (sub)institution the author is affiliated with. Publisher is used only in the bibliographic / functional sense, not an organisational one. Use only the full name of the given (commercial) publisher, not the name of an organization or institute that is otherwise [in a broader sense] associated with the creator.

With university publications place the name of the faculty and/or research group or research school after the name of the university. In the case of organizations where there is clearly a hierarchy present, list the parts of the hierarchy from largest to smallest, separated by full stops. If it is not clear whether there is a hierarchy present, or unclear which is the larger or smaller portion of the body, give the name as it appears in the eprint.

The use of publisher names from authority lists constructed according to local or national thesaurus files is optional.

**Do Not Confuse With**

* :ref:`dci:contributor`
* :ref:`dci:creator`

In most cases the publisher and the creator are not the same.


**Remarks**

* introduced in `DRIVER Guidelines v2 element publisher`_
* adapted from `DataCite MetadataKernel`_ v4.7

Property publisher (MA, 0-n)
----------------------------

Use the name of the publisher as value.

Attribute publisherIdentifier (R)
-----------------------------------

Uniquely identifies the publisher, according to various schemes.

* https://ror.org/037wpkx04 
* https://wikidata.org/wiki/Q29673
* https://doi.org/10.25504/FAIRsharing.066ce6

Attribute publisherIdentifierScheme (M)
-----------------------------------

The type of the publisherIdentifier (occurrence: 1). Mandatory if *publisherIdentifier* is used.

.. include:: vocabularies/publisherIdentifierScheme.rst

Attribute schemeURI (R)
-----------------------------------

The URI of the publisherIdentifierScheme (occurrences: 0-1).

**Allowed values, examples, other constraints**

Examples:

https://ror.org/
https://www.wikidata.org/wiki/
https://doi.org/

Attribute lang (O)
-----------------------------------

The language of the publisher name (occurrences: 0-1).

**Allowed values, examples, other constraints**

Use the ``xml:lang`` attribute to indicate the language of the title. The value of the attribute should be chosen from IETF BCP 47, the `IANA Language Subtag Registry <http://www.iana.org/assignments/language-subtag-registry>`_.

Example
~~~~~~~

.. code-block:: xml
   :linenos:

   <datacite:publisher xml:lang="en" publisherIdentifier="https://ror.org/0198xy071" publisherIdentifierScheme="ROR" schemeURI="https://ror.org/">
     Milano University Press
   </datacite:publisher>
