from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC CMTE ID', 'number': '2'},
            {'name': 'FEC CANDIDATE ID NUMBER', 'number': '3'},
            {'name': 'CANDIDATE NAME', 'number': '4'},
            {'name': 'CAN/OFFICE', 'number': '5'},
            {'name': 'CAN/STATE', 'number': '6'},
            {'name': 'CAN/DIST', 'number': '7'},
            {'name': 'ITEM ELECT CD', 'number': '8'},
            {'name': 'ITEM ELECT OTHER', 'number': '9'},
            {'name': 'AMENDED CD', 'number': '10'},
            {'name': 'TRAN ID', 'number': '11'},
            {'name': 'BACK REF TRAN ID', 'number': '12'},
            {'name': 'BACK REF SCHED NAME', 'number': '13'},
    ]
        self.fields_names = self.hash_names(self.fields)
