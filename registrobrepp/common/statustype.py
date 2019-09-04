from enum import Enum


class StatusDefRegType(Enum):
    CLIENTDELETEPROHIBITED = 'clientDeleteProhibited'
    CLIENTRENEWPROHIBITED = 'clientRenewProhibited'
    CLIENTTRANSFERPROHIBITED = 'clientTransferProhibited'
    CLIENTUPDATEPROHIBITED = 'clientUpdateProhibited'
    OK = 'ok'
    PENDINGDELETE = 'pendingDelete'
    PENDINGTRANSFER = 'pendingTransfer'
    SERVERDELETEPROHIBITED = 'serverDeleteProhibited'
    SERVERRENEWPROHIBITED = 'serverRenewProhibited'
    SERVERTRANSFERPROHIBITED = 'serverTransferProhibited'
    SERVERUPDATEPROHIBITED = 'serverUpdateProhibited'


class StatusDomainType(Enum):
    CLIENTDELETEPROHIBITED = 'clientDeleteProhibited'
    CLIENTHOLD = 'clientHold'
    CLIENTRENEWPROHIBITED = 'clientRenewProhibited'
    CLIENTTRANSFERPROHIBITED = 'clientTransferProhibited'
    CLIENTUPDATEPROHIBITED = 'clientUpdateProhibited'
    INACTIVE = 'inactive'
    OK = 'ok'
    PENDINGCREATE = 'pendingCreate'
    PENDINGDELETE = 'pendingDelete'
    PENDINGRENEW = 'pendingRenew'
    PENDINGTRANSFER = 'pendingTransfer'
    PENDINGUPDATE = 'pendingUpdate'
    SERVERDELETEPROHIBITED = 'serverDeleteProhibited'
    SERVERHOLD = 'serverHold'
    SERVERRENEWPROHIBITED = 'serverRenewProhibited'
    SERVERTRANSFERPROHIBITED = 'serverTransferProhibited'
    SERVERUPDATEPROHIBITED = 'serverUpdateProhibited'


class StatusContactType(Enum):
    CLIENTDELETEPROHIBITED = 'clientDeleteProhibited'
    CLIENTTRANSFERPROHIBITED = 'clientTransferProhibited'
    CLIENTUPDATEPROHIBITED = 'clientUpdateProhibited'
    LINKED = 'linked'
    OK = 'ok'
    PENDINGCREATE = 'pendingCreate'
    PENDINGDELETE = 'pendingDelete'
    PENDINGTRANSFER = 'pendingTransfer'
    PENDINGUPDATE = 'pendingUpdate'
    SERVERDELETEPROHIBITED = 'serverDeleteProhibited'
    SERVERTRANSFERPROHIBITED = 'serverTransferProhibited'
    SERVERUPDATEPROHIBITED = 'serverUpdateProhibited'
