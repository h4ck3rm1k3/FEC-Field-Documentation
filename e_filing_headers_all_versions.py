import csv
import re
import os
import traceback
import posixpath as path
fec_fields = csv.reader(open('e-filing headers all versions.csv'), delimiter=',')

seen = {}

def save(version,key,field,number,name):

    item = {'name':name, 'number' : number}

    if len(seen[version][key]) ==0 :
        
        seen[version][key]=[item]
    else:
        seen[version][key].append(item)

def emit(version,key,field,number,name):
    #print ("        OUTPUT:input'%s'    number'%s'    number2'%s'    number3'%s'    name '%s'" % (field,number,name))
   
    if name == 'LLINOIS':
        print "bad match  field:'%s' name '%s'"  %(field,name)
        raise Exception()

    if re.match(r'[I]\)\s',name):
        print "bad match  field:'%s' name '%s'"  %(field,name)
        raise Exception()

    if re.match(r'(i|ii|iii)\s',name):
        print "bad match  field:'%s' name '%s'"  %(field,name)
        raise Exception()
  
    if re.match(r'[YN] (if|IF|If)',name):
        return save (version,key,field,number,name)


    if re.match(r'[acb]\)\s',name):
        print "bad match  field:'%s' name '%s'"  %(field,name)
        raise Exception()

    if re.match(r'[abc]\.\s',name):
        print "bad match  field:'%s' name '%s'"  %(field,name)
        raise Exception()

    if re.match(r'[A-Z]\.?\s',name):
        print "bad match  field:'%s' name '%s'"  %(field,name)
        raise Exception()

    if re.match(r'[A-Z]\d\.?\s',name):
        print "bad match  field:'%s' name '%s'"  %(field,name)
        raise Exception()

    if re.match(r'YESNO',name):
        print "bad match  field:'%s' name '%s'"  %(field,name)
        raise Exception()

    if re.match(r'YES\/NO',name):
        print "bad match  field:'%s' name '%s'"  %(field,name)
        raise Exception()

    if re.match(r'[A-E]\)',name):
        print "bad match  field:'%s' name '%s'"  %(field,name)
        raise Exception()

    if re.match(r'[A-E]\.',name):
        print "bad match  field:'%s' name '%s'"  %(field,name)
        raise Exception()

    return save (version,key,field,number,name)
    

