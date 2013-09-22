from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'TRANSACTION ID NUMBER', 'number': '3'},
            {'name': 'ACTIVITY/EVENT NAME', 'number': '4'},
            {'name': 'Direct Fundraising?', 'number': '5-'},
            {'name': 'Direct Candidate Support?', 'number': '6-'},
            {'name': 'RATIO CODE', 'number': '7'},
            {'name': 'FEDERAL PERCENTAGE', 'number': '8'},
            {'name': 'NONFEDERAL PERCENTAGE', 'number': '9'},
    ]
