import csv
import re
fec_fields = csv.reader(open('e-filing headers all versions.csv'), delimiter=',')

seen={}

def emit(field,number,number2,number3, name):
    #print ("\t\tOUTPUT:input'%s'\tnumber'%s'\tnumber2'%s'\tnumber3'%s'\tname '%s'" % (field,number,number2,number3, name))

    
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
        seen[name]=1
        return

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

    seen[name]=1

def proc(field):
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
        return emit(field,number,number2,number3, name)


    # 23-D 3 YESNO (PERFECTED INTEREST?)
    match = re.match(r'(\d+\-[A-F\d]+\s\d)\s(TYPENAME)\s\(([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,ftype,name) = items
        return emit(field,number,number2,number3, name)


    #21-D.1 DESC (Collateral)
    match = re.match(r'(\d+\-[A-F]\.\d)\s(TYPENAME)\s\(([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,ftype,name) = items
        return emit(field,number,number2,number3, name)

    #15-A1.YES/NO (Loan Restructured)
    match = re.match(r'(\d+\-[A-F\d]+)\.?\s*(TYPENAME)\s\(([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,ftype,name) = items
        return emit(field,number,number2,number3, name)
    
    # 1-A 
    match = re.match(r'(\d+\-[A-F])\s(TYPENAME)\s\(([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,ftype,name) = items
        return emit(field,number,number2,number3, name)

    #16-D. YESNO (effort made by creditor to collect...
    match = re.match(r'(\d+\-[A-F])\.\s(TYPENAME)\s\(([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,ftype,name) = items
        return emit(field,number,number2,number3, name)

    match = re.match(r'(\d+\-[A-F])\.\s(TYPENAME)\s\(([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,ftype,name) = items
        return emit(field,number,number2,number3, name)

    #21-11. Y DATE (PLANNED FOR TERMINATION RPT)
    match = re.match(r'(\d+\-\d+)\.?\s(TYPENAME)\s\(([A-Za-z].+)\)', field)
    if (match):
        items = match.groups()
        (number,ftype,name) = items
        return emit(field,number,number2,number3, name)

    # 20-11 YESNO (Is the cmte terminating activities)
    match = re.match(r'(\d+\-\d+)\.?\s(TYPENAME)\s\(([A-Za-z].+)\)', field)
    if (match):
        items = match.groups()
        (number,ftype,name) = items
        return emit(field,number,number2,number3, name)

    match = re.match(r'(\d+)\-(TYPENAME)\s\(([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,ftype,name) = items
        return emit(field,number,number2,number3, name)

    #20-6.(b) fdsf
    #                  111111-11111.(
    match = re.match(r'(\d+)\-(\d+)\.\([a-z]\)\s([A-Za-z].+)$', field)
    if (match):
        items = match.groups()
        (number,number2,name) = items
        return emit(field,number,number2,number3, name)

    # '61-6.(a) 19 -- (YEAR)
    #                  11    - 11  . (a )  11     -   (YEAR)   
    match = re.match(r'(\d+)\-(\d+\.\(a\)\s\d+)\s\-\-\s*\((YEAR)\)', field)
    if (match):
        items = match.groups()
        (number,number2,name) = items
        return emit(field,number,number2,number3, name)


    # 56-6(a) 19 --year
    #                  11    - 11  (a )  11     -   (YEAR)   
    match = re.match(r'(\d+)\-(\d+\(a\)\s\d+)\s\-\-\s*(year)', field)
    if (match):
        items = match.groups()
        (number,number2,name) = items
        return emit(field,number,number2,number3, name)

    #                  222222-_    3933
    match = re.match(r'(\d+)\-_\s([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,name) = items
        return emit(field,number,number2,"", name)

    #                  111111111111    2222222222222   AAAAA
    match = re.match(r'(\d+\-\(a\))\s+(\d+\(a\)iii)\s([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        #print(items)
        (number,number2,name) = items
        return emit(field,number,number2,number3, name)

    #'9-(b) 11(b) 
    match = re.match(r'(\d+\-\([a-z][a-z]?\))\s+(\d+\([a-z]\))\s([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        #print(items)
        (number,number2,name) = items
        return emit(field,number,number2,number3, name)

        #'88-9. a) BANK NAME
    match = re.match(r'\s*(\d+)\-([\dA-B]+\. [ab])\)\s+([A-Za-z].+)$', field)
    if (match):
        items = match.groups()
        (number,number2,name) = items
        return emit(field,number,number2,number3, name)

    #                     103112-122331   blahs
    match = re.match(r'\s*(\d+)\-([\dA-B]+)\.\s+([A-Za-z].+)$', field)
    if (match):
        items = match.groups()
        (number,number2,name) = items
        return emit(field,number,number2,number3, name)

        #'14-12a. DATE REACHED 100%
        #9-1b. Unitemized Receipts From Persons
    match = re.match(r'(\d+)\-(\d+)[abc]\. ([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,number2,name) = items
        return emit(field,number,number2,number3, name)

    #              111111-1111BALDDSSS
    match = re.match(r'(\d+)\-(\d+)([A-Za-z].+)$', field)
    if (match):
        items = match.groups()
        (number,number2,name) = items
        return emit(field,number,number2,number3, name)

    #              111111-11111 AAAAAAAAA
    match = re.match(r'(\d+)\-(\d+)\s([A-Za-z].+)$', field)
    if (match):
        items = match.groups()
        (number,number2,name) = items
        return emit(field,number,number2,number3, name)

    #                     103112-122331.   233333)   blahs
    match = re.match(r'\s*(\d+)\-(\d+)\.\s*([\d\w]+)\)\s*([A-Za-z].+)$', field)
    if (match):
        items = match.groups()
        (number,number2,number3,name) = items
        return emit(field,number,number2,number3, name)

    #                  11111-111111.   BLAHS
    match = re.match(r'\s*(\d+)\-([\da-bA-B]+)\.\s*([A-Za-z].+)', field) # could have a newline so no $
    if (match):
        items = match.groups()
        (number,number2,name) = items
        return emit(field,number,number2,"", name)

    #                  11111-. 111111.   BLAHS
    match = re.match(r'\s*(\d+)\-\.\s(\d+)\.\s*([A-Za-z].+)', field) # could have a newline so no $
    if (match):
        items = match.groups()
        (number,number2,name) = items
        return emit(field,number,number2,"", name)

    #7-II) a. IND/NAME (EVENT)
    match = re.match(r'\s*(\d+)\-([IVX]+\)\s[ab]\.)\s+([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,number2,name) = items
        return emit(field,number,number2,"", name)

                      #13-II) c. IND/NAME (EVENT)
    match = re.match(r'(\d+)\-([IVX]+\))\sc\.\s(IND\/NAME)\s\(([A-Za-z].+)\)', field)
    if (match):
        items = match.groups()
        (number,number2,typename,name) = items
        return emit(field,number,number2,"", name)

    #7-II) TOT DIRECT FUNDRAISING AMOUNT
    match = re.match(r'\s*(\d+)\-([IVX]+\))\s+([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,number2,name) = items
        return emit(field,number,number2,"", name)

    #                     222222-III             3933
    match = re.match(r'\s*(\d+)\-([IVX]+)\s([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,number2,name) = items
        return emit(field,number,number2,"", name)

    # 30-11(a)i Itemized
    match = re.match(r'\s*(\d+)\-(\d+)(\([\d\w\s\.]+\)(?:i|ii|iii))\s([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,number2,number3,name) = items
        return emit(field,number,number2,number3, name)


    #                     122222-1111     (233d222.223).       NNNNN
    match = re.match(r'\s*(\d+)\-(\d+)\s*\(([\d\w\s\.]+)\)\.?\s*([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,number2,number3,name) = items
        return emit(field,number,number2,number3, name)

    #                  11111-(111ss333333).      BBBB
    match = re.match(r'\s*(\d+)\-\(([\d\w]+)\)\.?\s*([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,number2,name) = items
        return emit(field,number,number2,number3, name)


    #                  11111-(111ss333333) 12.      BBBB
    match = re.match(r'\s*(\d+)\-(\([a-z]+\)\s\d+)\.?\s*([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,number2,name) = items
        return emit(field,number,number2,number3, name)

    match = re.match(r'\s*(\d+\-[A-F]\.)\s([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,name) = items
        return emit(field,number,number2,number3, name)

    match = re.match(r'\s*(\d+\-[A-F]\d?)\s([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,name) = items
        return emit(field,number,number2,number3, name)

    # 21-D 1 DESC (COLLATERAL
    match = re.match(r'\s*(\d+\-[A-F]\s\d+)\s([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,name) = items
        return emit(field,number,number2,number3, name)


    # '17-B.1. CREDIT AMOUNT THIS DRAW' name 'B.1. CREDIT AMOUNT THIS DRAW'
    match = re.match(r'(\d+\-\w\.\d\.)\s([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,name) = items
        return emit(field,number,number2,number3, name)


    #                 
    match = re.match(r'(\d+)\-(\w\.\d+)\s([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,number2,name) = items
        return emit(field,number,number2,number3, name)

        # 120-G. B
    match = re.match(r'(\d+)\-([A-Z])\.\s*([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,number2,name) = items
        return emit(field,number,number2,number3, name)

        # 120-G B

    match = re.match(r'(\d+)\-([A-Z]|EF)\s([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,number2,name) = items
        return emit(field,number,number2,number3, name)
        

    #'6-I) ADMIN/VOTER DRIVE
    match = re.match(r'\s*(\d+\-[I]\)\s)([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,name) = items
        return emit(field,number,number2,number3, name)

   #                 111111-BLHA
    match = re.match(r'\s*(\d+)\-([A-Za-z].+)', field)
    if (match):
        items = match.groups()
        (number,name) = items
        return emit(field,number,number2,number3, name)

    print "unmatched '%s'" % field


for fieldlist in fec_fields:    
#    print fieldlist
    version = fieldlist.pop(0)
    key     = fieldlist.pop(0)
    #print ("\n\nLine\t%s\t%s\n" % (version , key))

    for field in fieldlist :
        field = field.strip()
        proc(field)
print "REPORT"
print "\n".join(sorted(seen.keys()))
