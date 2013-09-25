from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FEC COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'RECIPIENT', 'number': '3-'},
            {'name': 'STREET 1', 'number': '4'},
            {'name': 'STREET 2', 'number': '5'},
            {'name': 'CITY', 'number': '6'},
            {'name': 'STATE', 'number': '7'},
            {'name': 'ZIP', 'number': '8'},
            {'name': 'DISBURSCODE', 'number': '9'},
            {'name': 'TRANSDESC', 'number': '10'},
            {'name': 'ITEM-PG-OTHER', 'number': '11'},
            {'name': 'PG-OTHER-DESCRIPTION', 'number': '12'},
            {'name': 'OF DISBURSEMENT', 'number': '13-'},
            {'name': 'AMOUNT DISBURSED CONTRIB/LOAN', 'number': '14'},
            {'name': 'FEC COMMITTEE ID NUMBER', 'number': '15'},
            {'name': 'COMMITTEE NAME', 'number': '16'},
            {'name': 'STREET 1', 'number': '17'},
            {'name': 'STREET 2', 'number': '18'},
            {'name': 'CITY', 'number': '19'},
            {'name': 'STATE', 'number': '20'},
            {'name': 'ZIP', 'number': '21'},
            {'name': 'FEC CANDIDATE ID NUMBER', 'number': '22'},
            {'name': 'CANDIDATE NAME', 'number': '23'},
            {'name': 'CAN/OFF', 'number': '24'},
            {'name': 'STATE (OF ELECTION)', 'number': '25'},
            {'name': 'CAN/DIST', 'number': '26'},
            {'name': 'MEMO CODE', 'number': '27'},
            {'name': 'MEMO TEXT', 'number': '28'},
            {'name': 'AMENDED', 'number': '29'},
    ]
        self.fields_names = self.hash_names(self.fields)
