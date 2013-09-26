
#'v1': <class fec.version.v1.Version at 0x123bd50>, 
#'v2': <class fec.version.v2.Version at 0x1261120>, 
#'v3': <class fec.version.v3.Version at 0x12bd4c8>, 
#'v5.0': <class fec.version.v5_0.Version at 0x131f1f0>, 
#'v5.1': <class fec.version.v5_1.Version at 0x1339e20>, 
#'v5.2': <class fec.version.v5_2.Version at 0x13a2a78>} 
#'v5.3': <class fec.version.v5_3.Version at 0x1411600>, 
#'v6.1': <class fec.version.v6_1.Version at 0x1448120>, 
#'v6.2': <class fec.version.v6_2.Version at 0x149cbb0>, 
#'v6.3': <class fec.version.v6_3.Version at 0x1507668>, 
#'v6.4': <class fec.version.v6_4.Version at 0x1528f58>, 
#'v7.0': <class fec.version.v7_0.Version at 0x15936d0>, 
#'v8.0': <class fec.version.v8_0.Version at 0x15ead50>, 

class VersionsBase:
    def __init__(self):
        pass 
    def lookup(self,version):
        orginal_version=version

        if version == "5.00":
            return self.versions["v5.0"]()
        elif version == "5.10":
            return self.versions["v5.1"]()
        elif version == "5.20":
            return self.versions["v5.2"]()
        elif version == "5.30":
            return self.versions["v5.3"]()
        elif version == "v3.0":
            return self.versions["v3"]()
        elif version == "3.0":
            return self.versions["v3"]()
        else:
            version  = version.replace(".00","")
            version = "v" + version
            version  = version.replace("\"","")
            if version in  self.versions:
                factory =self.versions[version]
                return factory()
            else:
                raise Exception("version '%s'/'%s' not in %s " % (orginal_version,version,sorted(self.versions.keys)))
        
