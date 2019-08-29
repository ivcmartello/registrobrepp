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
      <domain:check xmlns="urn:ietf:params:xml:ns:domain-1.0" xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <name>du.eti.br</name>
        <name>nic.br</name>
        <name>registro.br</name>
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
      <domain:check xmlns="urn:ietf:params:xml:ns:domain-1.0" xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <name>du.eti.br</name>
        <name>nic.br</name>
        <name>registro.br</name>
      </domain:check>
    </check>
    <extension>
      <launch:check type="claims" xmlns="urn:ietf:params:xml:ns:launch-1.0" xmlns:launch="urn:ietf:params:xml:ns:launch-1.0">
        <phase>claims</phase>
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
      <domain:check xmlns="urn:ietf:params:xml:ns:domain-1.0" xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <name>du.eti.br</name>
        <name>nic.br</name>
        <name>registro.br</name>
      </domain:check>
    </check>
    <extension>
      <brdomain:check xmlns="urn:ietf:params:xml:ns:brdomain-1.0" xmlns:brdomain="urn:ietf:params:xml:ns:brdomain-1.0">
        <organization>005.506.560/0001-36</organization>
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
      <domain:chkData xmlns="urn:ietf:params:xml:ns:domain-1.0" xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <cd>
          <name avail="1">example.com</name>
        </cd>
        <cd>
          <name avail="0">example.net</name>
          <reason>In use</reason>
        </cd>
        <cd>
          <name avail="1">example.org</name>
        </cd>
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
    return """<epp xmlns='urn:ietf:params:xml:ns:epp-1.0' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='urn:ietf:params:xml:ns:epp-1.0 epp-1.0.xsd'>
  <response>
    <result code='1000'>
      <msg>Command completed successfully</msg>
    </result>
    <resData>
      <domain:chkData xmlns:domain='urn:ietf:params:xml:ns:domain-1.0' xsi:schemaLocation='urn:ietf:params:xml:ns:domain-1.0 domain-1.0.xsd'>
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
      <brdomain:chkData xmlns:brdomain='urn:ietf:params:xml:ns:brdomain-1.0' xsi:schemaLocation='urn:ietf:params:xml:ns:brdomain-1.0 brdomain-1.0.xsd'>
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
      <domain:create xmlns="urn:ietf:params:xml:ns:domain-1.0" xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <name>example.com</name>
        <period unit="y">2</period>
        <ns>
          <hostObj>ns1.example.net</hostObj>
          <hostObj>ns2.example.net</hostObj>
        </ns>
        <registrant>jd1234</registrant>
        <contact type="admin">sh8013</contact>
        <contact type="tech">sh8013</contact>
        <contact type="billing">xxx</contact>
        <authInfo>
          <pw>2fooBAR</pw>
        </authInfo>
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
      <domain:create xmlns="urn:ietf:params:xml:ns:domain-1.0" xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <name>example.com</name>
        <period unit="y">2</period>
        <ns>
          <hostObj>ns1.example.net</hostObj>
          <hostObj>ns2.example.net</hostObj>
        </ns>
        <registrant>jd1234</registrant>
        <contact type="admin">sh8013</contact>
        <contact type="tech">sh8013</contact>
        <contact type="billing">xxx</contact>
        <authInfo>
          <pw>2fooBAR</pw>
        </authInfo>
      </domain:create>
    </create>
    <extension>
      <secDNS:create xmlns="urn:ietf:params:xml:ns:secDNS-1.1" xmlns:secDNS="urn:ietf:params:xml:ns:secDNS-1.1">
        <dsData>
          <keyTag>12345</keyTag>
          <alg>3</alg>
          <digestType>1</digestType>
          <digest>49FD46E6C4B45C55D4AC</digest>
        </dsData>
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
      <domain:create xmlns="urn:ietf:params:xml:ns:domain-1.0" xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <name>example.com</name>
        <period unit="y">2</period>
        <ns>
          <hostObj>ns1.example.net</hostObj>
          <hostObj>ns2.example.net</hostObj>
        </ns>
        <registrant>jd1234</registrant>
        <contact type="admin">sh8013</contact>
        <contact type="tech">sh8013</contact>
        <contact type="billing">xxx</contact>
        <authInfo>
          <pw>2fooBAR</pw>
        </authInfo>
      </domain:create>
    </create>
    <extension>
      <launch:create xmlns="urn:ietf:params:xml:ns:launch-1.0" xmlns:launch="urn:ietf:params:xml:ns:launch-1.0">
        <phase>sunrise</phase>
        <smd:encodedSignedMark xmlns="urn:ietf:params:xml:ns:signedMark-1.0" xmlns:smd="urn:ietf:params:xml:ns:signedMark-1.0">YkM1cFkyRnViaTV2Y21jdmRHMWphRjl3YVd4dmRDNWpjbXd3UlFZRFZSMGdCRDR3UERBNkJnTXFBd1F3TXpBeEJnZ3JCZ0VGQlFjQwpBUllsYUhSMGNEb3ZMM2QzZHk1cFkyRnViaTV2Y21jdmNHbHNiM1JmY21Wd2IzTnBkRzl5ZVRBTkJna3Foa2lHOXcwQkFRc0ZBQU9DCkFRRUFLVWZFSjVYNlFBdHRhampSVnNlSkZReFJYR0hUZ0NhRGs4Qy8xbmoxaWVsWkF1WnRnZFVwV0RVcjBObkdDaStMSFNzZ2RUWVIKK3ZNcnhpcjdFVllRZXZyQm9iRUxreGVURWZqRjlGVnFqQkhJbnlQRkxPRmt6MTV6R0cySXdQSnBzK3ZoQWQvN2dUMHBoMWsyRkVrSgpGR0w1THdSZjFtczRJWDB2RGt4VElYOFF4eTFqY3pDaVNzb1Y4cHdsaGgyTkhBa3BHUVdOL3BUUzBVcWk3dVU1Qm0vSW9HdlBCelVwCjVuNVNqVU1uVFp4LysxekF1ZXJTYWJ0NDgzc1hCY1dzamdsN01xRnRmT05pQXROZU1OZmg2MGxUTXU0emdWd0xaVE80VFFNNVEydXkKbFBQbVp0d25BODhRdk0ySUw4NWNJWUpIZDB6OWpwVVFNQkdIWEYyV1FBPT08L2RzOlg1MDlDZXJ0aWZpY2F0ZT48L2RzOlg1MDlEYXRhPjwvZHM6S2V5SW5mbz48L2RzOlNpZ25hdHVyZT48L3NtZDpzaWduZWRNYXJrPg==</smd:encodedSignedMark>
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
      <domain:create xmlns="urn:ietf:params:xml:ns:domain-1.0" xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <name>example.com</name>
        <period unit="y">2</period>
        <ns>
          <hostObj>ns1.example.net</hostObj>
          <hostObj>ns2.example.net</hostObj>
        </ns>
        <registrant>jd1234</registrant>
        <contact type="admin">sh8013</contact>
        <contact type="tech">sh8013</contact>
        <contact type="billing">xxx</contact>
        <authInfo>
          <pw>2fooBAR</pw>
        </authInfo>
      </domain:create>
    </create>
    <extension>
      <brdomain:create xmlns="urn:ietf:params:xml:ns:brdomain-1.0" xmlns:brdomain="urn:ietf:params:xml:ns:brdomain-1.0">
        <organization>005.506.560/0001-36</organization>
        <releaseProcessFlags flag1="1" />
        <autoRenew active="1" />
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
      <domain:creData xmlns="urn:ietf:params:xml:ns:domain-1.0" xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <name>example.com</name>
        <crDate>1999-04-03T22:00:00.0Z</crDate>
        <exDate>2001-04-03T22:00:00.0Z</exDate>
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
    return """<epp xmlns='urn:ietf:params:xml:ns:epp-1.0' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='urn:ietf:params:xml:ns:epp-1.0 epp-1.0.xsd'>
  <response>
    <result code='1001'>
      <msg>Command completed successfully; action pending</msg>
    </result>
    <resData>
      <domain:creData xmlns:domain='urn:ietf:params:xml:ns:domain-1.0' xsi:schemaLocation='urn:ietf:params:xml:ns:domain-1.0 domain-1.0.xsd'>
        <domain:name>example.com.br</domain:name>
        <domain:crDate>2006-01-30T22:00:00.0Z</domain:crDate>
      </domain:creData>
    </resData>
    <extension>
      <brdomain:creData xmlns:brdomain='urn:ietf:params:xml:ns:brdomain-1.0' xsi:schemaLocation='urn:ietf:params:xml:ns:brdomain-1.0 brdomain-1.0.xsd'>"
        <brdomain:ticketNumber>123456</brdomain:ticketNumber>
        <brdomain:pending>
          <brdomain:doc status='notReceived'>
            <brdomain:docType>CNPJ</brdomain:docType>
            <brdomain:limit>2006-03-01T22:00:00.0Z</brdomain:limit>
            <brdomain:description lang='pt'>Cadastro Nacional da Pessoa Juridica</brdomain:description>"
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
      <domain:delete xmlns="urn:ietf:params:xml:ns:domain-1.0" xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <name>example.com</name>
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
      <domain:delete xmlns="urn:ietf:params:xml:ns:domain-1.0" xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <name>example.com</name>
      </domain:delete>
    </delete>
    <extension>
      <launch:delete xmlns="urn:ietf:params:xml:ns:launch-1.0" xmlns:launch="urn:ietf:params:xml:ns:launch-1.0">
        <phase>sunrise</phase>
        <applicationID>abc123</applicationID>
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
      <domain:renew xmlns="urn:ietf:params:xml:ns:domain-1.0" xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <name>example.com.br</name>
        <curExpDate>2000-04-03</curExpDate>
        <period unit="y">5</period>
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
      <domain:renData xmlns="urn:ietf:params:xml:ns:domain-1.0" xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <name>example.com</name>
        <exDate>2005-04-03T22:00:00.0Z</exDate>
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
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="urn:ietf:params:xml:ns:epp-1.0 epp-1.0.xsd">
  <response>
    <result code="1000">
      <msg>Command completed successfully</msg>
    </result>
    <resData>
      <domain:renData xmlns:domain="urn:ietf:params:xml:ns:domain-1.0" xsi:schemaLocation="urn:ietf:params:xml:ns:domain-1.0 domain-1.0.xsd">
        <domain:name>example.com.br</domain:name>
        <domain:exDate>2007-04-03T00:00:00.0Z</domain:exDate>
      </domain:renData>
    </resData>
    <extension>
      <brdomain:renData xmlns:brdomain="urn:ietf:params:xml:ns:brdomain-1.0" xsi:schemaLocation="urn:ietf:params:xml:ns:brdomain-1.0 brdomain-1.0.xsd">
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
      <domain:info xmlns="urn:ietf:params:xml:ns:domain-1.0" xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <name hosts="all">example.com</name>
        <authInfo>
          <pw>2fooBAR</pw>
        </authInfo>
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
      <domain:info xmlns="urn:ietf:params:xml:ns:domain-1.0" xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <name hosts="all">example.com</name>
        <authInfo>
          <pw>2fooBAR</pw>
        </authInfo>
      </domain:info>
    </info>
    <extension>
      <launch:info includeMark="true" xmlns="urn:ietf:params:xml:ns:launch-1.0" xmlns:launch="urn:ietf:params:xml:ns:launch-1.0">
        <phase>claims</phase>
        <applicationID>abc123</applicationID>
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
      <domain:info xmlns="urn:ietf:params:xml:ns:domain-1.0" xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <name hosts="all">example.com</name>
        <authInfo>
          <pw>2fooBAR</pw>
        </authInfo>
      </domain:info>
    </info>
    <extension>
      <brdomain:info xmlns="urn:ietf:params:xml:ns:brdomain-1.0" xmlns:brdomain="urn:ietf:params:xml:ns:brdomain-1.0">
        <ticketNumber>123456</ticketNumber>
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
      <domain:infData xmlns="urn:ietf:params:xml:ns:domain-1.0" xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <name>example.com</name>
        <roid>EXAMPLE1-REP</roid>
        <status s="ok" />
        <registrant>jd1234</registrant>
        <contact type="admin">sh8013</contact>
        <contact type="tech">sh8013</contact>
        <ns>
          <hostObj>ns1.example.com</hostObj>
          <hostObj>ns1.example.net</hostObj>
        </ns>
        <host>ns1.example.com</host>
        <host>ns2.example.com</host>
        <clID>ClientX</clID>
        <crID>ClientY</crID>
        <crDate>1999-04-03T22:00:00.0Z</crDate>
        <upID>ClientX</upID>
        <upDate>1999-12-03T09:00:00.0Z</upDate>
        <exDate>2005-04-03T22:00:00.0Z</exDate>
        <trDate>2000-04-08T09:00:00.0Z</trDate>
        <authInfo>
          <pw>2fooBAR</pw>
        </authInfo>
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
      <domain:infData xmlns="urn:ietf:params:xml:ns:domain-1.0" xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <name>example.com</name>
        <roid>EXAMPLE1-REP</roid>
        <clID>ClientX</clID>
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
    return """<epp xmlns='urn:ietf:params:xml:ns:epp-1.0' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='urn:ietf:params:xml:ns:epp-1.0 epp-1.0.xsd'>
  <response>
    <result code='1000'>
      <msg>Command completed successfully</msg>
    </result>
    <resData>
      <domain:infData xmlns:domain='urn:ietf:params:xml:ns:domain-1.0' xsi:schemaLocation='urn:ietf:params:xml:ns:domain-1.0 domain-1.0.xsd'>
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
      <brdomain:infData xmlns:brdomain='urn:ietf:params:xml:ns:brdomain-1.0' xsi:schemaLocation='urn:ietf:params:xml:ns:brdomain-1.0 brdomain-1.0.xsd'>
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
      <domain:transfer xmlns="urn:ietf:params:xml:ns:domain-1.0" xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <name>example.com</name>
        <authInfo>
          <pw roid="JD1234-REP">2fooBAR</pw>
        </authInfo>
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
      <domain:transfer xmlns="urn:ietf:params:xml:ns:domain-1.0" xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <name>example.com</name>
        <period unit="y">1</period>
        <authInfo>
          <pw roid="JD1234-REP">2fooBAR</pw>
        </authInfo>
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
      <domain:trnData xmlns="urn:ietf:params:xml:ns:domain-1.0" xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <name>example.com</name>
        <trStatus>pending</trStatus>
        <reID>ClientX</reID>
        <reDate>2000-06-06T22:00:00.0Z</reDate>
        <acID>ClientY</acID>
        <acDate>2000-06-11T22:00:00.0Z</acDate>
        <exDate>2002-09-08T22:00:00.0Z</exDate>
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
      <domain:trnData xmlns="urn:ietf:params:xml:ns:domain-1.0" xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <name>example.com</name>
        <trStatus>pending</trStatus>
        <reID>ClientX</reID>
        <reDate>2000-06-08T22:00:00.0Z</reDate>
        <acID>ClientY</acID>
        <acDate>2000-06-13T22:00:00.0Z</acDate>
        <exDate>2002-09-08T22:00:00.0Z</exDate>
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
      <domain:update xmlns="urn:ietf:params:xml:ns:domain-1.0" xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <name>example.com</name>
        <add>
          <ns>
            <hostObj>ns2.example.com</hostObj>
          </ns>
          <contact type="tech">mak21</contact>
          <status lang="en" s="clientHold">Payment overdue.</status>
        </add>
        <rem>
          <ns>
            <hostObj>ns1.example.com</hostObj>
          </ns>
          <contact type="tech">sh8013</contact>
          <status s="clientUpdateProhibited" />
        </rem>
        <chg>
          <registrant>sh8013</registrant>
          <authInfo>
            <pw>2BARfoo</pw>
          </authInfo>
        </chg>
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
      <domain:update xmlns="urn:ietf:params:xml:ns:domain-1.0" xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <name>example.com</name>
        <add>
          <ns>
            <hostObj>ns2.example.com</hostObj>
          </ns>
          <contact type="tech">mak21</contact>
          <status lang="en" s="clientHold">Payment overdue.</status>
        </add>
        <rem>
          <ns>
            <hostObj>ns1.example.com</hostObj>
          </ns>
          <contact type="tech">sh8013</contact>
          <status s="clientUpdateProhibited" />
        </rem>
        <chg>
          <registrant>sh8013</registrant>
          <authInfo>
            <pw>2BARfoo</pw>
          </authInfo>
        </chg>
      </domain:update>
    </update>
    <extension>
      <secDNS:update urgent="true" xmlns="urn:ietf:params:xml:ns:secDNS-1.1" xmlns:secDNS="urn:ietf:params:xml:ns:secDNS-1.1">
        <add>
          <dsData>
            <keyTag>12346</keyTag>
            <alg>3</alg>
            <digestType>1</digestType>
            <digest>38EC35D5B3A34B44C39B</digest>
          </dsData>
        </add>
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
      <domain:update xmlns="urn:ietf:params:xml:ns:domain-1.0" xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <name>example.com</name>
        <add>
          <ns>
            <hostObj>ns2.example.com</hostObj>
          </ns>
          <contact type="tech">mak21</contact>
          <status lang="en" s="clientHold">Payment overdue.</status>
        </add>
        <rem>
          <ns>
            <hostObj>ns1.example.com</hostObj>
          </ns>
          <contact type="tech">sh8013</contact>
          <status s="clientUpdateProhibited" />
        </rem>
        <chg>
          <registrant>sh8013</registrant>
          <authInfo>
            <pw>2BARfoo</pw>
          </authInfo>
        </chg>
      </domain:update>
    </update>
    <extension>
      <rgp:update xmlns="urn:ietf:params:xml:ns:rgp-1.0" xmlns:rgp="urn:ietf:params:xml:ns:rgp-1.0">
        <restore op="report">
          <report>
            <preData>Pre-delete registration data goes here. Both XML and free text are allowed.</preData>
            <postData>Post-restore registration data goes here. Both XML and free text are allowed.</postData>
            <delTime>2003-07-10T22:00:00.0Z</delTime>
            <resTime>2003-07-20T22:00:00.0Z</resTime>
            <resReason>Registrant error.</resReason>
            <statement>This registrar has not restored the Registered Name in order to assume the rights to use or sell the Registered Name for itself or for any third party.</statement>
            <statement lang="en">The information in this report is true to best of this registrar knowledge, and this registrar acknowledges that intentionally supplying false information in this report shall constitute an incurable material breach of the Registry-Registrar Agreement.</statement>
            <other>Supporting information goes here.</other>
          </report>
        </restore>
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
      <domain:update xmlns="urn:ietf:params:xml:ns:domain-1.0" xmlns:domain="urn:ietf:params:xml:ns:domain-1.0">
        <name>example.com</name>
        <add>
          <ns>
            <hostObj>ns2.example.com</hostObj>
          </ns>
          <contact type="tech">mak21</contact>
          <status lang="en" s="clientHold">Payment overdue.</status>
        </add>
        <rem>
          <ns>
            <hostObj>ns1.example.com</hostObj>
          </ns>
          <contact type="tech">sh8013</contact>
          <status s="clientUpdateProhibited" />
        </rem>
        <chg>
          <registrant>sh8013</registrant>
          <authInfo>
            <pw>2BARfoo</pw>
          </authInfo>
        </chg>
      </domain:update>
    </update>
    <extension>
      <launch: update xmlns="urn:ietf:params:xml:ns:launch-1.0" xmlns:launch="urn:ietf:params:xml:ns:launch-1.0">
        <phase>sunrise</phase>
        <applicationID>abc123</applicationID>
      </launch: update>
    </extension>
    <clTRID>ABC-12345</clTRID>
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
    return """<epp xmlns='urn:ietf:params:xml:ns:epp-1.0' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='urn:ietf:params:xml:ns:epp-1.0 epp-1.0.xsd'>
  <response>
    <result code='1000'>
      <msg>Command completed successfully</msg>
    </result>
    <extension>
      <brdomain:updData xmlns:brdomain='urn:ietf:params:xml:ns:brdomain-1.0' xsi:schemaLocation='urn:ietf:params:xml:ns:brdomain-1.0 brdomain-1.0.xsd'>
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
    return """<epp xmlns='urn:ietf:params:xml:ns:epp-1.0' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='urn:ietf:params:xml:ns:epp-1.0 epp-1.0.xsd'>
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
      <brdomain:updData xmlns:brdomain='urn:ietf:params:xml:ns:brdomain-1.0' xsi:schemaLocation='urn:ietf:params:xml:ns:brdomain-1.0 brdomain-1.0.xsd'>
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
