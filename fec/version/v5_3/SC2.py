from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC CMTE ID', 'number': '2'},
            {'name': 'BACK REFERENCE TRAN ID', 'number': '3'},
            {'name': 'Endorser/Guarantor', 'number': '4-'},
            {'name': 'STREET 1', 'number': '5'},
            {'name': 'STREET 2', 'number': '6'},
            {'name': 'CITY', 'number': '7'},
            {'name': 'STATE', 'number': '8'},
            {'name': 'ZIP', 'number': '9'},
            {'name': 'INDEMP', 'number': '10'},
            {'name': 'INDOCC', 'number': '11'},
            {'name': 'AMOUNT GUARANTEED BALANCE', 'number': '12'},
            {'name': 'AMENDED CD', 'number': '13'},
    ]
        self.fields_names = self.hash_names(self.fields)
