.. _dc:description:

12. Description (MA)
====================

``dc:description``


Cardinality
~~~~~~~~~~~

*Mandatory if applicable*

*Occurence: 0-n*

Definition and Usage Instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The language of the description (occurences: 0-n)

**Usage Instruction**

This element is used for a textual description of the content. When a resource consists of several separate physical object files, do not use ``dc:description`` to list the URLs of these files.

**Remarks**

* introduced in `DRIVER Guidelines v2 element description`_

.. _dc:description_lang:

Attribute lang (O)
------------------

The language of the description (occurences: 0-1).


Example
~~~~~~~
.. code-block:: xml
   :linenos:

   <dc:description>
     Foreword [by] Hazel Anderson; Introduction; The scientific heresy:
     transformation of a society; Consciousness as causal reality [etc]
   </dc:description>

   <dc:description xml:lang="en-US">
     A number of problems in quantum state and system identification are
     addressed.
   </dc:description>

.. _DRIVER Guidelines v2 element description: https://wiki.surfnet.nl/display/DRIVERguidelines/Description