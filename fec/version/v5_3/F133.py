from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC CMTE ID', 'number': '2'},
            {'name': 'ENTITY TYPE', 'number': '3'},
            {'name': 'CONTRIB ORGANIZATION NAME', 'number': '4'},
            {'name': 'CONTRIBUTOR LAST NAME', 'number': '5'},
            {'name': 'CONTRIBUTOR FIRST NAME', 'number': '6'},
            {'name': 'CONTRIBUTOR MIDDLE NAME', 'number': '7'},
            {'name': 'CONTRIBUTOR PREFIX', 'number': '8'},
            {'name': 'CONTRIBUTOR SUFFIX', 'number': '9'},
            {'name': 'STREET 1', 'number': '10'},
            {'name': 'STREET 2', 'number': '11'},
            {'name': 'CITY', 'number': '12'},
            {'name': 'STATE', 'number': '13'},
            {'name': 'ZIP', 'number': '14'},
            {'name': 'DATE OF EXPENDITURE', 'number': '15'},
            {'name': 'AMOUNT OF EXPENDITURE', 'number': '16'},
            {'name': 'INTERNAL USE ONLY', 'number': '17'},
            {'name': 'TRAN ID', 'number': '18'},
            {'name': 'BACK REF TRAN ID', 'number': '19'},
            {'name': 'BACK REF SCHED NAME', 'number': '20'},
    ]
