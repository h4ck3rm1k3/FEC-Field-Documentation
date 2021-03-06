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
            {'name': 'TRANS Purpose DESCRIP', 'number': '10'},
            {'name': 'DATE', 'number': '11'},
            {'name': 'TOTAL AMOUNT', 'number': '12'},
            {'name': 'FEDERAL SHARE', 'number': '13'},
            {'name': 'NON FEDERAL SHARE', 'number': '14'},
            {'name': 'Activity Is Admin./Voter Drive', 'number': '15-'},
            {'name': 'Activity is Direct Fundrainsig', 'number': '16-'},
            {'name': 'Activity is an Exempt Activity', 'number': '17-'},
            {'name': 'Act. Direct Candidate Support', 'number': '18-'},
            {'name': 'EVENT YEAR-TO-DATE', 'number': '19'},
            {'name': 'ADDITIONAL DESCRIPTION', 'number': '20'},
            {'name': 'FEC COMMITTEE ID NUMBER', 'number': '21'},
            {'name': 'FEC CANDIDATE ID NUMBER', 'number': '22'},
            {'name': 'CANDIDATE NAME', 'number': '23'},
            {'name': 'CAN/OFFICE', 'number': '24'},
            {'name': 'CAN/STATE', 'number': '25'},
            {'name': 'CAN/DIST', 'number': '26'},
            {'name': 'CONDUIT NAME', 'number': '27'},
            {'name': 'CONDUIT STREET 1', 'number': '28'},
            {'name': 'CONDUIT STREET 2', 'number': '29'},
            {'name': 'CONDUIT CITY', 'number': '30'},
            {'name': 'CONDUIT STATE', 'number': '31'},
            {'name': 'CONDUIT ZIP', 'number': '32'},
            {'name': 'AMENDED CD', 'number': '33'},
            {'name': 'TRAN ID', 'number': '34'},
            {'name': 'MEMO CODE', 'number': '35'},
            {'name': 'MEMO TEXT', 'number': '36'},
            {'name': 'BACK REF TRAN ID', 'number': '37'},
            {'name': 'BACK REF SCHED NAME', 'number': '38'},
            {'name': 'Activity is Administrative - Only', 'number': '39-'},
            {'name': 'Activity is Generic Voter Drive - Only', 'number': '40-'},
            {'name': 'CATEGORY CODE', 'number': '41'},
            {'name': 'TRANS CODE', 'number': '42'},
    ]
        self.fields_names = self.hash_names(self.fields)
