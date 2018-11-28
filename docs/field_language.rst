.. _dc:language:

Language (MA)
=============

``dc:language``

Cardinality
~~~~~~~~~~~

*Mandatory if applicable*

*Occurrence: 0-n*

Definition and Usage Instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**DCMI Definition**

A language of the intellectual content of the resource.

**Usage Instruction**

A specific resource (an instance of scientific output) is either written in one human language or more. In these cases all used languages are used in the DC element ``language``. If a specific resource (an instance of scientific output) is written in one human language and is translated into other human languages, each translation does have its own record.

Recommendation: take values from one of the following lists: 

* IETF BCP 47, the `IANA Language Subtag Registry <http://www.iana.org/assignments/language-subtag-registry>`_
* ISO 639-x, where x can be 1,2 or 3. Best Practice: we use ISO 639-3 and by doing so we follow: http://www.sil.org/iso639-3/

If necessary, repeat this element to indicate multiple languages.

If ISO 639-2 and 639-1 are sufficient for the contents of a repository they can be used alternatively. Since there is a unique mapping this can be done during an aggregation process.

**Remarks**

* introduced in `DRIVER Guidelines v2 element language`_

Property language (MA, 0-n)
---------------------------

Use the language code as value.

Example
~~~~~~~

.. code-block:: xml
   :linenos:


   <dc:language>eng</dc:language>
   <dc:language>deu</dc:language>
   <dc:language>nld</dc:language>
   <dc:language>nld/dut</dc:language>
   <dc:language>dut</dc:language>
   <dc:language>nl</dc:language>

.. _DRIVER Guidelines v2 element language: https://wiki.surfnet.nl/display/DRIVERguidelines/Language