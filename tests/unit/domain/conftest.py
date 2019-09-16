import pytest
from decouple import config


@pytest.fixture
def domainxmlschema():
    from lxml import etree

    schema = config('EPPSCHEMAPATH', '../../../schemas') + '/domain-1.0.xsd'
    xmlschema_doc = etree.parse(schema)
    return etree.XMLSchema(xmlschema_doc)


@pytest.fixture
def checkdomaincommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <check>
      <domain:check xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <domain:name>du.eti.br</domain:name>
        <domain:name>nic.br</domain:name>
        <domain:name>registro.br</domain:name>
      </domain:check>
    </check>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def checkdomaincommandwithlaunchxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <check>
      <domain:check xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <domain:name>du.eti.br</domain:name>
        <domain:name>nic.br</domain:name>
        <domain:name>registro.br</domain:name>
      </domain:check>
    </check>
    <extension>
      <launch:check type="claims" xmlns:launch="urn:ietf:params:xml:ns:launch-1.0">
        <launch:phase>claims</launch:phase>
      </launch:check>
    </extension>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def checkdomaincommandwithbrdomainxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <check>
      <domain:check xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <domain:name>du.eti.br</domain:name>
        <domain:name>nic.br</domain:name>
        <domain:name>registro.br</domain:name>
      </domain:check>
    </check>
    <extension>
      <brdomain:check xmlns:brdomain="urn:ietf:params:xml:ns:brdomain-1.0">
        <brdomain:organization>005.506.560/0001-36</brdomain:organization>
      </brdomain:check>
    </extension>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def responsecheckdomaincommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <response>
    <result code="1000">
      <msg>Command completed successfully</msg>
    </result>
    <resData>
      <domain:chkData xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <domain:cd>
          <domain:name avail="1">example.com</domain:name>
        </domain:cd>
        <domain:cd>
          <domain:name avail="0">example.net</domain:name>
          <domain:reason>In use</domain:reason>
        </domain:cd>
        <domain:cd>
          <domain:name avail="1">example.org</domain:name>
        </domain:cd>
      </domain:chkData>
    </resData>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54322-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def responsecheckdomaincommandwithbrdomainxmlexpected():
    return """<epp xmlns='urn:ietf:params:xml:ns:epp-1.0'>
  <response>
    <result code='1000'>
      <msg>Command completed successfully</msg>
    </result>
    <resData>
      <domain:chkData xmlns:domain='urn:ietf:params:xml:ns:domain-1.0'>
        <domain:cd>
          <domain:name avail='0'>e-xample.net.br</domain:name>
          <domain:reason>In use</domain:reason>
        </domain:cd>
        <domain:cd>
          <domain:name avail='1'>example.com.br</domain:name>
        </domain:cd>
        <domain:cd>
          <domain:name avail='1'>example.ind.br</domain:name>
        </domain:cd>
        <domain:cd>
          <domain:name avail='0'>example.org.br</domain:name>
        </domain:cd>
      </domain:chkData>
    </resData>
    <extension>
      <brdomain:chkData xmlns:brdomain='urn:ietf:params:xml:ns:brdomain-1.0'>
        <brdomain:cd>
          <brdomain:name>e-xample.net.br</brdomain:name>
          <brdomain:equivalentName>example.net.br</brdomain:equivalentName>
          <brdomain:organization>043.828.151/0001-45</brdomain:organization>
        </brdomain:cd>
        <brdomain:cd hasConcurrent='1'>
          <brdomain:name>example.com.br</brdomain:name>
          <brdomain:ticketNumber>123456</brdomain:ticketNumber>
        </brdomain:cd>
        <brdomain:cd inReleaseProcess='1'>
          <brdomain:name>example.ind.br</brdomain:name>
        </brdomain:cd>
        <brdomain:cd>
          <brdomain:name>example.org.br</brdomain:name>
          <brdomain:organization>043.828.151/0001-45</brdomain:organization>
        </brdomain:cd>
      </brdomain:chkData>
    </extension>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54322-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def createdomaincommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <create>
      <domain:create xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <domain:name>example.com</domain:name>
        <domain:period unit="y">2</domain:period>
        <domain:ns>
          <domain:hostObj>ns1.example.net</domain:hostObj>
          <domain:hostObj>ns2.example.net</domain:hostObj>
        </domain:ns>
        <domain:registrant>jd1234</domain:registrant>
        <domain:contact type="admin">sh8013</domain:contact>
        <domain:contact type="tech">sh8013</domain:contact>
        <domain:contact type="billing">xxx</domain:contact>
        <domain:authInfo>
          <domain:pw>2fooBAR</domain:pw>
        </domain:authInfo>
      </domain:create>
    </create>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def createdomaincommandwithnshostattxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <create>
      <domain:create xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <domain:name>example.com</domain:name>
        <domain:period unit="y">2</domain:period>
        <domain:ns>
          <domain:hostAttr>
            <domain:hostName>ns1.example.com</domain:hostName>
            <domain:hostAddr ip="v4">192.168.0.0</domain:hostAddr>
          </domain:hostAttr>
        </domain:ns>
        <domain:registrant>jd1234</domain:registrant>
        <domain:contact type="admin">sh8013</domain:contact>
        <domain:contact type="tech">sh8013</domain:contact>
        <domain:contact type="billing">xxx</domain:contact>
        <domain:authInfo>
          <domain:pw>2fooBAR</domain:pw>
        </domain:authInfo>
      </domain:create>
    </create>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def createdomaincommandwithsecdnsxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <create>
      <domain:create xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <domain:name>example.com</domain:name>
        <domain:period unit="y">2</domain:period>
        <domain:ns>
          <domain:hostObj>ns1.example.net</domain:hostObj>
          <domain:hostObj>ns2.example.net</domain:hostObj>
        </domain:ns>
        <domain:registrant>jd1234</domain:registrant>
        <domain:contact type="admin">sh8013</domain:contact>
        <domain:contact type="tech">sh8013</domain:contact>
        <domain:contact type="billing">xxx</domain:contact>
        <domain:authInfo>
          <domain:pw>2fooBAR</domain:pw>
        </domain:authInfo>
      </domain:create>
    </create>
    <extension>
      <secDNS:create xmlns:secDNS="urn:ietf:params:xml:ns:secDNS-1.1">
        <secDNS:dsData>
          <secDNS:keyTag>12345</secDNS:keyTag>
          <secDNS:alg>3</secDNS:alg>
          <secDNS:digestType>1</secDNS:digestType>
          <secDNS:digest>49FD46E6C4B45C55D4AC</secDNS:digest>
        </secDNS:dsData>
      </secDNS:create>
    </extension>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def createdomaincommandwithlaunchxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <create>
      <domain:create xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <domain:name>example.com</domain:name>
        <domain:period unit="y">2</domain:period>
        <domain:ns>
          <domain:hostObj>ns1.example.net</domain:hostObj>
          <domain:hostObj>ns2.example.net</domain:hostObj>
        </domain:ns>
        <domain:registrant>jd1234</domain:registrant>
        <domain:contact type="admin">sh8013</domain:contact>
        <domain:contact type="tech">sh8013</domain:contact>
        <domain:contact type="billing">xxx</domain:contact>
        <domain:authInfo>
          <domain:pw>2fooBAR</domain:pw>
        </domain:authInfo>
      </domain:create>
    </create>
    <extension>
      <launch:create xmlns:launch="urn:ietf:params:xml:ns:launch-1.0">
        <launch:phase>sunrise</launch:phase>
        <smd:encodedSignedMark xmlns:smd="urn:ietf:params:xml:ns:signedMark-1.0">YkM1cFkyRnViaTV2Y21jdmRHMWphRjl3YVd4dmRDNWpjbXd3UlFZRFZSMGdCRDR3UERBNkJnTXFBd1F3TXpBeEJnZ3JCZ0VGQlFjQwpBUllsYUhSMGNEb3ZMM2QzZHk1cFkyRnViaTV2Y21jdmNHbHNiM1JmY21Wd2IzTnBkRzl5ZVRBTkJna3Foa2lHOXcwQkFRc0ZBQU9DCkFRRUFLVWZFSjVYNlFBdHRhampSVnNlSkZReFJYR0hUZ0NhRGs4Qy8xbmoxaWVsWkF1WnRnZFVwV0RVcjBObkdDaStMSFNzZ2RUWVIKK3ZNcnhpcjdFVllRZXZyQm9iRUxreGVURWZqRjlGVnFqQkhJbnlQRkxPRmt6MTV6R0cySXdQSnBzK3ZoQWQvN2dUMHBoMWsyRkVrSgpGR0w1THdSZjFtczRJWDB2RGt4VElYOFF4eTFqY3pDaVNzb1Y4cHdsaGgyTkhBa3BHUVdOL3BUUzBVcWk3dVU1Qm0vSW9HdlBCelVwCjVuNVNqVU1uVFp4LysxekF1ZXJTYWJ0NDgzc1hCY1dzamdsN01xRnRmT05pQXROZU1OZmg2MGxUTXU0emdWd0xaVE80VFFNNVEydXkKbFBQbVp0d25BODhRdk0ySUw4NWNJWUpIZDB6OWpwVVFNQkdIWEYyV1FBPT08L2RzOlg1MDlDZXJ0aWZpY2F0ZT48L2RzOlg1MDlEYXRhPjwvZHM6S2V5SW5mbz48L2RzOlNpZ25hdHVyZT48L3NtZDpzaWduZWRNYXJrPg==</smd:encodedSignedMark>
      </launch:create>
    </extension>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def createdomaincommandwithbrdomainxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <create>
      <domain:create xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <domain:name>example.com</domain:name>
        <domain:period unit="y">2</domain:period>
        <domain:ns>
          <domain:hostObj>ns1.example.net</domain:hostObj>
          <domain:hostObj>ns2.example.net</domain:hostObj>
        </domain:ns>
        <domain:registrant>jd1234</domain:registrant>
        <domain:contact type="admin">sh8013</domain:contact>
        <domain:contact type="tech">sh8013</domain:contact>
        <domain:contact type="billing">xxx</domain:contact>
        <domain:authInfo>
          <domain:pw>2fooBAR</domain:pw>
        </domain:authInfo>
      </domain:create>
    </create>
    <extension>
      <brdomain:create xmlns:brdomain="urn:ietf:params:xml:ns:brdomain-1.0">
        <brdomain:organization>005.506.560/0001-36</brdomain:organization>
        <brdomain:releaseProcessFlags flag1="1" />
        <brdomain:autoRenew active="1" />
      </brdomain:create>
    </extension>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def responsecreatedomaincommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <response>
    <result code="1000">
      <msg>Command completed successfully</msg>
    </result>
    <resData>
      <domain:creData xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <domain:name>example.com</domain:name>
        <domain:crDate>1999-04-03T22:00:00.0Z</domain:crDate>
        <domain:exDate>2001-04-03T22:00:00.0Z</domain:exDate>
      </domain:creData>
    </resData>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54321-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def responsecreatedomaincommandwithbrdomaixmlexpected():
    return """<epp xmlns='urn:ietf:params:xml:ns:epp-1.0'>
  <response>
    <result code='1001'>
      <msg>Command completed successfully; action pending</msg>
    </result>
    <resData>
      <domain:creData xmlns:domain='urn:ietf:params:xml:ns:domain-1.0'>
        <domain:name>example.com.br</domain:name>
        <domain:crDate>2006-01-30T22:00:00.0Z</domain:crDate>
      </domain:creData>
    </resData>
    <extension>
      <brdomain:creData xmlns:brdomain='urn:ietf:params:xml:ns:brdomain-1.0'>
        <brdomain:ticketNumber>123456</brdomain:ticketNumber>
        <brdomain:pending>
          <brdomain:doc status='notReceived'>
            <brdomain:docType>CNPJ</brdomain:docType>
            <brdomain:limit>2006-03-01T22:00:00.0Z</brdomain:limit>
            <brdomain:description lang='pt'>Cadastro Nacional da Pessoa Juridica</brdomain:description>
          </brdomain:doc>
          <brdomain:dns status='queryTimeOut'>
            <brdomain:hostName>ns1.example.com.br</brdomain:hostName>
            <brdomain:limit>2006-02-13T22:00:00.0Z</brdomain:limit>
          </brdomain:dns>
        </brdomain:pending>
        <brdomain:ticketNumberConc>123451</brdomain:ticketNumberConc>
        <brdomain:ticketNumberConc>123455</brdomain:ticketNumberConc>
      </brdomain:creData>
    </extension>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54321-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def deletedomaincommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <delete>
      <domain:delete xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <domain:name>example.com</domain:name>
      </domain:delete>
    </delete>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def deletedomaincommandwithlaunchxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <delete>
      <domain:delete xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <domain:name>example.com</domain:name>
      </domain:delete>
    </delete>
    <extension>
      <launch:delete xmlns:launch="urn:ietf:params:xml:ns:launch-1.0">
        <launch:phase>sunrise</launch:phase>
        <launch:applicationID>abc123</launch:applicationID>
      </launch:delete>
    </extension>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def responsedeletedomaincommandxmlexpected():
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
def renewdomaincommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <renew>
      <domain:renew xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <domain:name>example.com.br</domain:name>
        <domain:curExpDate>2000-04-03</domain:curExpDate>
        <domain:period unit="y">5</domain:period>
      </domain:renew>
    </renew>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def responserenewdomaincommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <response>
    <result code="1000">
      <msg>Command completed successfully</msg>
    </result>
    <resData>
      <domain:renData xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <domain:name>example.com</domain:name>
        <domain:exDate>2005-04-03T22:00:00.0Z</domain:exDate>
      </domain:renData>
    </resData>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54322-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def responserenewdomaincommandwithbrdomaixmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <response>
    <result code="1000">
      <msg>Command completed successfully</msg>
    </result>
    <resData>
      <domain:renData xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <domain:name>example.com.br</domain:name>
        <domain:exDate>2007-04-03T00:00:00.0Z</domain:exDate>
      </domain:renData>
    </resData>
    <extension>
      <brdomain:renData xmlns:brdomain="urn:ietf:params:xml:ns:brdomain-1.0">
        <brdomain:publicationStatus publicationFlag="onHold">
          <brdomain:onHoldReason>billing</brdomain:onHoldReason>
          <brdomain:onHoldReason>dns</brdomain:onHoldReason>
        </brdomain:publicationStatus>
      </brdomain:renData>
    </extension>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54322-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def infodomaincommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <info>
      <domain:info xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <domain:name hosts="all">example.com</domain:name>
        <domain:authInfo>
          <domain:pw>2fooBAR</domain:pw>
        </domain:authInfo>
      </domain:info>
    </info>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def infodomaincommandwithlaunchxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <info>
      <domain:info xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <domain:name hosts="all">example.com</domain:name>
        <domain:authInfo>
          <domain:pw>2fooBAR</domain:pw>
        </domain:authInfo>
      </domain:info>
    </info>
    <extension>
      <launch:info includeMark="true" xmlns:launch="urn:ietf:params:xml:ns:launch-1.0">
        <launch:phase>claims</launch:phase>
        <launch:applicationID>abc123</launch:applicationID>
      </launch:info>
    </extension>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def infodomaincommandwithbrdomainxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <info>
      <domain:info xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <domain:name hosts="all">example.com</domain:name>
        <domain:authInfo>
          <domain:pw>2fooBAR</domain:pw>
        </domain:authInfo>
      </domain:info>
    </info>
    <extension>
      <brdomain:info xmlns:brdomain="urn:ietf:params:xml:ns:brdomain-1.0">
        <brdomain:ticketNumber>123456</brdomain:ticketNumber>
      </brdomain:info>
    </extension>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def responseinfodomaincommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <response>
    <result code="1000">
      <msg>Command completed successfully</msg>
    </result>
    <resData>
      <domain:infData xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <domain:name>example.com</domain:name>
        <domain:roid>EXAMPLE1-REP</domain:roid>
        <domain:status s="ok" />
        <domain:registrant>jd1234</domain:registrant>
        <domain:contact type="admin">sh8013</domain:contact>
        <domain:contact type="tech">sh8013</domain:contact>
        <domain:ns>
          <domain:hostObj>ns1.example.com</domain:hostObj>
          <domain:hostObj>ns1.example.net</domain:hostObj>
        </domain:ns>
        <domain:host>ns1.example.com</domain:host>
        <domain:host>ns2.example.com</domain:host>
        <domain:clID>ClientX</domain:clID>
        <domain:crID>ClientY</domain:crID>
        <domain:crDate>1999-04-03T22:00:00.0Z</domain:crDate>
        <domain:upID>ClientX</domain:upID>
        <domain:upDate>1999-12-03T09:00:00.0Z</domain:upDate>
        <domain:exDate>2005-04-03T22:00:00.0Z</domain:exDate>
        <domain:trDate>2000-04-08T09:00:00.0Z</domain:trDate>
        <domain:authInfo>
          <domain:pw>2fooBAR</domain:pw>
        </domain:authInfo>
      </domain:infData>
    </resData>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54322-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def responseinfodomaincommandxmlunauthorizedclient():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <response>
    <result code="1000">
      <msg>Command completed successfully</msg>
    </result>
    <resData>
      <domain:infData xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <domain:name>example.com</domain:name>
        <domain:roid>EXAMPLE1-REP</domain:roid>
        <domain:clID>ClientX</domain:clID>
      </domain:infData>
    </resData>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54322-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def responseinfodomaincommandwithbrdomainxmlexpected():
    return """<epp xmlns='urn:ietf:params:xml:ns:epp-1.0'>
  <response>
    <result code='1000'>
      <msg>Command completed successfully</msg>
    </result>
    <resData>
      <domain:infData xmlns:domain='urn:ietf:params:xml:ns:domain-1.0'>
        <domain:name>example.com.br</domain:name>
        <domain:roid>EXAMPLE1-REP</domain:roid>
        <domain:status s='pendingCreate'/>
        <domain:contact type='admin'>fan</domain:contact>
        <domain:contact type='billing'>fan</domain:contact>
        <domain:contact type='tech'>fan</domain:contact>    
        <domain:ns>
          <domain:hostAttr>
            <domain:hostName>ns1.example.com.br</domain:hostName>
            <domain:hostAddr ip='v4'>192.0.2.1</domain:hostAddr>
          </domain:hostAttr>
          <domain:hostAttr>
            <domain:hostName>ns1.example.net.br</domain:hostName>
          </domain:hostAttr>
        </domain:ns>
        <domain:clID>ClientX</domain:clID>
        <domain:crID>ClientX</domain:crID>
        <domain:crDate>2006-01-30T22:00:00.0Z</domain:crDate>
        <domain:upID>ClientX</domain:upID>
        <domain:upDate>2006-01-31T09:00:00.0Z</domain:upDate>
      </domain:infData>
    </resData>
    <extension>
      <brdomain:infData xmlns:brdomain='urn:ietf:params:xml:ns:brdomain-1.0'>
        <brdomain:organization>005.506.560/0001-36</brdomain:organization>"
        <brdomain:publicationStatus publicationFlag="onHold">
          <brdomain:onHoldReason>billing</brdomain:onHoldReason>
          <brdomain:onHoldReason>dns</brdomain:onHoldReason>
        </brdomain:publicationStatus>
        <brdomain:autoRenew active="1"/>
      </brdomain:infData>
    </extension>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54322-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def transferquerydomaincommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <transfer op="query">
      <domain:transfer xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <domain:name>example.com</domain:name>
        <domain:authInfo>
          <domain:pw roid="JD1234-REP">2fooBAR</domain:pw>
        </domain:authInfo>
      </domain:transfer>
    </transfer>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def transferrequestdomaincommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <transfer op="request">
      <domain:transfer xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <domain:name>example.com</domain:name>
        <domain:period unit="y">1</domain:period>
        <domain:authInfo>
          <domain:pw roid="JD1234-REP">2fooBAR</domain:pw>
        </domain:authInfo>
      </domain:transfer>
    </transfer>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def responsetransferquerydomaincommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <response>
    <result code="1000">
      <msg>Command completed successfully</msg>
    </result>
    <resData>
      <domain:trnData xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <domain:name>example.com</domain:name>
        <domain:trStatus>pending</domain:trStatus>
        <domain:reID>ClientX</domain:reID>
        <domain:reDate>2000-06-06T22:00:00.0Z</domain:reDate>
        <domain:acID>ClientY</domain:acID>
        <domain:acDate>2000-06-11T22:00:00.0Z</domain:acDate>
        <domain:exDate>2002-09-08T22:00:00.0Z</domain:exDate>
      </domain:trnData>
    </resData>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54322-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def responsetransferrequestdomaincommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <response>
    <result code="1001">
      <msg>Command completed successfully; action pending</msg>
    </result>
    <resData>
      <domain:trnData xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <domain:name>example.com</domain:name>
        <domain:trStatus>pending</domain:trStatus>
        <domain:reID>ClientX</domain:reID>
        <domain:reDate>2000-06-08T22:00:00.0Z</domain:reDate>
        <domain:acID>ClientY</domain:acID>
        <domain:acDate>2000-06-13T22:00:00.0Z</domain:acDate>
        <domain:exDate>2002-09-08T22:00:00.0Z</domain:exDate>
      </domain:trnData>
    </resData>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54322-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def updatedomaincommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <update>
      <domain:update xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <domain:name>example.com</domain:name>
        <domain:add>
          <domain:ns>
            <domain:hostObj>ns2.example.com</domain:hostObj>
          </domain:ns>
          <domain:contact type="tech">mak21</domain:contact>
          <domain:status lang="en" s="clientHold">Payment overdue.</domain:status>
        </domain:add>
        <domain:rem>
          <domain:ns>
            <domain:hostObj>ns1.example.com</domain:hostObj>
          </domain:ns>
          <domain:contact type="tech">sh8013</domain:contact>
          <domain:status s="clientUpdateProhibited" />
        </domain:rem>
        <domain:chg>
          <domain:registrant>sh8013</domain:registrant>
          <domain:authInfo>
            <domain:pw>2BARfoo</domain:pw>
          </domain:authInfo>
        </domain:chg>
      </domain:update>
    </update>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def updatedomaincommandwithsecdnsxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <update>
      <domain:update xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <domain:name>example.com</domain:name>
        <domain:add>
          <domain:ns>
            <domain:hostObj>ns2.example.com</domain:hostObj>
          </domain:ns>
          <domain:contact type="tech">mak21</domain:contact>
          <domain:status lang="en" s="clientHold">Payment overdue.</domain:status>
        </domain:add>
        <domain:rem>
          <domain:ns>
            <domain:hostObj>ns1.example.com</domain:hostObj>
          </domain:ns>
          <domain:contact type="tech">sh8013</domain:contact>
          <domain:status s="clientUpdateProhibited" />
        </domain:rem>
        <domain:chg>
          <domain:registrant>sh8013</domain:registrant>
          <domain:authInfo>
            <domain:pw>2BARfoo</domain:pw>
          </domain:authInfo>
        </domain:chg>
      </domain:update>
    </update>
    <extension>
      <secDNS:update urgent="true" xmlns:secDNS="urn:ietf:params:xml:ns:secDNS-1.1">
        <secDNS:add>
          <secDNS:dsData>
            <secDNS:keyTag>12346</secDNS:keyTag>
            <secDNS:alg>3</secDNS:alg>
            <secDNS:digestType>1</secDNS:digestType>
            <secDNS:digest>38EC35D5B3A34B44C39B</secDNS:digest>
          </secDNS:dsData>
        </secDNS:add>
      </secDNS:update>
    </extension>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def updatedomaincommandwithrgpxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <update>
      <domain:update xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <domain:name>example.com</domain:name>
        <domain:add>
          <domain:ns>
            <domain:hostObj>ns2.example.com</domain:hostObj>
          </domain:ns>
          <domain:contact type="tech">mak21</domain:contact>
          <domain:status lang="en" s="clientHold">Payment overdue.</domain:status>
        </domain:add>
        <domain:rem>
          <domain:ns>
            <domain:hostObj>ns1.example.com</domain:hostObj>
          </domain:ns>
          <domain:contact type="tech">sh8013</domain:contact>
          <domain:status s="clientUpdateProhibited" />
        </domain:rem>
        <domain:chg>
          <domain:registrant>sh8013</domain:registrant>
          <domain:authInfo>
            <domain:pw>2BARfoo</domain:pw>
          </domain:authInfo>
        </domain:chg>
      </domain:update>
    </update>
    <extension>
      <rgp:update xmlns:rgp="urn:ietf:params:xml:ns:rgp-1.0">
        <rgp:restore op="report">
          <rgp:report>
            <rgp:preData>Pre-delete registration data goes here. Both XML and free text are allowed.</rgp:preData>
            <rgp:postData>Post-restore registration data goes here. Both XML and free text are allowed.</rgp:postData>
            <rgp:delTime>2003-07-10T22:00:00.0Z</rgp:delTime>
            <rgp:resTime>2003-07-20T22:00:00.0Z</rgp:resTime>
            <rgp:resReason>Registrant error.</rgp:resReason>
            <rgp:statement>This registrar has not restored the Registered Name in order to assume the rights to use or sell the Registered Name for itself or for any third party.</rgp:statement>
            <rgp:statement lang="en">The information in this report is true to best of this registrar knowledge, and this registrar acknowledges that intentionally supplying false information in this report shall constitute an incurable material breach of the Registry-Registrar Agreement.</rgp:statement>
            <rgp:other>Supporting information goes here.</rgp:other>
          </rgp:report>
        </rgp:restore>
      </rgp:update>
    </extension>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def updatedomaincommandwithlaunchxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <update>
      <domain:update xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <domain:name>example.com</domain:name>
        <domain:add>
          <domain:ns>
            <domain:hostObj>ns2.example.com</domain:hostObj>
          </domain:ns>
          <domain:contact type="tech">mak21</domain:contact>
          <domain:status lang="en" s="clientHold">Payment overdue.</domain:status>
        </domain:add>
        <domain:rem>
          <domain:ns>
            <domain:hostObj>ns1.example.com</domain:hostObj>
          </domain:ns>
          <domain:contact type="tech">sh8013</domain:contact>
          <domain:status s="clientUpdateProhibited" />
        </domain:rem>
        <domain:chg>
          <domain:registrant>sh8013</domain:registrant>
          <domain:authInfo>
            <domain:pw>2BARfoo</domain:pw>
          </domain:authInfo>
        </domain:chg>
      </domain:update>
    </update>
    <extension>
      <launch:update xmlns:launch="urn:ietf:params:xml:ns:launch-1.0">
        <launch:phase>sunrise</launch:phase>
        <launch:applicationID>abc123</launch:applicationID>
      </launch:update>
    </extension>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def updatedomaincommandwithbrdomainxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <update>
      <domain:update xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <domain:name>teste.com.br</domain:name>
      </domain:update>
    </update>
    <extension>
      <brdomain:update xmlns:brdomain="urn:ietf:params:xml:ns:brdomain-1.0">
        <brdomain:ticketNumber>ab-1234</brdomain:ticketNumber>
        <brdomain:chg>
          <brdomain:releaseProcessFlags flag1="1" />
          <brdomain:autoRenew active="1" />
          <brdomain:publicationStatus>onHold</brdomain:publicationStatus>
        </brdomain:chg>
      </brdomain:update>
    </extension>
  </command>
</epp>
"""


