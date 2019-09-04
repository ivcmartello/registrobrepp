import pytest
from decouple import config


@pytest.fixture
def defregxmlschema():
    from lxml import etree

    schema = config('EPPSCHEMAPATH', '../../../schemas') + '/defReg-1.0.xsd'
    xmlschema_doc = etree.parse(schema)
    return etree.XMLSchema(xmlschema_doc)


@pytest.fixture
def checkdefregcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <check>
      <defReg:check xmlns:defReg="http://nic.br/epp/defReg-1.0">
        <defReg:name level="premium">doe</defReg:name>
        <defReg:name level="standard">john.doe</defReg:name>
      </defReg:check>
    </check>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def responsecheckdefregcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <response>
    <result code="1000">
      <msg>Command completed successfully</msg>
    </result>
    <resData>
      <defReg:chkData xmlns:defReg="http://nic.br/epp/defReg-1.0">
        <defReg:cd>
          <defReg:name avail="1" level="premium">doe</defReg:name>
        </defReg:cd>
        <defReg:cd>
          <defReg:name avail="0" level="standard">john.doe</defReg:name>
          <defReg:reason>Conflicting object exists</defReg:reason>
        </defReg:cd>
      </defReg:chkData>
    </resData>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54322-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def createdefregcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <create>
      <defReg:create xmlns:defReg="http://nic.br/epp/defReg-1.0">
        <defReg:name level="premium">doe</defReg:name>
        <defReg:registrant>jd1234</defReg:registrant>
        <defReg:tm>XYZ-123</defReg:tm>
        <defReg:tmCountry>US</defReg:tmCountry>
        <defReg:tmDate>1990-04-03</defReg:tmDate>
        <defReg:adminContact>sh8013</defReg:adminContact>
        <defReg:authInfo>
          <defReg:pw roid="SH8013-REP">abc123</defReg:pw>
        </defReg:authInfo>
      </defReg:create>
    </create>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def responsecreatedefregcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <response>
    <result code="1000">
      <msg>Command completed successfully</msg>
    </result>
    <resData>
      <defReg:creData xmlns:defReg="http://nic.br/epp/defReg-1.0">
        <defReg:roid>EXAMPLE1-REP</defReg:roid>
        <defReg:name level="premium">doe</defReg:name>
        <defReg:crDate>1999-04-03T22:00:00.0Z</defReg:crDate>
        <defReg:exDate>2000-04-03T22:00:00.0Z</defReg:exDate>
      </defReg:creData>
    </resData>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54322-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def deletedefregcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <delete>
      <defReg:delete xmlns:defReg="http://nic.br/epp/defReg-1.0">
        <defReg:roid>EXAMPLE1-REP</defReg:roid>
      </defReg:delete>
    </delete>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def responsedeletedefregcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <response>
    <result code="1000">
      <msg>Command completed successfully</msg>
    </result>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54322-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def infodefregcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <info>
      <defReg:info xmlns:defReg="http://nic.br/epp/defReg-1.0">
        <defReg:roid>EXAMPLE1-REP</defReg:roid>
        <defReg:authInfo>
          <defReg:pw roid="SH8013-REP">abc123</defReg:pw>
        </defReg:authInfo>
      </defReg:info>
    </info>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def responseinfodefregcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <response>
    <result code="1000">
      <msg>Command completed successfully</msg>
    </result>
    <resData>
      <defReg:infData xmlns:defReg="http://nic.br/epp/defReg-1.0">
        <defReg:roid>EXAMPLE1-REP</defReg:roid>
        <defReg:name level="premium">doe</defReg:name>
        <defReg:registrant>jd1234</defReg:registrant>
        <defReg:tm>XYZ-123</defReg:tm>
        <defReg:tmCountry>US</defReg:tmCountry>
        <defReg:tmDate>1990-04-03</defReg:tmDate>
        <defReg:adminContact>sh8013</defReg:adminContact>
        <defReg:status s="ok" />
        <defReg:clID>ClientX</defReg:clID>
        <defReg:crID>ClientY</defReg:crID>
        <defReg:crDate>1999-04-03T22:00:00.0Z</defReg:crDate>
        <defReg:upID>ClientX</defReg:upID>
        <defReg:upDate>1999-12-03T09:00:00.0Z</defReg:upDate>
        <defReg:exDate>2000-04-03T22:00:00.0Z</defReg:exDate>
        <defReg:trDate>2000-01-08T09:00:00.0Z</defReg:trDate>
        <defReg:authInfo>
          <defReg:pw>2fooBAR</defReg:pw>
        </defReg:authInfo>
      </defReg:infData>
    </resData>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54322-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def renewdefregcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <renew>
      <defReg:renew xmlns:defReg="http://nic.br/epp/defReg-1.0">
        <defReg:roid>EXAMPLE1-REP</defReg:roid>
        <defReg:curExpDate>2000-04-03</defReg:curExpDate>
        <defReg:period unit="y">1</defReg:period>
      </defReg:renew>
    </renew>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def responserenewdefregcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <response>
    <result code="1000">
      <msg>Command completed successfully</msg>
    </result>
    <resData>
      <defReg:renData xmlns:defReg="http://nic.br/epp/defReg-1.0">
        <defReg:roid>EXAMPLE1-REP</defReg:roid>
        <defReg:exDate>2001-04-03T22:00:00.0Z</defReg:exDate>
      </defReg:renData>
    </resData>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54322-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def transferquerydefregcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <transfer op="query">
      <defReg:transfer xmlns:defReg="http://nic.br/epp/defReg-1.0">
        <defReg:roid>EXAMPLE1-REP</defReg:roid>
        <defReg:authInfo>
          <defReg:pw roid="SH8013-REP">abc123</defReg:pw>
        </defReg:authInfo>
      </defReg:transfer>
    </transfer>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def responsetransferquerydefregcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <response>
    <result code="1000">
      <msg>Command completed successfully</msg>
    </result>
    <resData>
      <defReg:trnData xmlns:defReg="http://nic.br/epp/defReg-1.0">
        <defReg:roid>EXAMPLE1-REP</defReg:roid>
        <defReg:trStatus>pending</defReg:trStatus>
        <defReg:reID>ClientX</defReg:reID>
        <defReg:reDate>2000-06-06T22:00:00.0Z</defReg:reDate>
        <defReg:acID>ClientY</defReg:acID>
        <defReg:acDate>2000-06-11T22:00:00.0Z</defReg:acDate>
        <defReg:exDate>2002-09-08T22:00:00.0Z</defReg:exDate>
      </defReg:trnData>
    </resData>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54322-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


