from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FEC COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'ACTIVITY/EVENT', 'number': '3-'},
            {'name': 'ACTIVITY/EVENT NUMBER', 'number': '4'},
            {'name': 'ACTIVITY IS FUNDRAISING', 'number': '5-'},
            {'name': 'ACTIVITY IS EXEMPT', 'number': '6-'},
            {'name': 'ACT DIRECT CAN SUPPORT', 'number': '7-'},
            {'name': 'RATIO CODE (N,R,S)', 'number': '8'},
            {'name': 'FEDERAL PERCENTAGE', 'number': '9'},
            {'name': 'NON-FEDERAL PERCENTAGE', 'number': '10'},
            {'name': 'AMENDED', 'number': '11'},
    ]
        self.fields_names = self.hash_names(self.fields)
