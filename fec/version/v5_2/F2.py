import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC CAND ID', 'number': '2'},
            {'name': 'CANDIDATE NAME', 'number': '3'},
            {'name': 'STREET 1', 'number': '4'},
            {'name': 'STREET 2', 'number': '5'},
            {'name': 'CITY', 'number': '6'},
            {'name': 'STATE', 'number': '7'},
            {'name': 'ZIP', 'number': '8'},
            {'name': 'PTY/CODE', 'number': '9'},
            {'name': 'CAN/OFFICE', 'number': '10'},
            {'name': 'CAN/STATE', 'number': '11'},
            {'name': 'CAN/DIST', 'number': '12'},
            {'name': 'YEAR OF ELECTION 1900-2999', 'number': '13'},
            {'name': 'FEC COMMITTEE ID NUMBER (PCC)', 'number': '14'},
            {'name': 'COMMITTEE NAME (PCC)', 'number': '15'},
            {'name': 'STREET 1', 'number': '16'},
            {'name': 'STREET 2', 'number': '17'},
            {'name': 'CITY', 'number': '18'},
            {'name': 'STATE', 'number': '19'},
            {'name': 'ZIP', 'number': '20'},
            {'name': 'FEC COMMITTEE ID NUMBER (Auth)', 'number': '21'},
            {'name': 'COMMITTEE NAME (Auth)', 'number': '22'},
            {'name': 'STREET 1', 'number': '23'},
            {'name': 'STREET 2', 'number': '24'},
            {'name': 'CITY', 'number': '25'},
            {'name': 'STATE', 'number': '26'},
            {'name': 'ZIP', 'number': '27'},
            {'name': 'NAME/CAN (as signed)', 'number': '28'},
            {'name': 'Signed', 'number': '29-'},
            {'name': 'PRI PERSONAL FUNDS DECLARED', 'number': '30'},
            {'name': 'GEN PERSONAL FUNDS DECLARED', 'number': '31'},
            {'name': 'CANDIDATE LAST NAME', 'number': '32'},
            {'name': 'CANDIDATE FIRST NAME', 'number': '33'},
            {'name': 'CANDIDATE MIDDLE NAME', 'number': '34'},
            {'name': 'CANDIDATE PREFIX', 'number': '35'},
            {'name': 'CANDIDATE SUFFIX', 'number': '36'},
    ]
        self.fields_names = self.hash_names(self.fields)
