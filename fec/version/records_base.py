class RecordsBase:
    def __init__(self):
        pass
    def hash_names(self, fields):
        names={}
        for f in fields:
            names[f['name']]=f
        return names

    def parse(self,fields,line):

        expected_count=len(self.fields)
        input_count   =len(fields)
        result={}
        result["input"]=line
        result["result"]=[]

        #copy of fields
        fields2=fields

        if not input_count == expected_count :
            #print ("%s != %s" % (expected_count,    input_count))
            result["expected_count"]=expected_count
            result["input_count"]=input_count


            result["attempt"]=[]

            # now just fill out what we can
            for field_descriptor in self.fields:
                if (len(fields2)>0):
                    v = fields2.pop(0)
                    field_descriptor["value"]=v
                else:
                    field_descriptor["value"]="NO VALUE!"

                result["attempt"].append(field_descriptor)

            # now the rest of the fields
            while len(fields2)>0:
                v = fields2.pop(0)
                field_descriptor ={"value": v}
                result["attempt"].append(field_descriptor)

            return result


        # exact match
        # now just fill out what we can
        for field_descriptor in self.fields:
            v = fields2.pop(0)
            field_descriptor["value"]=v
            result["result"].append(field_descriptor)


        return result
