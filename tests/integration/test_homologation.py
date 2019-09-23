import datetime
import os

import pytest
from decouple import config
from eppy.doc import EppPollCommand

from registrobrepp.breppclient import BrEppClient
from registrobrepp.contact.addr import Addr
from registrobrepp.contact.brcheckcontactcommand import BrEppCheckContactCommand
from registrobrepp.contact.brcreatecontactcommand import BrEppCreateContactCommand
from registrobrepp.contact.brinfocontactcommand import BrEppInfoContactCommand
from registrobrepp.contact.brupdatecontactcommand import BrEppUpdateContactCommand
from registrobrepp.contact.cd import Cd
from registrobrepp.contact.chgcontact import ChgContact
from registrobrepp.contact.contactbrorg import ContactBrOrg
from registrobrepp.contact.eppcheckbrorg import EppCheckBrOrg
from registrobrepp.contact.eppcreatebrorg import EppCreateBrOrg
from registrobrepp.contact.eppinfobrorg import EppInfoBrOrg
from registrobrepp.contact.eppupdatebrorg import EppUpdateBrOrg
from registrobrepp.contact.phone import Phone
from registrobrepp.contact.postalinfo import PostalInfo
from registrobrepp.domain.adddomain import AddDomain
from registrobrepp.domain.brcheckdomaincommand import BrEppCheckDomainCommand
from registrobrepp.domain.brcreatedomaincommand import BrEppCreateDomainCommand
from registrobrepp.domain.brdeletedomaincommand import BrEppDeleteDomainCommand
from registrobrepp.domain.brinfodomaincommand import BrEppInfoDomainCommand
from registrobrepp.domain.brrenewdomaincommand import BrEppRenewDomainCommand
from registrobrepp.domain.brupdatedomaincommand import BrEppUpdateDomainCommand
from registrobrepp.domain.contactdomain import ContactDomain

from registrobrepp.domain.eppcreatebrdomain import EppCreateBrDomain
from registrobrepp.domain.eppinfobrdomain import EppInfoBrDomain
from registrobrepp.domain.eppupdatebrdomain import EppUpdateBrDomain, ChgBrDomain
from registrobrepp.domain.hostaddr import HostAddr
from registrobrepp.domain.hostattr import HostAttr
from registrobrepp.domain.nshostatt import NsHostAtt
from registrobrepp.domain.remdomain import RemDomain


# Documentation
# ftp://ftp.registro.br/pub/libepp-nicbr/pt-epp-accreditation-proc.txt


