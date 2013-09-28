import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC CMTE ID', 'number': '2'},
            {'name': 'COMMITTEE NAME', 'number': '3'},
            {'name': 'STREET 1', 'number': '4'},
            {'name': 'STREET 2', 'number': '5'},
            {'name': 'CITY', 'number': '6'},
            {'name': 'STATE', 'number': '7'},
            {'name': 'ZIP', 'number': '8'},
            {'name': 'FEC CANDIDATE ID NUMBER', 'number': '9'},
            {'name': 'CANDIDATE NAME', 'number': '10'},
            {'name': 'CAN/OFF', 'number': '11'},
            {'name': 'STATE (OF ELECTION)', 'number': '12'},
            {'name': 'CAN/DIST', 'number': '13'},
            {'name': 'SIGNED', 'number': '14-'},
    ]
        self.fields_names = self.hash_names(self.fields)
