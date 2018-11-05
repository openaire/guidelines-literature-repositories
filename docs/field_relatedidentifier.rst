.. _dci:relatedIdentifier:

6. RelatedIdentifier (R)
========================

``datacite:relatedIdentifier``

An identifier of a related resource other than the primary Identifier applied to the resource being registered. 

6.1 relatedIdentifierType (M)
-----------------------------

The type of the RelatedIdentifier

**Usage Instruction**

 the value is defined in a controlled list:

* ``ark`` – Archival Resource Key
* ``arxiv`` – arXiv.org identifier
* ``bibcode`` – Astrophysics Data System bibliographic codes;  bibcodes can be resolved via http://adsabs.harvard.edu/abs/bibcode
* ``doi`` – Digital Object Identifier
* ``ean13`` – European Article Number, now renamed International Article Number, but retaining the original acronym, is a 13-digit barcoding standard which is a superset of the original 12-digit Universal Product Code (UPC) system.
* ``eissn`` – International Standard Serial Number (electronic Version)
* ``handle`` – Handle
* ``igsn`` – International Geo Sample Number; a 9-digit alphanumeric code that uniquely identifies samples from our natural environment and related sampling features.
* ``isbn`` – International Standard Book Number
* ``issn`` – International Standard Serial Number; a unique 8-digit number used to identify a print or electronic periodical publication.
* ``istc`` – International Standard Text Code; a unique “number” assigned to a textual work. An ISTC consists of 16 numbers and/or letters.
* ``lissn`` – The linking ISSN or ISSN-L enables collocation or linking among different media versions of a continuing resource.
* ``lsid`` – Life Science Identifiers; a unique identifier for data in the Life Science domain. Format: urn:lsid:authority:namespace:identifier:revision
* ``pissn`` – International Standard Serial Number (print version)
* ``pmid`` – PubMed ID
* ``purl`` – Persistent Uniform Resource Locator
* ``upc`` – Universal Product Code is a barcode symbology used for tracking trade items in stores. Its most common form, the UPC-A, consists of 12 numerical digits.
* ``url`` – Uniform Resource Locator
* ``urn`` – Uniform Resource Name
* ``wos`` – Web of Science accession number

6.2 relationType (M)
--------------------

 the value is defined in a controlled list:

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

6.3 relatedMetadataScheme (O)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The name of the scheme (occurrences: 0-1).

**Allowed values, examples, other constraints**

Use only with this relation pair: (``HasMetadata``/``IsMetadataFor``).


6.4 schemeURI (O)
~~~~~~~~~~~~~~~~~~

The URI of the relatedMetadataScheme (occurrences: 0-1).

**Allowed values, examples, other constraints**

Use only with this relation pair: (``HasMetadata``/``IsMetadataFor``).


6.5 schemeType (O)
~~~~~~~~~~~~~~~~~~~

The type of the relatedMetadataScheme, linked with the schemeURI (occurrences: 0-1).

**Allowed values, examples, other constraints**

Use only with this relation pair: (``HasMetadata``/``IsMetadataFor``).

Examples: ``XSD``, ``DDT``, ``Turtle``

Example
-------

.. code-block:: xml
   :linenos:

   <datacite:relatedIdentifiers>
      <datacite:relatedIdentifier relatedIdentifierType="url" relationType="HasPart">http://someUrl</datacite:relatedIdentifier>
   </datacite:relatedIdentifiers>
