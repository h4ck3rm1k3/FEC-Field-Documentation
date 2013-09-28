import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC CMTE ID', 'number': '2'},
            {'name': 'ACCOUNT NAME', 'number': '3'},
            {'name': 'Of Receipt/Transfer In', 'number': '4-'},
            {'name': 'Amount Voter Registration', 'number': '5'},
            {'name': 'Amount Voter ID', 'number': '6'},
            {'name': 'Amount GOTV', 'number': '7'},
            {'name': 'Amount Generic Campaing Activity', 'number': '8'},
            {'name': 'TOTAL AMOUNT TRANSFERRED', 'number': '9'},
            {'name': 'AMENDED CD', 'number': '10'},
            {'name': 'TRAN ID', 'number': '11'},
    ]
        self.fields_names = self.hash_names(self.fields)
