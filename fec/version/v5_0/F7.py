from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC CMTE ID', 'number': '2'},
            {'name': 'COMMITTEE NAME', 'number': '3'},
            {'name': 'STREET 1', 'number': '4'},
            {'name': 'STREET 2', 'number': '5'},
            {'name': 'CITY', 'number': '6'},
            {'name': 'STATE', 'number': '7'},
            {'name': 'ZIP', 'number': '8'},
            {'name': 'ORGANIZATION TYPE', 'number': '9'},
            {'name': 'RPTCODE', 'number': '10'},
            {'name': 'Of Election', 'number': '11-'},
            {'name': 'STATE (Of Election)', 'number': '12'},
            {'name': 'Coverage From', 'number': '13-'},
            {'name': 'Coverage To', 'number': '14-'},
            {'name': 'TOTAL COSTS', 'number': '15'},
            {'name': 'NAME/FILER (as signed)', 'number': '16'},
            {'name': 'Signed', 'number': '17-'},
            {'name': 'TITLE', 'number': '18'},
    ]
        self.fields_names = self.hash_names(self.fields)
