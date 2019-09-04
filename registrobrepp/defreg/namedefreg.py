from eppy.xmldict import XmlDictObject

from registrobrepp.defreg.leveltype import LevelType


class NameDefReg(XmlDictObject):
    def __init__(self, leveltype: LevelType, name: str):
        dct = {
            '@level': leveltype.value,
            '_text': name
        }
        super(NameDefReg, self).__init__(initdict=dct)
