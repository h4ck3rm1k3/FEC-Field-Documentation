from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC CMTE ID', 'number': '2'},
            {'name': 'OF ACCOUNT', 'number': '3-'},
            {'name': 'OF RECEIPT', 'number': '4-'},
            {'name': 'TOTAL AMOUNT TRANSFERRED', 'number': '5'},
            {'name': 'ADMIN/VOTER DRIVE', 'number': '6-I)'},
            {'name': 'TOT DIRECT FUNDRAISING AMOUNT', 'number': '7-II)'},
            {'name': 'TOT EXEMPT ACTIVITY DIRECT CANDIDATE SUPPORT', 'number': '8-III)'},
            {'name': 'AMENDED-CD', 'number': '9'},
            {'name': 'TRAN_ID', 'number': '10'},
            {'name': 'ORIG_TRAN_ID', 'number': '11'},
            {'name': 'SUPR_TRAN_ID', 'number': '12'},
    ]
        self.fields_names = self.hash_names(self.fields)
