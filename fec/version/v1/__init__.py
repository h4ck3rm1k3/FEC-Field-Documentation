import fec.version.v1.F1
import fec.version.v1.F1M
import fec.version.v1.F2
import fec.version.v1.F3
import fec.version.v1.F3P
import fec.version.v1.F3P31
import fec.version.v1.F3X
import fec.version.v1.F3Z
import fec.version.v1.F4
import fec.version.v1.F5
import fec.version.v1.F56
import fec.version.v1.F57
import fec.version.v1.F6
import fec.version.v1.F65
import fec.version.v1.F7
import fec.version.v1.F76
import fec.version.v1.F8
import fec.version.v1.F82
import fec.version.v1.F83
import fec.version.v1.SA
import fec.version.v1.SB
import fec.version.v1.SC
import fec.version.v1.SC1
import fec.version.v1.SD
import fec.version.v1.SE
import fec.version.v1.SF
import fec.version.v1.SH1
import fec.version.v1.SH2
import fec.version.v1.SH3
import fec.version.v1.SH4
import fec.version.v1.SI
from fec.version.version_base import VersionBase
class Version(VersionBase):
    def __init__(self):
        self.records = {
            'F1' : fec.version.v1.F1.Records,
            'F1M' : fec.version.v1.F1M.Records,
            'F2' : fec.version.v1.F2.Records,
            'F3' : fec.version.v1.F3.Records,
            'F3P' : fec.version.v1.F3P.Records,
            'F3P31' : fec.version.v1.F3P31.Records,
            'F3X' : fec.version.v1.F3X.Records,
            'F3Z' : fec.version.v1.F3Z.Records,
            'F4' : fec.version.v1.F4.Records,
            'F5' : fec.version.v1.F5.Records,
            'F56' : fec.version.v1.F56.Records,
            'F57' : fec.version.v1.F57.Records,
            'F6' : fec.version.v1.F6.Records,
            'F65' : fec.version.v1.F65.Records,
            'F7' : fec.version.v1.F7.Records,
            'F76' : fec.version.v1.F76.Records,
            'F8' : fec.version.v1.F8.Records,
            'F82' : fec.version.v1.F82.Records,
            'F83' : fec.version.v1.F83.Records,
            'SA' : fec.version.v1.SA.Records,
            'SB' : fec.version.v1.SB.Records,
            'SC' : fec.version.v1.SC.Records,
            'SC1' : fec.version.v1.SC1.Records,
            'SD' : fec.version.v1.SD.Records,
            'SE' : fec.version.v1.SE.Records,
            'SF' : fec.version.v1.SF.Records,
            'SH1' : fec.version.v1.SH1.Records,
            'SH2' : fec.version.v1.SH2.Records,
            'SH3' : fec.version.v1.SH3.Records,
            'SH4' : fec.version.v1.SH4.Records,
            'SI' : fec.version.v1.SI.Records,
        }
