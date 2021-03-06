import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FEC COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'COMMITTEE NAME', 'number': '3'},
            {'name': 'STREET 1', 'number': '4'},
            {'name': 'STREET 2', 'number': '5'},
            {'name': 'CITY', 'number': '6'},
            {'name': 'STATE', 'number': '7'},
            {'name': 'ZIP', 'number': '8'},
            {'name': 'CHG OF ADDRESS', 'number': '9'},
            {'name': 'QUAL/NON-Q', 'number': '10-'},
            {'name': 'INDEMP', 'number': '11'},
            {'name': 'INDOCC', 'number': '12'},
            {'name': 'RPTCODE', 'number': '13'},
            {'name': 'RPTPGI', 'number': '14'},
            {'name': 'OF ELECTION', 'number': '15-'},
            {'name': 'STATE (OF ELECTION)', 'number': '16'},
            {'name': 'COVERAGE FROM', 'number': '17-'},
            {'name': 'COVERAGE TO', 'number': '18-'},
            {'name': 'TOTAL CONTRIBUTION total on page 1', 'number': '19'},
            {'name': 'TOTAL INDEP. EXPEND total on page 1', 'number': '20'},
            {'name': 'PERSON COMPLETING FORM', 'number': '21-'},
            {'name': 'SIGNED', 'number': '22-'},
            {'name': 'NOTARIZED', 'number': '23-'},
            {'name': 'NOTARY COMMISSION EXPIRES', 'number': '24-'},
            {'name': 'NOTARY', 'number': '25-'},
    ]
        self.fields_names = self.hash_names(self.fields)
