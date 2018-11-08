.. _dci:alternativeIdentifier:

5. Alternate Identifier (R)
===========================

``datacite:alternateIdentifier``

Cardinality
~~~~~~~~~~~

*Recommended*

*Occurence: 0-n*

Definition and Usage Instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An identifier or identifiers other than the primary Identifier applied to the resource being registered. This may be any alphanumeric string which is unique within its domain of issue. May be used for local identifiers. AlternateIdentifier should be used for another identifier of the same instance (same location, same file).

**Remarks**

* adapted from `DataCite MetadataKernel`_ v4.1

Property alternateIdentifier (R, 0-n)
-------------------------------------

Value of the atlernate identifier.

Attribute alternateIdentifierType (M)
-------------------------------------

The type of the AlternateIdentifier (occurence: 1). Mandatory if *AlternateIdentifier* is used.

 The type value is *suggested* in the following list:

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

Example
~~~~~~~

.. code-block:: xml
   :linenos:

   <datacite:alternateIdentifiers>
      <datacite:alternateIdentifier alternateIdentifierType="URL">http://someUrl</datacite:alternateIdentifier>
   </datacite:alternateIdentifiers>

.. _DataCite MetadataKernel: http://schema.datacite.org/meta/kernel-4.1/