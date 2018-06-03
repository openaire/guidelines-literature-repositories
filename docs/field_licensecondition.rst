.. _dc:rightsLicensecondition:

18. License Condition (R)
=========================

DC Field
~~~~~~~~
``dc:rights``

Usage
~~~~~

*Recommended*

DCMI Definition
~~~~~~~~~~~~~~~

Information about license ights held in and over the resource.

Usage Instruction
~~~~~~~~~~~~~~~~~

Typically, a rights element will contain a rights management statement for the access or use of the object, or reference a service providing such information. Rights information often encompasses Intellectual Property Rights (IPR), Copyright, and various Property Rights. It is preferred to refer to a rights service where the reuse rights are made clear to the end-user by using a URL. For example the Creative Commons organisation has created URIs for their different licences in the different jurisdictions. This can be applied to create machine readable usage licenses.

Since
~~~~~

OpenAIRE Guidelines v3

Example
~~~~~~~

.. code-block:: xml
   :linenos:

   <!-- example 1 -->
   <dc:rights rdf:resource="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial</dc:rights>

The URL provides the location where the license can be read. With creative common licenses the type of license can be recognized in the URL name itself. A pro for having the license point to an URL in this way, is that this is machine readable.
