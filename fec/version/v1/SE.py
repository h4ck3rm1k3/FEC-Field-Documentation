from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FEC COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'PAYEE', 'number': '3-'},
            {'name': 'STREET 1', 'number': '4'},
            {'name': 'STREET 2', 'number': '5'},
            {'name': 'CITY', 'number': '6'},
            {'name': 'STATE', 'number': '7'},
            {'name': 'ZIP', 'number': '8'},
            {'name': 'TRANSDESC', 'number': '9'},
            {'name': 'DATE', 'number': '10'},
            {'name': 'AMOUNT EXPENDED', 'number': '11'},
            {'name': 'FEC CANDIDATE ID NUMBER', 'number': '12'},
            {'name': 'CANDIDATE NAME', 'number': '13'},
            {'name': 'CAN/OFF', 'number': '14'},
            {'name': 'STATE (OF ELECTION)', 'number': '15'},
            {'name': 'CAN/DIST', 'number': '16'},
            {'name': 'SUPPORT/OPPOSE', 'number': '17'},
            {'name': 'PERSON COMPLETING FORM', 'number': '18-'},
            {'name': 'SIGNED', 'number': '19-'},
            {'name': 'NOTARIZED', 'number': '20-'},
            {'name': 'NOTARY COMMISSION EXPIRES', 'number': '21-'},
            {'name': 'NOTARY', 'number': '22-'},
            {'name': 'AMENDED', 'number': '23'},
    ]