@pytest.fixture
def updatedefregcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <command>
    <update>
      <defReg:update xmlns:defReg="http://nic.br/epp/defReg-1.0">
        <defReg:roid>EXAMPLE1-REP</defReg:roid>
        <defReg:add>
          <defReg:status lang="en" s="clientDeleteProhibited">Deletions not desired.</defReg:status>
        </defReg:add>
        <defReg:rem>
          <defReg:status s="clientUpdateProhibited" />
        </defReg:rem>
        <defReg:chg>
          <defReg:registrant>sh8013</defReg:registrant>
          <defReg:tm>XYZ-123</defReg:tm>
          <defReg:tmCountry>US</defReg:tmCountry>
          <defReg:tmDate>1990-04-03</defReg:tmDate>
          <defReg:adminContact>sh8013</defReg:adminContact>
          <defReg:authInfo>
            <defReg:pw roid="SH8013-REP">abc123</defReg:pw>
          </defReg:authInfo>
        </defReg:chg>
      </defReg:update>
    </update>
    <clTRID>ABC-12345</clTRID>
  </command>
</epp>
"""


@pytest.fixture
def responseupdatedefregcommandxmlexpected():
    return """<epp xmlns="urn:ietf:params:xml:ns:epp-1.0">
  <response>
    <result code=\"1000\">
      <msg>Command completed successfully</msg>
    </result>
    <trID>
      <clTRID>ABC-12345</clTRID>
      <svTRID>54322-XYZ</svTRID>
    </trID>
  </response>
</epp>
"""


