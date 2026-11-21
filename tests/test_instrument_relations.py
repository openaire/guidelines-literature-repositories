"""Validate Instrument / IsCollectedBy / Collects support (issue #53) against the local 4.0 schema.

Run: python -m unittest discover tests
"""
import os
import unittest

from lxml import etree

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCHEMA = os.path.join(ROOT, "schemas", "4.0", "openaire.xsd")
SAMPLE = os.path.join(ROOT, "samples", "sample_minimal.xml")
DATACITE_NS = "http://datacite.org/schema/kernel-4"

# Minimal offline stand-in for http://www.w3.org/2009/01/xml.xsd (imported by the schemas).
XML_XSD = b"""<?xml version="1.0"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
           targetNamespace="http://www.w3.org/XML/1998/namespace" xml:lang="en">
  <xs:attribute name="lang" type="xs:string"/>
  <xs:attribute name="space" type="xs:NCName"/>
  <xs:attribute name="base" type="xs:anyURI"/>
  <xs:attribute name="id" type="xs:ID"/>
</xs:schema>"""


class _XmlXsdResolver(etree.Resolver):
    def resolve(self, url, pubid, context):
        if url.endswith("www.w3.org/2009/01/xml.xsd"):
            return self.resolve_string(XML_XSD, context)
        return None


def _load_schema():
    parser = etree.XMLParser()
    parser.resolvers.add(_XmlXsdResolver())
    return etree.XMLSchema(etree.parse(SCHEMA, parser))


def _record(relation_type, resource_type_general="Instrument"):
    doc = etree.parse(SAMPLE)
    related = etree.SubElement(doc.getroot(), "{%s}relatedIdentifiers" % DATACITE_NS)
    rel = etree.SubElement(related, "{%s}relatedIdentifier" % DATACITE_NS)
    rel.set("relatedIdentifierType", "DOI")
    rel.set("relationType", relation_type)
    rel.set("resourceTypeGeneral", resource_type_general)
    rel.text = "10.1234/instrument-pid"
    return doc


class InstrumentRelationsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = _load_schema()

    def assertValid(self, doc):
        self.assertTrue(self.schema.validate(doc), str(self.schema.error_log))

    def test_baseline_sample_is_valid(self):
        self.assertValid(etree.parse(SAMPLE))

    def test_is_collected_by_instrument(self):
        self.assertValid(_record("IsCollectedBy"))

    def test_collects(self):
        self.assertValid(_record("Collects"))

    def test_references_instrument(self):
        self.assertValid(_record("References"))

    def test_unknown_relation_type_is_rejected(self):
        self.assertFalse(self.schema.validate(_record("IsCollectedFrom")))

    def test_unknown_resource_type_general_is_rejected(self):
        self.assertFalse(self.schema.validate(_record("IsCollectedBy", "Instruments")))


if __name__ == "__main__":
    unittest.main()
