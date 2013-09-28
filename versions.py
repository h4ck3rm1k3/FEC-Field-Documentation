import fec.version.v1
import fec.version.v2
import fec.version.v3
import fec.version.v5_0
import fec.version.v5_1
import fec.version.v5_2
import fec.version.v5_3
import fec.version.v6_1
import fec.version.v6_2
import fec.version.v6_3
import fec.version.v6_4
import fec.version.v7_0
import fec.version.v8_0
import fechbase
class Versions(fechbase.VersionsBase):
    def __init__(self):
        fechbase.VersionsBase.__init__(self)
        self.versions = {
            'v1' : fec.version.v1.Version,
            'v2' : fec.version.v2.Version,
            'v3' : fec.version.v3.Version,
            'v5.0' : fec.version.v5_0.Version,
            'v5.1' : fec.version.v5_1.Version,
            'v5.2' : fec.version.v5_2.Version,
            'v5.3' : fec.version.v5_3.Version,
            'v6.1' : fec.version.v6_1.Version,
            'v6.2' : fec.version.v6_2.Version,
            'v6.3' : fec.version.v6_3.Version,
            'v6.4' : fec.version.v6_4.Version,
            'v7.0' : fec.version.v7_0.Version,
            'v8.0' : fec.version.v8_0.Version,
        }
