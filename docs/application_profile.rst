.. _application_profile:

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
  It is not important whether the property is used or not, but if used it may provide complementary information about the resource

This documentation uses the following namespace abbreviations:

* ``dc``: http://purl.org/dc/elements/1.1/
* ``dcterms``: http://purl.org/dc/terms/
* ``datacite``: http://datacite.org/schema/kernel-4
* ``oaire``: http://namespace.openaire.eu/schema/oaire/

======================================== ============================= ===========================================================================
OpenAIRE-Field                           Metadata Element              Refinement by vocabulary
======================================== ============================= ===========================================================================
:ref:`dci:title`                         datacite:title                DataCite title type
:ref:`dci:creator`                       datacite:creator              DataCite name type
:ref:`dci:contributor`                   datacite:contributor          DataCite name type, contributor type
:ref:`aire:fundingReference`             oaire:fundingReference        DataCite funderIdentifier type
:ref:`dci:alternativeIdentifier`         datacite:alternateIdentifier  alternateIdentifier type
:ref:`dci:relatedIdentifier`             datacite:relatedIdentifier    DataCite relatedIdentifier type
:ref:`dci:dateEmbargo`                   datacite:date                 DataCite dateType
:ref:`dc:language`                       dc:language                   `IETF BCP 47`_, ISO 639-1,2,3
:ref:`dc:publisher`                      dc:publisher
:ref:`dci:datePublication`               datacite:date                 DataCite dateType
:ref:`aire:resourceType`                 oaire:resourceType            `COAR Resource Type Vocabulary`_
:ref:`dc:description`                    dc:description
:ref:`dc:format`                         dc:format
:ref:`dci:identifier`                    datacite:identifier           identifierType
:ref:`dci:accessrights`                  datacite:accessRights         `COAR Access Right Vocabulary`_
:ref:`dc:source`                         dc:source
:ref:`dci:subject`                       datacite:subject              
:ref:`aire:licenseCondition`             oaire:licenseCondition
:ref:`dc:coverage`                       dc:coverage
:ref:`dci:size`                          datacite:size
:ref:`dci:geolocation`                   datacite:geoLocation
:ref:`aire:version`                      oaire:version                 `COAR Version Vocabulary`_ 
:ref:`aire:file`                         oaire:file        
:ref:`aire:citationTitle`                oaire:citationTitle 	
:ref:`aire:citationVolume`               oaire:citationVolume
:ref:`aire:citationIssue`                oaire:citationIssue
:ref:`aire:citationStartPage`            oaire:citationStartPage
:ref:`aire:citationEndPage`              oaire:citationEndPage
:ref:`aire:citationEdition`              oaire:citationEdition
:ref:`aire:citationConferencePlace`      oaire:citationConferencePlace
:ref:`aire:citationConferenceDate`       oaire:citationConferenceDate
:ref:`dct:audience`                      dcterms:audience
======================================== ============================= ===========================================================================

.. _COAR Resource Type Vocabulary: http://vocabularies.coar-repositories.org/documentation/resource_types/
.. _COAR Access Right Vocabulary: http://vocabularies.coar-repositories.org/documentation/access_rights/
.. _COAR Version Vocabulary: http://vocabularies.coar-repositories.org/documentation/version_types/
.. _IETF BCP 47: http://tools.ietf.org/rfc/bcp/bcp47.txt

.. toctree::
   :maxdepth: 1
   :hidden:

   field_title
   field_creator
   field_contributor
   field_projectid
   field_alternativeidentifier
   field_relatedidentifier
   field_embargoenddate
   field_language
   field_publisher
   field_publicationdate
   field_publicationtype
   field_description
   field_format
   field_resourceidentifier
   field_accessrights
   field_source
   field_subject
   field_licensecondition
   field_coverage
   field_size
   field_geolocation
   field_resourceversion
   field_filelocation
   field_citationtitle
   field_citationvolume
   field_citationissue
   field_citationstartpage
   field_citationendpage
   field_citationedition
   field_citationconferenceplace
   field_citationconferencedate
   field_audience
