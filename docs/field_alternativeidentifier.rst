.. _dci:alternativeIdentifier:

5. AlternateIdentifier (R)
==========================

``datacite:alternateIdentifier``

An identifier or identifiers other than the primary Identifier applied to the resource being registered. This may be any alphanumeric string which is unique within its domain of issue. May be used for local identifiers. AlternateIdentifier should be used for another identifier of the same instance (same location, same file).

5.1 alternateIdentifierType (O)
-------------------------------


**Usage Instruction**

List alternative identifiers for this publication that are not the primary identifier (repository splash page), e.g., the DOI of publisher’s version, the PubMed/arXiv ID. The value is defined in a controlled list:

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

Example
-------

.. code-block:: xml
   :linenos:

   <datacite:alternateIdentifiers>
      <datacite:alternateIdentifier alternateIdentifierType="url">http://someUrl</datacite:alternateIdentifier>
   </datacite:alternateIdentifiers>
