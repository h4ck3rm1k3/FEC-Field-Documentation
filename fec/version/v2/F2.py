from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC CMTE ID', 'number': '2'},
            {'name': 'CANDIDATE NAME', 'number': '3'},
            {'name': 'STREET 1', 'number': '4'},
            {'name': 'STREET 2', 'number': '5'},
            {'name': 'CITY', 'number': '6'},
            {'name': 'STATE', 'number': '7'},
            {'name': 'ZIP', 'number': '8'},
            {'name': 'PTY/CODE', 'number': '9'},
            {'name': 'CAN/OFF', 'number': '10'},
            {'name': 'STATE (Of Election)', 'number': '11'},
            {'name': 'CAN/DIST', 'number': '12'},
            {'name': 'YEAR OF ELECTION 1900-2999', 'number': '13'},
            {'name': 'FEC COMMITTEE ID NUMBER (PCC)', 'number': '14'},
            {'name': 'COMMITTEE NAME (PCC)', 'number': '15'},
            {'name': 'STREET 1', 'number': '16'},
            {'name': 'STREET 2', 'number': '17'},
            {'name': 'CITY', 'number': '18'},
            {'name': 'STATE', 'number': '19'},
            {'name': 'ZIP', 'number': '20'},
            {'name': 'FEC COMMITTEE ID NUMBER (Auth)', 'number': '21'},
            {'name': 'COMMITTEE NAME (Auth)', 'number': '22'},
            {'name': 'STREET 1', 'number': '23'},
            {'name': 'STREET 2', 'number': '24'},
            {'name': 'CITY', 'number': '25'},
            {'name': 'STATE', 'number': '26'},
            {'name': 'ZIP', 'number': '27'},
            {'name': 'NAME', 'number': '28'},
            {'name': 'Signed', 'number': '29-'},
    ]
        self.fields_names = self.hash_names(self.fields)
