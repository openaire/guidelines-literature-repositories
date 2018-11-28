.. _dci:accessrights:

Access Rights (M)
=================

``datacite:rights``

Cardinality
~~~~~~~~~~~

*Mandatory*

*Occurrence: 1*

Definition and Usage Instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Access right of the resource.

Information about the right or mode the resource can be accessed.
If the metadata describe more than one resource, e.g. fulltext and supplementary material, the access right of the main resource should be provided.

Use terms from the `COAR Access Right Vocabulary`_ (occurrence: 1).

======================================== ========================
conceptURI                               label
======================================== ========================
http://purl.org/coar/access_right/c_abf2 ``open access``
http://purl.org/coar/access_right/c_f1cf ``embargoed access``
http://purl.org/coar/access_right/c_16ec ``restricted access``
http://purl.org/coar/access_right/c_14cb ``metadata only access``
======================================== ========================

.. note::
   Unlike DataCite, OpenAIRE restricts the use of this property to indicate the access right. 

**Do Not Confuse With**

* :ref:`aire:licenseCondition` (Use ``oaire:licenseCondition`` for license information related to the resource.)

**Remarks**

* former versions of the OpenAIRE Guidelines used the `info:eu-repo-Access-Terms vocabulary <https://wiki.surfnet.nl/display/standards/info-eu-repo/#info-eu-repo-AccessRights>`_.


Property accessRights (M, 1)
----------------------------

Use the label of the vocabulary term as value.

Attribute uri (M)
-----------------

Use the conceptURI of the vocabulary term.

Example
~~~~~~~

.. code-block:: xml
   :linenos:

   <datacite:rights rightsURI="http://purl.org/coar/access_right/c_abf2">open access</datacite:rights>

.. _COAR Access Right Vocabulary: http://vocabularies.coar-repositories.org/documentation/access_rights/