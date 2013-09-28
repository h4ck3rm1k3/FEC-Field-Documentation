import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC CMTE ID', 'number': '2'},
            {'name': 'ENTITY TYPE', 'number': '3'},
            {'name': 'NAME (Payee)', 'number': '4'},
            {'name': 'STREET 1', 'number': '5'},
            {'name': 'STREET 2', 'number': '6'},
            {'name': 'CITY', 'number': '7'},
            {'name': 'STATE', 'number': '8'},
            {'name': 'ZIP', 'number': '9'},
            {'name': 'TRANSDESC', 'number': '10'},
            {'name': 'Of Expenditure', 'number': '11-'},
            {'name': 'AMOUNT', 'number': '12'},
            {'name': 'SUPPORT/OPPOSE', 'number': '13'},
            {'name': 'S/O FEC CAN ID NUMBER', 'number': '14'},
            {'name': 'S/O CAN/NAME', 'number': '15'},
            {'name': 'S/O CAN/OFFICE', 'number': '16'},
            {'name': 'S/O CAN/STATE', 'number': '17'},
            {'name': 'S/O CAN/DIST', 'number': '18'},
            {'name': 'FEC COMMITTEE ID NUMBER', 'number': '19'},
            {'name': 'Unused field', 'number': '20'},
            {'name': 'Unused field', 'number': '21'},
            {'name': 'Unused field', 'number': '22'},
            {'name': 'Unused field', 'number': '23'},
            {'name': 'Unused field', 'number': '24'},
            {'name': 'CONDUIT NAME', 'number': '25'},
            {'name': 'CONDUIT STREET 1', 'number': '26'},
            {'name': 'CONDUIT STREET 2', 'number': '27'},
            {'name': 'CONDUIT CITY', 'number': '28'},
            {'name': 'CONDUIT STATE', 'number': '29'},
            {'name': 'CONDUIT ZIP', 'number': '30'},
            {'name': 'AMENDED CD', 'number': '31'},
            {'name': 'TRAN ID', 'number': '32'},
    ]
        self.fields_names = self.hash_names(self.fields)
