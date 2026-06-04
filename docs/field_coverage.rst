.. _dc:coverage:

Coverage (R)
============

``dc:coverage``

Cardinality
~~~~~~~~~~~

*Recommended*

*Occurrence: 0-n*

Definition and Usage Instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The extent or scope of the content of the resource. Coverage will typically include temporal period (a period label, date, or date range) or jurisdiction (such as a named administrative entity).

**Usage Instruction**

It is recommended to use literal or non-literal values. If necessary, repeat this element to encode multiple periods.

**Remarks**

* introduced in `DRIVER Guidelines v2 element coverage`_
* this version of the application profile adopts the Date element in combination with dateType="Coverage" attribute from DataCite MetadataKernel v4.1.
* to describe spatial location information (a place name or geographic coordinates) use the property :ref:`dci:geolocation`

Property coverage (R, 0-n)
--------------------------

Use temporal period or jurisdiction information as value.

Example
~~~~~~~

Example Spatial: temporal topic:

.. code-block:: xml
   :linenos:

   <datacite:dates>
      <datacite:date dateType="Coverage">1578-01-01/1810-12-31</datacite:date>
   </datacite:dates>
