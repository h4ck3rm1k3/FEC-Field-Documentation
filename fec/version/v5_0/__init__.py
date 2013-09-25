import fec.version.v5_0.F1
import fec.version.v5_0.F10
import fec.version.v5_0.F105
import fec.version.v5_0.F11
import fec.version.v5_0.F12
import fec.version.v5_0.F1M
import fec.version.v5_0.F1S
import fec.version.v5_0.F2
import fec.version.v5_0.F24
import fec.version.v5_0.F3
import fec.version.v5_0.F3P
import fec.version.v5_0.F3P31
import fec.version.v5_0.F3PS
import fec.version.v5_0.F3S
import fec.version.v5_0.F3X
import fec.version.v5_0.F3Z
import fec.version.v5_0.F4
import fec.version.v5_0.F5
import fec.version.v5_0.F56
import fec.version.v5_0.F57
import fec.version.v5_0.F6
import fec.version.v5_0.F65
import fec.version.v5_0.F7
import fec.version.v5_0.F76
import fec.version.v5_0.F8
import fec.version.v5_0.F82
import fec.version.v5_0.F83
import fec.version.v5_0.F9
import fec.version.v5_0.F91
import fec.version.v5_0.F92
import fec.version.v5_0.F93
import fec.version.v5_0.F94
import fec.version.v5_0.F99
import fec.version.v5_0.HRD
import fec.version.v5_0.SA
import fec.version.v5_0.SB
import fec.version.v5_0.SC
import fec.version.v5_0.SC1
import fec.version.v5_0.SC2
import fec.version.v5_0.SD
import fec.version.v5_0.SE
import fec.version.v5_0.SF
import fec.version.v5_0.SH1
import fec.version.v5_0.SH2
import fec.version.v5_0.SH3
import fec.version.v5_0.SH4
import fec.version.v5_0.SH5
import fec.version.v5_0.SH6
import fec.version.v5_0.SI
import fec.version.v5_0.SL
import fec.version.v5_0.TEXT
from fec.version.version_base import VersionBase
class Version(VersionBase):
    def __init__(self):
        VersionBase.__init__(self)
        self.records = {
            'F1' : fec.version.v5_0.F1.Records,
            'F10' : fec.version.v5_0.F10.Records,
            'F105' : fec.version.v5_0.F105.Records,
            'F11' : fec.version.v5_0.F11.Records,
            'F12' : fec.version.v5_0.F12.Records,
            'F1M' : fec.version.v5_0.F1M.Records,
            'F1S' : fec.version.v5_0.F1S.Records,
            'F2' : fec.version.v5_0.F2.Records,
            'F24' : fec.version.v5_0.F24.Records,
            'F3' : fec.version.v5_0.F3.Records,
            'F3P' : fec.version.v5_0.F3P.Records,
            'F3P31' : fec.version.v5_0.F3P31.Records,
            'F3PS' : fec.version.v5_0.F3PS.Records,
            'F3S' : fec.version.v5_0.F3S.Records,
            'F3X' : fec.version.v5_0.F3X.Records,
            'F3Z' : fec.version.v5_0.F3Z.Records,
            'F4' : fec.version.v5_0.F4.Records,
            'F5' : fec.version.v5_0.F5.Records,
            'F56' : fec.version.v5_0.F56.Records,
            'F57' : fec.version.v5_0.F57.Records,
            'F6' : fec.version.v5_0.F6.Records,
            'F65' : fec.version.v5_0.F65.Records,
            'F7' : fec.version.v5_0.F7.Records,
            'F76' : fec.version.v5_0.F76.Records,
            'F8' : fec.version.v5_0.F8.Records,
            'F82' : fec.version.v5_0.F82.Records,
            'F83' : fec.version.v5_0.F83.Records,
            'F9' : fec.version.v5_0.F9.Records,
            'F91' : fec.version.v5_0.F91.Records,
            'F92' : fec.version.v5_0.F92.Records,
            'F93' : fec.version.v5_0.F93.Records,
            'F94' : fec.version.v5_0.F94.Records,
            'F99' : fec.version.v5_0.F99.Records,
            'HRD' : fec.version.v5_0.HRD.Records,
            'SA' : fec.version.v5_0.SA.Records,
            'SB' : fec.version.v5_0.SB.Records,
            'SC' : fec.version.v5_0.SC.Records,
            'SC1' : fec.version.v5_0.SC1.Records,
            'SC2' : fec.version.v5_0.SC2.Records,
            'SD' : fec.version.v5_0.SD.Records,
            'SE' : fec.version.v5_0.SE.Records,
            'SF' : fec.version.v5_0.SF.Records,
            'SH1' : fec.version.v5_0.SH1.Records,
            'SH2' : fec.version.v5_0.SH2.Records,
            'SH3' : fec.version.v5_0.SH3.Records,
            'SH4' : fec.version.v5_0.SH4.Records,
            'SH5' : fec.version.v5_0.SH5.Records,
            'SH6' : fec.version.v5_0.SH6.Records,
            'SI' : fec.version.v5_0.SI.Records,
            'SL' : fec.version.v5_0.SL.Records,
            'TEXT' : fec.version.v5_0.TEXT.Records,
        }
        self.field_order = [
            'F1',
            'F10',
            'F105',
            'F11',
            'F12',
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
