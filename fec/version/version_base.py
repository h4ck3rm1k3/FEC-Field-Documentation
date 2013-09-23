from fec.version.HDR import HDR

class VersionBase:

      def __init__(self):
            self.record_list=[]

      def parse(self,x):
            fieldtype=x[0]
            if fieldtype == "HDR":
                  self.hdr=HDR(x)
                  self.hdr.emit()
            else:
                  print "Version Base, parse," + str(x)
            
            #raise Exception(x)

      def parse_record(self,fields, record_type):
            self.current_record=self.records[record_type]()
            result = self.current_record.parse(fields)
            self.record_list.append(result)            

      def parse_body(self,fields):
            fields_temp=fields.split(",")
            fields=[]
            for f in fields_temp:
                  f=f.replace('\"',"")
                  fields.append(f)
            record_type=fields[0]

            if record_type == "": 
                  return 

            #hack
            if record_type == "H4":
                  record_type = "SH4"

            if record_type == "H1":
                  record_type = "SH1"

            if record_type == "H2":
                  record_type = "SH2"

            if record_type == "H3":
                  record_type = "SH3"

            if record_type in self.records:                  
                  self.parse_record(fields,record_type)
            else:
                  record_type=record_type[:2]
                  if record_type in self.records:                  
                        self.parse_record(fields,record_type)
                  else:
                        raise Exception("recordtype '%s' not known %s record %s" % (record_type, sorted(self.records.keys()), str(fields) ))
                        #'F3' : fec.version.v1.F3.Records,

      def set_attr_hash(self, attrdict):
            self.record_list=[]
            pass
            #print attrdict
      
            # example
            #{'FEC_Ver_# ': '1.02', 
            #'NameDelim ': '^',             
            #'Date_Fmat ': 'CCYYMMDD', 'SA11B     ': '00002', 'SA11C     ': '00011', 'DEC/NODEC ': 'DEC', 'SB20A     ': '00002', 'SB17      ': '00139', 'SA11A1    ': '00263', 'Committee ': 'Christopher Shays for Congress Committee', 'FEC_IDnum ': 'C00215699', 'SA15      ': '00003', 'Form_Name ': 'F3N', 'Control_# ': 'M042228N'}
            
