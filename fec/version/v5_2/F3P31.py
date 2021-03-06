import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC CMTE ID', 'number': '2'},
            {'name': 'ENTITY TYPE', 'number': '3'},
            {'name': 'NAME (Contributor/Lender)', 'number': '4'},
            {'name': 'STREET 1', 'number': '5'},
            {'name': 'STREET 2', 'number': '6'},
            {'name': 'CITY', 'number': '7'},
            {'name': 'STATE', 'number': '8'},
            {'name': 'ZIP', 'number': '9'},
            {'name': 'RPTPGI', 'number': '10'},
            {'name': 'INDEMP', 'number': '11'},
            {'name': 'INDOCC', 'number': '12'},
            {'name': 'Of Contribution', 'number': '13-'},
            {'name': 'FAIR MARKET VALUE OF ITEM', 'number': '14'},
            {'name': 'TRANSACTION CODE', 'number': '15'},
            {'name': 'TRANSDESC', 'number': '16'},
            {'name': 'FEC COMMITTEE ID NUMBER', 'number': '17'},
            {'name': 'FEC CANDIDATE ID NUMBER', 'number': '18'},
            {'name': 'CANDIDATE NAME', 'number': '19'},
            {'name': 'CAN/OFFICE', 'number': '20'},
            {'name': 'CAN/STATE', 'number': '21'},
            {'name': 'CAN/DIST', 'number': '22'},
            {'name': 'CONDUIT NAME', 'number': '23'},
            {'name': 'CONDUIT STREET 1', 'number': '24'},
            {'name': 'CONDUIT STREET 2', 'number': '25'},
            {'name': 'CONDUIT CITY', 'number': '26'},
            {'name': 'CONDUIT STATE', 'number': '27'},
            {'name': 'CONDUIT ZIP', 'number': '28'},
            {'name': 'MEMO CODE', 'number': '29'},
            {'name': 'MEMO TEXT', 'number': '30'},
            {'name': 'AMENDED CD', 'number': '31'},
            {'name': 'TRAN ID', 'number': '32'},
    ]
        self.fields_names = self.hash_names(self.fields)
