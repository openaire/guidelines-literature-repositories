.. _dc:rightsAccessrights:

15. Access Rights (M)
=====================

``dcterms:accessRights``

**OpenAIRE Definition**

Access right of the resource.

Usage Instruction
~~~~~~~~~~~~~~~~~
*Mandatory*

*Occurences: 1*

Information about the right or mode the resource can be accessed.
If the metadata describe more than one resource, e.g. fulltext and supplementary material, the access right of the main resource should be provided.


Use terms from the `COAR Access Right Vocabulary`_.

======================================== ========================
conceptURI                               label
======================================== ========================
http://purl.org/coar/access_right/c_abf2 ``open access``
http://purl.org/coar/access_right/c_f1cf ``embargoed access``
http://purl.org/coar/access_right/c_16ec ``restricted access``
http://purl.org/coar/access_right/c_14cb ``metadata only access``
======================================== ========================


Example
~~~~~~~

.. code-block:: xml
   :linenos:

   <dcterms:accessRights rdf:resource="http://purl.org/coar/access_right/c_abf2">open access</dcterms:accessRights>

.. _COAR Access Right Vocabulary: http://vocabularies.coar-repositories.org/documentation/access_rights/