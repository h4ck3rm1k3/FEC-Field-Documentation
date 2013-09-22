from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
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
            {'name': 'OF ELECTION', 'number': '11-'},
            {'name': 'STATE (OF ELECTION)', 'number': '12'},
            {'name': 'COVERAGE FROM', 'number': '13-'},
            {'name': 'COVERAGE TO', 'number': '14-'},
            {'name': 'TOTAL COSTS', 'number': '15'},
            {'name': 'FILER', 'number': '16-'},
            {'name': 'SIGNED', 'number': '17-'},
            {'name': 'TITLE', 'number': '18'},
    ]
