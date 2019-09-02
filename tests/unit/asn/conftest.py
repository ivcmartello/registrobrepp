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
      <asn:check xmlns:asn="urn:ietf:params:xml:ns:asn-1.0">
        <asn:number>12345</asn:number>
        <asn:number>11111</asn:number>
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
      <asn:chkData xmlns:asn="urn:ietf:params:xml:ns:asn-1.0">
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
      <asn:create xmlns:asn="urn:ietf:params:xml:ns:asn-1.0">
        <asn:number>12345</asn:number>
        <asn:organization>BR-ABCD-LACNIC</asn:organization>
        <asn:contact type="routing">fan</asn:contact>
        <asn:contact type="security">hkk</asn:contact>
        <asn:asIn>from AS2 10 accept AS1 A2</asn:asIn>
        <asn:asOut>to AS2 announce AS3 AS4</asn:asOut>
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
      <asn:creData xmlns:asn="urn:ietf:params:xml:ns:asn-1.0">
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
      <asn:delete xmlns:asn="urn:ietf:params:xml:ns:asn-1.0">
        <asn:number>64500</asn:number>
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
      <asn:info xmlns:asn="urn:ietf:params:xml:ns:asn-1.0">
        <asn:number>64500</asn:number>
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
      <asn:infData xmlns:asn="urn:ietf:params:xml:ns:asn-1.0">
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
      <asn:renew xmlns:asn="urn:ietf:params:xml:ns:asn-1.0">
        <asn:number>64500</asn:number>
        <asn:curExpDate>2008-04-03T00:00:00.0Z</asn:curExpDate>
        <asn:period unit="y">3</asn:period>
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
      <asn:renData xmlns:asn="urn:ietf:params:xml:ns:asn-1.0">
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
      <asnReserve:create xmlns:asnReserve="urn:ietf:params:xml:ns:asnReserve-1.0">
        <asnReserve:startASN>65536</asnReserve:startASN>
        <asnReserve:endASN>131072</asnReserve:endASN>
        <asnReserve:organization>BR-ABCD-LACNIC</asnReserve:organization>
        <asnReserve:comment>Test Reservation</asnReserve:comment>
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
      <asnReserve:creData xmlns:asnReserve="urn:ietf:params:xml:ns:asnReserve-1.0">
        <asnReserve:id>1024</asnReserve:id>
        <asnReserve:crDate>1999-04-03T22:00:00.0Z</asnReserve:crDate>
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
      <asnReserve:delete xmlns:asnReserve="urn:ietf:params:xml:ns:asnReserve-1.0">
        <asnReserve:id>64500</asnReserve:id>
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
      <asn:transfer xmlns:asn="urn:ietf:params:xml:ns:asn-1.0">
        <asn:number>64500</asn:number>
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
      <asn:trnData xmlns:asn="urn:ietf:params:xml:ns:asn-1.0">
        <asn:number>64500</asn:number>
        <asn:trStatus>pending</asn:trStatus>
        <asn:reID>ClientX</asn:reID>
        <asn:reDate>2000-06-08T22:00:00.0Z</asn:reDate>
        <asn:acID>ClientY</asn:acID>
        <asn:acDate>2000-06-13T22:00:00.0Z</asn:acDate>
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
      <asn:update xmlns:asn="urn:ietf:params:xml:ns:asn-1.0">
        <asn:number>64500</asn:number>
        <asn:add>
          <asn:contact type="routing">fan</asn:contact>
          <asn:asIn>from AS2 10 accept AS1 A2</asn:asIn>
        </asn:add>
        <asn:rem>
          <asn:contact type="security">hkk</asn:contact>
          <asn:asOut>to AS2 announce AS3 AS4</asn:asOut>
        </asn:rem>
        <asn:chg>
          <asn:organization>BR-ABCD-LACNIC</asn:organization>
        </asn:chg>
        <asn:creation_date>2011-01-27T00:00:00.0Z</asn:creation_date>
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