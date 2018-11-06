.. _aire:version:

22. Resource Version (MA)
===========================

``oaire:version``

Cardinality
~~~~~~~~~~~

*Mandatory if applicable*

*Occurence: 0-1*

Definition and Usage Instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Usage**

*Recommended*: Version (controlled): to indicate the status in the publication process.

Terms are reused from the  "Journal Article Versions (JAV): Recommendations of the NISO/ALPSP JAV Technical Working Group" (`JAV`_).

This property *must* include the attribute 'uri'.  Allowed HTTP URI are from the `COAR Version Types Vocabulary`_.
The value of the property is the corresponding label of the HTTP URI.

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

   <oaire:version uri="http://purl.org/coar/version/c_be7fb7dd8ff6fe43">AM</oaire:version>

.. _COAR Version Types Vocabulary: http://vocabularies.coar-repositories.org/documentation/version_types/
.. _JAV: https://www.niso.org/publications/niso-rp-8-2008-jav