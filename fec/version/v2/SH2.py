import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC CMTE ID', 'number': '2'},
            {'name': 'Activity/Event', 'number': '3-'},
            {'name': 'ACTIVITY IS FUNDRAISING', 'number': '4-'},
            {'name': 'ACTIVITY IS EXEMPT', 'number': '5-'},
            {'name': 'ACT DIRECT CAN SUPPORT', 'number': '6-'},
            {'name': 'RATIO CODE (N,R,S)', 'number': '7'},
            {'name': 'FEDERAL PERCENTAGE', 'number': '8'},
            {'name': 'NON-FEDERAL PERCENTAGE', 'number': '9'},
            {'name': 'AMENDED-CD', 'number': '10'},
            {'name': 'TRAN_ID', 'number': '11'},
            {'name': 'ORIG_TRAN_ID', 'number': '12'},
            {'name': 'SUPR_TRAN_ID', 'number': '13'},
    ]
        self.fields_names = self.hash_names(self.fields)
