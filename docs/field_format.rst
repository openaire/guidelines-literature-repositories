.. _dc:format:

Format (R)
==========

``dc:format``

Cardinality
~~~~~~~~~~~

*Recommended*

*Occurrence: 0-n*

Definition and Usage Instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**DCMI Definition**

The physical or digital manifestation of the resource. Typically, Format may include the media-type or dimensions of the resource. Format may be used to determine the software, hardware or other equipment needed to display or operate the resource. Examples of dimensions include size and duration. Recommended best practice is to select a value from a controlled vocabulary (for example, the list of Internet Media Types [MIME] defining computer media formats).

**Usage Instruction**

Based on best practice, the IANA registered list of Internet Media Types (MIME types) is used to select a term from. For the full list see http://www.iana.org/assignments/media-types

If one specific resource (an instance of scientific output) has more than one physical formats (e.g. postscript and pdf) stored as different object files, all formats are mentioned in the DC element format, for example:

* ``<dc:format>application/pdf</dc:format>``
* ``<dc:format>application/postscript</dc:format>``
* ``<dc:format>application/vnd.oasis.opendocument.text</dc:format>``

**Do Not Confuse With**

* :ref:`aire:resourceType`
* :ref:`dci:identifier`

DC element ``format`` describes the media type of this resource. ``oaire:resourceType`` describes the kind of academic output the resource is a representation of. ``datacite:identifier`` is used to represent the manifestation of the digital resource.

**Remarks**

* introduced in `DRIVER Guidelines v2 element format`_

Property format (R, 0-n)
------------------------

Use the media type of the resource as value.

Example
~~~~~~~

.. code-block:: xml
   :linenos:

   <dc:format>video/quicktime</dc:format>
   <dc:format>application/pdf</dc:format>
   <dc:format>application/xml</dc:format>
   <dc:format>application/xhtml+xml</dc:format>
   <dc:format>application/html</dc:format>
   <dc:format>application/vnd.oasis.opendocument.text</dc:format>

.. _DRIVER Guidelines v2 element format: https://wiki.surfnet.nl/display/DRIVERguidelines/Format