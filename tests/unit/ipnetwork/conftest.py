import pytest
from decouple import config


@pytest.fixture
def ipnetworkxmlschema():
    from lxml import etree

    schema = config('EPPSCHEMAPATH', '../../../schemas') + '/ipnetwork-1.0.xsd'
    xmlschema_doc = etree.parse(schema)
    return etree.XMLSchema(xmlschema_doc)


@pytest.fixture
def checkipnetworkcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <check>
      <ipnetwork:check xmlns:ipnetwork="urn:ietf:params:xml:ns:ipnetwork-1.0">
        <ipnetwork:ipRange version="v4">
          <ipnetwork:startAddress>192.168.0.0</ipnetwork:startAddress>
          <ipnetwork:endAddress>192.168.0.255</ipnetwork:endAddress>
        </ipnetwork:ipRange>
      </ipnetwork:check>
    </check>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def responsecheckipnetworkcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <response>
    <result code="1000">
      <msg>Command completed successfully</msg>
    </result>
    <resData>
      <ipnetwork:chkData xmlns:ipnetwork="urn:ietf:params:xml:ns:ipnetwork-1.0">
        <ipnetwork:cd>
          <ipnetwork:ipRange avail="0" version="v4">
            <ipnetwork:startAddress>192.168.0.0</ipnetwork:startAddress>
            <ipnetwork:endAddress>192.168.0.255</ipnetwork:endAddress>
          </ipnetwork:ipRange>
          <ipnetwork:reason>In use</ipnetwork:reason>
        </ipnetwork:cd>
      </ipnetwork:chkData>
    </resData>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54322-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def createipnetworkcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <create>
      <ipnetwork:create xmlns:ipnetwork="urn:ietf:params:xml:ns:ipnetwork-1.0">
        <ipnetwork:ipRange version="v4">
          <ipnetwork:startAddress>192.168.16.0</ipnetwork:startAddress>
          <ipnetwork:endAddress>192.168.31.255</ipnetwork:endAddress>
        </ipnetwork:ipRange>
        <ipnetwork:organization>BR-ABC-LACNIC</ipnetwork:organization>
        <ipnetwork:allocType>assignment</ipnetwork:allocType>
        <ipnetwork:contact type="admin">ABC123</ipnetwork:contact>
        <ipnetwork:reverseDNS>
          <ipnetwork:ipRange version="v4">
            <ipnetwork:startAddress>192.168.16.0</ipnetwork:startAddress>
            <ipnetwork:endAddress>192.168.17.255</ipnetwork:endAddress>
          </ipnetwork:ipRange>
          <ipnetwork:hostName>a.example.com</ipnetwork:hostName>
          <ipnetwork:hostName>b.example.com</ipnetwork:hostName>
        </ipnetwork:reverseDNS>
        <ipnetwork:dsData>
          <ipnetwork:ipRange version="v4">
            <ipnetwork:startAddress>192.168.16.0</ipnetwork:startAddress>
            <ipnetwork:endAddress>192.168.16.255</ipnetwork:endAddress>
          </ipnetwork:ipRange>
          <ipnetwork:keyTag>12345</ipnetwork:keyTag>
          <ipnetwork:alg>3</ipnetwork:alg>
          <ipnetwork:digestType>1</ipnetwork:digestType>
          <ipnetwork:digest>49FD46E6C4B45C55D4AC</ipnetwork:digest>
        </ipnetwork:dsData>
      </ipnetwork:create>
    </create>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def responsecreateipnetworkcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <response>
    <result code="1000">
      <msg>Command completed successfully</msg>
    </result>
    <resData>
      <ipnetwork:creData xmlns:ipnetwork="urn:ietf:params:xml:ns:ipnetwork-1.0">
        <ipnetwork:ipRange version="v4">
          <ipnetwork:startAddress>192.168.16.0</ipnetwork:startAddress>
          <ipnetwork:endAddress>192.168.31.255</ipnetwork:endAddress>
        </ipnetwork:ipRange>
        <ipnetwork:roid>b_123456-LACNIC</ipnetwork:roid>
        <ipnetwork:crDate>1999-04-03T22:00:00.0Z</ipnetwork:crDate>
      </ipnetwork:creData>
    </resData>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54321-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def deleteipnetworkcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <delete>
      <ipnetwork:delete xmlns:ipnetwork="urn:ietf:params:xml:ns:ipnetwork-1.0">
        <ipnetwork:roid>b_123456-LACNIC</ipnetwork:roid>
      </ipnetwork:delete>
    </delete>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def responsedeleteipnetworkcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
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


