from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC CMTE ID', 'number': '2'},
            {'name': 'Activity/Event', 'number': '3-'},
            {'name': 'Activity Is Direct Fundraising', 'number': '4-'},
            {'name': 'Activity Is Exempt', 'number': '5-'},
            {'name': 'Act. Direct Candidate Support', 'number': '6-'},
            {'name': 'RATIO CODE', 'number': '7'},
            {'name': 'FEDERAL PERCENTAGE', 'number': '8'},
            {'name': 'NON-FEDERAL PERCENTAGE', 'number': '9'},
            {'name': 'AMENDED CD', 'number': '10'},
            {'name': 'TRAN ID', 'number': '11'},
    ]
