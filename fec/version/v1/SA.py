import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FEC COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'CONTRIB/LENDER', 'number': '3-'},
            {'name': 'STREET 1', 'number': '4'},
            {'name': 'STREET 2', 'number': '5'},
            {'name': 'CITY', 'number': '6'},
            {'name': 'STATE', 'number': '7'},
            {'name': 'ZIP', 'number': '8'},
            {'name': 'ITEM-PG-OTHER', 'number': '9'},
            {'name': 'PG-OTHER-DESCRIPTION', 'number': '10'},
            {'name': 'INDEMP', 'number': '11'},
            {'name': 'INDOCC', 'number': '12'},
            {'name': 'AGGR YTD AMOUNT (TOTAL FOR THE YEAR)', 'number': '13'},
            {'name': 'OF CONTRIBUTION', 'number': '14-'},
            {'name': 'AMOUNT RECEIVED', 'number': '15'},
            {'name': 'RECEIPTCODE', 'number': '16'},
            {'name': 'TRANSDESC', 'number': '17'},
            {'name': 'FEC COMMITTEE ID NUMBER', 'number': '18'},
            {'name': 'COMMITTEE NAME', 'number': '19'},
            {'name': 'STREET 1', 'number': '20'},
            {'name': 'STREET 2', 'number': '21'},
            {'name': 'CITY', 'number': '22'},
            {'name': 'STATE', 'number': '23'},
            {'name': 'ZIP', 'number': '24'},
            {'name': 'FEC CANDIDATE ID NUMBER', 'number': '25'},
            {'name': 'CANDIDATE NAME', 'number': '26'},
            {'name': 'CAN/OFF', 'number': '27'},
            {'name': 'STATE (OF ELECTION)', 'number': '28'},
            {'name': 'CAN/DIST', 'number': '29'},
            {'name': 'MEMO CODE', 'number': '30'},
            {'name': 'MEMO-TEXT', 'number': '31'},
            {'name': 'AMENDED', 'number': '32'},
    ]
        self.fields_names = self.hash_names(self.fields)
