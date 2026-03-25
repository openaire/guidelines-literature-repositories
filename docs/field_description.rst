.. _dci:description:

Description (MA)
================

``datacite:description``


Cardinality
~~~~~~~~~~~

*Mandatory if applicable*

*Occurrence: 0-n*

Definition and Usage Instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**DCMI Definition**

An account of the content of the resource. Description may include but is not limited to: an abstract, table of contents, reference to a graphical representation of content or a free-text account of the content.

**Usage Instruction**

This element is used for a textual description of the content. When a resource consists of several separate physical object files, do not use ``dc:description`` to list the URLs of these files.

**Remarks**

* introduced in `DRIVER Guidelines v2 element description`_
* adapted from `DataCite MetadataKernel`_ v4.7


Property description (MA, 0-n)
------------------------------

Use the textual description as value.

.. _dc:description_lang:

Attribute descriptionType (M)
------------------

The type of the description (occurrence: 0-1). Mandatory if description property is used.

**Controlled list values**

* Abstract
* Methods
* SeriesInformation
* TableOfContents
* TechnicalInfo
* Other

Attribute lang (O)
------------------

The language of the description (occurrence: 0-1).

Use the ``xml:lang`` attribute to indicate the language of the description.

Example
~~~~~~~
.. code-block:: xml
   :linenos:

   <datacite:description descriptionType="Abstract">
     Foreword [by] Hazel Anderson; Introduction; The scientific heresy:
     transformation of a society; Consciousness as causal reality [etc]
   </datacite:description>

   <datacite:description xml:lang="en-US">
     A number of problems in quantum state and system identification are
     addressed.
   </datacite:description>
