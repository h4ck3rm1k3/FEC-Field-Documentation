from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC COMMITTEE ID', 'number': '2'},
            {'name': 'CANDIDATE NAME', 'number': '3'},
            {'name': 'CANDIDATE ID', 'number': '4'},
            {'name': 'CAN/OFFICE', 'number': '5'},
            {'name': 'CANDIDATE STATE', 'number': '6'},
            {'name': 'CANDIDATE DISTRICT', 'number': '7'},
            {'name': 'COMMITTEE NAME', 'number': '8'},
            {'name': 'STREET 1', 'number': '9'},
            {'name': 'STREET 2', 'number': '10'},
            {'name': 'CITY', 'number': '11'},
            {'name': 'STATE', 'number': '12'},
            {'name': 'ZIP', 'number': '13'},
            {'name': 'PREVIOUS EXPENDITURE AGGREGATE', 'number': '14'},
            {'name': 'EXP TOTAL THIS REPORT', 'number': '15'},
            {'name': 'EXP TOTAL CYCLE-TO-DATE', 'number': '16'},
            {'name': 'as signed', 'number': '17-NAME/CANDI'},
            {'name': 'Signed', 'number': '18-'},
            {'name': 'MEETS F6 FILING REQUIREMENTS', 'number': '19'},
            {'name': 'CANDIDATE EMPLOYER', 'number': '20'},
            {'name': 'CANDIDATE OCCUPATION', 'number': '21'},
    ]
