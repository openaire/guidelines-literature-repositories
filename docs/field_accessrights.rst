.. _aire:accessrights:

15. Access Rights (M)
=====================

``oaire:accessRights``

Cardinality
~~~~~~~~~~~

*Mandatory*

*Occurence: 1*

Definition and Usage Instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Access right of the resource.

Information about the right or mode the resource can be accessed.
If the metadata describe more than one resource, e.g. fulltext and supplementary material, the access right of the main resource should be provided.

**Remarks**

* former versions of the OpenAIRE Guidelines used the `info:eu-repo-Access-Terms vocabulary <https://wiki.surfnet.nl/display/standards/info-eu-repo/#info-eu-repo-AccessRights>`_.

Attribute uri (M)
-----------------

Use terms from the `COAR Access Right Vocabulary`_ (occurence: 1).

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

   <oaire:accessRights uri="http://purl.org/coar/access_right/c_abf2">open access</oaire:accessRights>

.. _COAR Access Right Vocabulary: http://vocabularies.coar-repositories.org/documentation/access_rights/