from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FEC COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'SEQUENCE NUMBER', 'number': '3'},
            {'name': 'CONTRIB/LENDER', 'number': '4-'},
            {'name': 'STREET 1', 'number': '5'},
            {'name': 'STREET 2', 'number': '6'},
            {'name': 'CITY', 'number': '7'},
            {'name': 'STATE', 'number': '8'},
            {'name': 'ZIP', 'number': '9'},
            {'name': 'TYPE OF CREDITOR CODE', 'number': '10'},
            {'name': 'INCURRED', 'number': '11-'},
            {'name': 'AMOUNT OWED TO CREDITOR', 'number': '12'},
            {'name': 'AMOUNT OFFERED IN SETTLEMENT', 'number': '13'},
            {'name': 'INITIAL TERMS AND NATURE OF DEBT', 'number': '14-A '},
            {'name': 'EFFORTS MADE BY CMTE TO PAY DEBT', 'number': '15-B '},
            {'name': 'STEPS TAKEN BY CREDITOR TO COLLECT', 'number': '16-C '},
            {'name': 'WAS THE effort made BY creditor to collect similar to other debt collection efforts', 'number': '17-D '},
            {'name': 'N IF NO EXPLAIN', 'number': '18-D '},
            {'name': 'Are the terms of the debt settlement comparable to other settlements', 'number': '19-E '},
            {'name': 'N IF NO EXPLAIN', 'number': '20-E '},
            {'name': 'NAME of creditor or representative', 'number': '21'},
            {'name': 'SIGNED', 'number': '22-'},
            {'name': 'AMENDED', 'number': '23'},
    ]
        self.fields_names = self.hash_names(self.fields)
