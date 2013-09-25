from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC CMTE ID', 'number': '2'},
            {'name': 'BACK-REF TRAN ID', 'number': '3'},
            {'name': 'ACCOUNT NAME', 'number': '4'},
            {'name': 'EVENT NAME', 'number': '5'},
            {'name': 'EVENT TYPE', 'number': '6'},
            {'name': 'Of Receipt', 'number': '7-'},
            {'name': 'AMOUNT TRANSFERRED', 'number': '8'},
            {'name': 'TOTAL AMOUNT TRANSFERRED', 'number': '9'},
            {'name': 'AMENDED CD', 'number': '10'},
            {'name': 'TRAN ID', 'number': '11'},
    ]
        self.fields_names = self.hash_names(self.fields)
