from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'ENTITY TYPE', 'number': '3'},
            {'name': 'ORGANIZATION NAME', 'number': '4'},
            {'name': 'INDIVIDUAL LAST NAME', 'number': '5'},
            {'name': 'INDIVIDUAL FIRST NAME', 'number': '6'},
            {'name': 'INDIVIDUAL MIDDLE NAME', 'number': '7'},
            {'name': 'INDIVIDUAL PREFIX', 'number': '8'},
            {'name': 'INDIVIDUAL SUFFIX', 'number': '9'},
            {'name': 'CHANGE OF ADDRESS', 'number': '10'},
            {'name': 'STREET 1', 'number': '11'},
            {'name': 'STREET 2', 'number': '12'},
            {'name': 'CITY', 'number': '13'},
            {'name': 'STATE', 'number': '14'},
            {'name': 'ZIP', 'number': '15'},
            {'name': 'INDIVIDUAL EMPLOYER', 'number': '16'},
            {'name': 'INDIVIDUAL OCCUPATION', 'number': '17'},
            {'name': 'COVERAGE FROM DATE', 'number': '18'},
            {'name': 'COVERAGE THROUGH DATE', 'number': '19'},
            {'name': 'DATE OF PUBLIC DISTRIBUTION', 'number': '20'},
            {'name': 'COMMUNICATION TITLE', 'number': '21'},
            {'name': 'FILER CODE', 'number': '22'},
            {'name': 'FILER CODE DESCRIPTION', 'number': '23'},
            {'name': 'SEGREGATED BANK ACCOUNT', 'number': '24'},
            {'name': 'CUSTODIAN LAST NAME', 'number': '25'},
            {'name': 'CUSTODIAN FIRST NAME', 'number': '26'},
            {'name': 'CUSTODIAN MIDDLE NAME', 'number': '27'},
            {'name': 'CUSTODIAN PREFIX', 'number': '28'},
            {'name': 'CUSTODIAN SUFFIX', 'number': '29'},
            {'name': 'CUSTODIAN STREET 1', 'number': '30'},
            {'name': 'CUSTODIAN STREET 2', 'number': '31'},
            {'name': 'CUSTODIAN CITY', 'number': '32'},
            {'name': 'CUSTODIAN STATE', 'number': '33'},
            {'name': 'CUSTODIAN ZIP', 'number': '34'},
            {'name': 'CUSTODIAN EMPLOYER', 'number': '35'},
            {'name': 'CUSTODIAN OCCUPATION', 'number': '36'},
            {'name': 'TOTAL DONATIONS THIS STATEMENT', 'number': '37-9.'},
            {'name': 'TOTAL DISB./OBLIG. THIS STATEMENT', 'number': '38-10.'},
            {'name': 'PERSON COMPLETING LAST NAME', 'number': '39'},
            {'name': 'PERSON COMPLETING FIRST NAME', 'number': '40'},
            {'name': 'PERSON COMPLETING MIDDLE NAME', 'number': '41'},
            {'name': 'PERSON COMPLETING PREFIX', 'number': '42'},
            {'name': 'PERSON COMPLETING SUFFIX', 'number': '43'},
            {'name': 'DATE SIGNED', 'number': '44'},
    ]
        self.fields_names = self.hash_names(self.fields)
