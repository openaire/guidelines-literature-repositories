.. _dci:dateEmbargo:

Embargo Period Date (MA)
========================

``datacite:date``


Cardinality
~~~~~~~~~~~

*Mandatory if applicable*

*Occurrence: 2*

Definition and Usage Instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dates relevant to describe an embargo period.

A date associated with an event in the life cycle of the resource. Typically, Date will be associated with the creation or availability of the resource. Recommended best practice for encoding the date value is defined in a profile of ISO 8601 [W3CDTF] and follows the ``YYYY-MM-DD`` format.

**Remarks**

* introduced as `info:eu-repo/date/embargoEnd/[YYYY-MM-DD] <https://wiki.surfnet.nl/display/standards/info-eu-repo/#info-eu-repo-DateTypesandvalue>`_ in previous versions of the OpenAIRE Guidelines
* this version of the application profile adopts the *Date* element in combination with *dateType* attributes from DataCite MetadataKernel v4.1 which replaces the ``info:eu-repo/date/EmbargoEnd`` syntax.

When :ref:`dci:accessrights` is set to::

    <datacite:rights uri="http://purl.org/coar/access_right/c_f1cf">embargoed access</<datacite:rights>

the start and end date of the embargo period must be provided.

Property date (MA, 2)
-----------------------

Use the date of the embargo start as value in one property and the date of the embargo end in the other property.

Attribute dateType (M)
----------------------

The type of date. Choose from the :ref:`date type <vocab:datetype_datetype>` vocabulary the controlled term ``Accepted`` to indicate the start and the term ``Available`` to indicate the end of an embargo period.

Example
~~~~~~~
.. code-block:: xml
   :linenos:

   <datacite:dates>
     <datacite:date dateType="Accepted">2011-12-01</datacite:date>
     <datacite:date dateType="Available">2012-12-01</datacite:date>
   </datacite:dates>
