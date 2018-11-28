Use of OAI-PMH
==============

OpenAIRE supports a number of transfer protocols and interfaces for collecting bibliographic metadata.
The usage of one of the major protocols, `OAI-PMH v2.0 protocol <http://www.openarchives.org/OAI/openarchivesprotocol.html>`_, in the context of these Guidelines and its application profile is described below.

Metadata Format
^^^^^^^^^^^^^^^
OpenAIRE expects metadata to be encoded following the metadata format defined in the OpenAIRE Application Profile.
The recommended metadataPrefix is ``oai_openaire``. 
For information on how to use the individual properties, please refer to the section :ref:`application_profile`.

Metadata Content
^^^^^^^^^^^^^^^^

OpenAIRE collects metadata of scientific products according to the OpenAIRE Content Acquisition Policy published at https://doi.org/10.5281/zenodo.1446407 .
This includes bibliographic metadata describing open access and non open access items.

.. OpenAIRE OAI Set
   ~~~~~~~~~~~~~~~~
   For harvesting the records relevant to OpenAIRE, the use of a specific `OAI-Set <http://www.openarchives.org/OAI/openarchivesprotocol.html#Set>`_ at the local repository is *mandatory*. The set must have the following characteristics:

.. FIXME

.. ======== ============
   setName  setSpec
   ======== ============
   OpenAIRE ``openaire``
   ======== ============

.. note
   A harvester only uses the **setSpec** value to perform selective harvesting. The letters of the setSpec must be in small caps.

.. Set content
   ~~~~~~~~~~~

   Publications to be inserted in the OpenAIRE set must conform to **at least one**
   of the following criteria:

   * They are available in Open Access (full text with no access restrictions)
   * They are the outcome of a funded research project identified by a project identifier (see below) regardless of their access status (see section below on [[Literature Guidelines: Metadata Field Access Level|Application Profile Field Access Level]]).

.. FIXME

Compatibility of Aggregators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Besides individual repositories and journals, also aggregators (e.g., on the national level) can become OpenAIRE compatible. In this case, additional provenance information on the original content providers harvested by such an aggregator has to be encoded for OpenAIRE on the metadata record level.
In accordance with the `OAI-PMH guidelines <http://www.openarchives.org/OAI/2.0/guidelines-provenance.htm>`_, the provenance information has to be provided in the ``about`` node element of an OAI record, as displayed in the following example:

.. code-block:: xml
   :linenos:

    <about>
      <provenance xmlns="http://www.openarchives.org/OAI/2.0/provenance"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/provenance
      http://www.openarchives.org/OAI/2.0/provenance.xsd">
        <originDescription altered="true" harvestDate="2012-09-17T14:58:36Z">
          <baseURL>http://dspace.library.uu.nl:8080/dspace-oai/request</baseURL>
          <identifier>oai:dspace.library.uu.nl:1874/218065</identifier>
          <datestamp>2012-01-19T12:38:56Z</datestamp>
          <metadataNamespace>
            http://www.openarchives.org/OAI/2.0/oai_dc/
          </metadataNamespace>
        </originDescription>
      </provenance>
    </about>

This means information encoded in the following elements is expected (taken from https://www.openarchives.org/OAI/2.0/guidelines-provenance.htm):

* baseURL - the baseURL of the originating repository from which the metadata record was harvested.
* identifier - the unique identifier of the item in the originating repository from which the metadata record was disseminated.
* datestamp - the datestamp of the metadata record disseminated by the originating repository.
* metadataNamespace - the XML namespace URI of the metadata format of the record harvested from the originating repository.
* originDescription - an optional originDescription block which was that obtained when the metadata record was harvested. A set of nested originDescription blocks will describe provenance over a sequence of harvests.

Each originDescription must also have the following two attributes which relate to the act of harvesting and any subsequent processing:

* harvestDate - the responseDate of the OAI-PMH response that resulted in the record being harvested from the originating repository.
* altered - a boolean value which must be true if the harvested record was altered before being disseminated again.


