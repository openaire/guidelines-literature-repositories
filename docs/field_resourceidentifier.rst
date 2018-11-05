.. _dc:identifier:

14 Resource Identifier (M)
==========================

``dc:identifier``

**DCMI Definition**

An unambiguous reference to the resource within a given context.

(occurences: 1)

**Usage Instruction**

Recommended best practice is to identify the resource by means of a string or number conforming to a formal identification system. Example formal identification systems include the Uniform Resource Identifier (URI), the Uniform Resource Locator (URL), the Digital Object Identifier (DOI), and the ``URN:NBN``. Also this can be a direct URL, or a redirection URL, like PURL, HANDLE or other international resolution mechanisms.

The ideal use of this element is to use a direct link or a link to a jump-off page (persistent URL) from ``dc:identifier`` in the metadata record to the digital resource or a jump-off page.

Smart practice:

* use a stable URL

**Do Not Confuse With**

* :ref:`dci:alternativeIdentifier` (Use ``dci:alternativeIdentifier`` to list other identifiers than the primary identifier applied to the same resource.)
* :ref:`dci:relatedIdentifier` (Use ``dci:relatedIdentifier`` to refer to related resources.)
* :ref:`aire:file` (Use ``oaire:file`` to point to the resource being desccribed by this metadata, e.g. the fulltext file.)
* :ref:`dc:source` (Use ``dc:source`` for bibliographic citation of the originating resource.)

Example
~~~~~~~

In this example the handle redirects to the jump-off page. A jump-off page is a good way to refer to. The end-user has the opportunity to see more information about the object(s) he has found, see the context and enjoy the other services a local repository has to offer:

.. code-block:: xml
   :linenos:

   <dc:identifier>http://hdl.handle.net/1234/5628</dc:identifier>
