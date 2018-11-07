.. _dci:relatedIdentifier:

6. Related Identifier (R)
=========================

``datacite:relatedIdentifier``

Cardinality
~~~~~~~~~~~

*Recommended*

*Occurence: 0-n*

Definition and Usage Instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An identifier of a related resource other than the primary Identifier applied to the resource being registered. 

**Remarks**

* adapted from `DataCite MetadataKernel`_ v4.1

Attribute relatedIdentifierType (M)
-----------------------------------

The type of the RelatedIdentifier (occurence: 1). Mandatory if *RelatedIdentifier* is used.

The type value is defined in a controlled list:

* ``ARK`` – Archival Resource Key
* ``arXiv`` – arXiv.org identifier
* ``bibcode`` – Astrophysics Data System bibliographic codes;  bibcodes can be resolved via http://adsabs.harvard.edu/abs/bibcode
* ``DOI`` – Digital Object Identifier
* ``EAN13`` – European Article Number, now renamed International Article Number, but retaining the original acronym, is a 13-digit barcoding standard which is a superset of the original 12-digit Universal Product Code (UPC) system.
* ``EISSN`` – International Standard Serial Number (electronic Version)
* ``Handle`` – Handle
* ``IGSN`` – International Geo Sample Number; a 9-digit alphanumeric code that uniquely identifies samples from our natural environment and related sampling features.
* ``ISBN`` – International Standard Book Number
* ``ISSN`` – International Standard Serial Number; a unique 8-digit number used to identify a print or electronic periodical publication.
* ``ISTC`` – International Standard Text Code; a unique “number” assigned to a textual work. An ISTC consists of 16 numbers and/or letters.
* ``LISSN`` – The linking ISSN or ISSN-L enables collocation or linking among different media versions of a continuing resource.
* ``LSID`` – Life Science Identifiers; a unique identifier for data in the Life Science domain. Format: urn:lsid:authority:namespace:identifier:revision
* ``PISSN`` – International Standard Serial Number (print version)
* ``PMID`` – PubMed ID
* ``PURL`` – Persistent Uniform Resource Locator
* ``UPC`` – Universal Product Code is a barcode symbology used for tracking trade items in stores. Its most common form, the UPC-A, consists of 12 numerical digits.
* ``URL`` – Uniform Resource Locator
* ``URN`` – Uniform Resource Name
* ``WOS`` – Web of Science accession number

Attribute relationType (M)
--------------------------

Description of the relationship of the resource being registered (A) and the related resource (B) (occurence: 1). Mandatory if *RelatedIdentifier* is used.

The type value is defined in a controlled list:

* ``IsCitedBy`` (indicates that B includes A in a citation)
* ``Cites`` (indicates that A includes B in a citation)
* ``IsSupplementTo`` (indicates that A is a supplement to B)
* ``IsSupplementedBy`` (indicates that B is a supplement to A)
* ``IsContinuedBy`` (indicates A is continued by the work B)
* ``Continues`` (indicates A is a continuation of the work B)
* ``IsDescribedBy`` (indicates A is described by B)
* ``Describes`` (indicates A describes B)
* ``HasMetadata`` (indicates resource A has additional metadata B)
* ``IsMetadataFor`` (indicates additional metadata A for a resource B)
* ``HasVersion`` (indicates A has a version B)
* ``IsVersionOf`` (indicates A is a version of B)
* ``IsNewVersionOf`` (indicates A is a new edition of B, where the new edition has been modified or updated)
* ``IsPreviousVersionOf`` (indicates A is a previous edition of B)
* ``IsPartOf`` (indicates A is a portion of B;may be used for elements of a series)
* ``HasPart`` (indicates A includes the part B)
* ``IsReferencedBy`` (indicates A is used as a source of information by B)
* ``References`` (indicates B is used as a source of information for A)
* ``IsDocumentedBy`` (indicates B is documentation about/explaining A)
* ``Documents`` (indicates A is documentation about/explaining B)
* ``IsCompiledBy`` (indicates B is used to compile or create A)
* ``Compiles`` (indicates B is the result of a compile or creation event using A)
* ``IsVariantFormOf`` (indicates A is a variant or different form of B, e.g. calculated or calibrated form or different packaging)
* ``IsOriginalFormOf`` (indicates A is the original form of B)
* ``IsIdenticalTo`` (indicates that A is identical to B, for use when there is a need to register two separate instances of the same resource)
* ``IsReviewedBy`` (indicates that A is reviewed by B)
* ``Reviews`` (indicates that A is a review of B)
* ``IsDerivedFrom`` (indicates B is a source upon which A is based)
* ``IsSourceOf`` (indicates A is a source upon which B is based)
* ``IsRequiredBy`` (indicates A is required by B)
* ``Requires`` (indicates A requires B)

Attribute relatedMetadataScheme (O)
-----------------------------------

The name of the scheme (occurrences: 0-1).

**Allowed values, examples, other constraints**

Use only with this relation pair: (``HasMetadata``/``IsMetadataFor``).


Attribute schemeURI (O)
-----------------------

The URI of the relatedMetadataScheme (occurrences: 0-1).

**Allowed values, examples, other constraints**

Use only with this relation pair: (``HasMetadata``/``IsMetadataFor``).


Attribute schemeType (O)
------------------------

The type of the relatedMetadataScheme, linked with the schemeURI (occurrences: 0-1).

**Allowed values, examples, other constraints**

Use only with this relation pair: (``HasMetadata``/``IsMetadataFor``).

Examples: ``XSD``, ``DDT``, ``Turtle``

Attribute resourceTypeGeneral (O)
---------------------------------

The general type of the related resource (occurrences: 0-1).

The type value is defined in a controlled list:

* Audiovisual
* Collection
* DataPaper
* Dataset
* Event
* Image
* InteractiveResource
* Model
* PhysicalObject
* Service
* Software
* Sound
* Text24
* Workflow
* Other


Example
~~~~~~~

.. code-block:: xml
   :linenos:

   <datacite:relatedIdentifiers>
      <datacite:relatedIdentifier relatedIdentifierType="URL" relationType="HasPart">http://someUrl</datacite:relatedIdentifier>
   </datacite:relatedIdentifiers>

.. _DataCite MetadataKernel: http://schema.datacite.org/meta/kernel-4.1/