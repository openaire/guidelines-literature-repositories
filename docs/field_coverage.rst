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
* to describe spatial location information (a place name or geographic coordinates) use the property :ref:`dci:geolocation`

Property coverage (R, 0-n)
--------------------------

Use temporal period or jurisdiction information as value.

Example
~~~~~~~

Example Spatial: temporal topic:

.. code-block:: xml
   :linenos:

   <dc:coverage>2000-2010</dc:coverage>

Example Spatial: BOX:

.. code-block:: xml
   :linenos:

   <dc:coverage>
     scheme=historic; content=Ming Dynasty
   </dc:coverage>

.. _DRIVER Guidelines v2 element coverage: https://wiki.surfnet.nl/display/DRIVERguidelines/Coverage