@pytest.fixture
def infoipnetworkcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <info>
      <ipnetwork:info xmlns:ipnetwork="urn:ietf:params:xml:ns:ipnetwork-1.0">
        <ipnetwork:ipRange version="v4">
          <ipnetwork:startAddress>192.168.0.0</ipnetwork:startAddress>
          <ipnetwork:endAddress>192.168.15.255</ipnetwork:endAddress>
        </ipnetwork:ipRange>
        <ipnetwork:roid>b_123456-LACNIC</ipnetwork:roid>
      </ipnetwork:info>
    </info>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def responseinfoipnetworkcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <response>
    <result code="1000">
      <msg>Command completed successfully</msg>
    </result>
    <resData>
      <ipnetwork:infData xmlns:ipnetwork="urn:ietf:params:xml:ns:ipnetwork-1.0">
        <ipnetwork:ipRange version="v4">
          <ipnetwork:startAddress>192.168.0.0</ipnetwork:startAddress>
          <ipnetwork:endAddress>192.168.15.255</ipnetwork:endAddress>
        </ipnetwork:ipRange>
        <ipnetwork:ipRangeInfo>
          <ipnetwork:roid>b_123456-LACNIC</ipnetwork:roid>
          <ipnetwork:allocType>allocation</ipnetwork:allocType>
          <ipnetwork:organization>BR-ABC-LACNIC</ipnetwork:organization>
          <ipnetwork:contact type="admin">HKK</ipnetwork:contact>
          <ipnetwork:reverseDNS>
            <ipnetwork:ipRange version="v4">
              <ipnetwork:startAddress>192.168.0.0</ipnetwork:startAddress>
              <ipnetwork:endAddress>192.168.0.255</ipnetwork:endAddress>
            </ipnetwork:ipRange>
            <ipnetwork:hostName>a.example.com</ipnetwork:hostName>
            <ipnetwork:hostName>b.example.com</ipnetwork:hostName>
          </ipnetwork:reverseDNS>
          <ipnetwork:reverseDNS>
            <ipnetwork:ipRange version="v4">
              <ipnetwork:startAddress>192.168.2.0</ipnetwork:startAddress>
              <ipnetwork:endAddress>192.168.2.255</ipnetwork:endAddress>
            </ipnetwork:ipRange>
            <ipnetwork:hostName>d.example.com</ipnetwork:hostName>
            <ipnetwork:hostName>e.example.com</ipnetwork:hostName>
          </ipnetwork:reverseDNS>
          <ipnetwork:dsData>
            <ipnetwork:ipRange version="v4">
              <ipnetwork:startAddress>192.168.0.0</ipnetwork:startAddress>
              <ipnetwork:endAddress>192.168.0.255</ipnetwork:endAddress>
            </ipnetwork:ipRange>
            <ipnetwork:keyTag>12345</ipnetwork:keyTag>
            <ipnetwork:alg>3</ipnetwork:alg>
            <ipnetwork:digestType>1</ipnetwork:digestType>
            <ipnetwork:digest>49FD46E6C4B45C55D4AC</ipnetwork:digest>
          </ipnetwork:dsData>
          <ipnetwork:dsData>
            <ipnetwork:ipRange version="v4">
              <ipnetwork:startAddress>192.168.2.0</ipnetwork:startAddress>
              <ipnetwork:endAddress>192.168.2.255</ipnetwork:endAddress>
            </ipnetwork:ipRange>
            <ipnetwork:keyTag>54321</ipnetwork:keyTag>
            <ipnetwork:alg>3</ipnetwork:alg>
            <ipnetwork:digestType>1</ipnetwork:digestType>
            <ipnetwork:digest>49FD46E6C4B45C55D4AC</ipnetwork:digest>
          </ipnetwork:dsData>
          <ipnetwork:parentNetwork>
            <ipnetwork:ipRange version="v4">
              <ipnetwork:startAddress>192.168.0.0</ipnetwork:startAddress>
              <ipnetwork:endAddress>192.168.255.255</ipnetwork:endAddress>
            </ipnetwork:ipRange>
            <ipnetwork:roid>b_12345-LACNIC</ipnetwork:roid>
          </ipnetwork:parentNetwork>
          <ipnetwork:childNetwork>
            <ipnetwork:ipRange version="v4">
              <ipnetwork:startAddress>192.168.0.0</ipnetwork:startAddress>
              <ipnetwork:endAddress>192.168.0.127</ipnetwork:endAddress>
            </ipnetwork:ipRange>
            <ipnetwork:roid>b_234567-LACNIC</ipnetwork:roid>
          </ipnetwork:childNetwork>
          <ipnetwork:clID>ClientY</ipnetwork:clID>
          <ipnetwork:crID>ClientX</ipnetwork:crID>
          <ipnetwork:crDate>1999-04-03T22:00:00.0Z</ipnetwork:crDate>
          <ipnetwork:upID>ClientX</ipnetwork:upID>
          <ipnetwork:upDate>1999-12-03T09:00:00.0Z</ipnetwork:upDate>
        </ipnetwork:ipRangeInfo>
      </ipnetwork:infData>
    </resData>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54322-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def renewipnetworkcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <renew>
      <ipnetwork:renew xmlns:ipnetwork="urn:ietf:params:xml:ns:ipnetwork-1.0">
        <ipnetwork:roid>b_12345-LACNIC</ipnetwork:roid>
        <ipnetwork:curExpDate>2008-04-03T00:00:00.0Z</ipnetwork:curExpDate>
        <ipnetwork:period unit="y">3</ipnetwork:period>
      </ipnetwork:renew>
    </renew>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def responserenewipnetworkcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <response>
    <result code="1000">
      <msg>Command completed successfully</msg>
    </result>
    <resData>
      <ipnetwork:renData xmlns:ipnetwork="urn:ietf:params:xml:ns:ipnetwork-1.0">
        <ipnetwork:roid>b_12345-LACNIC</ipnetwork:roid>
        <ipnetwork:exDate>2011-04-03T00:00:00.0Z</ipnetwork:exDate>
      </ipnetwork:renData>
    </resData>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54322-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def transferrequestipnetworkcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <transfer op="request">
      <ipnetwork:transfer xmlns:ipnetwork="urn:ietf:params:xml:ns:ipnetwork-1.0">
        <ipnetwork:roid>b_12345-LACNIC</ipnetwork:roid>
      </ipnetwork:transfer>
    </transfer>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def responsetransferipnetworkcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <response>
    <result code="1000">
      <msg>Command completed successfully</msg>
    </result>
    <resData>
      <ipnetwork:trnData xmlns:ipnetwork="urn:ietf:params:xml:ns:ipnetwork-1.0">
        <ipnetwork:roid>b_12345-LACNIC</ipnetwork:roid>
        <ipnetwork:trStatus>pending</ipnetwork:trStatus>
        <ipnetwork:reID>ClientX</ipnetwork:reID>
        <ipnetwork:reDate>2000-06-08T22:00:00.0Z</ipnetwork:reDate>
        <ipnetwork:acID>ClientY</ipnetwork:acID>
        <ipnetwork:acDate>2000-06-13T22:00:00.0Z</ipnetwork:acDate>
      </ipnetwork:trnData>
    </resData>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54322-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def updateipnetworkcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <update>
      <ipnetwork:update xmlns:ipnetwork="urn:ietf:params:xml:ns:ipnetwork-1.0">
        <ipnetwork:roid>b_123456-LACNIC</ipnetwork:roid>
        <ipnetwork:add>
          <ipnetwork:dsData>
            <ipnetwork:ipRange version="v4">
              <ipnetwork:startAddress>192.168.16.0</ipnetwork:startAddress>
              <ipnetwork:endAddress>192.168.16.255</ipnetwork:endAddress>
            </ipnetwork:ipRange>
            <ipnetwork:keyTag>12345</ipnetwork:keyTag>
            <ipnetwork:alg>3</ipnetwork:alg>
            <ipnetwork:digestType>1</ipnetwork:digestType>
            <ipnetwork:digest>49FD46E6C4B45C55D4AC</ipnetwork:digest>
          </ipnetwork:dsData>
          <ipnetwork:contact type="tech">AAA1</ipnetwork:contact>
        </ipnetwork:add>
        <ipnetwork:rem>
          <ipnetwork:dsData>
            <ipnetwork:ipRange version="v4">
              <ipnetwork:startAddress>192.168.16.0</ipnetwork:startAddress>
              <ipnetwork:endAddress>192.168.16.255</ipnetwork:endAddress>
            </ipnetwork:ipRange>
            <ipnetwork:keyTag>12345</ipnetwork:keyTag>
            <ipnetwork:alg>3</ipnetwork:alg>
            <ipnetwork:digestType>1</ipnetwork:digestType>
            <ipnetwork:digest>49FD46E6C4B45C55D4AC</ipnetwork:digest>
          </ipnetwork:dsData>
          <ipnetwork:contact type="abuse">AAA1</ipnetwork:contact>
        </ipnetwork:rem>
        <ipnetwork:chg>
          <ipnetwork:organization>BR-DEF-LACNIC</ipnetwork:organization>
          <ipnetwork:allocType>assignment</ipnetwork:allocType>
          <ipnetwork:asn>2</ipnetwork:asn>
        </ipnetwork:chg>
        <ipnetwork:aggr>
          <ipnetwork:roid>b_123456-LACNIC</ipnetwork:roid>
          <ipnetwork:hostName>a.a.com</ipnetwork:hostName>
        </ipnetwork:aggr>
        <ipnetwork:creation_date>2011-01-27T00:00:00.0Z</ipnetwork:creation_date>
      </ipnetwork:update>
    </update>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def responseupdateipnetworkcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
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