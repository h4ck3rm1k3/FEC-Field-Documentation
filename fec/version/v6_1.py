import fec.version.v6_1.F1
import fec.version.v6_1.F10
import fec.version.v6_1.F105
import fec.version.v6_1.F13
import fec.version.v6_1.F132
import fec.version.v6_1.F133
import fec.version.v6_1.F1M
import fec.version.v6_1.F1S
import fec.version.v6_1.F2
import fec.version.v6_1.F24
import fec.version.v6_1.F2S
import fec.version.v6_1.F3
import fec.version.v6_1.F3P
import fec.version.v6_1.F3P31
import fec.version.v6_1.F3PS
import fec.version.v6_1.F3S
import fec.version.v6_1.F3X
import fec.version.v6_1.F3Z
import fec.version.v6_1.F4
import fec.version.v6_1.F5
import fec.version.v6_1.F56
import fec.version.v6_1.F57
import fec.version.v6_1.F6
import fec.version.v6_1.F65
import fec.version.v6_1.F7
import fec.version.v6_1.F76
import fec.version.v6_1.F8
import fec.version.v6_1.F82
import fec.version.v6_1.F83
import fec.version.v6_1.F9
import fec.version.v6_1.F91
import fec.version.v6_1.F92
import fec.version.v6_1.F93
import fec.version.v6_1.F94
import fec.version.v6_1.F99
import fec.version.v6_1.HRD
import fec.version.v6_1.SA
import fec.version.v6_1.SB
import fec.version.v6_1.SC
import fec.version.v6_1.SC1
import fec.version.v6_1.SC2
import fec.version.v6_1.SD
import fec.version.v6_1.SE
import fec.version.v6_1.SF
import fec.version.v6_1.SH1
import fec.version.v6_1.SH2
import fec.version.v6_1.SH3
import fec.version.v6_1.SH4
import fec.version.v6_1.SH5
import fec.version.v6_1.SH6
import fec.version.v6_1.SI
import fec.version.v6_1.SL
import fec.version.v6_1.TEXT
from fec.version.version_base import VersionBase
class Version(VersionBase):
    def __init__(self):
        self.records = {
            'F1' : fec.version.v6_1.F1.Record,
            'F10' : fec.version.v6_1.F10.Record,
            'F105' : fec.version.v6_1.F105.Record,
            'F13' : fec.version.v6_1.F13.Record,
            'F132' : fec.version.v6_1.F132.Record,
            'F133' : fec.version.v6_1.F133.Record,
            'F1M' : fec.version.v6_1.F1M.Record,
            'F1S' : fec.version.v6_1.F1S.Record,
            'F2' : fec.version.v6_1.F2.Record,
            'F24' : fec.version.v6_1.F24.Record,
            'F2S' : fec.version.v6_1.F2S.Record,
            'F3' : fec.version.v6_1.F3.Record,
            'F3P' : fec.version.v6_1.F3P.Record,
            'F3P31' : fec.version.v6_1.F3P31.Record,
            'F3PS' : fec.version.v6_1.F3PS.Record,
            'F3S' : fec.version.v6_1.F3S.Record,
            'F3X' : fec.version.v6_1.F3X.Record,
            'F3Z' : fec.version.v6_1.F3Z.Record,
            'F4' : fec.version.v6_1.F4.Record,
            'F5' : fec.version.v6_1.F5.Record,
            'F56' : fec.version.v6_1.F56.Record,
            'F57' : fec.version.v6_1.F57.Record,
            'F6' : fec.version.v6_1.F6.Record,
            'F65' : fec.version.v6_1.F65.Record,
            'F7' : fec.version.v6_1.F7.Record,
            'F76' : fec.version.v6_1.F76.Record,
            'F8' : fec.version.v6_1.F8.Record,
            'F82' : fec.version.v6_1.F82.Record,
            'F83' : fec.version.v6_1.F83.Record,
            'F9' : fec.version.v6_1.F9.Record,
            'F91' : fec.version.v6_1.F91.Record,
            'F92' : fec.version.v6_1.F92.Record,
            'F93' : fec.version.v6_1.F93.Record,
            'F94' : fec.version.v6_1.F94.Record,
            'F99' : fec.version.v6_1.F99.Record,
            'HRD' : fec.version.v6_1.HRD.Record,
            'SA' : fec.version.v6_1.SA.Record,
            'SB' : fec.version.v6_1.SB.Record,
            'SC' : fec.version.v6_1.SC.Record,
            'SC1' : fec.version.v6_1.SC1.Record,
            'SC2' : fec.version.v6_1.SC2.Record,
            'SD' : fec.version.v6_1.SD.Record,
            'SE' : fec.version.v6_1.SE.Record,
            'SF' : fec.version.v6_1.SF.Record,
            'SH1' : fec.version.v6_1.SH1.Record,
            'SH2' : fec.version.v6_1.SH2.Record,
            'SH3' : fec.version.v6_1.SH3.Record,
            'SH4' : fec.version.v6_1.SH4.Record,
            'SH5' : fec.version.v6_1.SH5.Record,
            'SH6' : fec.version.v6_1.SH6.Record,
            'SI' : fec.version.v6_1.SI.Record,
            'SL' : fec.version.v6_1.SL.Record,
            'TEXT' : fec.version.v6_1.TEXT.Record,
        }
