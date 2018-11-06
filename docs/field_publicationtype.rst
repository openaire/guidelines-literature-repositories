.. _aire:resourceType:

11. Resource Type (M)
=====================

``oaire:resourceType``

Cardinality
~~~~~~~~~~~

*Mandatory*

*Occurence: 1*

Definition and Usage Instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The type of scientific output the resource is a manifestation of. It describes the genre of the resource.

**Usage**

The attribute *resourceTypeGeneral* is used to categorize the resource to belong to a main class of research outputs.
The attribute *uri* holds an HTTP URI of a resource type concept and indicates the sub-property of *resourceTypeGeneral*.
The label of this concept is used as value for the *ResourceType* element.

**Do Not Confuse With**

* :ref:`dc:format` which describes the media type of this resource.

**Remarks**

* former versions of the OpenAIRE Guidelines used the `info:eu-repo vocabulary for publication types <https://wiki.surfnet.nl/display/standards/info-eu-repo/#info-eu-repo-Semantics>`_.
* adopting *resourceType* element from DataCite MetadataKernel v4.1.
* adding the *uri* attribute for resource type concept URI to this application profile

Attribute resourceTypeGeneral (M)
---------------------------------

The general type of a resource.

*Controlled list values*

* Publication
* Dataset
* Software
* Other Research Product

Attribute uri (M)
-----------------

Use terms from the `COAR Resource Type Vocabulary`_ (occurence: 1).

Example
~~~~~~~

.. code-block:: xml
   :linenos:

   <oaire:resourceType resourceTypeGeneral="publication" uri="http://purl.org/coar/resource_type/c_6501">journal article</oaire:resourceType>

.. _COAR Resource Type Vocabulary: http://vocabularies.coar-repositories.org/documentation/resource_types/