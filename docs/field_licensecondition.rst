.. _aire:licenseCondition:

18. License Condition (R)
=========================

``oaire:licenseCondition``

18.1 licenseURI (MA)
--------------------

The URL provides the location where the license can be read. With creative common licenses the type of license can be recognized in the URL name itself. A pro for having the license point to an URL in this way, is that this is machine readable.

18.2 startDate (MA)
-------------------

This attribute indicates the date when the license comes into effect.
Recommended best practice for encoding the date value is defined in a profile of ISO 8601 [W3CDTF] and follows the ``YYYY-MM-DD`` format.


Usage
~~~~~

*Recommended*

DCMI Definition
~~~~~~~~~~~~~~~

Information about license rights held in and over the resource.

Usage Instruction
~~~~~~~~~~~~~~~~~

Typically, a rights element will contain a rights management statement for the access or use of the object, or reference a service providing such information. Rights information often encompasses Intellectual Property Rights (IPR), Copyright, and various Property Rights. It is preferred to refer to a rights service where the reuse rights are made clear to the end-user by using a URL. For example the Creative Commons organisation has created URIs for their different licences in the different jurisdictions. This can be applied to create machine readable usage licenses.


Example
-------

.. code-block:: xml
   :linenos:

   <!-- example 1 -->
   <oaire:licenseCondition startDate="2019-02-01" licenseURI="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial</oaire:licenseCondition>

