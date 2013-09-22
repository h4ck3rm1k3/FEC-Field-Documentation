import fec.version.v2.F1
import fec.version.v2.F1M
import fec.version.v2.F2
import fec.version.v2.F3
import fec.version.v2.F3P
import fec.version.v2.F3P31
import fec.version.v2.F3X
import fec.version.v2.F3Z
import fec.version.v2.F4
import fec.version.v2.F5
import fec.version.v2.F56
import fec.version.v2.F57
import fec.version.v2.F6
import fec.version.v2.F65
import fec.version.v2.F7
import fec.version.v2.F76
import fec.version.v2.F8
import fec.version.v2.F82
import fec.version.v2.F83
import fec.version.v2.SA
import fec.version.v2.SB
import fec.version.v2.SC
import fec.version.v2.SC1
import fec.version.v2.SC2
import fec.version.v2.SD
import fec.version.v2.SE
import fec.version.v2.SF
import fec.version.v2.SH1
import fec.version.v2.SH2
import fec.version.v2.SH3
import fec.version.v2.SH4
import fec.version.v2.SI
from fec.version.version_base import VersionBase
class Version(VersionBase):
    def __init__(self):
        self.records = {
            'F1' : fec.version.v2.F1.Record,
            'F1M' : fec.version.v2.F1M.Record,
            'F2' : fec.version.v2.F2.Record,
            'F3' : fec.version.v2.F3.Record,
            'F3P' : fec.version.v2.F3P.Record,
            'F3P31' : fec.version.v2.F3P31.Record,
            'F3X' : fec.version.v2.F3X.Record,
            'F3Z' : fec.version.v2.F3Z.Record,
            'F4' : fec.version.v2.F4.Record,
            'F5' : fec.version.v2.F5.Record,
            'F56' : fec.version.v2.F56.Record,
            'F57' : fec.version.v2.F57.Record,
            'F6' : fec.version.v2.F6.Record,
            'F65' : fec.version.v2.F65.Record,
            'F7' : fec.version.v2.F7.Record,
            'F76' : fec.version.v2.F76.Record,
            'F8' : fec.version.v2.F8.Record,
            'F82' : fec.version.v2.F82.Record,
            'F83' : fec.version.v2.F83.Record,
            'SA' : fec.version.v2.SA.Record,
            'SB' : fec.version.v2.SB.Record,
            'SC' : fec.version.v2.SC.Record,
            'SC1' : fec.version.v2.SC1.Record,
            'SC2' : fec.version.v2.SC2.Record,
            'SD' : fec.version.v2.SD.Record,
            'SE' : fec.version.v2.SE.Record,
            'SF' : fec.version.v2.SF.Record,
            'SH1' : fec.version.v2.SH1.Record,
            'SH2' : fec.version.v2.SH2.Record,
            'SH3' : fec.version.v2.SH3.Record,
            'SH4' : fec.version.v2.SH4.Record,
            'SI' : fec.version.v2.SI.Record,
        }
