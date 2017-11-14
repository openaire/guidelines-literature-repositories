.. _dc:typePublicationtype:

11. Publication Type (M)
========================

**Usage**

Publication type is used for the following purposes:

* **Mandatory (M)**: Publication type (controlled): to indicate the type of publication based on the COAR Resource Types Vocabulary.
* **Optional (O)**: Publication type (free): to indicate the type of publication based on a local repository vocabulary.

**DCMI Definition**

The type of scientific output the resource is a manifestation of. In the DC element type the kind of dissemination, or the intellectual and/or content type of the resource is described. It is used to explain to the user what kind of resource he is looking at. Is it a book or an article. Was it written for internal or external use, etc.

**Usage Instruction**

**Publication types (controlled):**

The first occurrence of the DC Element ``type`` is mandatory and should be used for the type indication of the scientific output based on the COAR Resource Type Vocabulary.

**Publication types (free text):**

The second occurrence of the DC Element ``type`` is optional and should be used for the subtype indication of the scientific output.

**Do Not Confuse With**

* :ref:`dc:format`

DC element `type` describes the kind of academic output the resource is a representation of. DC element ‘format’ describes the media type of this resource.

**Example**

.. code-block:: xml
   :linenos:

   <dc:type rdf:resource="http://purl.org/coar/resource_type/c_6501">journal article</dc:type>