# This class can be ignored after homologation
@pytest.mark.skip
class TestBrEppClientHomologation:

    @classmethod
    def setup_class(cls):
        # Runs once per class
        path = config('EPPCERTPATH')
        client = ''.join(['../../', path, '/client.pem'])
        root = ''.join(['../../', path, '/root.pem'])
        cls.registrobr = BrEppClient(host='beta.registro.br', port=700, ssl_certfile=client, ssl_cacerts=root)

        # Modificar conforme necessidade
        cls.doc1 = '79.345.491/0001-62'
        cls.dominio1 = 'dominiohomologa10.com.br'
        cls.dominio2 = 'dominiohomologa11.com.br'
        cls.contact1 = 'contacthomologa10'
        cls.org1 = 'organizationhomologa10'
        cls.newcontact1 = 'newcontacthomologa10'

    @classmethod
    def teardown_class(cls):
        # Runs at end of class
        pass

    @pytest.mark.skip
    def test_part1(self):
        self.registrobr.connect('beta.registro.br', 700)
        assert self.registrobr.greeting

        username = config('EPPUSERNAME')
        password = config('EPPPASSWORD')
        newpassword = config('EPPNEWPASSWORD')
        response = self.registrobr.login(username, password, newpassword)
        assert response.ok
        assert response.code == '1000'
        assert response.success

        response = self.registrobr.hello()
        assert response

        self.registrobr.logout()

    @pytest.mark.skip
    def test_part2(self):

        self.registrobr.connect('beta.registro.br', 700)
        assert self.registrobr.greeting

        username = config('EPPUSERNAME')
        newpassword = config('EPPNEWPASSWORD')
        response = self.registrobr.login(username, newpassword)
        assert response.ok
        assert response.code == '1000'
        assert response.success

        # 2.2.1. Create
        # Executar o comando EPP Contact Create para criar um novo contato.
        addr = Addr('Rua Foo', '555', 'Sao Paulo', 'BR', street3='AP11', sp='SP', pc='03047-000')
        postalinfo = PostalInfo.build('Contact One', addr, 'Example Inc.')
        voice = Phone('55.1155555555')
        command = BrEppCreateContactCommand(self.contact1, postalinfo, 'abc@digisat.com.br', voice=voice)
        response = self.registrobr.send(command)
        assert response.ok
        assert response.code == '1000'
        assert response.success

        # 2.2.2. Info
        # Executar o comando EPP Contact Info para buscar informacoes do
        # contato criado informando o ID retornado pelo servidor.  Verificar o
        # campo "contact:id" na resposta do comando anterior.
        contactdata1 = response['epp']['response']['resData']['contact:creData']
        command = BrEppInfoContactCommand(contactdata1.id)
        response = self.registrobr.send(command)
        assert response.ok
        assert response.code == '1000'
        assert response.success

        if os.path.isfile('test.txt'):
            os.remove('test.txt')

        with open('test.txt', '+w') as f:
            f.write(contactdata1.id)

        # 2.2.3. Update
        # Executar o comando EPP Contact Update para atualizar os dados do
        # contato recem-criado.  A atualizacao deve alterar os seguintes
        # atributos:
        #   - Endereco
        #   - Telefone
        #   - E-mail
        addr = Addr('Rua Bar', '666', 'Sao Paulo', 'BR', street3='CJ00')
        voice = Phone('55.1198765432')
        postalinfo = PostalInfo.build('Contact One', addr)
        chg = ChgContact(postalinfo, 'ivan@digisat.com.br', voice=voice)
        command = BrEppUpdateContactCommand(contactdata1.id, chg=chg)
        response = self.registrobr.send(command)
        assert response.ok
        assert response.code == '1000'
        assert response.success

        # 2.3.1. Check
        # Executar o comando EPP Contact Check extendido para Organizacao para
        # checar a disponibilidade de provisionamento de uma determinada
        # organizacao.  Um documento deve ser especificado (CPF ou CNPJ).
        id = ['e123456']
        command = BrEppCheckContactCommand(id)
        cds = [Cd(id[0], self.doc1)]
        brorg = EppCheckBrOrg(cds)
        command.add_command_extension(brorg)
        response = self.registrobr.send(command, extra_nsmap={'brorg': 'urn:ietf:params:xml:ns:brorg-1.0'})
        assert response.ok
        assert response.code == '1000'
        assert response.success

        # 2.3.2. Create
        # Executar o comando EPP Contact Create extendido para Organizacao para
        # criar a nova organizacao ou entidade como e chamada no sistema do
        # Registro.br.  Detalhe: o contato da entidade deve ser o usuario
        # cadastrado na secao 2.2.1.
        contacts = [ContactBrOrg.build(contactdata1.id, admin=True)]
        brorg = EppCreateBrOrg(self.doc1, contacts)
        addr = Addr('Rua Foobar', '123', 'Sao Paulo', 'BR', street3='CJ11', sp='SP', pc='03047-000')
        postalinfo = PostalInfo.build('My business', addr)
        voice = Phone('55.1155555555', '2222')
        command = BrEppCreateContactCommand(self.org1, postalinfo, 'ivan@digisat.com.br', voice=voice)
        command.add_command_extension(brorg)
        response = self.registrobr.send(command, extra_nsmap={'brorg': 'urn:ietf:params:xml:ns:brorg-1.0'})
        assert response.pending
        assert response.code == '1001'
        assert response.success

        # 2.3.3. Info
        # Executar o comando EPP Contact Info extendido para Organizacao para
        # buscar informacoes da organizacao criada no passo anterior.
        orgdata1 = response['epp']['response']['resData']['contact:creData']
        brorg = EppInfoBrOrg(self.doc1)
        command = BrEppInfoContactCommand(orgdata1.id)
        command.add_command_extension(brorg)
        response = self.registrobr.send(command, extra_nsmap={'brorg': 'urn:ietf:params:xml:ns:brorg-1.0'})
        assert response.ok
        assert response.code == '1000'
        assert response.success

        # 2.4.1. Domain Check
        # Executar o comando EPP Domain Check como especificado no Mapping de
        # Dominio para checar a disponibilidade de provisionamento de um
        # determinado nome de dominio.
        names = [self.dominio1]
        command = BrEppCheckDomainCommand(names)
        response = self.registrobr.send(command)
        assert response.ok
        assert response.code == '1000'
        assert response.success

        # 2.4.2. Domain Create
        # Executar o comando EPP Domain Create extendido para dominios .BR.  O
        # dominio deve ser criado sem contatos e com 3 servidores DNS da
        # seguinte forma:
        #   - Primeiro servidor sem glue record
        #   - Segundo servidor com glue record IPv4
        #   - Terceiro servidor com glue record IPv4 e IPv6
        # Nesse passo nao e importante que os servidores DNS tenham autoridade
        # sobre o dominio.
        ns = NsHostAtt([HostAttr('foo.xyz.com.br'),
                        HostAttr('ns1.bar.xyz.com.br', [HostAddr('192.168.0.10')]),
                        HostAttr('ns2.kzx.com.br', [HostAddr('192.168.2.10'),
                                                    HostAddr('2804:218:d2:0:0:0:0:cafe', 'v6')])])
        command = BrEppCreateDomainCommand(self.dominio1, ns)
        brdomain = EppCreateBrDomain(self.doc1)
        command.add_command_extension(brdomain)
        response = self.registrobr.send(command, extra_nsmap={'brdomain': 'urn:ietf:params:xml:ns:brdomain-1.0'})
        assert response.pending
        assert response.code == '1001'
        assert response.success

        # 2.4.3. Ticket Info
        # O comando anterior, se executado com sucesso, retornara um numero de
        # ticket no campo 'brdomain:ticketNumber'. Executar o comando EPP
        # Domain Info extendido para Ticket para buscar informacoes sobre este
        # ticket.
        domainextension1 = response.get_response_extension('brdomain:creData')
        command = BrEppInfoDomainCommand(self.dominio1)
        brdomain = EppInfoBrDomain(domainextension1.ticketNumber)
        command.add_command_extension(brdomain)
        response = self.registrobr.send(command, extra_nsmap={'brdomain': 'urn:ietf:params:xml:ns:brdomain-1.0'})
        assert response.ok
        assert response.code == '1000'
        assert response.success

        # 2.4.4. Ticket Update
        # Executar o comando EPP Domain Update extendido para Ticket para fazer
        # as alteracoes necessarias para resolver todas as pendencias DNS. Ao
        # menos dois servidores de nomes devem ser fornecidos e TODOS os
        # servidores fornecidos devem responder com autoridade sobre o dominio
        # caso contrario o ticket sera cancelado assim que o prazo para
        # resolver as pendencias expirar.
        nsadd = NsHostAtt([HostAttr('a.auto.dns.br'),
                           HostAttr('b.auto.dns.br')])
        add = AddDomain(nsadd)
        nsrem = NsHostAtt([HostAttr('foo.xyz.com.br'),
                           HostAttr('ns1.bar.xyz.com.br'),
                           HostAttr('ns2.kzx.com.br')])
        rem = RemDomain(nsrem)
        command = BrEppUpdateDomainCommand(self.dominio1, add, rem)
        brdomain = EppUpdateBrDomain(domainextension1.ticketNumber)
        command.add_command_extension(brdomain)
        response = self.registrobr.send(command, extra_nsmap={'brdomain': 'urn:ietf:params:xml:ns:brdomain-1.0'})
        assert response.ok
        assert response.code == '1000'
        assert response.success
        # Neste momento, uma vez resolvidas todas as pendencias do ticket
        # criado, e necessario aguardar para que o mesmo seja processado (ate
        # 15 minutos).

        # 2.5. Domain Create (dominio 2)
        # Execute mais um comando Domain Create para um segundo dominio.
        # Certifique-se via o comando Domain Check de que este nome de dominio
        # esteja disponivel e informe ja neste momento servidores DNS que
        # estejam respondendo com autoridade para o dominio em questao.
        names = [self.dominio2]
        command = BrEppCheckDomainCommand(names)
        response = self.registrobr.send(command)
        assert response.ok
        assert response.code == '1000'
        assert response.success

        ns = NsHostAtt([HostAttr('a.auto.dns.br'),
                        HostAttr('b.auto.dns.br')])
        command = BrEppCreateDomainCommand(self.dominio2, ns)
        brdomain = EppCreateBrDomain(self.doc1)
        command.add_command_extension(brdomain)
        response = self.registrobr.send(command, extra_nsmap={'brdomain': 'urn:ietf:params:xml:ns:brdomain-1.0'})
        assert response.pending
        assert response.code == '1001'
        assert response.success
        # Neste momento, uma vez criado o ticket sem pendencias, e necessario
        # aguardar para que o mesmo seja processado e convertido em dominio
        # (ate 15 minutos).

        self.registrobr.logout()

    @pytest.mark.skip
    def test_part3(self):

        if not os.path.isfile('test.txt'):
            raise ValueError()

        with open('test.txt', 'r') as f:
            contactdata1 = {'id': f.readlines()[0]}

        self.registrobr.connect('beta.registro.br', 700)
        assert self.registrobr.greeting

        username = config('EPPUSERNAME')
        newpassword = config('EPPNEWPASSWORD')
        response = self.registrobr.login(username, newpassword)
        assert response.ok
        assert response.code == '1000'
        assert response.success

        # 2.6.1. Poll Request
        # Executar o comando EPP Poll Request para requisitar a primeira
        # mensagem EPP da fila.  Devera receber como resposta a notificacao de
        # criacao da organizacao.  Esse comando nao foi extendido e deve ser
        # usado como especificado em [RFC4930].
        command = EppPollCommand(op='req')
        response = self.registrobr.send(command)
        assert response

        # 2.6.2. Poll Acknowledge
        # Executar o comando EPP Poll Acknowledge para confirmar a remocao da
        # ultima mensagem EPP lida.  Para tal e necessario informar o atributo
        # 'id' dentro de 'msgQ' da mensagem recebida na resposta ao comando
        # anterior.
        try:
            id = response.msgQ['@id']
            command = EppPollCommand(op='ack', msgID=id)
            response = self.registrobr.send(command)
            assert response
        except:
            pass

        # 2.7.1.  Organization Update
        # Uma vez cadastrado o primeiro dominio para uma determinada entidade,
        # ja sera possivel alterar os dados da mesma.
        # Executar o comando EPP Contact Update extendido para Organizacao para
        # atualizar os seguintes atributos:
        #   - Endereco
        #   - Telefone
        brorg = EppUpdateBrOrg(self.doc1)
        addr = Addr('Rua Barfoo', '321', 'Sao Paulo', 'BR', street3='7-AND')
        postalinfo = PostalInfo.build('My business', addr)
        voice = Phone('55.1198761234')
        chg = ChgContact(postalinfo, voice=voice)
        command = BrEppUpdateContactCommand(self.org1, chg=chg)
        command.add_command_extension(brorg)
        response = self.registrobr.send(command, extra_nsmap={'brorg': 'urn:ietf:params:xml:ns:brorg-1.0'})
        assert response.ok
        assert response.code == '1000'
        assert response.success

        # 2.7.2. Organization Info
        # Executar o comando EPP Contact Info para buscar as informacoes
        # atualizadas da organizacao.
        brorg = EppInfoBrOrg(self.doc1)
        command = BrEppInfoContactCommand(self.org1)
        command.add_command_extension(brorg)
        response = self.registrobr.send(command, extra_nsmap={'brorg': 'urn:ietf:params:xml:ns:brorg-1.0'})
        assert response.ok
        assert response.code == '1000'
        assert response.success

        # 2.7.3. Domain Info
        # Executar o comando EPP Domain Info para checar os dados do dominio
        # recem-criado.
        command = BrEppInfoDomainCommand(self.dominio1)
        response = self.registrobr.send(command)
        assert response.ok
        assert response.code == '1000'
        assert response.success

        # 2.7.4. Domain Renew
        # Executar o comando EPP Domain Renew para renovar o dominio por um ano
        # a partir da data de expiracao 'domain:exDate' obtida na resposta do
        # comando anterior.
        expdate = response['epp']['response']['resData']['domain:infData']['exDate']
        expdate_obj = datetime.datetime.strptime(expdate, '%Y-%m-%dT%H:%M:%S.0Z')
        command = BrEppRenewDomainCommand(self.dominio1, expdate_obj, 1)
        response = self.registrobr.send(command)
        assert response.ok
        assert response.code == '1000'
        assert response.success

        # 2.7.5. Domain Update - Contatos
        # Criar um novo contato e executar o comando EPP Domain Update para
        # atualizar o contato de cobranca do dominio recem-criado.
        addr = Addr('Rua Bar', '123', 'Sao Paulo', 'BR', street3='AP44', sp='SP', pc='03047-000')
        postalinfo = PostalInfo.build('New Contact One', addr)
        voice = Phone('55.1155555555')
        command = BrEppCreateContactCommand(self.newcontact1, postalinfo, 'ivan@digisat.com.br', voice=voice)
        response = self.registrobr.send(command)
        assert response.ok
        assert response.code == '1000'
        assert response.success

        newcontact1 = response['epp']['response']['resData']['contact:creData']
        ctd1 = ContactDomain.build(newcontact1.id)
        ctd2 = ContactDomain.build(contactdata1['id'])
        add = AddDomain(contact=ctd1)
        rem = RemDomain(contact=ctd2)
        command = BrEppUpdateDomainCommand(self.dominio1, add=add, rem=rem)
        response = self.registrobr.send(command)
        assert response.ok
        assert response.code == '1000'
        assert response.success

        # 2.7.6. Domain Update - Habilitar Renovacao Automatica
        # Executar o comando EPP Domain Update para habilitar a renovacao
        # automatica do dominio.  Com esta opcao habilitada o dominio sera
        # renovado quando chegar o prazo de expiracao e o valor da manutencao
        # sera debitado automaticamente.
        command = BrEppUpdateDomainCommand(self.dominio1)
        brdomain = EppUpdateBrDomain(chg=ChgBrDomain(autorenew=True))
        command.add_command_extension(brdomain)
        response = self.registrobr.send(command)
        assert response.ok
        assert response.code == '1000'
        assert response.success

        # 2.7.7. Domain Update - Desabilitar Renovacao Automatica
        # Executar o comando EPP Domain Update para desabilitar a renovacao
        # automatica do dominio.  Com esta opcao desabilitada, caso o provedor
        # nao envie um comando EPP Domain Renew ate a data de expiracao do
        # dominio, o mesmo sera congelado e em seguida removido.
        command = BrEppUpdateDomainCommand(self.dominio1)
        brdomain = EppUpdateBrDomain(chg=ChgBrDomain(autorenew=False))
        command.add_command_extension(brdomain)
        response = self.registrobr.send(command)
        assert response.ok
        assert response.code == '1000'
        assert response.success

        # 2.7.8. Domain Delete
        # Executar o comando EPP Domain Delete para excluir o segundo dominio
        # criado anteriormente.
        command = BrEppDeleteDomainCommand(self.dominio2)
        response = self.registrobr.send(command)
        assert response.ok
        assert response.code == '1000'
        assert response.success

        self.registrobr.logout()
