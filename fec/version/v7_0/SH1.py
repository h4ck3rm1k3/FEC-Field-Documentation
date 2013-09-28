import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'TRANSACTION ID NUMBER', 'number': '3'},
            {'name': 'State and Local Party Committee Presidential-Only Election Year (28% Federal)', 'number': '4'},
            {'name': 'State and Local Party Committee Presidential and Senate Election Year (36% Federal)', 'number': '5'},
            {'name': 'State and Local Party Committee Senate-Only Election Year (21% Federal)', 'number': '6'},
            {'name': 'State and Local Party Committee Non-Presidential and Non-Senate Election Year (15% Federal)', 'number': '7'},
            {'name': 'FLAT MINIMUM FEDERAL PERCENTAGE', 'number': '8'},
            {'name': 'FEDERAL PERCENT', 'number': '9'},
            {'name': 'NONFEDERAL PERCENT', 'number': '10'},
            {'name': 'ADMINISTRATIVE RATIO APPLIES', 'number': '11'},
            {'name': 'GENERIC VOTER DRIVE RATIO APPLIES', 'number': '12'},
            {'name': 'PUBLIC COMMUNICATIONS REFERENCING PARTY ONLY RATIO APPLIES', 'number': '13'},
    ]
        self.fields_names = self.hash_names(self.fields)
