from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC COMMITTEE ID', 'number': '2'},
            {'name': 'CANDIDATE NAME', 'number': '3-1.'},
            {'name': 'CANDIDATE ID', 'number': '4-2.'},
            {'name': 'CAN/OFFICE', 'number': '5-3.'},
            {'name': 'CANDIDATE STATE', 'number': '6-4.'},
            {'name': 'CANDIDATE DISTRICT', 'number': '7-5.'},
            {'name': 'COMMITTEE NAME', 'number': '8-6.'},
            {'name': 'STREET 1', 'number': '9-8.'},
            {'name': 'STREET 2', 'number': '10-8.'},
            {'name': 'CITY', 'number': '11-9.'},
            {'name': 'STATE', 'number': '12-9.'},
            {'name': 'ZIP', 'number': '13-9.'},
            {'name': 'DATE REACHED 100%', 'number': '14-12a.'},
            {'name': 'PERSE FUNDS AMT', 'number': '15-12a.'},
            {'name': 'PREV FORM 11 DATE', 'number': '16-12a.'},
            {'name': 'DATE REACHED 110%', 'number': '17-12B.'},
            {'name': 'PERSE FUNDS AMT', 'number': '18-12a.'},
            {'name': 'PREV FORM 11 DATE', 'number': '19-12a.'},
            {'name': 'NAME/CANDIDATE/TREAS (as signed)', 'number': '20'},
            {'name': 'Signed', 'number': '21-'},
    ]
