from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC CMTE ID', 'number': '2'},
            {'name': 'COMMUNICATION TYPE', 'number': '3'},
            {'name': 'Comm. Descrip', 'number': '4-TRANS'},
            {'name': 'COMMUNICATION CLASS', 'number': '5'},
            {'name': 'Of Communication', 'number': '6-'},
            {'name': 'SUPPORT/OPPOSE', 'number': '7'},
            {'name': 'FEC CANDIDATE ID NUMBER', 'number': '8'},
            {'name': 'CANDIDATE NAME', 'number': '9'},
            {'name': 'CAN/OFFICE', 'number': '10'},
            {'name': 'CAN/STATE', 'number': '11'},
            {'name': 'CAN/DIST', 'number': '12'},
            {'name': 'RPTPGI', 'number': '13'},
            {'name': 'COST OF COMMUNICATION', 'number': '14'},
            {'name': 'AMENDED CD', 'number': '15'},
            {'name': 'TRAN ID', 'number': '16'},
    ]
        self.fields_names = self.hash_names(self.fields)
