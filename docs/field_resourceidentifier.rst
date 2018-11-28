.. _dci:identifier:

Resource Identifier (M)
=======================

``datacite:identifier``

Cardinality
~~~~~~~~~~~

*Mandatory*

*Occurrence: 1*

Definition and Usage Instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Identifier is a unique string that identifies a resource.

**Usage Instruction**

Recommended best practice is to identify the resource by means of a string or number conforming to a formal identification system. Example formal identification systems include the Uniform Resource Identifier (URI), the Uniform Resource Locator (URL), the Digital Object Identifier (DOI), and the ``URN:NBN``. Also this can be a direct URL, or a redirection URL, like PURL, HANDLE or other international resolution mechanisms.

The ideal use of this element is to use a direct link or a link to a jump-off page (persistent URL) from ``identifier`` in the metadata record to the digital resource or a jump-off page.

Smart practice:

* use a stable URL

**Do Not Confuse With**

* :ref:`dci:alternativeIdentifier` (Use ``datacite:alternativeIdentifier`` to list other identifiers than the primary identifier applied to the same resource.)
* :ref:`dci:relatedIdentifier` (Use ``datacite:relatedIdentifier`` to refer to related resources.)
* :ref:`aire:file` (Use ``oaire:file`` to point to the resource being desccribed by this metadata, e.g. the fulltext file.)
* :ref:`dc:source` (Use ``dc:source`` for bibliographic citation of the originating resource.)

Property identifier (M, 1)
--------------------------

Use the identifier link as value.

Attribute identifierType (M)
----------------------------

The type of the Identifier (occurrences: 1).

**Allowed values, examples, other constraints**

.. include:: vocabularies/identifiertype.rst

.. note::
   Unlike DataCite, OpenAIRE allows for DOIs and other types of identifiers.

Example
~~~~~~~

In this example the handle redirects to the jump-off page. A jump-off page is a good way to refer to. The end-user has the opportunity to see more information about the object(s) he has found, see the context and enjoy the other services a local repository has to offer:

.. code-block:: xml
   :linenos:

   <datacite:identifier identifierType="Handle">http://hdl.handle.net/1234/5628</datacite:identifier>
