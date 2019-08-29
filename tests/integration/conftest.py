import pytest
from eppy.doc import EppResponse


@pytest.fixture
def objuris():
    return [
        'urn:ietf:params:xml:ns:domain-1.0',
        'urn:ietf:params:xml:ns:contact-1.0'
    ]


@pytest.fixture
def extraexturis():
    return [
        'urn:ietf:params:xml:ns:brdomain-1.0',
        'urn:ietf:params:xml:ns:brorg-1.0',
        'urn:ietf:params:xml:ns:secDNS-1.0',
        'urn:ietf:params:xml:ns:secDNS-1.1'
    ]


@pytest.fixture
def eppresponsecode1000():
    xml = """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <response>
    <result code="1000">
      <msg>Command completed successfully</msg>
    </result>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54321-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""
    return EppResponse.from_xml(xml)


@pytest.fixture
def eppresponsecode1500():
    xml = """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <response>
    <result code="1500">
      <msg>Command completed successfully; ending session</msg>
    </result>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54321-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""
    return EppResponse.from_xml(xml)
