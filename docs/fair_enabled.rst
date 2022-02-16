.. _fair_enabled:

FAIR enabled
============

The OpenAIRE and DRIVER guidelines, at the beginning of their time in `2006 <https://www.openaire.eu/history>`_, had already put the focus on elements that can be found today in the FAIR principles.
Community-based refinement and enhancement of the guidelines over time to include elements with their descriptions that are consistent with motivation of FAIR. 
The following section describe the FAIRification process of the OpenAIRE Guidelines for institutional & thematic Repository Manager.

.. _fair_overview:

Overview
~~~~~~~~

The `FAIR maturity model: specification and guidelines <https://www.rd-alliance.org/group/fair-data-maturity-model-wg/outcomes/fair-data-maturity-model-specification-and-guidelines-0>`_ of the `Research Data Alliance (RDA) <https://www.rd-alliance.org>`_ (DOI: `10.15497/rda00050 <https://doi.org/10.15497/rda00050>`_)
has the aim to specify the objective indicators for the FAIR assessment. The guidelines are intended to assist evaluators to implement the indicators in the evaluation approach or tool 
they manage.

The evaluation level analyse is done thru the RDA FAIR Data Maturity specification sheet provided at `https://www.rd-alliance.org/system/files/FAIR_evaluation_levels_v0.01.xlsx <https://www.rd-alliance.org/system/files/FAIR_evaluation_levels_v0.01.xlsx>`_.
The result of this evaluation shows the figure below.

In the case of *Findability* indicators

- RDA-F2-01M: Rich metadata is provided to allow discovery
- RDA-F4-01M: Metadata is offered in such a way that it can be harvested and indexed

are implicit covered.

In such a case for *Accessibility* indicators

- RDA-A1-02M: Metadata can be accessed manually (i.e. with human intervention)
- RDA-A1-04M: Metadata is accessed through standardised protocol

are implemented via the standardized OAI-PMH interface.

And for *Reusability* indicator

- RDA-R1.3-02M: Metadata is expressed in compliance with a machine-understandable community standard

is implicit covered by the guidelines.



.. image:: _static/FAIR-Indicator_InstThemRepoGuidelines.png
    :width: 800px
    :align: center
    :alt: analyzed FAIR Indicator for the OpenAIRE Guidelines for instiutional and thematic repository managers


Out of the scope of these guidelines are the indicators:

- RDA-A1-02D: Data can be accessed manually (i.e. with human intervention)
- RDA-A2-01M: Metadata is guaranteed to remain available after data is no longer available
- RDA-I2-01D: Data uses FAIR-compliant vocabularies
- RDA-I3-01D: Data includes references to other data
- RDA-I3-02D: Data includes qualified references to other data


Not directly supported or crosswalks exists are:

- RDA-A1.2-01D: Data is accessible through an access protocol that supports authentication and authorisation
- RDA-I1-02D: Data uses machine-understandable knowledge representation
- RDA-R1.2-01M: Metadata includes provenance information according to community-specific standards
- RDA-R1.2-02M: Metadata includes provenance information according to a cross-community language
- RDA-R1.3-01D: Data complies with a community standard
- RDA-R1.3-02D: Data is expressed in compliance with a machine-understandable community standard
