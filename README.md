#registrobrepp

##About

registrobrepp is a python library to manage domains at registro.br

##Table of contents

- [registrobrepp](#registrobrepp)
    * [About](#about)
    * [Table of contents](#table-of-contents)
    * [Installation](#installation)
    * [Examples](#examples)
        + [Client](#client)
        + Contacts
            + [Check contacts](#check-contacts)
            + [Create contacts](#create-contacts)
            + [Delete contacts](#delete-contacts)
            + [Info contacts](#info-contacts)
            + [Transfer contacts](#transfer-contacts)
            + [Update contacts](#update-contacts)
        + Domains
            + [Check domains](#check-domains)
            + [Create domains](#create-domains)
            + [Delete domains](#delete-domains)
            + [Info domains](#info-domains)
            + [Renew domains](#renew-domains)
            + [Transfer domains](#transfer-domains)
            + [Update domains](#update-domains)
        
##Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install regitrobrepp.

```bash
pip install registrobrepp
```

##Examples
###Client
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

#Send a command (BrEppCheckContact, BrEppCheckDomainCommand, etc.)
names = ['du.eti.br', 'nic.br', 'registro.br']
command = BrEppCheckDomainCommand(names)
resp = registrobr.send(command)

##Logout
registrobr.logout()
```

### Check contacts
```python
ids = ['ab-12345', 'aa-11111']
command = BrEppCheckContactCommand(ids)
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
command = BrEppCreateContactCommand(id, postalinfo, 'jdoe@example.com', authinfo, postalinfo2=postalinfo2, voice=voice, disclose=disclose)
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
###Update contacts
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

###Check domains
```python
names = ['du.eti.br', 'nic.br', 'registro.br']
command = BrEppCheckDomainCommand(names)
##Send command with a client
```
###Create domains
```python
authinfo = AuthInfo('2fooBAR')
ns = Ns(['ns1.example.net', 'ns2.example.net'])
contacts = [Contact.build('sh8013', admin=True), Contact.build('sh8013', tech=True)]
command = BrEppCreateDomainCommand('example.com.br', ns, authinfo, 2, 'y', 'jd1234', contacts)
##Send command with a client
```
###Delete domains
```python
command = BrEppDeleteDomainCommand('example.com.br')
##Send command with a client
```
###Info domains
```python
authinfo = AuthInfo('2fooBAR')
command = BrEppInfoDomainCommand('example.com.br', authinfo)
##Send command with a client
```
###Renew domains
```python
curexpdate = datetime.date(2000, 4, 3)
command = BrEppRenewDomainCommand('example.com.br', curexpdate, 5)
##Send command with a client
```
###Transfer domains
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
###Update domains
```python
authinfo = AuthInfo('2BARfoo')
ns = Ns(['ns2.example.com.br'])
contact = Contact.build(info='mak21', tech=True)
statusadd = Status(s='clientHold', lang='en', info='Payment overdue.')
add = AddDomain(ns, contact, statusadd)
ns = Ns(['ns1.example.com.br'])
contact = Contact.build(info='sh8013', tech=True)
statusrem = Status(s='clientUpdateProhibited')
rem = RemDomain(ns, contact, statusrem)
chg = ChgDomain('sh8013', authinfo)
command = BrEppUpdateDomainCommand('example.com.br', add, rem, chg)
##Send command with a client
```