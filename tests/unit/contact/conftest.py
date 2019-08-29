import pytest
from decouple import config


@pytest.fixture
def contactxmlschema():
    from lxml import etree

    schema = config('EPPSCHEMAPATH', '../../../schemas') + '/contact-1.0.xsd'
    xmlschema_doc = etree.parse(schema)
    return etree.XMLSchema(xmlschema_doc)


@pytest.fixture
def checkcontactcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <check>
      <contact:check xmlns="urn:ietf:params:xml:ns:contact-1.0" xmlns:contact="urn:ietf:params:xml:ns:contact-1.0">
        <id>ab-12345</id>
        <id>aa-11111</id>
      </contact:check>
    </check>
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
      <contact:chkData xmlns="urn:ietf:params:xml:ns:contact-1.0" xmlns:contact="urn:ietf:params:xml:ns:contact-1.0">
        <cd>
          <id avail="1">sh8013</id>
        </cd>
        <cd>
          <id avail="0">sah8013</id>
          <reason>In use</reason>
        </cd>
        <cd>
          <id avail="1">8013sah</id>
        </cd>
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
def createcontactcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <create>
      <contact:create xmlns="urn:ietf:params:xml:ns:contact-1.0" xmlns:contact="urn:ietf:params:xml:ns:contact-1.0">
        <id>ab-12345</id>
        <postalInfo type="loc">
          <name>Joe Doe</name>
          <org>Example Inc.</org>
          <addr>
            <street>123 Example Dr.</street>
            <street>Suite 100</street>
            <street>xyz</street>
            <city>Dulles</city>
            <sp>VA</sp>
            <pc>20166-6503</pc>
            <cc>US</cc>
          </addr>
        </postalInfo>
        <postalInfo type="int">
          <name>Anna Doe</name>
          <org>Example Inc.</org>
          <addr>
            <street>123 Example Dr.</street>
            <street>Suite 100</street>
            <street>xyz</street>
            <city>Dulles</city>
            <sp>VA</sp>
            <pc>20166-6503</pc>
            <cc>US</cc>
          </addr>
        </postalInfo>
        <voice x="1234">+1.7035555555</voice>
        <email>jdoe@example.com</email>
        <authInfo>
          <pw>123</pw>
        </authInfo>
        <disclose flag="1">
          <name type="loc" />
          <org type="loc" />
          <addr type="loc" />
          <voice />
          <fax />
          <email />
        </disclose>
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
      <contact:create xmlns="urn:ietf:params:xml:ns:contact-1.0" xmlns:contact="urn:ietf:params:xml:ns:contact-1.0">
        <id>ab-12345</id>
        <postalInfo type="loc">
          <name>Joe Doe</name>
          <org>Example Inc.</org>
          <addr>
            <street>123 Example Dr.</street>
            <street>Suite 100</street>
            <street>xyz</street>
            <city>Dulles</city>
            <sp>VA</sp>
            <pc>20166-6503</pc>
            <cc>US</cc>
          </addr>
        </postalInfo>
        <postalInfo type="int">
          <name>Anna Doe</name>
          <org>Example Inc.</org>
          <addr>
            <street>123 Example Dr.</street>
            <street>Suite 100</street>
            <street>xyz</street>
            <city>Dulles</city>
            <sp>VA</sp>
            <pc>20166-6503</pc>
            <cc>US</cc>
          </addr>
        </postalInfo>
        <voice x="1234">+1.7035555555</voice>
        <email>jdoe@example.com</email>
        <authInfo>
          <pw>123</pw>
        </authInfo>
        <disclose flag="1">
          <name type="loc" />
          <org type="loc" />
          <addr type="loc" />
          <voice />
          <fax />
          <email />
        </disclose>
      </contact:create>
    </create>
    <extension>
      <lacniccontact:create xmlns="urn:ietf:params:xml:ns:lacniccontact-1.0" xmlns:lacniccontact="urn:ietf:params:xml:ns:lacniccontact-1.0">
        <password>abc123</password>
        <reminder>Default</reminder>
        <language>pt</language>
      </lacniccontact:create>
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
      <contact:creData xmlns="urn:ietf:params:xml:ns:contact-1.0" xmlns:contact="urn:ietf:params:xml:ns:contact-1.0">
        <id>sh8013</id>
        <crDate>1999-04-03T22:00:00.0Z</crDate>
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
def deletecontactcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <delete>
      <contact:delete xmlns="urn:ietf:params:xml:ns:contact-1.0" xmlns:contact="urn:ietf:params:xml:ns:contact-1.0">
        <id>ab-12345</id>
      </contact:delete>
    </delete>
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
      <contact:info xmlns="urn:ietf:params:xml:ns:contact-1.0" xmlns:contact="urn:ietf:params:xml:ns:contact-1.0">
        <id>ab-12345</id>
        <authInfo>
          <pw>123</pw>
        </authInfo>
      </contact:info>
    </info>
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
      <contact:infData xmlns="urn:ietf:params:xml:ns:contact-1.0" xmlns:contact="urn:ietf:params:xml:ns:contact-1.0">
        <id>sh8013</id>
        <roid>SH8013-REP</roid>
        <status s="linked" />
        <status s="clientDeleteProhibited" />
        <postalInfo type="int">
          <name>John Doe</name>
          <org>Example Inc.</org>
          <addr>
            <street>123 Example Dr.</street>
            <street>Suite 100</street>
            <city>Dulles</city>
            <sp>VA</sp>
            <pc>20166-6503</pc>
            <cc>US</cc>
          </addr>
        </postalInfo>
        <voice x="1234">+1.7035555555</voice>
        <fax>+1.7035555556</fax>
        <email>jdoe@example.com</email>
        <clID>ClientY</clID>
        <crID>ClientX</crID>
        <crDate>1999-04-03T22:00:00.0Z</crDate>
        <upID>ClientX</upID>
        <upDate>1999-12-03T09:00:00.0Z</upDate>
        <trDate>2000-04-08T09:00:00.0Z</trDate>
        <authInfo>
          <pw>2fooBAR</pw>
        </authInfo>
        <disclose flag="0">
          <voice />
          <email />
        </disclose>
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
def transferquerycontactcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <transfer op="query">
      <contact:transfer xmlns="urn:ietf:params:xml:ns:contact-1.0" xmlns:contact="urn:ietf:params:xml:ns:contact-1.0">
        <id>ab-12345</id>
        <authInfo>
          <pw>123</pw>
        </authInfo>
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
      <contact:trnData xmlns="urn:ietf:params:xml:ns:contact-1.0" xmlns:contact="urn:ietf:params:xml:ns:contact-1.0">
        <id>sh8013</id>
        <trStatus>pending</trStatus>
        <reID>ClientX</reID>
        <reDate>2000-06-06T22:00:00.0Z</reDate>
        <acID>ClientY</acID>
        <acDate>2000-06-11T22:00:00.0Z</acDate>
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
      <contact:transfer xmlns="urn:ietf:params:xml:ns:contact-1.0" xmlns:contact="urn:ietf:params:xml:ns:contact-1.0">
        <id>ab-12345</id>
        <authInfo>
          <pw>123</pw>
        </authInfo>
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
      <contact:trnData xmlns="urn:ietf:params:xml:ns:contact-1.0" xmlns:contact="urn:ietf:params:xml:ns:contact-1.0">
        <id>sh8013</id>
        <trStatus>pending</trStatus>
        <reID>ClientX</reID>
        <reDate>2000-06-08T22:00:00.0Z</reDate>
        <acID>ClientY</acID>
        <acDate>2000-06-13T22:00:00.0Z</acDate>
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
      <contact:update xmlns="urn:ietf:params:xml:ns:contact-1.0" xmlns:contact="urn:ietf:params:xml:ns:contact-1.0">
        <id>ab-12345</id>
        <add>
          <status s="clientDeleteProhibited" />
        </add>
        <rem>
          <status s="clientDeleteProhibited" />
        </rem>
        <chg>
          <postalInfo type="loc">
            <name>Joe Doe</name>
            <org>Example Inc.</org>
            <addr>
              <street>123 Example Dr.</street>
              <street>Suite 100</street>
              <street>xyz</street>
              <city>Dulles</city>
              <sp>VA</sp>
              <pc>20166-6503</pc>
              <cc>US</cc>
            </addr>
          </postalInfo>
          <postalInfo type="int">
            <name>Anna Doe</name>
            <org>Example Inc.</org>
            <addr>
              <street>123 Example Dr.</street>
              <street>Suite 100</street>
              <street>xyz</street>
              <city>Dulles</city>
              <sp>VA</sp>
              <pc>20166-6503</pc>
              <cc>US</cc>
            </addr>
          </postalInfo>
          <voice x="1234">+1.7035555555</voice>
          <email>jdoe@example.com</email>
          <authInfo>
            <pw>123</pw>
          </authInfo>
          <disclose flag="1">
            <name type="int" />
            <org type="int" />
            <addr type="int" />
            <voice />
            <fax />
            <email />
          </disclose>
        </chg>
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
      <contact:update xmlns="urn:ietf:params:xml:ns:contact-1.0" xmlns:contact="urn:ietf:params:xml:ns:contact-1.0">
        <id>ab-12345</id>
        <add>
          <status s="clientDeleteProhibited" />
        </add>
        <rem>
          <status s="clientDeleteProhibited" />
        </rem>
        <chg>
          <postalInfo type="loc">
            <name>Joe Doe</name>
            <org>Example Inc.</org>
            <addr>
              <street>123 Example Dr.</street>
              <street>Suite 100</street>
              <street>xyz</street>
              <city>Dulles</city>
              <sp>VA</sp>
              <pc>20166-6503</pc>
              <cc>US</cc>
            </addr>
          </postalInfo>
          <postalInfo type="int">
            <name>Anna Doe</name>
            <org>Example Inc.</org>
            <addr>
              <street>123 Example Dr.</street>
              <street>Suite 100</street>
              <street>xyz</street>
              <city>Dulles</city>
              <sp>VA</sp>
              <pc>20166-6503</pc>
              <cc>US</cc>
            </addr>
          </postalInfo>
          <voice x="1234">+1.7035555555</voice>
          <email>jdoe@example.com</email>
          <authInfo>
            <pw>123</pw>
          </authInfo>
          <disclose flag="1">
            <name type="int" />
            <org type="int" />
            <addr type="int" />
            <voice />
            <fax />
            <email />
          </disclose>
        </chg>
      </contact:update>
    </update>
    <extension>
      <lacniccontact:update xmlns="urn:ietf:params:xml:ns:lacniccontact-1.0" xmlns:lacniccontact="urn:ietf:params:xml:ns:lacniccontact-1.0">
        <add>
          <property>bulkwhois</property>
        </add>
        <rem>
          <property>inactive</property>
        </rem>
        <chg>
          <password>abc123</password>
          <reminder>Default</reminder>
          <language>pt</language>
        </chg>
      </lacniccontact:update>
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
