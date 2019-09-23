# registrobrepp

[![Build Status](https://travis-ci.com/ivcmartello/registrobrepp.svg?branch=master)](https://travis-ci.org/ivcmartello/registrobrepp)

## About

registrobrepp is a python library to manage domains at registro.br

## Test enviroment information

https://beta.registro.br/

## Table of contents

- [registrobrepp](#registrobrepp)
    * [About](#about)
    * [Test enviroment information](#test-enviroment-information)
    * [Table of contents](#table-of-contents)
    * [Installation](#installation)
    * [Examples](#examples)
        + [Client](#client)
        + Asn
            + [Check Asns](#check-asns)
            + [Create Asns](#create-asns)
            + [Create Reserve Asns](#create-reserve-asns)
            + [Delete Asns](#delete-asns)
            + [Delete Reserve Asns](#delete-reserve-asns)
            + [Info Asns](#info-asns)
            + [Renew Asns](#renew-asns)
            + [Transfer Asns](#transfer-asns)
            + [Update Asns](#update-asns)
        + Contacts
            + [Check contacts](#check-contacts)
            + [Check contacts with brorg extension](#check-contacts-with-brorg-extension)
            + [Create contacts](#create-contacts)
            + [Create contacts with lacniccontact extension](#create-contacts-with-lacniccontact-extension)
            + [Create contacts with brorg and lacnicorg extension](#create-contacts-with-brorg-and-lacnicorg-extension)
            + [Delete contacts](#delete-contacts)
            + [Info contacts](#info-contacts)
            + [Transfer contacts](#transfer-contacts)
            + [Update contacts](#update-contacts)
        + DefRegs
            + [Check defregs](#check-defregs)
            + [Create defregs](#create-defregs)
            + [Delete defregs](#delete-defregs)
            + [Info defregs](#info-defregs)
            + [Transfer defregs](#transfer-defregs)
            + [Update defregs](#update-defregs)
        + Domains
            + [Check domains](#check-domains)
            + [Check domains with launch extension](#check-domains-with-launch-extension)
            + [Check domains with brorg extension](#check-domains-with-brorg-extension)
            + [Create domains](#create-domains)
            + [Create domains with secdns extension](#create-domains-with-secdns-extension)
            + [Create domains with launch extension](#create-domains-with-launch-extension)
            + [Create domains with brorg extension](#create-domains-with-brorg-extension)
            + [Delete domains](#delete-domains)
            + [Delete domains with launch extension](#delete-domains-with-launch-extension)
            + [Info domains](#info-domains)
            + [Info domains with launch extension](#info-domains-with-launch-extension)
            + [Info domains with brorg extension](#info-domains-with-brorg-extension)
            + [Renew domains](#renew-domains)
            + [Transfer domains](#transfer-domains)
            + [Update domains](#update-domains)
            + [Update domains with secdns extension](#update-domains-with-secdns-extension)
            + [Update domains with rgp extension](#update-domains-with-rgp-extension)
            + [Update domains with launch extension](#update-domains-with-launch-extension)
            + [Update domains with brdomain extension](#update-domains-with-brdomain-extension)
        + IpNetworks
            + [Check ipnetworks](#check-ipnetworks)
            + [Create ipnetworks](#create-ipnetworks)
            + [Delete ipnetworks](#delete-ipnetworks)
            + [Info ipnetworks](#info-ipnetworks)
            + [Transfer ipnetworks](#transfer-ipnetworks)
            + [Update ipnetworks](#update-ipnetworks)
        
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install registrobrepp.

```bash
pip install git+https://github.com/ivcmartello/registrobrepp.git
```

## Examples

### Client
```python
host='beta.registro.br'
port=700
ssl_keyfile='file.key'
ssl_certfile='file.pem', 
ssl_cacerts='anotherfile.pem'
registrobr = BrEppClient(host, port, ssl_keyfile=ssl_keyfile, ssl_certfile=ssl_certfile, ssl_cacerts=ssl_cacerts)

##Optional
ouris = ['urn:ietf:params:xml:ns:abc-1.0']
euris = ['urn:ietf:params:xml:ns:xyz-1.0']

##Login
username = 'user'
password = '123'
resp = registrobr.login(username, password, obj_uris=ouris, extra_ext_uris=euris)

##Create a command (BrEppCheckContact, BrEppCheckDomainCommand, etc.)
names = ['du.eti.br', 'nic.br', 'registro.br']
command = BrEppCheckDomainCommand(names)

##The command accept extensions:
brdomain = EppCheckBrDomain('000.000.000/0000-00')
command.add_command_extension(brdomain)

##Send a command
resp = registrobr.send(command)
##Or
##If you want to apply the prefix at the response extension, just set extra_nsmap:
resp = registrobr.send(command, extra_nsmap={'brdomain': 'urn:ietf:params:xml:ns:brdomain-1.0'})

##Logout
registrobr.logout()
```

### Check asns
```python
numbers = [12345, 11111]

command = BrEppCheckAsnCommand(numbers)
##Send command with a client
```

### Create asns
```python
number = 12345
organization = 'BR-ABCD-LACNIC'
contacts = [ContactAsn.build('fan', routing=True), ContactAsn.build('hkk')]
asIn = ['from AS2 10 accept AS1 A2']
asOut = ['to AS2 announce AS3 AS4']

command = BrEppCreateAsnCommand(number, organization, contacts, asIn, asOut)
##Send command with a client
```

### Create reserve asns
```python
startAsn = 65536
endAsn = 131072
organization = 'BR-ABCD-LACNIC'
comment = 'Test Reservation'

command = BrEppCreateReserveAsnCommand(startAsn, endAsn, organization, comment)
##Send command with a client
```

### Delete asns
```python
number = 64500

command = BrEppDeleteAsnCommand(number)
##Send command with a client
```

### Delete reserve asns
```python
id = 64500

command = BrEppDeleteReserveAsnCommand(id)
##Send command with a client
```

### Info asns
```python
number = 64500

command = BrEppInfoAsnCommand(number)
##Send command with a client
```

### Renew asns
```python
number = 64500
curexpdate = datetime.datetime(2008, 4, 3, 00, 00, 00)

command = BrEppRenewAsnCommand(number, curexpdate, period=3)
##Send command with a client
```

### Transfer asns
###### 1 - Request
```python
number = 64500

command = BrEppTransferAsnCommand('request', number)
##Send command with a client
```

### Update asns
```python
number = 64500
contactsadd = [ContactAsn.build('fan', routing=True)]
asIn = ['from AS2 10 accept AS1 A2']
add = AddAsn(contactsadd, asIn)
contactsrem = [ContactAsn.build('hkk')]
asOut = ['to AS2 announce AS3 AS4']
rem = RemAsn(contactsrem, asOut)
chg = ChgAsn('BR-ABCD-LACNIC')
creationdate = datetime.datetime(2011, 1, 27, 00, 00, 00)

command = BrEppUpdateAsnCommand(number, creationdate, add, rem, chg)
##Send command with a client
```

### Check contacts
```python
ids = ['ab-12345', 'aa-11111']

command = BrEppCheckContactCommand(ids)
##Send command with a client
```

### Check contacts with brorg extension
```python
# First create a BrEppCheckContactCommand, after add the extension
cds = [Cd('e123456', '043.828.151/0001-45'), Cd('e654321', '005.506.560/0001-36')]
brorg = EppCheckBrOrg(cds)

command.add_command_extension(brorg)
##Send command with a client
```

### Create contacts
```python
addr = Addr('123 Example Dr.', 'Suite 100', 'Dulles', 'US', street3='xyz', sp='VA', pc='20166-6503')
voice = Phone('1234', '+1.7035555555')
postalinfo = PostalInfo.build('Joe Doe', addr, 'Example Inc.')
postalinfo2 = PostalInfo.build('Anna Doe', addr, 'Example Inc.', international=True)
authinfo = AuthInfo('123')
disclose = Disclose(flag=True, name_loc=True, org_loc=True, addr_loc=True, voice=True, fax=True, email=True)
id = 'ab-12345'
email = 'jdoe@example.com'

command = BrEppCreateContactCommand(id, postalinfo, email, authinfo, postalinfo2=postalinfo2, voice=voice, disclose=disclose)
##Send command with a client
```

### Create contacts with lacniccontact extension
```python
# First create a BrEppCreateContactCommand, after add the extension
lacnic = EppCreateLacnicContact('abc123')

command.add_command_extension(lacnic)
##Send command with a client
```

### Create contacts with brorg and lacnicorg extension
```python
# First create a BrEppCreateContactCommand, after add the extensions
organization = '005.506.560/0001-36'
contacts = [ContactBrOrg.build('fan', admin=True), ContactBrOrg.build('fun'),
            ContactBrOrg.build('fuc', member=True)]
responsible = 'John Doe'
brorg = EppCreateBrOrg(organization, contacts, responsible)

eppips = ['192.168.0.1', '192.0.2.0/24', '203.0.113.0/24']
renewtypes = [RenewalType.MEMBER, RenewalType.SMALL, RenewalType.FOUNDING_PARTNER]
lacnicorg = EppCreateLacnicOrg(OrgType.NORMAL, 'abc123', eppips, renewtypes, ResourcesClass.ALL_RESOURCES)

command.add_command_extension(brorg)
command.add_command_extension(lacnicorg)
##Send command with a client
```

### Delete contacts
```python
id = 'ab-12345'

command = BrEppDeleteContactCommand(id)
##Send command with a client
```

### Info contacts
```python
authinfo = AuthInfo('123')
id = 'ab-12345'

command = BrEppInfoContactCommand(id, authinfo)
##Send command with a client
```

### Transfer contacts

###### 1 - Query
```python
authinfo = AuthInfo('123')
id = 'ab-12345'

command = BrEppTransferContactCommand('query', id, authinfo)
##Send command with a client
```

###### 2 - Request
```python
authinfo = AuthInfo('123')
id = 'ab-12345'

command = BrEppTransferContactCommand('request', id, authinfo)
##Send command with a client
```

### Update contacts
```python
authinfo = AuthInfo('123')
addr = Addr('123 Example Dr.', 'Suite 100', 'Dulles', 'US', street3='xyz', sp='VA', pc='20166-6503')
voice = Phone('1234', '+1.7035555555')
postalinfo = PostalInfo.build('Joe Doe', addr, 'Example Inc.')
postalinfo2 = PostalInfo.build('Anna Doe', addr, 'Example Inc.', international=True)
disclose = Disclose(flag=True, name_int=True, org_int=True, addr_int=True, voice=True, fax=True, email=True)
statusadd = [Status(s='clientDeleteProhibited')]
statusrem = [Status(s='clientDeleteProhibited')]
chg = ChgContact(postalinfo, 'jdoe@example.com', authinfo, postalinfo2=postalinfo2, voice=voice, disclose=disclose)

command = BrEppUpdateContactCommand('ab-12345', statusadd, status_rem=statusrem, chg=chg)
##Send command with a client
```

### Check defregs
```python
names = [NameDefReg(LevelType.PREMIUM, 'doe'), NameDefReg(LevelType.STANDARD, 'john.doe')]

command = BrEppCheckDefRegCommand(names)
##Send command with a client
```

### Create defregs
```python
name = NameDefReg(LevelType.PREMIUM, 'doe')
registrant = 'jd1234'
tm = 'XYZ-123'
tmcountry = 'US'
tmdate = datetime.date(1990, 4, 3)
admincontact = 'sh8013'
authinfo = AuthInfo('abc123', 'SH8013-REP')

command = BrEppCreateDefRegCommand(name, registrant, tm, tmcountry, tmdate, admincontact, authinfo)
##Send command with a client
```

### Delete defregs
```python
roid = 'EXAMPLE1-REP'

command = BrEppDeleteDefRegCommand(roid)
##Send command with a client
```

### Info defregs
```python
roid = 'EXAMPLE1-REP'
authinfo = AuthInfo('abc123', 'SH8013-REP')

command = BrEppInfoDefRegCommand(roid, authinfo)
##Send command with a client
```

### Renew defregs
```python
roid = 'EXAMPLE1-REP'
curexpdate = datetime.date(2000, 4, 3)
period = 1

command = BrEppRenewDefRegCommand(roid, curexpdate, period, PeriodType.YEAR)
##Send command with a client
```

### Transfer defregs
###### 1 - Query
```python
roid = 'EXAMPLE1-REP'
authinfo = AuthInfo('abc123', 'SH8013-REP')

command = BrEppTransferDefRegCommand('query', roid, authinfo)
##Send command with a client
```

### Update defregs
```python
roid = 'EXAMPLE1-REP'
add = AddDefReg([StatusDefReg(StatusDefRegType.CLIENTDELETEPROHIBITED, 'Deletions not desired.', Language.EN)])
rem = RemDefReg([StatusDefReg(StatusDefRegType.CLIENTUPDATEPROHIBITED)])
registrant = 'sh8013'
tm = 'XYZ-123'
tmcountry = 'US'
tmdate = datetime.date(1990, 4, 3)
admincontact = 'sh8013'
authinfo = AuthInfo('abc123', 'SH8013-REP')
chg = ChgDefReg(registrant, tm, tmcountry, tmdate, admincontact, authinfo)

command = BrEppUpdateDefRegCommand(roid, add, rem, chg)
##Send command with a client
```

### Check domains
```python
names = ['du.eti.br', 'nic.br', 'registro.br']

command = BrEppCheckDomainCommand(names)
##Send command with a client
```

### Check domains with launch extension
```python
# First create a BrEppCheckDomainCommand, after add the extension
launch = EppCheckLaunch.build('claims')

command.add_command_extension(launch)
##Send command with a client
```

### Check domains with brorg extension
```python
# First create a BrEppCheckDomainCommand, after add the extension
brdomain = EppCheckBrDomain('005.506.560/0001-36')

command.add_command_extension(brdomain)
##Send command with a client
```

### Create domains
```python
authinfo = AuthInfo('2fooBAR')
ns = NsHostAtt([HostAttr('a.auto.dns.br'),
                HostAttr('b.auto.dns.br')])
contacts = [Contact.build('sh8013', admin=True), Contact.build('sh8013', tech=True)]

command = BrEppCreateDomainCommand('example.com.br', ns, authinfo, 2, 'y', 'jd1234', contacts)
##Send command with a client
```

### Create domains with secdns extension
```python
# First create a BrEppCreateDomainCommand, after add the extension
secdns = EppCreateSecDns('12345', 3, 1, '49FD46E6C4B45C55D4AC')

command.add_command_extension(secdns)
##Send command with a client
```

### Create domains with launch extension
```python
# First create a BrEppCreateDomainCommand, after add the extension
smd = Smd('YkM1cFkyRnViaTV2Y21jdmRHMWphRjl3YVd4dmRDNWpjbXd3UlFZRFZSMGdCRDR3UERBNkJnTXFBd1F3TXpBeEJnZ3JCZ0VGQlFjQ==')
launch = EppCreateLaunch('sunrise', smd)

command.add_command_extension(launch)
##Send command with a client
```

### Create domains with brorg extension
```python
# First create a BrEppCreateDomainCommand, after add the extension
brdomain = EppCreateBrDomain('005.506.560/0001-36', flag1='1', autorenew=True)

command.add_command_extension(brdomain)
##Send command with a client
```

### Delete domains
```python
command = BrEppDeleteDomainCommand('example.com.br')
##Send command with a client
```

### Delete domains with launch extension
```python
# First create a BrEppDeleteDomainCommand, after add the extension
launch = EppDeleteLaunch('sunrise', 'abc123')

command.add_command_extension(launch)
##Send command with a client
```

### Info domains
```python
authinfo = AuthInfo('2fooBAR')

command = BrEppInfoDomainCommand('example.com.br', authinfo)
##Send command with a client
```

### Info domains with launch extension
```python
# First create a BrEppInfoDomainCommand, after add the extension
launch = EppInfoLaunch('claims', 'abc123')

command.add_command_extension(launch)
##Send command with a client
```

### Info domains with brorg extension
```python
# First create a BrEppInfoDomainCommand, after add the extension
brdomain = EppInfoBrDomain('123456')

command.add_command_extension(brdomain)
##Send command with a client
```

### Renew domains
```python
curexpdate = datetime.date(2000, 4, 3)

command = BrEppRenewDomainCommand('example.com.br', curexpdate, 5)
##Send command with a client
```

### Transfer domains
###### 1 - Query
```python
authinfo = AuthInfo('2fooBAR', roid='JD1234-REP')

command = BrEppTransferDomainCommand('query', 'example.com.br', authinfo)
##Send command with a client
```

###### 2 - Request
```python
authinfo = AuthInfo('2fooBAR', roid='JD1234-REP')

command = BrEppTransferDomainCommand('request', 'example.com.br', authinfo, period=1)
##Send command with a client
```

### Update domains
```python
authinfo = AuthInfo('2BARfoo')
nsadd = NsHostAtt([HostAttr('a.auto.dns.br'),
                   HostAttr('b.auto.dns.br')])
contact = Contact.build(info='mak21', tech=True)
statusadd = Status(s='clientHold', lang='en', info='Payment overdue.')
add = AddDomain(nsadd, contact, statusadd)
nsrem = NsHostAtt([HostAttr('foo.xyz.com.br'),
                   HostAttr('ns1.bar.xyz.com.br'),
                   HostAttr('ns2.kzx.com.br')])
contact = Contact.build(info='sh8013', tech=True)
statusrem = Status(s='clientUpdateProhibited')
rem = RemDomain(nsrem, contact, statusrem)
chg = ChgDomain('sh8013', authinfo)

command = BrEppUpdateDomainCommand('example.com.br', add, rem, chg)
##Send command with a client
```

### Update domains with secdns extension
```python
# First create a BrEppUpdateDomainCommand, after add the extension
secdns = EppUpdateSecDns('12346', 3, 1, '38EC35D5B3A34B44C39B')

command.add_command_extension(secdns)
##Send command with a client
```

### Update domains with rgp extension
```python
# First create a BrEppUpdateDomainCommand, after add the extension
predata = 'Pre-delete registration data goes here. Both XML and free text are allowed.'
postdata = 'Post-restore registration data goes here. Both XML and free text are allowed.'
deltime = datetime.datetime(2003, 7, 10, 22, 00, 00)
restime = datetime.datetime(2003, 7, 20, 22, 00, 00)
resreason = 'Registrant error.'
statement1 = 'This registrar has not restored the Registered Name in order to assume the rights to use ' \
    'or sell the Registered Name for itself or for any ' \
    'third party.'
statement2 = 'The information in this report is ' \
    'true to best of this registrar knowledge, and this ' \
    'registrar acknowledges that intentionally supplying ' \
    'false information in this report shall constitute an ' \
    'incurable material breach of the ' \
    'Registry-Registrar Agreement.'
other = 'Supporting information goes here.'
st1 = Statement(statement1)
st2 = Statement(statement2, 'en')
rgp = EppUpdateRgp(predata, postdata, deltime, restime, resreason, [st1, st2], other)

command.add_command_extension(rgp)
##Send command with a client
```

### Update domains with launch extension
```python
# First create a BrEppUpdateDomainCommand, after add the extension
launch = EppUpdateLaunch('sunrise', 'abc123')

command.add_command_extension(launch)
##Send command with a client
```

### Update domains with brdomain extension
```python
# First create a BrEppUpdateDomainCommand, after add the extension
brdomain = EppUpdateBrDomain('ab-1234', chg=ChgBrDomain(flag1=1, publicationstatus=PublicationStatus.ONHOLD,
                                                        autorenew=True))
command.add_command_extension(brdomain)
##Send command with a client
```

### Check ipnetworks
```python
startAddress = '192.168.0.0'
endAddress = '192.168.0.255'

command = BrEppCheckIpNetworkCommand(startAddress, endAddress)
##Send command with a client
```

### Create ipnetworks
```python
iprange = IpRange('192.168.16.0', '192.168.31.255')
organization = 'BR-ABC-LACNIC'
alloctype = 'assignment'
contact = ContactIpNetwork.build('ABC123', admin=True)
reversedns = ReverseDns(IpRange('192.168.16.0', '192.168.17.255'), ['a.example.com', 'b.example.com'])
dsdata = DsData(IpRange('192.168.16.0', '192.168.16.255'), '12345', 3, 1, '49FD46E6C4B45C55D4AC')

command = BrEppCreateIpNetworkCommand(iprange, organization, alloctype, contact, reversedns, dsdata)
##Send command with a client
```

### Delete ipnetworks
```python
roid = 'b_123456-LACNIC'

command = BrEppDeleteIpNetworkCommand(roid)
##Send command with a client
```

### Info ipnetworks
```python
iprange = IpRange('192.168.0.0', '192.168.15.255')
roid = 'b_123456-LACNIC'

command = BrEppInfoIpNetworkCommand(iprange, roid)
##Send command with a client
```

### Renew ipnetworks
```python
roid = 'b_12345-LACNIC'
curexpdate = datetime.datetime(2008, 4, 3, 00, 00, 00)
period = 3

command = BrEppRenewIpNetworkCommand(roid, curexpdate, period)
##Send command with a client
```

### Transfer ipnetworks
###### 1 - Request
```python
roid = 'b_12345-LACNIC'

command = BrEppTransferIpNetworkCommand('request', roid)
##Send command with a client
```

### Update ipnetworks
```python
roid = 'b_123456-LACNIC'
creationdate = datetime.datetime(2011, 1, 27, 00, 00, 00)
dsdata = DsData(IpRange('192.168.16.0', '192.168.16.255'), '12345', 3, 1, '49FD46E6C4B45C55D4AC')
contact = ContactIpNetwork.build('AAA1', tech=True)
add = AddIpNetwork([dsdata], [contact])
contact = ContactIpNetwork.build('AAA1')
rem = RemIpNetwork([dsdata], [contact])
organization = 'BR-DEF-LACNIC'
alloctype = 'assignment'
asn = 2
chg = ChgIpNetwork(organization, alloctype, asn)

command = BrEppUpdateIpNetworkCommand(roid, creationdate, add, rem, chg)
##Send command with a client
```