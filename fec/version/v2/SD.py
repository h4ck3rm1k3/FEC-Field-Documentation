import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC CMTE ID', 'number': '2'},
            {'name': 'ENTITY-TYPE', 'number': '3'},
            {'name': 'NAME (Debtor/Creditor)', 'number': '4'},
            {'name': 'STREET 1', 'number': '5'},
            {'name': 'STREET 2', 'number': '6'},
            {'name': 'CITY', 'number': '7'},
            {'name': 'STATE', 'number': '8'},
            {'name': 'ZIP', 'number': '9'},
            {'name': 'NATURE/PURPOSE DEBT DESCRIPTION', 'number': '10'},
            {'name': 'BEGINNING BALANCE', 'number': '11'},
            {'name': 'INCURRED THIS PERIOD', 'number': '12'},
            {'name': 'PAYMENT THIS PERIOD', 'number': '13'},
            {'name': 'BALANCE AT CLOSE', 'number': '14'},
            {'name': 'FEC-COMMITTEE-ID-NUMBER', 'number': '15'},
            {'name': 'FEC-CANDIDATE-ID-NUMBER', 'number': '16'},
            {'name': 'CANDIDATE-NAME', 'number': '17'},
            {'name': 'CAND-OFFICE', 'number': '18'},
            {'name': 'CAND-STATE (OF ELECTION)', 'number': '19'},
            {'name': 'CAND-DISTRICT', 'number': '20'},
            {'name': 'CONDUIT-NAME', 'number': '21'},
            {'name': 'CONDUIT-STREET-1', 'number': '22'},
            {'name': 'CONDUIT-STREET-2', 'number': '23'},
            {'name': 'CONDUIT-CITY', 'number': '24'},
            {'name': 'CONDUIT-STATE', 'number': '25'},
            {'name': 'CONDUIT-ZIP', 'number': '26'},
            {'name': 'AMENDED-CD', 'number': '27'},
            {'name': 'TRAN_ID', 'number': '28'},
            {'name': 'ORIG_TRAN_ID', 'number': '29'},
            {'name': 'SUPR_TRAN_ID', 'number': '30'},
    ]
        self.fields_names = self.hash_names(self.fields)
