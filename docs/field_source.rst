.. _dc:source:

Source (R)
==========

``dc:source``

Cardinality
~~~~~~~~~~~

*Recommended*

*Occurrence: 0-n*

Definition and Usage Instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**DCMI Definition**

A reference to a resource from which the present resource is derived.

**Usage Instruction**

The present resource may be derived from the *Source* resource in whole or in part. Recommended best practice is to reference the resource by means of a string or number conforming to a formal identification system.

Best practice: Use only when the described resource is the result of digitization of non-digital originals. Otherwise, use *:ref:`dci:relatedIdentifier`*. Optionally metadata about the current location and call number of the digitized publication can be added.

Use: Guidelines for Encoding Bibliographic Citation Information in Dublin Core Metadata (http://dublincore.org/documents/dc-citation-guidelines/).

**Do Not Confuse With**

* :ref:`dci:identifier`

**Remarks**

* introduced in `DRIVER Guidelines v2 element source`_

Property source (R, 0-n)
------------------------

Use source information as value.

Example
~~~~~~~
.. code-block:: xml
   :linenos:

   <dc:source>Ecology  Letters (1461023X)  vol.4 (2001)</dc:source>

.. _DRIVER Guidelines v2 element source: https://wiki.surfnet.nl/display/DRIVERguidelines/Source