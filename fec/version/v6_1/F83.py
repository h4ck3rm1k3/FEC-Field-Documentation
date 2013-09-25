from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'TRANSACTION ID NUMBER', 'number': '3'},
            {'name': 'ENTITY TYPE', 'number': '4'},
            {'name': 'CREDITOR ORGANIZATION NAME', 'number': '5'},
            {'name': 'CREDITOR LAST NAME', 'number': '6'},
            {'name': 'CREDITOR FIRST NAME', 'number': '7'},
            {'name': 'CREDITOR MIDDLE NAME', 'number': '8'},
            {'name': 'CREDITOR PREFIX', 'number': '9'},
            {'name': 'CREDITOR SUFFIX', 'number': '10'},
            {'name': 'CREDITOR STREET 1', 'number': '11'},
            {'name': 'CREDITOR STREET 2', 'number': '12'},
            {'name': 'CREDITOR CITY', 'number': '13'},
            {'name': 'CREDITOR STATE', 'number': '14'},
            {'name': 'CREDITOR ZIP', 'number': '15'},
            {'name': 'DATE INCURRED', 'number': '16'},
            {'name': 'AMOUNT OWED TO CREDITOR', 'number': '17'},
            {'name': 'AMOUNT EXPECTED TO PAY/OFFER', 'number': '18'},
            {'name': 'CREDITOR CODE', 'number': '19'},
            {'name': 'Disputed Debt?', 'number': '20-'},
            {'name': 'CREDITOR COMMITTEE ID NUMBER', 'number': '21'},
            {'name': 'CREDITOR CANDIDATE ID NUMBER', 'number': '22'},
            {'name': 'CREDITOR CANDIDATE LAST NAME', 'number': '23'},
            {'name': 'CREDITOR CANDIDATE FIRST NAME', 'number': '24'},
            {'name': 'CREDITOR CANDIDATE MIDDLE NAME', 'number': '25'},
            {'name': 'CREDITOR CANDIDATE PREFIX', 'number': '26'},
            {'name': 'CREDITOR CANDIDATE SUFFIX', 'number': '27'},
            {'name': 'CREDITOR CANDIDATE OFFICE', 'number': '28'},
            {'name': 'CREDITOR CANDIDATE STATE', 'number': '29'},
            {'name': 'CREDITOR CANDIDATE DISTRICT', 'number': '30'},
    ]
        self.fields_names = self.hash_names(self.fields)
