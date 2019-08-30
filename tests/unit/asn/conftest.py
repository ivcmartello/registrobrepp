import pytest
from decouple import config


@pytest.fixture
def asnxmlschema():
    from lxml import etree

    schema = config('EPPSCHEMAPATH', '../../../schemas') + '/asn-1.0.xsd'
    xmlschema_doc = etree.parse(schema)
    return etree.XMLSchema(xmlschema_doc)


@pytest.fixture
def asnreservexmlschema():
    from lxml import etree

    schema = config('EPPSCHEMAPATH', '../../../schemas') + '/asnReserve-1.0.xsd'
    xmlschema_doc = etree.parse(schema)
    return etree.XMLSchema(xmlschema_doc)


@pytest.fixture
def checkasncommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <check>
      <asn:check xmlns="urn:ietf:params:xml:ns:asn-1.0" xmlns:asn="urn:ietf:params:xml:ns:asn-1.0">
        <number>12345</number>
        <number>11111</number>
      </asn:check>
    </check>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def responsecheckasncommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <response>
    <result code='1000'>
      <msg>Command completed successfully</msg>
    </result>
    <resData>
      <asn:chkData xmlns="urn:ietf:params:xml:ns:asn-1.0" xmlns:asn="urn:ietf:params:xml:ns:asn-1.0">
        <asn:cd>
          <asn:number avail="0">64500</asn:number>
          <asn:reason>In use</asn:reason>
        </asn:cd>
      </asn:chkData>
    </resData>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54322-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def createasncommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <create>
      <asn:create xmlns="urn:ietf:params:xml:ns:asn-1.0" xmlns:asn="urn:ietf:params:xml:ns:asn-1.0">
        <number>12345</number>
        <organization>BR-ABCD-LACNIC</organization>
        <contact type="routing">fan</contact>
        <contact type="security">hkk</contact>
        <asIn>from AS2 10 accept AS1 A2</asIn>
        <asOut>to AS2 announce AS3 AS4</asOut>
      </asn:create>
    </create>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def responseasncommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <response>
    <result code='1000'>
      <msg>Command completed successfully</msg>
    </result>
    <resData>
      <asn:creData xmlns="urn:ietf:params:xml:ns:asn-1.0" xmlns:asn="urn:ietf:params:xml:ns:asn-1.0">
        <asn:number>64500</asn:number>
        <asn:roid>64500-REP</asn:roid>
        <asn:crDate>1999-04-03T22:00:00.0Z</asn:crDate>
      </asn:creData>
    </resData>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54321-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def deleteasncommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <delete>
      <asn:delete xmlns="urn:ietf:params:xml:ns:asn-1.0" xmlns:asn="urn:ietf:params:xml:ns:asn-1.0">
        <number>64500</number>
      </asn:delete>
    </delete>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def responsedeleteasncommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <response>
    <result code='1000'>
      <msg>Command completed successfully</msg>
    </result>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54321-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def infoasncommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <info>
      <asn:info xmlns="urn:ietf:params:xml:ns:asn-1.0" xmlns:asn="urn:ietf:params:xml:ns:asn-1.0">
        <number>64500</number>
      </asn:info>
    </info>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def responseinfoasncommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <response>
    <result code='1000'>
      <msg>Command completed successfully</msg>
    </result>
    <resData>
      <asn:infData xmlns="urn:ietf:params:xml:ns:asn-1.0" xmlns:asn="urn:ietf:params:xml:ns:asn-1.0">
        <asn:number>64500</asn:number>
        <asn:roid>64500-REP</asn:roid>
        <asn:organization>BR-ABCD-LACNIC</asn:organization>
        <asn:contact type='routing'>fan</asn:contact>
        <asn:contact type='security'>hkk</asn:contact>
        <asn:clID>ClientY</asn:clID>
        <asn:crID>ClientX</asn:crID>
        <asn:crDate>1999-04-03T22:00:00.0Z</asn:crDate>
        <asn:upID>ClientX</asn:upID>
        <asn:upDate>2005-12-03T09:00:00.0Z</asn:upDate>
        <asn:trDate>2004-04-08T09:00:00.0Z</asn:trDate>
        <asn:asIn>from AS2 10 accept AS1 A2</asn:asIn>
        <asn:asIn>from AS3 10 accept AS1 A2</asn:asIn>
        <asn:asOut>to AS2 announce AS3 AS4</asn:asOut>
        <asn:asOut>to AS5 announce AS3 AS4</asn:asOut>
      </asn:infData>
    </resData>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54322-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def renewasncommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <renew>
      <asn:renew xmlns="urn:ietf:params:xml:ns:asn-1.0" xmlns:asn="urn:ietf:params:xml:ns:asn-1.0">
        <number>64500</number>
        <curExpDate>2008-04-03T00:00:00.0Z</curExpDate>
        <period unit="y">3</period>
      </asn:renew>
    </renew>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def responserenewasncommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <response>
    <result code='1000'>
      <msg>Command completed successfully</msg>
    </result>
    <resData>
      <asn:renData xmlns="urn:ietf:params:xml:ns:asn-1.0" xmlns:asn="urn:ietf:params:xml:ns:asn-1.0">
        <asn:number>64500</asn:number>
        <asn:exDate>2011-04-03T00:00:00.0Z</asn:exDate>
      </asn:renData>
    </resData>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54322-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def createreserveasncommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <create>
      <asnReserve:create xmlns="urn:ietf:params:xml:ns:asnReserve-1.0" xmlns:asnReserve="urn:ietf:params:xml:ns:asnReserve-1.0">
        <startASN>65536</startASN>
        <endASN>131072</endASN>
        <organization>BR-ABCD-LACNIC</organization>
        <comment>Test Reservation</comment>
      </asnReserve:create>
    </create>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def responsecreatereserveasncommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">		
  <response>
    <result code='1000'>
      <msg>Command completed successfully</msg>
    </result>
    <resData>
      <asnReserve:creData xmlns="urn:ietf:params:xml:ns:asnReserve-1.0" xmlns:asnReserve="urn:ietf:params:xml:ns:asnReserve-1.0">
        <id>1024</id>
        <crDate>1999-04-03T22:00:00.0Z</crDate>
      </asnReserve:creData>
    </resData>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54321-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def deletereserveasncommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <delete>
      <asnReserve:delete xmlns="urn:ietf:params:xml:ns:asnReserve-1.0" xmlns:asnReserve="urn:ietf:params:xml:ns:asnReserve-1.0">
        <id>64500</id>
      </asnReserve:delete>
    </delete>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def responsedeletereserveasncommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <response>
    <result code='1000'>
      <msg>Command completed successfully</msg>
    </result>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54321-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def transferrequestasncommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <transfer op="request">
      <asn:transfer xmlns="urn:ietf:params:xml:ns:asn-1.0" xmlns:asn="urn:ietf:params:xml:ns:asn-1.0">
        <number>64500</number>
      </asn:transfer>
    </transfer>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def responsetransferrequestasncommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <response>
    <result code='1000'>
      <msg>Command completed successfully</msg>
    </result>
    <resData>
      <asn:trnData xmlns="urn:ietf:params:xml:ns:asn-1.0" xmlns:asn="urn:ietf:params:xml:ns:asn-1.0">
        <number>64500</number>
        <trStatus>pending</trStatus>
        <reID>ClientX</reID>
        <reDate>2000-06-08T22:00:00.0Z</reDate>
        <acID>ClientY</acID>
        <acDate>2000-06-13T22:00:00.0Z</acDate>
      </asn:trnData>
    </resData>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54322-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def updateasncommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <update>
      <asn:update xmlns="urn:ietf:params:xml:ns:asn-1.0" xmlns:asn="urn:ietf:params:xml:ns:asn-1.0">
        <number>64500</number>
        <add>
          <contact type="routing">fan</contact>
          <asIn>from AS2 10 accept AS1 A2</asIn>
        </add>
        <rem>
          <contact type="security">hkk</contact>
          <asOut>to AS2 announce AS3 AS4</asOut>
        </rem>
        <chg>
          <organization>BR-ABCD-LACNIC</organization>
        </chg>
        <creation_date>2011-01-27T00:00:00.0Z</creation_date>
      </asn:update>
    </update>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def responseupdateasncommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <response>
    <result code='1000'>
      <msg>Command completed successfully</msg>
    </result>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54321-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""