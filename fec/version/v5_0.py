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
        self.records = {
            'F1' : fec.version.v5_0.F1.Record,
            'F10' : fec.version.v5_0.F10.Record,
            'F105' : fec.version.v5_0.F105.Record,
            'F11' : fec.version.v5_0.F11.Record,
            'F12' : fec.version.v5_0.F12.Record,
            'F1M' : fec.version.v5_0.F1M.Record,
            'F1S' : fec.version.v5_0.F1S.Record,
            'F2' : fec.version.v5_0.F2.Record,
            'F24' : fec.version.v5_0.F24.Record,
            'F3' : fec.version.v5_0.F3.Record,
            'F3P' : fec.version.v5_0.F3P.Record,
            'F3P31' : fec.version.v5_0.F3P31.Record,
            'F3PS' : fec.version.v5_0.F3PS.Record,
            'F3S' : fec.version.v5_0.F3S.Record,
            'F3X' : fec.version.v5_0.F3X.Record,
            'F3Z' : fec.version.v5_0.F3Z.Record,
            'F4' : fec.version.v5_0.F4.Record,
            'F5' : fec.version.v5_0.F5.Record,
            'F56' : fec.version.v5_0.F56.Record,
            'F57' : fec.version.v5_0.F57.Record,
            'F6' : fec.version.v5_0.F6.Record,
            'F65' : fec.version.v5_0.F65.Record,
            'F7' : fec.version.v5_0.F7.Record,
            'F76' : fec.version.v5_0.F76.Record,
            'F8' : fec.version.v5_0.F8.Record,
            'F82' : fec.version.v5_0.F82.Record,
            'F83' : fec.version.v5_0.F83.Record,
            'F9' : fec.version.v5_0.F9.Record,
            'F91' : fec.version.v5_0.F91.Record,
            'F92' : fec.version.v5_0.F92.Record,
            'F93' : fec.version.v5_0.F93.Record,
            'F94' : fec.version.v5_0.F94.Record,
            'F99' : fec.version.v5_0.F99.Record,
            'HRD' : fec.version.v5_0.HRD.Record,
            'SA' : fec.version.v5_0.SA.Record,
            'SB' : fec.version.v5_0.SB.Record,
            'SC' : fec.version.v5_0.SC.Record,
            'SC1' : fec.version.v5_0.SC1.Record,
            'SC2' : fec.version.v5_0.SC2.Record,
            'SD' : fec.version.v5_0.SD.Record,
            'SE' : fec.version.v5_0.SE.Record,
            'SF' : fec.version.v5_0.SF.Record,
            'SH1' : fec.version.v5_0.SH1.Record,
            'SH2' : fec.version.v5_0.SH2.Record,
            'SH3' : fec.version.v5_0.SH3.Record,
            'SH4' : fec.version.v5_0.SH4.Record,
            'SH5' : fec.version.v5_0.SH5.Record,
            'SH6' : fec.version.v5_0.SH6.Record,
            'SI' : fec.version.v5_0.SI.Record,
            'SL' : fec.version.v5_0.SL.Record,
            'TEXT' : fec.version.v5_0.TEXT.Record,
        }
