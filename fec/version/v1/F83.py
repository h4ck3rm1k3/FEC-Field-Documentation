import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FEC COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'SEQUENCE NUMBER', 'number': '3'},
            {'name': 'CONTRIB/LENDER', 'number': '4-'},
            {'name': 'STREET 1', 'number': '5'},
            {'name': 'STREET 2', 'number': '6'},
            {'name': 'CITY', 'number': '7'},
            {'name': 'STATE', 'number': '8'},
            {'name': 'ZIP', 'number': '9'},
            {'name': 'TYPE OF CREDITOR CODE', 'number': '10'},
            {'name': 'IS THIS A DISPUTED DEBT', 'number': '11-'},
            {'name': 'INCURRED', 'number': '12-'},
            {'name': 'AMOUNT OWED TO CREDITOR', 'number': '13'},
            {'name': 'AMOUNT EXPECTED TO PAY/OFFER SETTLEMENT', 'number': '14'},
            {'name': 'AMENDED', 'number': '15'},
    ]
        self.fields_names = self.hash_names(self.fields)
