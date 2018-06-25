.. _dci:subject:

17. Subject (MA)
^^^^^^^^^^^^^^^^

Subject, keyword, classification code, or key phrase describing the resource (occurrences: 0-n).

Field under the DataCite namespace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``datacite:subject``

Usage
~~~~~
*Mandatory when applicable (MA)*

Usage Instruction
~~~~~~~~~~~~~~~~~
In the subject property two kinds of values are possible: encode either a keyword or a classification. 

In general, choose the most significant and unique words for keywords, avoiding those too general to describe a particular resource. 

For keywords/keyphrases that are not controlled by a vocabulary or thesaurus either encode multiple terms with a semi-colon separating each keyword/keyphrase;
or repeat the element for each term. There are no requirements regarding the capitalization of keywords though internal (within archive) consistency is recommended.

Where terms are taken from a standard classification schema: encode each term using the additional attributes of the subject property. Encode the complete subject descriptor according to the relevant scheme. Use the capitalisation and punctuation used in the original scheme.

It is recommended to use an URI when using classification schemes or controlled vocabularies especially when codified schemes are used DDC or UDC. Service providers can recognise encoding schemas more easy when the schema is “URI-fied” by an authority namespace. When the classification scheme is codified, use a human readable text of the code, preferably in English, directly below the codified element. For example:

.. code-block:: xml
   :linenos:

   <dc:subject>info:eu-repo/classification/ddc/641</dc:subject>
   <dc:subject>Anatomy</dc:subject>


If no specific classification scheme is used we recommend the Dewey Decimal Classification (DDC). 
More information about the DDC and the DDC Summaries can be found at https://www.oclc.org/en/dewey/resources.html . Please note that OCLC owns all copyright rights in the Dewey Decimal Classification system. Dewey, Dewey Decimal Classification, DDC, OCLC and WebDewey are registered trademarks of OCLC.

17.1 subjectScheme (O)
~~~~~~~~~~~~~~~~~~~~~~
The name of the subject scheme or classification code or authority if one is used (occurrences: 01).

**Allowed values, examples, other constraints**

Free text.

.. _d:subject_schemeuri:

17.2 schemeURI (O)
~~~~~~~~~~~~~~~~~~
The URI of the subject identifier scheme (occurrences: 0-1).

**Allowed values, examples, other constraints**

Examples:

* http://id.loc.gov/authorities/subjects
* http://dewey.info/

17.3 valueURI
~~~~~~~~~~~~~
The URI of the subject term.

Example
~~~~~~~
.. code-block:: xml
   :linenos:

   <subjects>
    <subject>Earth sciences and geology</subject>
    <subject subjectScheme="DDC" schemeURI="http://dewey.info/" valueURI="">
    551 Geology, hydrology, meteorology
    </subject>
   </subjects>
