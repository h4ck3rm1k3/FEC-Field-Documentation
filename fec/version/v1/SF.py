import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FEC COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'HAS FILER BEEN DESIG. TO MAKE CORD. EXPEND.', 'number': '3-'},
            {'name': 'FEC COMMITTEE ID NUMBER DESIGNATING CMTE', 'number': '4'},
            {'name': 'COMMITTEE NAME', 'number': '5'},
            {'name': 'STREET 1', 'number': '6'},
            {'name': 'STREET 2', 'number': '7'},
            {'name': 'CITY', 'number': '8'},
            {'name': 'STATE', 'number': '9'},
            {'name': 'ZIP', 'number': '10'},
            {'name': 'PAYEE', 'number': '11-'},
            {'name': 'STREET 1', 'number': '12'},
            {'name': 'STREET 2', 'number': '13'},
            {'name': 'CITY', 'number': '14'},
            {'name': 'STATE', 'number': '15'},
            {'name': 'ZIP', 'number': '16'},
            {'name': 'FEC CANDIDATE ID NUMBER', 'number': '17'},
            {'name': 'CANDIDATE NAME', 'number': '18'},
            {'name': 'CAN/OFF', 'number': '19'},
            {'name': 'STATE (OF ELECTION)', 'number': '20'},
            {'name': 'CAN/DIST', 'number': '21'},
            {'name': 'AGG. GEN. ELE. AMOUNT EXPENDED', 'number': '22'},
            {'name': 'TRANSDESC', 'number': '23'},
            {'name': 'DATE', 'number': '24'},
            {'name': 'AMOUNT EXPENDED', 'number': '25'},
            {'name': 'AMENDED', 'number': '26'},
    ]
        self.fields_names = self.hash_names(self.fields)
