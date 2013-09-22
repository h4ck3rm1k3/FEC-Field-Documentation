class VersionsBase:

    def lookup(self,version):
        version  = version.replace(".00","")
        version = "v" + version
        version  = version.replace("\"","")
        #        version  = version.replace(".","_")
        if version in  self.versions:
            factory =self.versions[version]
            return factory()
        else:
            raise Exception("version %s not in %s " % (version,self.versions))
        