@pytest.fixture
def responseupdatedomaincommandxmlexpected():
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
def responseupdatedomaincommandwithbrdomainxmlexpected_case1():
    return """<epp xmlns='urn:ietf:params:xml:ns:epp-1.0'>
  <response>
    <result code='1000'>
      <msg>Command completed successfully</msg>
    </result>
    <extension>
      <brdomain:updData xmlns:brdomain='urn:ietf:params:xml:ns:brdomain-1.0'>
        <brdomain:ticketNumber>123456</brdomain:ticketNumber>
        <brdomain:pending>
          <brdomain:doc status='notReceived'>
            <brdomain:docType>CNPJ</brdomain:docType>
            <brdomain:limit>2006-03-01T22:00:00.0Z</brdomain:limit>
            <brdomain:description lang='pt'>Cadastro Nacional da Pessoa Juridica</brdomain:description>
          </brdomain:doc>
        </brdomain:pending>
      </brdomain:updData>
    </extension>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54321-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def responseupdatedomaincommandwithbrdomainxmlexpected_case2():
    return """<epp xmlns='urn:ietf:params:xml:ns:epp-1.0'>
  <response>
    <result code='2308'>
      <msg>Data management policy violation</msg>
      <extValue>
        <value xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
          <domain:hostName>ns2.example.com</domain:hostName>
        </value>
        <reason>Query refused</reason>
      </extValue>
    </result>
    <extension>
      <brdomain:updData xmlns:brdomain='urn:ietf:params:xml:ns:brdomain-1.0'>
        <brdomain:hostStatus>
          <brdomain:hostName>ns2.example.com</brdomain:hostName>
          <brdomain:dnsAnswer>Query refused</brdomain:dnsAnswer>
        </brdomain:hostStatus>
        <brdomain:publicationStatus publicationFlag="onHold">
          <brdomain:onHoldReason>billing</brdomain:onHoldReason>
          <brdomain:onHoldReason>dns</brdomain:onHoldReason>
        </brdomain:publicationStatus>
      </brdomain:updData>
    </extension>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54321-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""
