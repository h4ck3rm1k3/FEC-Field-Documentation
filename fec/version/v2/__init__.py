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
import fechbase
class Version(fechbase.VersionBase):
    def __init__(self):
        fechbase.VersionBase.__init__(self)
        self.records = {
            'F1' : fec.version.v2.F1.Records,
            'F1M' : fec.version.v2.F1M.Records,
            'F2' : fec.version.v2.F2.Records,
            'F3' : fec.version.v2.F3.Records,
            'F3P' : fec.version.v2.F3P.Records,
            'F3P31' : fec.version.v2.F3P31.Records,
            'F3X' : fec.version.v2.F3X.Records,
            'F3Z' : fec.version.v2.F3Z.Records,
            'F4' : fec.version.v2.F4.Records,
            'F5' : fec.version.v2.F5.Records,
            'F56' : fec.version.v2.F56.Records,
            'F57' : fec.version.v2.F57.Records,
            'F6' : fec.version.v2.F6.Records,
            'F65' : fec.version.v2.F65.Records,
            'F7' : fec.version.v2.F7.Records,
            'F76' : fec.version.v2.F76.Records,
            'F8' : fec.version.v2.F8.Records,
            'F82' : fec.version.v2.F82.Records,
            'F83' : fec.version.v2.F83.Records,
            'SA' : fec.version.v2.SA.Records,
            'SB' : fec.version.v2.SB.Records,
            'SC' : fec.version.v2.SC.Records,
            'SC1' : fec.version.v2.SC1.Records,
            'SC2' : fec.version.v2.SC2.Records,
            'SD' : fec.version.v2.SD.Records,
            'SE' : fec.version.v2.SE.Records,
            'SF' : fec.version.v2.SF.Records,
            'SH1' : fec.version.v2.SH1.Records,
            'SH2' : fec.version.v2.SH2.Records,
            'SH3' : fec.version.v2.SH3.Records,
            'SH4' : fec.version.v2.SH4.Records,
            'SI' : fec.version.v2.SI.Records,
        }
        self.field_order = [
            'F1',
            'F1M',
            'F2',
            'F3',
            'F3P',
            'F3P31',
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
            'SI',
        ]
