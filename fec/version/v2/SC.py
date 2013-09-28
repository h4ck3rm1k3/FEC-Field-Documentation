import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC CMTE ID', 'number': '2'},
            {'name': 'ENTITY TYPE', 'number': '3'},
            {'name': 'NAME (Loan Source)', 'number': '4'},
            {'name': 'STREET 1', 'number': '5'},
            {'name': 'STREET 2', 'number': '6'},
            {'name': 'CITY', 'number': '7'},
            {'name': 'STATE', 'number': '8'},
            {'name': 'ZIP', 'number': '9'},
            {'name': 'ELECTION', 'number': '10'},
            {'name': 'ELECTION DESCRIPTION', 'number': '11'},
            {'name': 'ORIG AMT OF LOAN AMOUNT', 'number': '12'},
            {'name': 'PAYMENT TO DATE', 'number': '13'},
            {'name': 'LOAN BALANCE', 'number': '14'},
            {'name': 'INCURRED', 'number': '15-'},
            {'name': 'DUE-DATE-TERMS', 'number': '16'},
            {'name': 'PCT-RATE-TERMS', 'number': '17'},
            {'name': 'SECURED LOAN', 'number': '18-'},
            {'name': 'FEC-COMMITTEE-ID-NUMBER', 'number': '19'},
            {'name': 'FEC-CANDIDATE-ID-NUMBER', 'number': '20'},
            {'name': 'CANDIDATE-NAME', 'number': '21'},
            {'name': 'CAND-OFFICE', 'number': '22'},
            {'name': 'CAND-STATE (OF ELECTION)', 'number': '23'},
            {'name': 'CAND-DISTRICT', 'number': '24'},
            {'name': 'AMENDED-CD', 'number': '25'},
            {'name': 'TRAN_ID', 'number': '26'},
            {'name': 'ORIG_TRAN_ID', 'number': '27'},
            {'name': 'SUPR_TRAN_ID', 'number': '28'},
    ]
        self.fields_names = self.hash_names(self.fields)
