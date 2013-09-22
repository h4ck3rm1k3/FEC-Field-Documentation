from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FEC COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'SEQUENCE NUMBER', 'number': '3'},
            {'name': 'CONTRIBUTOR', 'number': '4-'},
            {'name': 'STREET 1', 'number': '5'},
            {'name': 'STREET 2', 'number': '6'},
            {'name': 'CITY', 'number': '7'},
            {'name': 'STATE', 'number': '8'},
            {'name': 'ZIP', 'number': '9'},
            {'name': 'INDEMP', 'number': '10'},
            {'name': 'INDOCC', 'number': '11'},
            {'name': 'OF CONTRIBUTION', 'number': '12-'},
            {'name': 'AMOUNT CONTRIBUTION AMOUNT', 'number': '13'},
            {'name': 'AMENDED', 'number': '14'},
    ]
