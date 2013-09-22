import fec.version.v6_4.F1
import fec.version.v6_4.F13
import fec.version.v6_4.F132
import fec.version.v6_4.F133
import fec.version.v6_4.F1M
import fec.version.v6_4.F1S
import fec.version.v6_4.F2
import fec.version.v6_4.F24
import fec.version.v6_4.F2S
import fec.version.v6_4.F3
import fec.version.v6_4.F3L
import fec.version.v6_4.F3P
import fec.version.v6_4.F3P31
import fec.version.v6_4.F3S
import fec.version.v6_4.F3X
import fec.version.v6_4.F3Z
import fec.version.v6_4.F4
import fec.version.v6_4.F5
import fec.version.v6_4.F56
import fec.version.v6_4.F57
import fec.version.v6_4.F6
import fec.version.v6_4.F65
import fec.version.v6_4.F7
import fec.version.v6_4.F76
import fec.version.v6_4.F8
import fec.version.v6_4.F82
import fec.version.v6_4.F83
import fec.version.v6_4.F9
import fec.version.v6_4.F91
import fec.version.v6_4.F92
import fec.version.v6_4.F93
import fec.version.v6_4.F94
import fec.version.v6_4.F99
import fec.version.v6_4.HRD
import fec.version.v6_4.SA
import fec.version.v6_4.SB
import fec.version.v6_4.SC
import fec.version.v6_4.SC1
import fec.version.v6_4.SC2
import fec.version.v6_4.SD
import fec.version.v6_4.SE
import fec.version.v6_4.SF
import fec.version.v6_4.SH1
import fec.version.v6_4.SH2
import fec.version.v6_4.SH3
import fec.version.v6_4.SH4
import fec.version.v6_4.SH5
import fec.version.v6_4.SH6
import fec.version.v6_4.SI
import fec.version.v6_4.SL
import fec.version.v6_4.TEXT
from fec.version.version_base import VersionBase
class Version(VersionBase):
    def __init__(self):
        self.records = {
            'F1' : fec.version.v6_4.F1.Records,
            'F13' : fec.version.v6_4.F13.Records,
            'F132' : fec.version.v6_4.F132.Records,
            'F133' : fec.version.v6_4.F133.Records,
            'F1M' : fec.version.v6_4.F1M.Records,
            'F1S' : fec.version.v6_4.F1S.Records,
            'F2' : fec.version.v6_4.F2.Records,
            'F24' : fec.version.v6_4.F24.Records,
            'F2S' : fec.version.v6_4.F2S.Records,
            'F3' : fec.version.v6_4.F3.Records,
            'F3L' : fec.version.v6_4.F3L.Records,
            'F3P' : fec.version.v6_4.F3P.Records,
            'F3P31' : fec.version.v6_4.F3P31.Records,
            'F3S' : fec.version.v6_4.F3S.Records,
            'F3X' : fec.version.v6_4.F3X.Records,
            'F3Z' : fec.version.v6_4.F3Z.Records,
            'F4' : fec.version.v6_4.F4.Records,
            'F5' : fec.version.v6_4.F5.Records,
            'F56' : fec.version.v6_4.F56.Records,
            'F57' : fec.version.v6_4.F57.Records,
            'F6' : fec.version.v6_4.F6.Records,
            'F65' : fec.version.v6_4.F65.Records,
            'F7' : fec.version.v6_4.F7.Records,
            'F76' : fec.version.v6_4.F76.Records,
            'F8' : fec.version.v6_4.F8.Records,
            'F82' : fec.version.v6_4.F82.Records,
            'F83' : fec.version.v6_4.F83.Records,
            'F9' : fec.version.v6_4.F9.Records,
            'F91' : fec.version.v6_4.F91.Records,
            'F92' : fec.version.v6_4.F92.Records,
            'F93' : fec.version.v6_4.F93.Records,
            'F94' : fec.version.v6_4.F94.Records,
            'F99' : fec.version.v6_4.F99.Records,
            'HRD' : fec.version.v6_4.HRD.Records,
            'SA' : fec.version.v6_4.SA.Records,
            'SB' : fec.version.v6_4.SB.Records,
            'SC' : fec.version.v6_4.SC.Records,
            'SC1' : fec.version.v6_4.SC1.Records,
            'SC2' : fec.version.v6_4.SC2.Records,
            'SD' : fec.version.v6_4.SD.Records,
            'SE' : fec.version.v6_4.SE.Records,
            'SF' : fec.version.v6_4.SF.Records,
            'SH1' : fec.version.v6_4.SH1.Records,
            'SH2' : fec.version.v6_4.SH2.Records,
            'SH3' : fec.version.v6_4.SH3.Records,
            'SH4' : fec.version.v6_4.SH4.Records,
            'SH5' : fec.version.v6_4.SH5.Records,
            'SH6' : fec.version.v6_4.SH6.Records,
            'SI' : fec.version.v6_4.SI.Records,
            'SL' : fec.version.v6_4.SL.Records,
            'TEXT' : fec.version.v6_4.TEXT.Records,
        }
        self.field_order = [
            'F1',
            'F13',
            'F132',
            'F133',
            'F1M',
            'F1S',
            'F2',
            'F24',
            'F2S',
            'F3',
            'F3L',
            'F3P',
            'F3P31',
            'F3S',
            'F3X',
            'F3Z',
            'F4',
            'F5',
            'F56',
            'F57',
            'F6',
            'F65',
            'F7',
            'F76',
            'F8',
            'F82',
            'F83',
            'F9',
            'F91',
            'F92',
            'F93',
            'F94',
            'F99',
            'HRD',
            'SA',
            'SB',
            'SC',
            'SC1',
            'SC2',
            'SD',
            'SE',
            'SF',
            'SH1',
            'SH2',
            'SH3',
            'SH4',
            'SH5',
            'SH6',
            'SI',
            'SL',
            'TEXT',
        ]
