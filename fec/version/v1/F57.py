import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FEC COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'SEQUENCE NUMBER', 'number': '3'},
            {'name': 'PAYEE', 'number': '4-'},
            {'name': 'STREET 1', 'number': '5'},
            {'name': 'STREET 2', 'number': '6'},
            {'name': 'CITY', 'number': '7'},
            {'name': 'STATE', 'number': '8'},
            {'name': 'ZIP', 'number': '9'},
            {'name': 'TRANSDESC', 'number': '10'},
            {'name': 'OF EXPENDITURE', 'number': '11-'},
            {'name': 'AMOUNT CONTRIBUTION AMOUNT', 'number': '12'},
            {'name': 'SUPPORT/OPPOSE', 'number': '13'},
            {'name': 'FEC CANDIDATE ID NUMBER', 'number': '14'},
            {'name': 'CANDIDATE NAME', 'number': '15'},
            {'name': 'CAN/OFF', 'number': '16'},
            {'name': 'STATE (OF ELECTION)', 'number': '17'},
            {'name': 'CAN/DIST', 'number': '18'},
            {'name': 'AMENDED', 'number': '19'},
    ]
        self.fields_names = self.hash_names(self.fields)
