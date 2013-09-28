import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'TRANSACTION ID NUMBER', 'number': '3'},
            {'name': 'BACK REFERENCE TRAN ID', 'number': '4'},
            {'name': 'ACCOUNT NAME', 'number': '5'},
            {'name': 'EVENT TYPE', 'number': '6'},
            {'name': 'EVENT/ACTIVITY ID/NAME', 'number': '7'},
            {'name': 'RECEIPT DATE', 'number': '8'},
            {'name': 'TOTAL AMOUNT TRANSFERRED', 'number': '9'},
            {'name': 'TRANSFERRED AMOUNT', 'number': '10'},
    ]
        self.fields_names = self.hash_names(self.fields)
