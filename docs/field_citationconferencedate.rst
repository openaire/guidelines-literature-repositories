.. _aire:citationConferenceDate:

Citation Conference Date (R)
============================

``oaire:citationConferenceDate``

Cardinality
~~~~~~~~~~~

*Recommended*

*Occurrence: 0-1*

Definition and Usage Instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The date when the conference took place. This property is considered to be part of the bibliographic citation. Recommended best practice for encoding the date value is defined in a profile of `ISO 8601 [W3CDTF] <https://www.iso.org/iso-8601-date-and-time-format.html>`_ and follows the ``YYYY-MM-DD`` format.

**Usage Instruction**

The date should be formatted according to the W3C encoding rules for dates and times:

**Complete date:**

``YYYY-MM-DD`` (e.g. 1997-07-16)

where:

* ``YYYY`` [four-digit year]
* ``MM`` [two-digit month (01=January, etc.)]
* ``DD`` [two-digit day of month (01 through 31)]

Property citationConferenceDate (R, 0-1)
----------------------------------------

Use the *single date* or *start date* and *end date* as values following these patterns:

* ``YYYY-MM-DD`` [*single date*]
* ``YYYY-MM-DD - YYYY-MM-DD`` [*start date* - *end date*]

Example
~~~~~~~

.. code-block:: xml
   :linenos:

   <oaire:citationConferenceDate>2013-10-22</oaire:citationConferenceDate>

.. code-block:: xml
   :linenos:

   <oaire:citationConferenceDate>2013-09-22 - 2013-09-26</oaire:citationConferenceDate>
