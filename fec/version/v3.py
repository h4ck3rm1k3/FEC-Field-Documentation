import fec.version.v3.F1
import fec.version.v3.F1M
import fec.version.v3.F1S
import fec.version.v3.F2
import fec.version.v3.F24
import fec.version.v3.F3
import fec.version.v3.F3P
import fec.version.v3.F3P31
import fec.version.v3.F3PS
import fec.version.v3.F3S
import fec.version.v3.F3X
import fec.version.v3.F3Z
import fec.version.v3.F4
import fec.version.v3.F5
import fec.version.v3.F56
import fec.version.v3.F57
import fec.version.v3.F6
import fec.version.v3.F65
import fec.version.v3.F7
import fec.version.v3.F76
import fec.version.v3.F8
import fec.version.v3.F82
import fec.version.v3.F83
import fec.version.v3.F99
import fec.version.v3.HRD
import fec.version.v3.SA
import fec.version.v3.SB
import fec.version.v3.SC
import fec.version.v3.SC1
import fec.version.v3.SC2
import fec.version.v3.SD
import fec.version.v3.SE
import fec.version.v3.SF
import fec.version.v3.SH1
import fec.version.v3.SH2
import fec.version.v3.SH3
import fec.version.v3.SH4
import fec.version.v3.SI
import fec.version.v3.TEXT
from fec.version.version_base import VersionBase
class Version(VersionBase):
    def __init__(self):
        self.records = {
            'F1' : fec.version.v3.F1.Record,
            'F1M' : fec.version.v3.F1M.Record,
            'F1S' : fec.version.v3.F1S.Record,
            'F2' : fec.version.v3.F2.Record,
            'F24' : fec.version.v3.F24.Record,
            'F3' : fec.version.v3.F3.Record,
            'F3P' : fec.version.v3.F3P.Record,
            'F3P31' : fec.version.v3.F3P31.Record,
            'F3PS' : fec.version.v3.F3PS.Record,
            'F3S' : fec.version.v3.F3S.Record,
            'F3X' : fec.version.v3.F3X.Record,
            'F3Z' : fec.version.v3.F3Z.Record,
            'F4' : fec.version.v3.F4.Record,
            'F5' : fec.version.v3.F5.Record,
            'F56' : fec.version.v3.F56.Record,
            'F57' : fec.version.v3.F57.Record,
            'F6' : fec.version.v3.F6.Record,
            'F65' : fec.version.v3.F65.Record,
            'F7' : fec.version.v3.F7.Record,
            'F76' : fec.version.v3.F76.Record,
            'F8' : fec.version.v3.F8.Record,
            'F82' : fec.version.v3.F82.Record,
            'F83' : fec.version.v3.F83.Record,
            'F99' : fec.version.v3.F99.Record,
            'HRD' : fec.version.v3.HRD.Record,
            'SA' : fec.version.v3.SA.Record,
            'SB' : fec.version.v3.SB.Record,
            'SC' : fec.version.v3.SC.Record,
            'SC1' : fec.version.v3.SC1.Record,
            'SC2' : fec.version.v3.SC2.Record,
            'SD' : fec.version.v3.SD.Record,
            'SE' : fec.version.v3.SE.Record,
            'SF' : fec.version.v3.SF.Record,
            'SH1' : fec.version.v3.SH1.Record,
            'SH2' : fec.version.v3.SH2.Record,
            'SH3' : fec.version.v3.SH3.Record,
            'SH4' : fec.version.v3.SH4.Record,
            'SI' : fec.version.v3.SI.Record,
            'TEXT' : fec.version.v3.TEXT.Record,
        }
