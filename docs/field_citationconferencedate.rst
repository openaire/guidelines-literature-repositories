.. _aire:citationConferenceDate:

31. Citation Conference Date (R)
================================

``oaire:citationConferenceDate``

Cardinality
~~~~~~~~~~~

*Recommended*

*Occurence: 0-1*

Definition and Usage Instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The date when the conference took place. This property is considered to be part of the bibliographic citation.

Property citationConferenceDate (R, 0-1)
----------------------------------------

Use the *single date* or *start date* and *end date* as values following these patterns:

* ``YYYY-MM-DD``
* ``YYYY-MM-DD - YYYY-MM-DD``

Example
~~~~~~~

.. code-block:: xml
   :linenos:

   <oaire:citationConferenceDate>2013-10-22</oaire:citationConferenceDate>

.. code-block:: xml
   :linenos:

   <oaire:citationConferenceDate>2013-09-22 - 2013-09-26</oaire:citationConferenceDate>
