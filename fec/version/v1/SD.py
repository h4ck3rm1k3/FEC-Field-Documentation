import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FEC COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'DEBTOR/CREDITOR', 'number': '3-'},
            {'name': 'STREET 1', 'number': '4'},
            {'name': 'STREET 2', 'number': '5'},
            {'name': 'CITY', 'number': '6'},
            {'name': 'STATE', 'number': '7'},
            {'name': 'ZIP', 'number': '8'},
            {'name': 'NATURE/PURPOSE DEBT DESCRIPTION', 'number': '9'},
            {'name': 'BEGINNING BALANCE', 'number': '10'},
            {'name': 'INCURRED THIS PERIOD', 'number': '11'},
            {'name': 'PAYMENT THIS PERIOD', 'number': '12'},
            {'name': 'BALANCE AT CLOSE', 'number': '13'},
            {'name': 'AMENDED', 'number': '14'},
    ]
        self.fields_names = self.hash_names(self.fields)
