.. _literature_intro:

Introduction
============

Aim
---
The OpenAIRE Guidelines for Literature Repository Managers 4.0 provide
orientation for repository managers to define and implement their local data
management policies according to the requirements of the `OpenAIRE - Open Access
Infrastructure for Research in Europe <http://www.openaire.eu>`_.

The OpenAIRE Guidelines were established to support the `Open Access strategy of the European Commission <http://ec.europa.eu/research/openscience/index.cfm?pg=openaccess>`_
and to meet requirements of the OpenAIRE infrastructure.
This new version of the Guidelines, according to the expansion of the aims of the
OpenAIRE initiative and its infrastructure, has a broader scope. In fact, these
Guidelines are intended to guide repository manager to expose to the OpenAIRE
infrastructure **open access and non-open access publications** together with **funding information**, where applicable.

By implementing these Guidelines, repository managers will not only be
enabling authors who deposit publications in their repository to fulfill the EC
Open Access requirements, and eventually also the requirements of other
(national or international) funders with whom OpenAIRE cooperates,
but also incorporating their publications into the OpenAIRE infrastructure for
discoverability and utilizing value-added services provided by the OpenAIRE portal.

The OpenAIRE Guidelines for Literature Repository Managers 4.0 are 
part of a set of OpenAIRE Guidelines that also include the OpenAIRE Guidelines
for Data Archive Managers, the OpenAIRE Guidelines for CRIS managers, the OpenAIRE Guidelines for Software Repository Managers, and the Guidelines for Other Research Products Repository Managers.

What's new
----------
In comparison with previous versions of the Guidelines, this version introduces
the following major changes:

* an application profile and schema based on Dublin Core and DataCite incl. a new OAI-metadataPrefix
* support of identifier schemes for authors, organizations, funders, scholarly resources
* introduction of COAR Controlled Vocabularies
* compliance with the `OpenAIRE Content Acquisition Policy <https://doi.org/10.5281/zenodo.1446407>`_, published on 05-Oct-2018.

How this document is structured
-------------------------------

Chapter two provides a brief overview of how to configure and use OAI-PMH for OpenAIRE metadata harvesting.
Chapter three describes the application profile.
It assignes properties from Dublin Core and DataCite metadata schemes to OpenAIRE fields.
Each OpenAIRE field is described in detail by

* the name of the field
* how it is mapped to an element in such metadata schemes
* the cardinality of the field
* definition and usage instructions with regard to allowed values in properties, sub-properties and attributes
* example(s)

Acknowledgements & Contributors
-------------------------------

**Editors**

* Jochen Schirrwagen (Bielefeld University, Germany)
* Miriam Baglioni (CNR, Italy)

**Experts & Reviewers**

*OpenAIRE*

* Pedro Principe (University of Minho, Portugal)
* Paolo Manghi (CNR, Italy)
* Aenne Loehden (Bielefeld University, Germany)
* Andreas Czerniak (Bielefeld University, Germany)
* Amelie Bäcker (Bielefeld University, Germany)

*LA Referencia*

* Alberto Cabezas (LA Referencia, Chile)
* Paola Azrilevich (MinCyT, Argentina)

*JPCOAR*

* Tomoko Kataoka (Ochanomizu University, Japan)

*Antleaf*

* Paul Walk (Antleaf, UK)

*University of Alberta Libraries*

* Sharon Farnel (University of Alberta Libraries, CA)

*CARL Open Repositories Working Group*

* Pierre Lasou (Université Laval, CA)

Versions
--------
* 4.0, November 2018 `doi:10.5281/zenodo.1299203 <http://dx.doi.org/10.5281/zenodo.1299203>`_

* 4.0 draft, November 2017

* 3.0, April 2013 `doi:10.5281/zenodo.1487968 <http://dx.doi.org/10.5281/zenodo.1487968>`_

* 3.0, beta December 2012

  * The OpenAIRE OAI set has been renamed from ``ec_fundedresources`` to ``openaire``.
  * New relation elements for indicating external identifiers, references and connections to datasets.

* 2.0, October 2012 `doi:10.5281/zenodo.59208 <http://dx.doi.org/10.5281/zenodo.59208>`_

  * Compatibility for aggregators; extended Namespace for Project Identification

* 1.1, November 2010 `doi:10.5281/zenodo.59206 <http://dx.doi.org/10.5281/zenodo.59206>`_

  * Correction of names and references; addition of license and version statement

* 1.0, July 2010 `doi:10.5281/zenodo.59204 <http://dx.doi.org/10.5281/zenodo.59204>`_

  * Initial document
