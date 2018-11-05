.. _dci:title:

1. Title (M)
------------

``datacite:title``

A name or title by which a resource is known (occurrences: 1-n).

**Allowed values, examples, other constraints**

Free text.

1.1 lang (O)
~~~~~~~~~~~~

The language of the title (occurences: 0-n)

1.2 titleType (O)
~~~~~~~~~~~~~~~~~
The type of Title (occurrences: 0-1).

**Allowed values, examples, other constraints**

*Controlled List Values:*

* Alternative Title
* Subtitle
* TranslatedTitle

Example
~~~~~~~
.. code-block:: xml
   :linenos:

    <datacite:title xml:lang="en-US">
     National Institute for Environmental Studies and Center
     for Climate System Research Japan
    </datacite:title>
    <datacite:title xml:lang="en-US" titleType="Subtitle">A survey</datacite:title>
