#-*- coding: UTF-8 -*-

import pytest
from decouple import config


@pytest.fixture
def contactxmlschema():
    from lxml import etree

    schema = config('EPPSCHEMAPATH', '../../../schemas') + '/contact-1.0.xsd'
    xmlschema_doc = etree.parse(schema)
    return etree.XMLSchema(xmlschema_doc)


@pytest.fixture
def brorgxmlschema():
    from lxml import etree

    schema = config('EPPSCHEMAPATH', '../../../schemas') + '/brorg-1.0.xsd'
    xmlschema_doc = etree.parse(schema)
    return etree.XMLSchema(xmlschema_doc)


@pytest.fixture
def lacnicorgxmlschema():
    from lxml import etree

    schema = config('EPPSCHEMAPATH', '../../../schemas') + '/lacnicorg-1.0.xsd'
    xmlschema_doc = etree.parse(schema)
    return etree.XMLSchema(xmlschema_doc)


@pytest.fixture
def checkcontactcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <check>
      <contact:check xmlns:contact="urn:ietf:params:xml:ns:contact-1.0">
        <contact:id>ab-12345</contact:id>
        <contact:id>aa-11111</contact:id>
      </contact:check>
    </check>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def checkcontactcommandwithbrorgxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <check>
      <contact:check xmlns:contact="urn:ietf:params:xml:ns:contact-1.0">
        <contact:id>ab-12345</contact:id>
        <contact:id>aa-11111</contact:id>
      </contact:check>
    </check>
    <extension>
      <brorg:check xmlns:brorg="urn:ietf:params:xml:ns:brorg-1.0">
        <brorg:cd>
          <brorg:id>e123456</brorg:id>
          <brorg:organization>043.828.151/0001-45</brorg:organization>
        </brorg:cd>
        <brorg:cd>
          <brorg:id>e654321</brorg:id>
          <brorg:organization>005.506.560/0001-36</brorg:organization>
        </brorg:cd>
      </brorg:check>
    </extension>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def responsecheckcontactcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <response>
    <result code="1000">
      <msg>Command completed successfully</msg>
    </result>
    <resData>
      <contact:chkData xmlns:contact="urn:ietf:params:xml:ns:contact-1.0">
        <contact:cd>
          <contact:id avail="1">sh8013</contact:id>
        </contact:cd>
        <contact:cd>
          <contact:id avail="0">sah8013</contact:id>
          <contact:reason>In use</contact:reason>
        </contact:cd>
        <contact:cd>
          <contact:id avail="1">8013sah</contact:id>
        </contact:cd>
      </contact:chkData>
    </resData>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54322-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def responsecheckcontactcommandwithbrorgxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">  
  <response>
    <result code="1000">
      <msg>Command completed successfully</msg>
    </result>
    <resData>
      <contact:chkData xmlns:contact="urn:ietf:params:xml:ns:contact-1.0"> 
        <contact:cd>
          <contact:id avail="0">004138888000184</contact:id>
          <contact:reason>In use</contact:reason>
        </contact:cd>
        <contact:cd>
          <contact:id avail="0">006994175000148</contact:id>
          <contact:reason>Temporary organization in use</contact:reason>
        </contact:cd>
        <contact:cd>
          <contact:id avail="0">067774281000100</contact:id>
          <contact:reason>Temporary organization in use</contact:reason>
        </contact:cd>
      </contact:chkData>
    </resData>
    <extension>
      <brorg:chkData xmlns:brorg="urn:ietf:params:xml:ns:brorg-1.0"> 
        <brorg:ticketInfo>
          <brorg:organization>006.994.175/0001-48</brorg:organization>
          <brorg:ticketNumber>2822407</brorg:ticketNumber>
          <brorg:domainName>doremisolfalasi.com.br</brorg:domainName>
        </brorg:ticketInfo>
        <brorg:ticketInfo>
          <brorg:organization>067.774.281/0001-00</brorg:organization>
          <brorg:ticketNumber>2822403</brorg:ticketNumber>
          <brorg:domainName>edpgviva.com.br</brorg:domainName>
        </brorg:ticketInfo>
      </brorg:chkData>
    </extension>
    <trID>
      <clTRID>424238335</clTRID>
      <svTRID>20060822152406-015-0011</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def createcontactcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <create>
      <contact:create xmlns:contact="urn:ietf:params:xml:ns:contact-1.0">
        <contact:id>ab-12345</contact:id>
        <contact:postalInfo type="loc">
          <contact:name>Joe Doe</contact:name>
          <contact:org>Example Inc.</contact:org>
          <contact:addr>
            <contact:street>123 Example Dr.</contact:street>
            <contact:street>Suite 100</contact:street>
            <contact:street>xyz</contact:street>
            <contact:city>Dulles</contact:city>
            <contact:sp>VA</contact:sp>
            <contact:pc>20166-6503</contact:pc>
            <contact:cc>US</contact:cc>
          </contact:addr>
        </contact:postalInfo>
        <contact:postalInfo type="int">
          <contact:name>Anna Doe</contact:name>
          <contact:org>Example Inc.</contact:org>
          <contact:addr>
            <contact:street>123 Example Dr.</contact:street>
            <contact:street>Suite 100</contact:street>
            <contact:street>xyz</contact:street>
            <contact:city>Dulles</contact:city>
            <contact:sp>VA</contact:sp>
            <contact:pc>20166-6503</contact:pc>
            <contact:cc>US</contact:cc>
          </contact:addr>
        </contact:postalInfo>
        <contact:voice x="1234">+1.7035555555</contact:voice>
        <contact:email>jdoe@example.com</contact:email>
        <contact:authInfo>
          <contact:pw>123</contact:pw>
        </contact:authInfo>
        <contact:disclose flag="1">
          <contact:name type="loc" />
          <contact:org type="loc" />
          <contact:addr type="loc" />
          <contact:voice />
          <contact:fax />
          <contact:email />
        </contact:disclose>
      </contact:create>
    </create>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def createcontactcommandwithlacnicxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <create>
      <contact:create xmlns:contact="urn:ietf:params:xml:ns:contact-1.0">
        <contact:id>ab-12345</contact:id>
        <contact:postalInfo type="loc">
          <contact:name>Joe Doe</contact:name>
          <contact:org>Example Inc.</contact:org>
          <contact:addr>
            <contact:street>123 Example Dr.</contact:street>
            <contact:street>Suite 100</contact:street>
            <contact:street>xyz</contact:street>
            <contact:city>Dulles</contact:city>
            <contact:sp>VA</contact:sp>
            <contact:pc>20166-6503</contact:pc>
            <contact:cc>US</contact:cc>
          </contact:addr>
        </contact:postalInfo>
        <contact:postalInfo type="int">
          <contact:name>Anna Doe</contact:name>
          <contact:org>Example Inc.</contact:org>
          <contact:addr>
            <contact:street>123 Example Dr.</contact:street>
            <contact:street>Suite 100</contact:street>
            <contact:street>xyz</contact:street>
            <contact:city>Dulles</contact:city>
            <contact:sp>VA</contact:sp>
            <contact:pc>20166-6503</contact:pc>
            <contact:cc>US</contact:cc>
          </contact:addr>
        </contact:postalInfo>
        <contact:voice x="1234">+1.7035555555</contact:voice>
        <contact:email>jdoe@example.com</contact:email>
        <contact:authInfo>
          <contact:pw>123</contact:pw>
        </contact:authInfo>
        <contact:disclose flag="1">
          <contact:name type="loc" />
          <contact:org type="loc" />
          <contact:addr type="loc" />
          <contact:voice />
          <contact:fax />
          <contact:email />
        </contact:disclose>
      </contact:create>
    </create>
    <extension>
      <lacniccontact:create xmlns:lacniccontact="urn:ietf:params:xml:ns:lacniccontact-1.0">
        <lacniccontact:password>abc123</lacniccontact:password>
        <lacniccontact:reminder>Default</lacniccontact:reminder>
        <lacniccontact:language>pt</lacniccontact:language>
      </lacniccontact:create>
    </extension>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def createcontactcommandwithbrorglacnicorgxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <create>
      <contact:create xmlns:contact="urn:ietf:params:xml:ns:contact-1.0">
        <contact:id>ab-12345</contact:id>
        <contact:postalInfo type="loc">
          <contact:name>Joe Doe</contact:name>
          <contact:org>Example Inc.</contact:org>
          <contact:addr>
            <contact:street>123 Example Dr.</contact:street>
            <contact:street>Suite 100</contact:street>
            <contact:street>xyz</contact:street>
            <contact:city>Dulles</contact:city>
            <contact:sp>VA</contact:sp>
            <contact:pc>20166-6503</contact:pc>
            <contact:cc>US</contact:cc>
          </contact:addr>
        </contact:postalInfo>
        <contact:postalInfo type="int">
          <contact:name>Anna Doe</contact:name>
          <contact:org>Example Inc.</contact:org>
          <contact:addr>
            <contact:street>123 Example Dr.</contact:street>
            <contact:street>Suite 100</contact:street>
            <contact:street>xyz</contact:street>
            <contact:city>Dulles</contact:city>
            <contact:sp>VA</contact:sp>
            <contact:pc>20166-6503</contact:pc>
            <contact:cc>US</contact:cc>
          </contact:addr>
        </contact:postalInfo>
        <contact:voice x="1234">+1.7035555555</contact:voice>
        <contact:email>jdoe@example.com</contact:email>
        <contact:authInfo>
          <contact:pw>123</contact:pw>
        </contact:authInfo>
        <contact:disclose flag="1">
          <contact:name type="loc" />
          <contact:org type="loc" />
          <contact:addr type="loc" />
          <contact:voice />
          <contact:fax />
          <contact:email />
        </contact:disclose>
      </contact:create>
    </create>
    <extension>
      <brorg:create xmlns:brorg="urn:ietf:params:xml:ns:brorg-1.0">
        <brorg:organization>005.506.560/0001-36</brorg:organization>
        <brorg:contact type="admin">fan</brorg:contact>
        <brorg:contact type="billing">fun</brorg:contact>
        <brorg:contact type="member">fuc</brorg:contact>
        <brorg:responsible>John Doe</brorg:responsible>
      </brorg:create>
      <lacnicorg:create xmlns:lacnicorg="urn:ietf:params:xml:ns:lacnicorg-1.0">
        <lacnicorg:type>normal</lacnicorg:type>
        <lacnicorg:eppPassword>abc123</lacnicorg:eppPassword>
        <lacnicorg:eppIP>192.168.0.1</lacnicorg:eppIP>
        <lacnicorg:eppIP>192.0.2.0/24</lacnicorg:eppIP>
        <lacnicorg:eppIP>203.0.113.0/24</lacnicorg:eppIP>
        <lacnicorg:renewalType>member</lacnicorg:renewalType>
        <lacnicorg:renewalType>small</lacnicorg:renewalType>
        <lacnicorg:renewalType>founding-partner</lacnicorg:renewalType>
        <lacnicorg:resourcesClass>all-resources</lacnicorg:resourcesClass>
      </lacnicorg:create>
    </extension>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def responsecreatecontactcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <response>
    <result code="1000">
      <msg>Command completed successfully</msg>
    </result>
    <resData>
      <contact:creData xmlns:contact="urn:ietf:params:xml:ns:contact-1.0">
        <contact:id>sh8013</contact:id>
        <contact:crDate>1999-04-03T22:00:00.0Z</contact:crDate>
      </contact:creData>
    </resData>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54321-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def responsecreatecontactcommandwithbrorgxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <response>
    <result code="1000">
      <msg>Command completed successfully</msg>
    </result>
    <resData>
      <contact:creData xmlns:contact="urn:ietf:params:xml:ns:contact-1.0">
        <contact:id>cem456</contact:id>
        <contact:crDate>2006-01-30T22:00:00.0Z</contact:crDate>
      </contact:creData>
    </resData>
    <extension>
    <brorg:creData xmlns:brorg="urn:ietf:params:xml:ns:brorg-1.0">
      <brorg:organization>005.506.560/0001-36</brorg:organization>
    </brorg:creData>
    </extension>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>DEF-54321</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def deletecontactcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <delete>
      <contact:delete xmlns:contact="urn:ietf:params:xml:ns:contact-1.0">
        <contact:id>ab-12345</contact:id>
      </contact:delete>
    </delete>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def deletecontactcommandwithbrorgxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <delete>
      <contact:delete xmlns:contact="urn:ietf:params:xml:ns:contact-1.0">
        <contact:id>ab-12345</contact:id>
      </contact:delete>
    </delete>
    <extension>
      <brorg:delete xmlns:brorg="urn:ietf:params:xml:ns:brorg-1.0">
        <brorg:organization>005.506.560/0001-36</brorg:organization>
      </brorg:delete>
    </extension>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def responsedeletecontactcommandxmlexpected():
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
def infocontactcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <info>
      <contact:info xmlns:contact="urn:ietf:params:xml:ns:contact-1.0">
        <contact:id>ab-12345</contact:id>
        <contact:authInfo>
          <contact:pw>123</contact:pw>
        </contact:authInfo>
      </contact:info>
    </info>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def infocontactcommandwithbrorgxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <info>
      <contact:info xmlns:contact="urn:ietf:params:xml:ns:contact-1.0">
        <contact:id>ab-12345</contact:id>
        <contact:authInfo>
          <contact:pw>123</contact:pw>
        </contact:authInfo>
      </contact:info>
    </info>
    <extension>
      <brorg:info xmlns:brorg="urn:ietf:params:xml:ns:brorg-1.0">
        <brorg:organization>005.506.560/0001-36</brorg:organization>
      </brorg:info>
    </extension>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def responseinfocontactcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <response>
    <result code="1000">
      <msg>Command completed successfully</msg>
    </result>
    <resData>
      <contact:infData xmlns:contact="urn:ietf:params:xml:ns:contact-1.0">
        <contact:id>sh8013</contact:id>
        <contact:roid>SH8013-REP</contact:roid>
        <contact:status s="linked" />
        <contact:status s="clientDeleteProhibited" />
        <contact:postalInfo type="int">
          <contact:name>John Doe</contact:name>
          <contact:org>Example Inc.</contact:org>
          <contact:addr>
            <contact:street>123 Example Dr.</contact:street>
            <contact:street>Suite 100</contact:street>
            <contact:city>Dulles</contact:city>
            <contact:sp>VA</contact:sp>
            <contact:pc>20166-6503</contact:pc>
            <contact:cc>US</contact:cc>
          </contact:addr>
        </contact:postalInfo>
        <contact:voice x="1234">+1.7035555555</contact:voice>
        <contact:fax>+1.7035555556</contact:fax>
        <contact:email>jdoe@example.com</contact:email>
        <contact:clID>ClientY</contact:clID>
        <contact:crID>ClientX</contact:crID>
        <contact:crDate>1999-04-03T22:00:00.0Z</contact:crDate>
        <contact:upID>ClientX</contact:upID>
        <contact:upDate>1999-12-03T09:00:00.0Z</contact:upDate>
        <contact:trDate>2000-04-08T09:00:00.0Z</contact:trDate>
        <contact:authInfo>
          <contact:pw>2fooBAR</contact:pw>
        </contact:authInfo>
        <contact:disclose flag="0">
          <contact:voice />
          <contact:email />
        </contact:disclose>
      </contact:infData>
    </resData>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54322-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def responseinfocontactcommandwithbrorgxmlexpected():
    return """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <response>
    <result code="1000">
      <msg>Command completed successfully</msg>
    </result>
    <resData>
      <contact:infData xmlns:contact="urn:ietf:params:xml:ns:contact-1.0">
        <contact:id>e654321</contact:id>
        <contact:roid>e654321-REP</contact:roid>
        <contact:status s="ok" />
        <contact:postalInfo type="int">
          <contact:name>John Doe</contact:name>
          <contact:org>Example Inc.</contact:org>
          <contact:addr>
            <contact:street>Av. Nações Unidas, 11541</contact:street>
            <contact:street>7º andar</contact:street>
            <contact:city>São Paulo</contact:city>
            <contact:sp>SP</contact:sp>
            <contact:pc>04578-000</contact:pc>
            <contact:cc>BR</contact:cc>
          </contact:addr>
        </contact:postalInfo>
        <contact:voice x="1234">+55.1155093500</contact:voice>
        <contact:fax>+55.1155093501</contact:fax>
        <contact:email>jdoe@example.com.br</contact:email>
        <contact:clID>ClientY</contact:clID>
        <contact:crID>ClientX</contact:crID>
        <contact:crDate>2005-12-05T12:00:00.0Z</contact:crDate>
        <contact:upID>ClientX</contact:upID>
        <contact:upDate>2005-12-05T12:00:00.0Z</contact:upDate>
        <contact:disclose flag="0">
          <contact:voice />
          <contact:email />
        </contact:disclose>
      </contact:infData>
    </resData>
    <extension>
      <brorg:infData xmlns:brorg="urn:ietf:params:xml:ns:brorg-1.0">
        <brorg:organization>005.506.560/0001-36</brorg:organization>
        <brorg:contact type="admin">fan</brorg:contact>
        <brorg:responsible>João Cláudio da Silva</brorg:responsible>
        <brorg:proxy>EDS279</brorg:proxy>
        <brorg:exDate>2006-06-06T06:00:00.0Z</brorg:exDate>
        <brorg:domainName>nic.br</brorg:domainName>
        <brorg:domainName>ptt.br</brorg:domainName>
        <brorg:domainName>registro.br</brorg:domainName>
        <brorg:asNumber>64500</brorg:asNumber>
        <brorg:ipRange version="v4">
          <brorg:startAddress>192.168.0.0</brorg:startAddress>
          <brorg:endAddress>192.168.0.255</brorg:endAddress>
        </brorg:ipRange>
        <brorg:suspended>true</brorg:suspended>
      </brorg:infData>
      <lacnicorg:infData xmlns:lacnicorg="urn:ietf:params:xml:ns:lacnicorg-1.0">
        <lacnicorg:type>nir</lacnicorg:type>
        <lacnicorg:eppStatus>active</lacnicorg:eppStatus>
        <lacnicorg:eppIP>192.168.0.1</lacnicorg:eppIP>
        <lacnicorg:eppIP>192.0.2.0/24</lacnicorg:eppIP>
        <lacnicorg:renewalType>member</lacnicorg:renewalType>
        <lacnicorg:renewalType>small</lacnicorg:renewalType>
        <lacnicorg:renewalType>founding-partner</lacnicorg:renewalType>
        <lacnicorg:renewalDate>2015-06-01T12:00:00.0Z</lacnicorg:renewalDate>
        <lacnicorg:resourcesClass>non-legacy-only</lacnicorg:resourcesClass>
        <lacnicorg:password>abc123</lacnicorg:password>
        <lacnicorg:legacy>true</lacnicorg:legacy>
      </lacnicorg:infData>
    </extension>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54322-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def transferquerycontactcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <transfer op="query">
      <contact:transfer xmlns:contact="urn:ietf:params:xml:ns:contact-1.0">
        <contact:id>ab-12345</contact:id>
        <contact:authInfo>
          <contact:pw>123</contact:pw>
        </contact:authInfo>
      </contact:transfer>
    </transfer>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def responsetransferquerycontactcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <response>
    <result code="1000">
      <msg>Command completed successfully</msg>
    </result>
    <resData>
      <contact:trnData xmlns:contact="urn:ietf:params:xml:ns:contact-1.0">
        <contact:id>sh8013</contact:id>
        <contact:trStatus>pending</contact:trStatus>
        <contact:reID>ClientX</contact:reID>
        <contact:reDate>2000-06-06T22:00:00.0Z</contact:reDate>
        <contact:acID>ClientY</contact:acID>
        <contact:acDate>2000-06-11T22:00:00.0Z</contact:acDate>
      </contact:trnData>
    </resData>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54322-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def transferrequestcontactcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <transfer op="request">
      <contact:transfer xmlns:contact="urn:ietf:params:xml:ns:contact-1.0">
        <contact:id>ab-12345</contact:id>
        <contact:authInfo>
          <contact:pw>123</contact:pw>
        </contact:authInfo>
      </contact:transfer>
    </transfer>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def responsetransferrequestcontactcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <response>
    <result code="1001">
      <msg>Command completed successfully; action pending</msg>
    </result>
    <resData>
      <contact:trnData xmlns:contact="urn:ietf:params:xml:ns:contact-1.0">
        <contact:id>sh8013</contact:id>
        <contact:trStatus>pending</contact:trStatus>
        <contact:reID>ClientX</contact:reID>
        <contact:reDate>2000-06-08T22:00:00.0Z</contact:reDate>
        <contact:acID>ClientY</contact:acID>
        <contact:acDate>2000-06-13T22:00:00.0Z</contact:acDate>
      </contact:trnData>
    </resData>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54322-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def updatecontactcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <update>
      <contact:update xmlns:contact="urn:ietf:params:xml:ns:contact-1.0">
        <contact:id>ab-12345</contact:id>
        <contact:add>
          <contact:status s="clientDeleteProhibited" />
        </contact:add>
        <contact:rem>
          <contact:status s="clientDeleteProhibited" />
        </contact:rem>
        <contact:chg>
          <contact:postalInfo type="loc">
            <contact:name>Joe Doe</contact:name>
            <contact:org>Example Inc.</contact:org>
            <contact:addr>
              <contact:street>123 Example Dr.</contact:street>
              <contact:street>Suite 100</contact:street>
              <contact:street>xyz</contact:street>
              <contact:city>Dulles</contact:city>
              <contact:sp>VA</contact:sp>
              <contact:pc>20166-6503</contact:pc>
              <contact:cc>US</contact:cc>
            </contact:addr>
          </contact:postalInfo>
          <contact:postalInfo type="int">
            <contact:name>Anna Doe</contact:name>
            <contact:org>Example Inc.</contact:org>
            <contact:addr>
              <contact:street>123 Example Dr.</contact:street>
              <contact:street>Suite 100</contact:street>
              <contact:street>xyz</contact:street>
              <contact:city>Dulles</contact:city>
              <contact:sp>VA</contact:sp>
              <contact:pc>20166-6503</contact:pc>
              <contact:cc>US</contact:cc>
            </contact:addr>
          </contact:postalInfo>
          <contact:voice x="1234">+1.7035555555</contact:voice>
          <contact:email>jdoe@example.com</contact:email>
          <contact:authInfo>
            <contact:pw>123</contact:pw>
          </contact:authInfo>
          <contact:disclose flag="1">
            <contact:name type="int" />
            <contact:org type="int" />
            <contact:addr type="int" />
            <contact:voice />
            <contact:fax />
            <contact:email />
          </contact:disclose>
        </contact:chg>
      </contact:update>
    </update>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def updatecontactcommandwithlacnicxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <update>
      <contact:update xmlns:contact="urn:ietf:params:xml:ns:contact-1.0">
        <contact:id>ab-12345</contact:id>
        <contact:add>
          <contact:status s="clientDeleteProhibited" />
        </contact:add>
        <contact:rem>
          <contact:status s="clientDeleteProhibited" />
        </contact:rem>
        <contact:chg>
          <contact:postalInfo type="loc">
            <contact:name>Joe Doe</contact:name>
            <contact:org>Example Inc.</contact:org>
            <contact:addr>
              <contact:street>123 Example Dr.</contact:street>
              <contact:street>Suite 100</contact:street>
              <contact:street>xyz</contact:street>
              <contact:city>Dulles</contact:city>
              <contact:sp>VA</contact:sp>
              <contact:pc>20166-6503</contact:pc>
              <contact:cc>US</contact:cc>
            </contact:addr>
          </contact:postalInfo>
          <contact:postalInfo type="int">
            <contact:name>Anna Doe</contact:name>
            <contact:org>Example Inc.</contact:org>
            <contact:addr>
              <contact:street>123 Example Dr.</contact:street>
              <contact:street>Suite 100</contact:street>
              <contact:street>xyz</contact:street>
              <contact:city>Dulles</contact:city>
              <contact:sp>VA</contact:sp>
              <contact:pc>20166-6503</contact:pc>
              <contact:cc>US</contact:cc>
            </contact:addr>
          </contact:postalInfo>
          <contact:voice x="1234">+1.7035555555</contact:voice>
          <contact:email>jdoe@example.com</contact:email>
          <contact:authInfo>
            <contact:pw>123</contact:pw>
          </contact:authInfo>
          <contact:disclose flag="1">
            <contact:name type="int" />
            <contact:org type="int" />
            <contact:addr type="int" />
            <contact:voice />
            <contact:fax />
            <contact:email />
          </contact:disclose>
        </contact:chg>
      </contact:update>
    </update>
    <extension>
      <lacniccontact:update xmlns:lacniccontact="urn:ietf:params:xml:ns:lacniccontact-1.0">
        <lacniccontact:add>
          <lacniccontact:property>bulkwhois</lacniccontact:property>
        </lacniccontact:add>
        <lacniccontact:rem>
          <lacniccontact:property>inactive</lacniccontact:property>
        </lacniccontact:rem>
        <lacniccontact:chg>
          <lacniccontact:password>abc123</lacniccontact:password>
          <lacniccontact:reminder>Default</lacniccontact:reminder>
          <lacniccontact:language>pt</lacniccontact:language>
        </lacniccontact:chg>
      </lacniccontact:update>
    </extension>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def updatecontactcommandwithbrorgandlacnicorgxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <update>
      <contact:update xmlns:contact="urn:ietf:params:xml:ns:contact-1.0">
        <contact:id>ab-12345</contact:id>
        <contact:add>
          <contact:status s="clientDeleteProhibited" />
        </contact:add>
        <contact:rem>
          <contact:status s="clientDeleteProhibited" />
        </contact:rem>
        <contact:chg>
          <contact:postalInfo type="loc">
            <contact:name>Joe Doe</contact:name>
            <contact:org>Example Inc.</contact:org>
            <contact:addr>
              <contact:street>123 Example Dr.</contact:street>
              <contact:street>Suite 100</contact:street>
              <contact:street>xyz</contact:street>
              <contact:city>Dulles</contact:city>
              <contact:sp>VA</contact:sp>
              <contact:pc>20166-6503</contact:pc>
              <contact:cc>US</contact:cc>
            </contact:addr>
          </contact:postalInfo>
          <contact:postalInfo type="int">
            <contact:name>Anna Doe</contact:name>
            <contact:org>Example Inc.</contact:org>
            <contact:addr>
              <contact:street>123 Example Dr.</contact:street>
              <contact:street>Suite 100</contact:street>
              <contact:street>xyz</contact:street>
              <contact:city>Dulles</contact:city>
              <contact:sp>VA</contact:sp>
              <contact:pc>20166-6503</contact:pc>
              <contact:cc>US</contact:cc>
            </contact:addr>
          </contact:postalInfo>
          <contact:voice x="1234">+1.7035555555</contact:voice>
          <contact:email>jdoe@example.com</contact:email>
          <contact:authInfo>
            <contact:pw>123</contact:pw>
          </contact:authInfo>
          <contact:disclose flag="1">
            <contact:name type="int" />
            <contact:org type="int" />
            <contact:addr type="int" />
            <contact:voice />
            <contact:fax />
            <contact:email />
          </contact:disclose>
        </contact:chg>
      </contact:update>
    </update>
    <extension>
      <brorg:update xmlns:brorg="urn:ietf:params:xml:ns:brorg-1.0">
        <brorg:organization>005.506.560/0001-36</brorg:organization>
        <brorg:add>
          <brorg:contact type="admin">hkk</brorg:contact>
        </brorg:add>
        <brorg:rem>
          <brorg:contact type="admin">fan</brorg:contact>
        </brorg:rem>
        <brorg:chg>
          <brorg:responsible>Responsible Name</brorg:responsible>
          <brorg:exDate>2009-02-01T12:00:00.0Z</brorg:exDate>
          <brorg:suspended>true</brorg:suspended>
        </brorg:chg>
      </brorg:update>
      <lacnicorg:update xmlns:lacnicorg="urn:ietf:params:xml:ns:lacnicorg-1.0">
        <lacnicorg:add>
          <lacnicorg:eppIP>192.168.0.1</lacnicorg:eppIP>
          <lacnicorg:eppIP>192.0.2.0/24</lacnicorg:eppIP>
          <lacnicorg:renewalType>large</lacnicorg:renewalType>
        </lacnicorg:add>
        <lacnicorg:rem>
          <lacnicorg:eppIP>203.0.113.0/24</lacnicorg:eppIP>
          <lacnicorg:renewalType>small</lacnicorg:renewalType>
        </lacnicorg:rem>
        <lacnicorg:chg>
          <lacnicorg:type>normal</lacnicorg:type>
          <lacnicorg:eppStatus>active</lacnicorg:eppStatus>
          <lacnicorg:eppPassword>abc123</lacnicorg:eppPassword>
          <lacnicorg:resourcesClass>non-legacy-only</lacnicorg:resourcesClass>
        </lacnicorg:chg>
        <lacnicorg:password>abc123</lacnicorg:password>
      </lacnicorg:update>
    </extension>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def responseupdatecontactcommandxmlexpected():
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
