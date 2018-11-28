.. _dci:size:

Size (O)
========

``datacite:size``

Cardinality
~~~~~~~~~~~

*Optional*

*Occurrence: 0-n*

Definition and Usage Instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Unstructured size information about the resource.

**Allowed values, examples, other constraints**

Free text.

Examples: "15 pages", "6 MB"

**Remarks**

* adapted from `DataCite MetadataKernel`_ v4.1

Property size (O, 0-n)
----------------------

Use size information as value. Repeat the property for different size information domains.

Example
~~~~~~~
.. code-block:: xml
   :linenos:

     <datacite.sizes>
	     <datacite:size>15 pages</datacite:size>
	     <datacite:size>6 MB</datacite:size>
     </datacite.sizes>

.. _DataCite MetadataKernel: http://schema.datacite.org/meta/kernel-4.1/