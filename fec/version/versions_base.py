class VersionsBase:

    def lookup(self,version):
        orginal_version=version

        if version == "v3.0":
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
        
