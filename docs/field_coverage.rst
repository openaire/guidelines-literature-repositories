.. _dc:coverage:

19. Coverage (R)
================

``dc:coverage``

Cardinality
~~~~~~~~~~~

*Recommended*

*Occurence: 0-1*

Definition and Usage Instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


**DCMI Definition**

The extent or scope of the content of the resource. Coverage will typically include spatial location (a place name or geographic coordinates), temporal period (a period label, date, or date range) or jurisdiction (such as a named administrative entity).

**Usage Instruction**

Recommended best practice is to select the value from a controlled vocabulary (for example, the Getty Thesaurus of Geographic Names or TGN) and that, where appropriate, named places or time periods be used in preference to numeric identifiers as, for example, sets of coordinates or date ranges. If necessary, repeat this element to encode multiple locations or periods.

**Remarks**

* introduced in `DRIVER Guidelines v2 element coverage`_

Example
~~~~~~~

Example Spatial: ISO 3166:

.. code-block:: xml
   :linenos:

   <dc:coverage>NL</dc:coverage>

Example Spatial: BOX:

.. code-block:: xml
   :linenos:

   <dc:coverage>
     name=Western Australia; northlimit=-13.5; southlimit=-35.5;
     westlimit=112.5; eastlimit=129
   </dc:coverage>

.. note::

   The syntax used here is provisional, and is currently under review as part of the DCMI work on recommending coordinated syntax recommendations for HTML, XML, and RDF. These recommendations and minor editorial changes in this document can be expected to take place in the near future. Point http://dublincore.org/documents/dcmi-point/

.. _DRIVER Guidelines v2 element coverage: https://wiki.surfnet.nl/display/DRIVERguidelines/Coverage