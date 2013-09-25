from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC CMTE ID', 'number': '2'},
            {'name': 'IND/ORG/CORP NAME', 'number': '3'},
            {'name': 'STREET 1', 'number': '4'},
            {'name': 'STREET 2', 'number': '5'},
            {'name': 'CITY', 'number': '6'},
            {'name': 'STATE', 'number': '7'},
            {'name': 'ZIP', 'number': '8'},
            {'name': 'CHG OF ADDRESS', 'number': '9'},
            {'name': 'EMPLOYER', 'number': '10'},
            {'name': 'OCCUPATION', 'number': '11'},
            {'name': 'BEGINNING COVERAGE DATE', 'number': '12'},
            {'name': 'ENDING COVERAGE DATE', 'number': '13'},
            {'name': 'DATE OF PUBLIC DISTRIBUTION', 'number': '14'},
            {'name': 'COMMUNICATION TITLE', 'number': '15'},
            {'name': 'QUALIFIED NON-PROFIT', 'number': '16'},
            {'name': 'SEGREGATED BANK ACCOUNT', 'number': '17'},
            {'name': 'Custodian', 'number': '18-'},
            {'name': 'STREET 1', 'number': '19'},
            {'name': 'STREET 2', 'number': '20'},
            {'name': 'CITY', 'number': '21'},
            {'name': 'STATE', 'number': '22'},
            {'name': 'ZIP', 'number': '23'},
            {'name': 'EMPLOYER', 'number': '24'},
            {'name': 'OCCUPATION', 'number': '25'},
            {'name': 'TOTAL DONATIONS THIS STATEMENT', 'number': '26-9.'},
            {'name': 'TOTAL DISB./OBLIG. THIS STATEMENT', 'number': '27-10.'},
            {'name': 'NAME PERSON COMPLETING REPORT', 'number': '28'},
            {'name': 'Signed', 'number': '29-'},
    ]
        self.fields_names = self.hash_names(self.fields)
