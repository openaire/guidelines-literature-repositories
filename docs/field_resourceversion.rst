.. _aire:version:

Resource Version (R)
====================

``oaire:version``

Cardinality
~~~~~~~~~~~

*Recommended*

*Occurrence: 1*

Definition and Usage Instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Depening on the resource type this property is used to indicate

* the version number of a dataset or software
* the status in the publication process of journal articles.

**Usage**

For *software* and *dataset* resources any string will be accepted, but a semantically-versioned tag is recommended.
See <https://semver.org> for more information on semantic versioning.

For *preprints* and *articles* in the journal publishing process a controlled term must be used from the  "Journal Article Versions (JAV): Recommendations of the NISO/ALPSP JAV Technical Working Group" (`JAV`_). In tis case the property *must* include the attribute 'uri'.
The value of the property is the corresponding label of the HTTP URI.

Property version (R, 1)
------------------------

Use either a version number or the label of the vocabulary term as value.

Attribute uri (MA)
------------------

Allowed HTTP URI are from the `COAR Version Types Vocabulary`_.

**Version (controlled):**

=============================================== ========== =================================
conceptURI                                      label      comment
=============================================== ========== =================================
http://purl.org/coar/version/c_b1a7d7d4d402bcce ``AO``     Author's Original
http://purl.org/coar/version/c_71e4c1898caa6e32 ``SMUR``   Submitted Manuscript Under Review
http://purl.org/coar/version/c_ab4af688f83e57aa ``AM``     Accepted Manuscript
http://purl.org/coar/version/c_fa2ee174bc00049f ``P``      Proof
http://purl.org/coar/version/c_970fb48d4fbd8a85 ``VoR``    Version of Record
http://purl.org/coar/version/c_e19f295774971610 ``CVoR``   Corrected Version of Record
http://purl.org/coar/version/c_dc82b40f9837b551 ``EVoR``   Enhanced Version of Record
http://purl.org/coar/version/c_be7fb7dd8ff6fe43 ``NA``     Not Applicable (or Unknown)
=============================================== ========== =================================

Example
~~~~~~~
.. code-block:: xml
   :linenos:

   <oaire:version>1.0.3</oaire:version>

.. code-block:: xml
   :linenos:

   <oaire:version uri="http://purl.org/coar/version/c_be7fb7dd8ff6fe43">AM</oaire:version>


.. _COAR Version Types Vocabulary: http://vocabularies.coar-repositories.org/documentation/version_types/
.. _JAV: https://www.niso.org/publications/niso-rp-8-2008-jav