import csv
import re
fec_fields = csv.reader(open('e-filing headers all versions.csv'), delimiter=',')

for fieldlist in fec_fields:    
    version = fieldlist.pop(0)
    key     = fieldlist.pop(0)
    print ("\n\nLine\t%s\t%s\n" % (version , key))

    for field in fieldlist :
        field = field.strip()

        if (field == ""):
            continue

#        print "input: %s" % field

        if field.find("-") <= 0:
            print ("skipping %s" % name)
            #continue

        match = re.match(r'\s*(\w+)\-(.+)', field)
        if (match):
            items = match.groups()
#            print ("items: %s" % str(items))
            (number,name) = items
        else:
            number=""
            name = field

        match = re.match(r'\s*(\w+)\.(.+)', name)
        if (match):
            items = match.groups()
#            print "items2: %s" % items
            (number2,name) = items
        else:
            number2=""


        match = re.match(r'\s*(\w+)\)(.+)', name)
        if (match):
            items = match.groups()
#            print ("items3: %s" % str(items))
            (number3,name) = items
        else:
            number3=""

            # try again
        match = re.match(r'\s*\((\w+)\)(.+)', name)
        if (match):
            items = match.groups()
#            print ("items3: %s" % str(items))
            (number3,name) = items
        else:
            number3=""

        print ("\t\tOUTPUT:input'%s'\tnumber'%s'\tnumber2'%s'\tnumber3'%s'\tname '%s'" % (field,number,number2,number3, name))
