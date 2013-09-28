import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'TRANSACTION ID NUMBER', 'number': '3'},
            {'name': 'ACTIVITY/EVENT NAME', 'number': '4'},
            {'name': 'Direct Fundraising?', 'number': '5-'},
            {'name': 'Direct Candidate Support?', 'number': '6-'},
            {'name': 'RATIO CODE', 'number': '7'},
            {'name': 'FEDERAL PERCENTAGE', 'number': '8'},
            {'name': 'NON-FEDERAL PERCENTAGE', 'number': '9'},
    ]
        self.fields_names = self.hash_names(self.fields)
