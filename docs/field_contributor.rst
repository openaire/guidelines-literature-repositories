.. _dci:contributor:

3. Contributor (MA)
===================

The institution or person responsible for collecting, managing, distributing, or otherwise contributing to the development of the resource.

.. _dci:contributor_contributorName:

3.1 contributorName (M)
-----------------------

The name of the contributor.

3.1.1 nameType (R)
------------------

The type of name.

*Controlled list values*

* Organizational
* Personal

3.2 givenName (O)
-----------------

The personal or first name of the contributor.

3.3 familyName (O)
------------------

The surname or last name of the contributor.

3.4 nameIdentifier (R)
----------------------

Uniquely identifies an individual or legal entity, according to various schemes.

3.4.1 nameIdentifierScheme
^^^^^^^^^^^^^^^^^^^^^^^^^^

The name of the name identifier scheme.

3.4.2 schemeURI
^^^^^^^^^^^^^^^

The URI of the name identifier scheme.


3.5 affiliation
---------------

The organisational or institutional affiliation of the contributor.

3.6 contributorType
-------------------

The type of contributor of the resource

*Controlled list values*

* ContactPerson
* DataCollector
* DataCurator
* DataManager
* Distributor
* Editor
* HostingInstitution
* Producer
* ProjectLeader
* ProjectManager
* ProjectMember
* RegistrationAgency
* RegistrationAuthority
* RelatedPerson
* Researcher
* ResearchGroup
* RightsHolder
* Sponsor
* Supervisor
* WorkPackageLeader
* Other

**DCMI Definition**

An entity responsible for making contributions to the content of the resource. Examples of a Contributor include a person, an organization, or a service. Typically, the name of a Contributor should be used to indicate the entity.

**Usage Instruction**

Examples of contributors are: a supervisor, editor, technician or data collector.

Personal names should be listed as: see instructions under Creator. A “supervisor”, i.e. a professor supervising a student’s work for a doctor’s degree - is considered a contributor of a dissertation in his or her role as promotor/examiner. In the PhD thesis as a document, the key figures are the author and the supervisor. 

In the case of organizations : see instructions under Creator The inclusion of personal and corporate name headings from authority lists constructed according to local or national thesaurus files is optional.

**Do Not Confuse With**

* :ref:`dc:publisher`
* :ref:`dci:creator`
* :ref:`dci:fundingReference`

The element ``contributor`` describes the scientist(s) that has/have made contributions to the given scientific output, not as a primary creator or (commercial) publisher.

**Modified**

adopted ``contributor`` elements from DataCite schema in OpenAIRE Guidelines v4

**Example**

.. code-block:: xml
   :linenos:

   <contributor>
     <contributorName>Evans, R. J.</contributorName>
   <contributor>
   <contributor>
     <contributorName>International Human Genome Sequencing Consortium</contributorName>
   </contributor>
