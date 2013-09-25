from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FEC COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'SEQUENCE NUMBER', 'number': '3'},
            {'name': 'COMMUNICATION TYPE', 'number': '4'},
            {'name': 'COMMUN SPECIFICATION', 'number': '5-TRANS'},
            {'name': 'COMMUNICATION CLASS OR CATEGORY', 'number': '6'},
            {'name': 'OF COMMUNICATION', 'number': '7-'},
            {'name': 'SUPPORT/OPPOSE', 'number': '8'},
            {'name': 'FEC CANDIDATE ID NUMBER', 'number': '9'},
            {'name': 'CANDIDATE NAME', 'number': '10'},
            {'name': 'CAN/OFF', 'number': '11'},
            {'name': 'STATE (OF ELECTION)', 'number': '12'},
            {'name': 'CAN/DIST', 'number': '13'},
            {'name': 'RPTPGI', 'number': '14'},
            {'name': 'Cost of communication', 'number': '15'},
            {'name': 'AMENDED', 'number': '16'},
    ]
        self.fields_names = self.hash_names(self.fields)
