import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC CMTE ID', 'number': '2'},
            {'name': 'CREDITOR CODE', 'number': '3'},
            {'name': 'NAME (Contributor/Lender)', 'number': '4'},
            {'name': 'STREET 1', 'number': '5'},
            {'name': 'STREET 2', 'number': '6'},
            {'name': 'CITY', 'number': '7'},
            {'name': 'STATE', 'number': '8'},
            {'name': 'ZIP', 'number': '9'},
            {'name': 'INCURRED', 'number': '10-'},
            {'name': 'AMOUNT OWED TO CREDITOR', 'number': '11'},
            {'name': 'AMOUNT OFFERED IN SETTLEMENT', 'number': '12'},
            {'name': 'INITIAL TERMS AND NATURE OF DEBT', 'number': '13-A '},
            {'name': 'EFFORTS MADE BY CMTE TO PAY DEBT', 'number': '14-B '},
            {'name': 'STEPS TAKEN BY CREDITOR TO COLLECT', 'number': '15-C '},
            {'name': 'WAS THE effort made BY creditor to collect similar to other debt collection efforts', 'number': '16-D '},
            {'name': 'N IF NO EXPLAIN', 'number': '17-D '},
            {'name': 'Are the terms of the debt settlement comparable to other settlements', 'number': '18-E '},
            {'name': 'N IF NO EXPLAIN', 'number': '19-E '},
            {'name': 'FEC-COMMITTEE-ID-NUMBER', 'number': '20'},
            {'name': 'FEC-CANDIDATE-ID-NUMBER', 'number': '21'},
            {'name': 'CANDIDATE-NAME', 'number': '22'},
            {'name': 'CAND-OFFICE', 'number': '23'},
            {'name': 'CAND-STATE (OF ELECTION)', 'number': '24'},
            {'name': 'CAND-DISTRICT', 'number': '25'},
            {'name': 'NAME of creditor or representative', 'number': '26'},
            {'name': 'SIGNED', 'number': '27-'},
            {'name': 'AMENDED-CD', 'number': '28'},
            {'name': 'TRAN_ID', 'number': '29'},
            {'name': 'ORIG_TRAN_ID', 'number': '30'},
            {'name': 'SUPR_TRAN_ID', 'number': '31'},
    ]
        self.fields_names = self.hash_names(self.fields)
