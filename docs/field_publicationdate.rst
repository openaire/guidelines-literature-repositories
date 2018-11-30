.. _dci:datePublication:

Publication Date (M)
====================

``datacite:date``

Cardinality
~~~~~~~~~~~

*Mandatory*

*Occurrence: 1*

Definition and Usage Instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**DCMI Definition**

A date associated with an event in the life cycle of the resource. Typically, Date will be associated with the creation or availability of the resource. Recommended best practice for encoding the date value is defined in a profile of `ISO 8601 [W3CDTF] <https://www.iso.org/iso-8601-date-and-time-format.html>`_ and follows the ``YYYY-MM-DD`` format.

**Usage Instruction**

The date should be formatted according to the W3C encoding rules for dates and times:

**Complete date:**

``YYYY-MM-DD`` (e.g. 1997-07-16)

where:

* ``YYYY`` [four-digit year] is ''mandatory''
* ``MM`` [two-digit month (01=January, etc.)] is ''optional''
* ``DD`` [two-digit day of month (01 through 31)] is ''optional''

**One date field – Date of Publication:**

Often repository systems have more then one date fields that serve different purposes. Date of creation, publication, modified, promotion, etc. Preferably in the end-users perspective the most logical and meaningful date will be the date of publication. 

**No date of publication available:**

If no date of publication is available, use any other date available. It is better to use one date than no date at all.

**Datestamp additions:**

Additions like “Zulu time” should NOT be part of the metadata.

**Fuzzy dates:**

For fuzzy dates use a logical year that most represents that period, e.g. ``1650`` instead of ``17th century``.

To express more about that temporal period, one can use the ``dc:coverage`` field. A temporal period can be expressed in a standard way when precisely defined (see :ref:`dc:coverage`) or when “fuzzy” or uncertain by free text expressions. A service provider is able to sort dates based on date standards like W3CDTF. Since there is no standard for fuzzy dates for terms like “Renaissance” or “17th Century”, they will simply not appear on date-based query results.

**Remarks**

* introduced in `DRIVER Guidelines v2 element date`_
* this version of the application profile adopts the *Date* element in combination with *dateType* attribute from `DataCite MetadataKernel`_ v4.1.

Property date (M, 1)
--------------------

Use the publication date as value.

Attribute dateType (M)
----------------------

The type of date. Choose from the :ref:`date type <vocab:datetype_datetype>` vocabularyUse the controlled term ``Issued`` to indicate the date of publication.

Example
~~~~~~~

.. code-block:: xml
   :linenos:

   <datacite:date dateType="Issued">2000-12-25</datacite:date>

.. _DRIVER Guidelines v2 element date: https://wiki.surfnet.nl/display/DRIVERguidelines/Date
.. _DataCite MetadataKernel: http://schema.datacite.org/meta/kernel-4.1/