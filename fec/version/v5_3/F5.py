from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC CMTE ID', 'number': '2'},
            {'name': 'COMMITTEE NAME', 'number': '3'},
            {'name': 'STREET 1', 'number': '4'},
            {'name': 'STREET 2', 'number': '5'},
            {'name': 'CITY', 'number': '6'},
            {'name': 'STATE', 'number': '7'},
            {'name': 'ZIP', 'number': '8'},
            {'name': 'CHG OF ADDRESS', 'number': '9'},
            {'name': 'Qual/Non Q', 'number': '10-'},
            {'name': 'INDEMP', 'number': '11'},
            {'name': 'INDOCC', 'number': '12'},
            {'name': 'RPTCODE', 'number': '13'},
            {'name': 'SPACE HOLDER', 'number': '14'},
            {'name': 'SPACE HOLDER', 'number': '15'},
            {'name': 'SPACE HOLDER', 'number': '16'},
            {'name': 'Coverage From', 'number': '17-'},
            {'name': 'Coverage To', 'number': '18-'},
            {'name': 'TOTAL CONTRIBUTION', 'number': '19'},
            {'name': 'TOTAL INDEP. EXPEND', 'number': '20'},
            {'name': 'Person Completing Form', 'number': '21-'},
            {'name': 'Signed', 'number': '22-'},
            {'name': 'SPACE HOLDER', 'number': '23'},
            {'name': 'SPACE HOLDER', 'number': '24'},
            {'name': 'SPACE HOLDER', 'number': '25'},
            {'name': 'HOUR 48HOUR CODE', 'number': '26-24'},
    ]
        self.fields_names = self.hash_names(self.fields)
