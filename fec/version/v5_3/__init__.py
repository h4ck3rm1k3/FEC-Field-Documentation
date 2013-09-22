import fec.version.v5_3.F1
import fec.version.v5_3.F10
import fec.version.v5_3.F105
import fec.version.v5_3.F13
import fec.version.v5_3.F132
import fec.version.v5_3.F133
import fec.version.v5_3.F1M
import fec.version.v5_3.F1S
import fec.version.v5_3.F2
import fec.version.v5_3.F24
import fec.version.v5_3.F3
import fec.version.v5_3.F3P
import fec.version.v5_3.F3P31
import fec.version.v5_3.F3PS
import fec.version.v5_3.F3S
import fec.version.v5_3.F3X
import fec.version.v5_3.F3Z
import fec.version.v5_3.F4
import fec.version.v5_3.F5
import fec.version.v5_3.F56
import fec.version.v5_3.F57
import fec.version.v5_3.F6
import fec.version.v5_3.F65
import fec.version.v5_3.F7
import fec.version.v5_3.F76
import fec.version.v5_3.F8
import fec.version.v5_3.F82
import fec.version.v5_3.F83
import fec.version.v5_3.F9
import fec.version.v5_3.F91
import fec.version.v5_3.F92
import fec.version.v5_3.F93
import fec.version.v5_3.F94
import fec.version.v5_3.F99
import fec.version.v5_3.HRD
import fec.version.v5_3.SA
import fec.version.v5_3.SB
import fec.version.v5_3.SC
import fec.version.v5_3.SC1
import fec.version.v5_3.SC2
import fec.version.v5_3.SD
import fec.version.v5_3.SE
import fec.version.v5_3.SF
import fec.version.v5_3.SH1
import fec.version.v5_3.SH2
import fec.version.v5_3.SH3
import fec.version.v5_3.SH4
import fec.version.v5_3.SH5
import fec.version.v5_3.SH6
import fec.version.v5_3.SI
import fec.version.v5_3.SL
import fec.version.v5_3.TEXT
from fec.version.version_base import VersionBase
class Version(VersionBase):
    def __init__(self):
        self.records = {
            'F1' : fec.version.v5_3.F1.Records,
            'F10' : fec.version.v5_3.F10.Records,
            'F105' : fec.version.v5_3.F105.Records,
            'F13' : fec.version.v5_3.F13.Records,
            'F132' : fec.version.v5_3.F132.Records,
            'F133' : fec.version.v5_3.F133.Records,
            'F1M' : fec.version.v5_3.F1M.Records,
            'F1S' : fec.version.v5_3.F1S.Records,
            'F2' : fec.version.v5_3.F2.Records,
            'F24' : fec.version.v5_3.F24.Records,
            'F3' : fec.version.v5_3.F3.Records,
            'F3P' : fec.version.v5_3.F3P.Records,
            'F3P31' : fec.version.v5_3.F3P31.Records,
            'F3PS' : fec.version.v5_3.F3PS.Records,
            'F3S' : fec.version.v5_3.F3S.Records,
            'F3X' : fec.version.v5_3.F3X.Records,
            'F3Z' : fec.version.v5_3.F3Z.Records,
            'F4' : fec.version.v5_3.F4.Records,
            'F5' : fec.version.v5_3.F5.Records,
            'F56' : fec.version.v5_3.F56.Records,
            'F57' : fec.version.v5_3.F57.Records,
            'F6' : fec.version.v5_3.F6.Records,
            'F65' : fec.version.v5_3.F65.Records,
            'F7' : fec.version.v5_3.F7.Records,
            'F76' : fec.version.v5_3.F76.Records,
            'F8' : fec.version.v5_3.F8.Records,
            'F82' : fec.version.v5_3.F82.Records,
            'F83' : fec.version.v5_3.F83.Records,
            'F9' : fec.version.v5_3.F9.Records,
            'F91' : fec.version.v5_3.F91.Records,
            'F92' : fec.version.v5_3.F92.Records,
            'F93' : fec.version.v5_3.F93.Records,
            'F94' : fec.version.v5_3.F94.Records,
            'F99' : fec.version.v5_3.F99.Records,
            'HRD' : fec.version.v5_3.HRD.Records,
            'SA' : fec.version.v5_3.SA.Records,
            'SB' : fec.version.v5_3.SB.Records,
            'SC' : fec.version.v5_3.SC.Records,
            'SC1' : fec.version.v5_3.SC1.Records,
            'SC2' : fec.version.v5_3.SC2.Records,
            'SD' : fec.version.v5_3.SD.Records,
            'SE' : fec.version.v5_3.SE.Records,
            'SF' : fec.version.v5_3.SF.Records,
            'SH1' : fec.version.v5_3.SH1.Records,
            'SH2' : fec.version.v5_3.SH2.Records,
            'SH3' : fec.version.v5_3.SH3.Records,
            'SH4' : fec.version.v5_3.SH4.Records,
            'SH5' : fec.version.v5_3.SH5.Records,
            'SH6' : fec.version.v5_3.SH6.Records,
            'SI' : fec.version.v5_3.SI.Records,
            'SL' : fec.version.v5_3.SL.Records,
            'TEXT' : fec.version.v5_3.TEXT.Records,
        }
        self.field_order = [
            'F1',
            'F10',
            'F105',
            'F13',
            'F132',
            'F133',
            'F1M',
            'F1S',
            'F2',
            'F24',
            'F3',
            'F3P',
            'F3P31',
            'F3PS',
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
