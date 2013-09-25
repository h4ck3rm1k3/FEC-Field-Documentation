from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        RecordsBase.__init__(self)
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
            {'name': 'Is This A Disputed Debt', 'number': '10-'},
            {'name': 'Incurred', 'number': '11-'},
            {'name': 'AMOUNT OWED TO CREDITOR', 'number': '12'},
            {'name': 'AMOUNT EXPECTED TO', 'number': '13'},
            {'name': 'FEC COMMITTEE ID NUMBER', 'number': '14'},
            {'name': 'FEC CANDIDATE ID NUMBER', 'number': '15'},
            {'name': 'CANDIDATE NAME', 'number': '16'},
            {'name': 'CAN/OFFICE', 'number': '17'},
            {'name': 'CAN/STATE', 'number': '18'},
            {'name': 'CAN/DIST', 'number': '19'},
            {'name': 'AMENDED CD', 'number': '20'},
            {'name': 'TRAN ID', 'number': '21'},
    ]
        self.fields_names = self.hash_names(self.fields)
