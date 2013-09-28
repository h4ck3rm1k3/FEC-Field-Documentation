import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'ORGANIZATION NAME', 'number': '3'},
            {'name': 'ORGANIZATION STREET 1', 'number': '4'},
            {'name': 'ORGANIZATION STREET 2', 'number': '5'},
            {'name': 'ORGANIZATION CITY', 'number': '6'},
            {'name': 'ORGANIZATION STATE', 'number': '7'},
            {'name': 'ORGANIZATION ZIP', 'number': '8'},
            {'name': 'ORGANIZATION TYPE', 'number': '9'},
            {'name': 'REPORT CODE', 'number': '10'},
            {'name': 'DATE OF ELECTION', 'number': '11'},
            {'name': 'STATE OF ELECTION', 'number': '12'},
            {'name': 'COVERAGE FROM DATE', 'number': '13'},
            {'name': 'COVERAGE THROUGH DATE', 'number': '14'},
            {'name': 'TOTAL COSTS', 'number': '15'},
            {'name': 'PERSON DESIGNATED TO SIGN LAST NAME', 'number': '16'},
            {'name': 'PERSON DESIGNATED TO SIGN FIRST NAME', 'number': '17'},
            {'name': 'PERSON DESIGNATED TO SIGN MIDDLE NAME', 'number': '18'},
            {'name': 'PERSON DESIGNATED TO SIGN PREFIX', 'number': '19'},
            {'name': 'PERSON DESIGNATED TO SIGN SUFFIX', 'number': '20'},
            {'name': 'PERSON DESIGNATED TO SIGN TITLE', 'number': '21'},
            {'name': 'DATE SIGNED', 'number': '22'},
    ]
        self.fields_names = self.hash_names(self.fields)
