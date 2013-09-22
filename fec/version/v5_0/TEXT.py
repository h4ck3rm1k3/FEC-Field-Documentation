from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        self.fields = [
            {'name': 'REC TYPE', 'number': '1'},
            {'name': 'FORM TYPE', 'number': '2'},
            {'name': 'BACK REF TRAN ID', 'number': '3'},
            {'name': 'TEXT4000', 'number': '4'},
            {'name': 'AMENDED CD', 'number': '5'},
    ]
