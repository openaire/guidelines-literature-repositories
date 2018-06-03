.. _dci:dateEmbargo:

7. Embargo Period Date (MA)
===========================

Dates relevant to describe an embargo period.

A date associated with an event in the life cycle of the resource. Typically, Date will be associated with the creation or availability of the resource. Recommended best practice for encoding the date value is defined in a profile of ISO 8601 [W3CDTF] and follows the ``YYYY-MM-DD`` format.

7.1 dateType (M)
----------------

The type of date.

Example
~~~~~~~
.. code-block:: xml
   :linenos:

   <datacite:dates>
     <datacite:date dateType="Accepted">2011-12-01</datacite:date>
     <datacite:date dateType="Available">2012-12-01</datacite:date>
   </datacite:dates>
