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
                raise Exception("version '%s'/'%s' not in %s " % (orginal_version,version,self.versions))
        
