class RecordsBase:
    def parse(self,fields):

        expected_count=len(self.fields)
        input_count   =len(fields)
        result={}

        if not input_count == expected_count :
            #print ("%s != %s" % (expected_count,    input_count))
            result["expected_count"]=expected_count
            result["input_count"]=input_count
            result["field_description"]=self.fields
            result["field_inputs"]=fields
            return result
            #raise Exception(("%s != %s" % (expected_count,    input_count)))

        for field_descriptor in self.fields:
            value = fields.pop(0)
            #            field_descriptor["value"]=value
            #field_descriptor["value"]=value
            result[field_descriptor["name"]]=value
        
        if (len(fields)> 0):
            print("leftovers %s" % fields)
            result["leftovers"]=fields
            #raise Exception(fields)

        return result
