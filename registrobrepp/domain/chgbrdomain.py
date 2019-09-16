from eppy.xmldict import XmlDictObject

from registrobrepp.domain.publicationstatus import PublicationStatus


class ChgBrDomain(XmlDictObject):
    def __init__(self, organization: str = None, flag1: int = None, flag2: int = None, flag3: int = None,
                 publicationstatus: PublicationStatus = None, autorenew: bool = False):
        rpf = None
        if flag1 or flag2 or flag3:
            rpf = {'@flag1': flag1, '@flag2': flag2, '@flag3': flag3}
        ps = None
        if publicationstatus:
            ps = publicationstatus.value
        dct = {
            'releaseProcessFlags': rpf,
            'autoRenew': {'@active': '1' if autorenew else '0'},
            'publicationStatus': ps,
            'organization': organization,
        }
        super(ChgBrDomain, self).__init__(initdict=dct)
