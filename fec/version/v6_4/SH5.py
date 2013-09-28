import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'TRANSACTION ID NUMBER', 'number': '3'},
            {'name': 'ACCOUNT NAME', 'number': '4'},
            {'name': 'RECEIPT DATE', 'number': '5'},
            {'name': 'TOTAL AMOUNT TRANSFERRED', 'number': '6'},
            {'name': 'VOTER REGISTRATION AMOUNT', 'number': '7'},
            {'name': 'VOTER ID AMOUNT', 'number': '8'},
            {'name': 'GOTV AMOUNT', 'number': '9'},
            {'name': 'GENERIC CAMPAIGN AMOUNT', 'number': '10'},
    ]
        self.fields_names = self.hash_names(self.fields)
