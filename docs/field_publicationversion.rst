.. _aire:version:

21. Resource Version (R)
===========================

OAIRE Field
~~~~~~~~~~~
``oaire:version``

Usage
~~~~~

*Recommended*: Version (controlled): to indicate the status in the publication process.

Use terms from the COAR Version Types Vocabulary which reuses
terms from the  "Journal Article Versions (JAV): Recommendations of the NISO/ALPSP JAV Technical Working Group".

Usage Instruction
~~~~~~~~~~~~~~~~~

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

   <oaire:version rdf:resource="http://purl.org/coar/version/c_be7fb7dd8ff6fe43">AM</oaire:version>