def proc(version,key,field):
    if (field == ""):
        return

    if (field == "-"):
        return

    if field.find("-") <= 0:
        print ("skipping %s" % field)
        #continue

    number=""
    number2=""
    number3=""

    match = re.search(r'(.+)\s?(IND\/NAME|YES\/NO|YESNO|Y DATE|DATE|DESC|N DESC|Y DESC)\s\(([A-Za-z\-].+)\)', field)
    if (match):
        items = match.groups()
        (number,ftype,name) = items
        field=field.replace(ftype,"TYPENAME")
        return emit(version,key,field,number,name)


    # 23-D 3 YESNO (PERFECTED INTEREST?)
    match = re.match(r'(\d+\-[A-F\d]+\s\d)\s(TYPENAME)\s\(([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,ftype,name) = items
        return emit(version,key,field,number,name)


    #21-D.1 DESC (Collateral)
    match = re.match(r'(\d+\-[A-F]\.\d)\s(TYPENAME)\s\(([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,ftype,name) = items
        return emit(version,key,field,number,name)

    #15-A1.YES/NO (Loan Restructured)
    match = re.match(r'(\d+\-[A-F\d]+)\.?\s*(TYPENAME)\s\(([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,ftype,name) = items
        return emit(version,key,field,number,name)
    
    # 1-A 
    match = re.match(r'(\d+\-[A-F])\s(TYPENAME)\s\(([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,ftype,name) = items
        return emit(version,key,field,number,name)

    #16-D. YESNO (effort made by creditor to collect...
    match = re.match(r'(\d+\-[A-F])\.\s(TYPENAME)\s\(([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,ftype,name) = items
        return emit(version,key,field,number,name)

    match = re.match(r'(\d+\-[A-F])\.\s(TYPENAME)\s\(([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,ftype,name) = items
        return emit(version,key,field,number,name)

    #21-11. Y DATE (PLANNED FOR TERMINATION RPT)
    match = re.match(r'(\d+\-\d+)\.?\s(TYPENAME)\s\(([A-Za-z].+)\)', field)
    if (match):
        items = match.groups()
        (number,ftype,name) = items
        return emit(version,key,field,number,name)

    # 20-11 YESNO (Is the cmte terminating activities)
    match = re.match(r'(\d+\-\d+)\.?\s(TYPENAME)\s\(([A-Za-z].+)\)', field)
    if (match):
        items = match.groups()
        (number,ftype,name) = items
        return emit(version,key,field,number,name)

    match = re.match(r'(\d+)\-(TYPENAME)\s\(([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,ftype,name) = items
        return emit(version,key,field,number,name)

    #20-6.(b) fdsf
    #                  111111-11111.(
    match = re.match(r'(\d+\-\d+\.\([a-z]\))\s([A-Za-z].+)$', field)
    if (match):
        items = match.groups()
        (number,name) = items
        return emit(version,key,field,number,name)

    # '61-6.(a) 19 -- (YEAR)
    #                  11    - 11  . (a )  11     -   (YEAR)   
    match = re.match(r'(\d+\-\d+\.\(a\)\s\d+)\s\-\-\s*\((YEAR)\)', field)
    if (match):
        items = match.groups()
        (number,name) = items
        return emit(version,key,field,number,name)


    # 56-6(a) 19 --year
    #                  11    - 11  (a )  11     -   (YEAR)   
    match = re.match(r'(\d+\-\d+\(a\)\s\d+)\s\-\-\s*(year)', field)
    if (match):
        items = match.groups()
        (number,name) = items
        return emit(version,key,field,number,name)

    #                  222222-_    3933
    #27-_ RELATIONSHIP (w/ Above Cmte)
    match = re.match(r'(\d+\-_)\s([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,name) = items
        return emit(version,key,field,number,name)

    #                  111111111111    2222222222222   AAAAA
    match = re.match(r'(\d+\-\(a\)\s+\d+\(a\)iii)\s([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        #print(items)
        (number,name) = items
        return emit(version,key,field,number,name)
    
    # 30-11(a)i Itemized
    match = re.match(r'(\d+\-\d+\(a\)(?:i|ii|iii))\s([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        #print(items)
        (number,name) = items
        return emit(version,key,field,number,name)

    #'9-(b) 11(b) 
    match = re.match(r'(\d+\-\([a-z][a-z]?\)\s+\d+\([a-z]\))\s([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        #print(items)
        (number,name) = items
        return emit(version,key,field,number,name)

        #'88-9. a) BANK NAME
    match = re.match(r'(\d+\-[\dA-B]+\. [ab]\))\s+([A-Za-z].+)$', field)
    if (match):
        items = match.groups()
        (number,name) = items
        return emit(version,key,field,number,name)

    #                     103112-122331   blahs
    match = re.match(r'(\d+\-[\dA-B]+\.)\s+([A-Za-z].+)$', field)
    if (match):
        items = match.groups()
        (number,name) = items
        return emit(version,key,field,number,name)

        #'14-12a. DATE REACHED 100%
        #9-1b. Unitemized Receipts From Persons
    match = re.match(r'(\d+\-\d+[abc]\.) ([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,name) = items
        return emit(version,key,field,number,name)

    # 29-8CASH ON HAND AT CLOSE OF REPORTING PD:
    #              111111-1111BALDDSSS
    match = re.match(r'(\d+\-\d+)([A-Za-z].+)$', field)
    if (match):
        items = match.groups()
        (number,name) = items
        return emit(version,key,field,number,name)

    # 111111-11111 AAAAAAAAA
    # 14-5 TOTAL DONATIONS ACCEPTED
    match = re.match(r'(\d+\-\d+)\s([A-Za-z].+)$', field)
    if (match):
        items = match.groups()
        (number,name) = items
        return emit(version,key,field,number,name)

    #                     103112-122331.   233333)   blahs
    match = re.match(r'\s*(\d+)\-(\d+)\.\s*([\d\w]+)\)\s*([A-Za-z].+)$', field)
    if (match):
        items = match.groups()
        (number,name) = items
        return emit(version,key,field,number,name)

    #                  11111-111111.   BLAHS
    match = re.match(r'(\d+\-[\da-bA-B]+\.)\s*([A-Za-z].+)', field) # could have a newline so no $
    if (match):
        items = match.groups()
        (number,name) = items
        return emit(version,key,field,number,name)

    #                  11111-. 111111.   BLAHS
    match = re.match(r'(\d+\-\.\s\d+\.)\s*([A-Za-z].+)', field) # could have a newline so no $
    if (match):
        items = match.groups()
        (number,name) = items
        return emit(version,key,field,number,name)

    #7-II) a. IND/NAME (EVENT)
    match = re.match(r'(\d+\-[IVX]+\)\s[ab]\.)\s+([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,name) = items
        return emit(version,key,field,number,name)

        #13-II) c. IND/NAME (EVENT)
    match = re.match(r'(\d+\-[IVX]+\)\sc\.)\s(TYPENAME)\s\(([A-Za-z].+)\)', field)
    if (match):
        items = match.groups()
        (number,typename,name) = items
        return emit(version,key,field,number,name)

    #7-II) TOT DIRECT FUNDRAISING AMOUNT
    match = re.match(r'(\d+\-[IVX]+\))\s+([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,name) = items
        return emit(version,key,field,number,name)

    #                     222222-III             3933
    # 13-I CANDIDATE ID NUMBER
    match = re.match(r'(\d+\-[IVX]+)\s([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,name) = items
        return emit(version,key,field,number, name)

    # 30-11(a)i Itemized
    match = re.match(r'(\d+\-\d+\([\d\w\s\.]+\)?:i|ii|iii)\s([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,name) = items
        return emit(version,key,field,number,name)


    #                     122222-1111     (233d222.223).       NNNNN
    # 34-5 (e). ORGANIZATION TYPE
    # 30-11(a)i Itemized
    match = re.match(r'(\d+\-\d+\s*\([\d\w\s\.]+\)[\.i])\s([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,name) = items
        return emit(version,key,field,number,name)

    match = re.match(r'(\d+\-\d+\s*\([\d\w\s\.]+\))\s([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,name) = items
        return emit(version,key,field,number,name)

    # 11111-(111ss333333).      BBBB
    # 24-(6a) Total Contributions (NO Loans)
    match = re.match(r'(\d+\-\([\d\w]+\)\.?)\s*([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,name) = items
        return emit(version,key,field,number,name)


    #                  11111-(111ss333333) 12.      BBBB
    match = re.match(r'\s*(\d+\-\([a-z]+\)\s\d+\.?)\s*([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,name) = items
        return emit(version,key,field,number,name)

    match = re.match(r'\s*(\d+\-[A-F]\.)\s([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,name) = items
        return emit(version,key,field,number,name)

    match = re.match(r'\s*(\d+\-[A-F]\d?)\s([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,name) = items
        return emit(version,key,field,number,name)

    # 21-D 1 DESC (COLLATERAL
    match = re.match(r'\s*(\d+\-[A-F]\s\d+)\s([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,name) = items
        return emit(version,key,field,number,name)


    # '17-B.1. CREDIT AMOUNT THIS DRAW' name 'B.1. CREDIT AMOUNT THIS DRAW'
    match = re.match(r'(\d+\-\w\.\d\.)\s([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,name) = items
        return emit(version,key,field,number,name)


    #                 
    match = re.match(r'(\d+\-\w\.\d+)\s([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,name) = items
        return emit(version,key,field,number,name)

        # 120-G. B
    match = re.match(r'(\d+\-[A-Z]\.)\s*([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,name) = items
        return emit(version,key,field,number,name)

        # 120-G B

    match = re.match(r'(\d+\-(?:[A-Z]|EF))\s([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,name) = items
        return emit(version,key,field,number,name)
        

    #'6-I) ADMIN/VOTER DRIVE
    match = re.match(r'\s*(\d+\-[I]\)\s)([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,name) = items
        return emit(version,key,field,number,name)

   #                 111111-BLHA
    match = re.match(r'\s*(\d+)\-([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,name) = items
        return emit(version,key,field,number,name)


    #55-6(a)Cash on Hand
    match = re.match(r'(\d+\-\d\(a\))([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,name) = items
        return emit(version,key,field,number,name)

    print "unmatched '%s'" % field


for fieldlist in fec_fields:    
#    print fieldlist
    version = fieldlist.pop(0)
    key     = fieldlist.pop(0)
    #print ("\n\nLine    %s    %s\n" % (version , key))
    if version not in seen:
        seen[version] = {}

    if key not in seen[version]:
        seen[version][key] = {}

    for field in fieldlist :
        field = field.strip()
        try :
            proc(version,key, field)
        except Exception as e:
            print field 
            print traceback.format_exc()
            raise e
print "REPORT"

def emit_versions(seen):
    outf = open ("versions.py","w")
    for version in sorted(seen.keys()):
        versiond =         version.replace(".","_")
        outf.write( 'import fec.version.' +versiond + "\n")

    outf.write( "import fechbase\n")

    outf.write( "class Versions(fechbase.VersionsBase):\n")
    outf.write( "    def __init__(self):\n")
    outf.write( "        fechbase.VersionsBase.__init__(self)\n")
    outf.write( "        self.versions = {\n")
    for version in sorted(seen.keys()):    
        versiond =         version.replace(".","_")
        outf.write("            '"+ 
                   version +  
                   "' : "  + 
                   'fec.version.' + 
                   versiond + 
                   ".Version," + 
                "\n" 
               )
    outf.write( "        }\n")


def emit_versions_records(seen):

    for version in sorted(seen.keys()):
        versiond =         version.replace(".","_")
        if not path.exists("fec/version/"+versiond): 
            os.makedirs("fec/version/"+versiond)
        outf = open ("fec/version/"+versiond + "/__init__.py","w")
        for field in sorted(seen[version].keys()):   
            versiond =         version.replace(".","_")
            outf.write( 'import ' + 
                        'fec.version.' + 
                        versiond + "." +
                        field + "\n")
        outf.write("import fechbase\n")
        outf.write("class Version(fechbase.VersionBase):\n")

        outf.write("    def __init__(self):\n")
        outf.write("        fechbase.VersionBase.__init__(self)\n")
        outf.write("        self.records = {\n")
        versiond =         version.replace(".","_")
        for field in sorted(seen[version].keys()):   
            outf.write("            '"+ 
                field +  
                "' : "  + 
                'fec.version.' + 
                versiond + "." +
                field +  ".Records"
                "," + 
                "\n" 
            )
        outf.write( "        }\n")


        outf.write("        self.field_order = [\n")
        versiond =         version.replace(".","_")
        for field in sorted(seen[version].keys()):   
            outf.write("            '%s',\n" % field)            
        outf.write( "        ]\n")

def emit_versions_records_fields(seen):

    for version in sorted(seen.keys()):
        versiond =         version.replace(".","_")
        for record in sorted(seen[version].keys()):   
            if not path.exists("fec/version/"+versiond): 
                os.makedirs("fec/version/"+versiond)
            outf = open ("fec/version/"+versiond + "/" + record + ".py","w")
            outf.write("import fechbase\n")
            outf.write("class Records(fechbase.RecordsBase):\n")
            outf.write("    def __init__(self):\n")
            outf.write("        fechbase.RecordsBase.__init__(self)\n")
            outf.write("        self.fields = [\n")
            for field in seen[version][record]:   
                outf.write(
                    "            "+ 
                    str(field) +  
                    ",\n" 
                )
            outf.write( "    ]\n")

            # hash the fields with a base function
            outf.write("        self.fields_names = self.hash_names(self.fields)\n" )

if not path.exists("fec"): 
    os.makedirs("fec")

if not path.exists("fec/version"): 
    os.makedirs("fec/version")

#outf = open ("fec/__init__.py","w")
#outf.write ("#\n") 

emit_versions(seen)
emit_versions_records(seen)
emit_versions_records_fields(seen)
