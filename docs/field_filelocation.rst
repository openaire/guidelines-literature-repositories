.. _aire:file:

File Location (MA)
==================

``oaire:file``

Cardinality
~~~~~~~~~~~

*Mandatory if Applicable*

*Occurrence: 0-n*

Definition and Usage Instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An unambiguous reference to the files, e.g. fulltext, the resource is associated with. Repeat the property for each associated file.

Property file (MA, 0-n)
-----------------------

Use the HTTP URI of the file as value.

Attribute accessRightsURI (R)
-----------------------------

Use terms from the `COAR Access Right Vocabulary`_.

======================================== ========================
conceptURI                               label
======================================== ========================
http://purl.org/coar/access_right/c_abf2 ``open access``
http://purl.org/coar/access_right/c_f1cf ``embargoed access``
http://purl.org/coar/access_right/c_16ec ``restricted access``
http://purl.org/coar/access_right/c_14cb ``metadata only access``
======================================== ========================

Attribute mimeType (R)
----------------------

Specify the file format. It is recommended to select it from the MIME media type which is registered in IANA. For the full list see http://www.iana.org/assignments/media-types

Attribute objectType (R)
------------------------

Specify the type of object the file represents. Select it from the following controlled list:

* ``fulltext``
* ``dataset``
* ``software``
* ``other``

Example
~~~~~~~

.. code-block:: xml
   :linenos:

   <oaire:file accessRightsURI="http://purl.org/coar/access_right/c_abf2" mimeType="application/pdf" objectType="fulltext" version="4.0.1">http://link-to-the-fulltext.org</oaire:file>

.. _COAR Access Right Vocabulary: http://vocabularies.coar-repositories.org/documentation/access_rights/
