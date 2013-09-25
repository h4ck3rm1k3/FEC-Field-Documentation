from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'TRANSACTION ID NUMBER', 'number': '3'},
            {'name': 'ELECTION CODE', 'number': '4'},
            {'name': 'ELECTION OTHER DESCRIPTION', 'number': '5'},
            {'name': 'EXPENDITURE DATE', 'number': '6'},
            {'name': 'EXPENDITURE AMOUNT', 'number': '7'},
            {'name': 'LOAN CHECK', 'number': '8'},
    ]
        self.fields_names = self.hash_names(self.fields)
