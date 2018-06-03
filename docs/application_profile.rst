Application Profile Overview
----------------------------

The properties of the Application Profile for OpenAIRE Literature Repository Guidelines are listed in this section.
The following requirement levels for the metadata properties are used:

Mandatory (M)
  The property must always be present in the metadata. An empty value for the property is not allowed.

Mandatory if Applicable (MA)
  When the property value can be obtained it must be present in the metadata

Recommended (R)
  The use of the property is recommended

Optional (O)
  It is not important whether the property is used or not

This documentation uses the following namespace abbreviation:

* ``dc``: http://purl.org/dc/elements/1.1/
* ``datacite``: http://datacite.org/schema/kernel-4
* ``rdf`` : `<http://www.w3.org/1999/02/22-rdf-syntax-ns#>`__
* ``oaire``: http://namespace.openaire.eu/schema/oaire/

======================================== ============================= ===========================================================================
OpenAIRE-Field                           Metadata Element              Refinement by vocabulary
======================================== ============================= ===========================================================================
:ref:`dc:title`                          dc:title
:ref:`dci:creator`                       datacite:creator
:ref:`dci:contributor`                   datacite:contributor          DataCite contributor type
:ref:`dci:fundingReference`              datacite:fundingReference     DataCite funderIdentifier type
:ref:`dci:alternativeIdentifier`         datacite:alternateIdentifier   
:ref:`dci:relatedIdentifier`             datacite:relatedIdentifier    DataCite relatedIdentifier type
:ref:`dci:dateEmbargo`                   datacite:date                 DataCite dateType
:ref:`dc:language`                       dc:language                   `IETF BCP 47`_, ISO 639-1,2,3
:ref:`dc:publisher`                      dc:publisher
:ref:`dc:date`                           dc:date
:ref:`dc:typePublicationtype`            dc:type                       `COAR Resource Type Vocabulary`_
:ref:`dc:description`                    dc:description
:ref:`dc:format`                         dc:format
:ref:`dc:identifier`                     dc:identifier
:ref:`dc:rightsAccessrights`             dc:rights                     `COAR Access Right Vocabulary`_
:ref:`dc:source`                         dc:source
:ref:`dc:subject`                        dc:subject
:ref:`dc:rightsLicensecondition`         dc:rights
:ref:`dc:relation`                       dc:relation
:ref:`dc:coverage`                       dc:coverage
:ref:`aire:version`                      oaire:version        
:ref:`aire:file`                         oaire:file        
:ref:`aire:citationTitle`                oaire:citationTitle 	
:ref:`aire:citationVolume`               oaire:citationVolume
:ref:`aire:citationIssue`                oaire:citationIssue
:ref:`aire:citationStartPage`            oaire:citationStartPage
:ref:`aire:citationEndPage`              oaire:citationEndPage
:ref:`aire:citationEdition`              oaire:citationEdition
:ref:`aire:citationConferencePlace`      oaire:citationConferencePlace
:ref:`aire:citationConferenceDate`       oaire:citationConferenceDate
======================================== ============================= ===========================================================================

.. _COAR Resource Type Vocabulary: http://vocabularies.coar-repositories.org/documentation/resource_types/
.. _COAR Access Right Vocabulary: http://vocabularies.coar-repositories.org/documentation/access_rights/
.. _IETF BCP 47: http://tools.ietf.org/rfc/bcp/bcp47.txt
