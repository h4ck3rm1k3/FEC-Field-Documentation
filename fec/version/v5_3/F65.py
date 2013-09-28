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
            {'name': 'INDEMP', 'number': '10'},
            {'name': 'INDOCC', 'number': '11'},
            {'name': 'Of Contribution', 'number': '12-'},
            {'name': 'AMOUNT', 'number': '13'},
            {'name': 'FEC COMMITTEE ID NUMBER', 'number': '14'},
            {'name': 'FEC CANDIDATE ID NUMBER', 'number': '15'},
            {'name': 'CANDIDATE NAME', 'number': '16'},
            {'name': 'CAN/OFFICE', 'number': '17'},
            {'name': 'CAN/STATE', 'number': '18'},
            {'name': 'CAN/DIST', 'number': '19'},
            {'name': 'CONDUIT NAME', 'number': '20'},
            {'name': 'CONDUIT STREET 1', 'number': '21'},
            {'name': 'CONDUIT STREET 2', 'number': '22'},
            {'name': 'CONDUIT CITY', 'number': '23'},
            {'name': 'CONDUIT STATE', 'number': '24'},
            {'name': 'CONDUIT ZIP', 'number': '25'},
            {'name': 'AMENDED CD', 'number': '26'},
            {'name': 'TRAN ID', 'number': '27'},
    ]
        self.fields_names = self.hash_names(self.fields)
