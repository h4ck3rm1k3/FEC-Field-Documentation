import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC CMTE ID', 'number': '2'},
            {'name': 'Activity/Event', 'number': '3-'},
            {'name': 'Activity Is Fundraising', 'number': '4-'},
            {'name': 'Activity Is Exempt', 'number': '5-'},
            {'name': 'Act. Direct Can Support', 'number': '6-'},
            {'name': 'RATIO CODE', 'number': '7'},
            {'name': 'FEDERAL PERCENTAGE', 'number': '8'},
            {'name': 'NON-FEDERAL PERCENTAGE', 'number': '9'},
            {'name': 'AMENDED CD', 'number': '10'},
            {'name': 'TRAN ID', 'number': '11'},
    ]
        self.fields_names = self.hash_names(self.fields)
