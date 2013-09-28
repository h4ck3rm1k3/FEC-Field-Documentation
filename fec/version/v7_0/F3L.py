import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'COMMITTEE NAME', 'number': '3'},
            {'name': 'CHANGE OF ADDRESS', 'number': '4'},
            {'name': 'STREET 1', 'number': '5'},
            {'name': 'STREET 2', 'number': '6'},
            {'name': 'CITY', 'number': '7'},
            {'name': 'STATE', 'number': '8'},
            {'name': 'ZIP', 'number': '9'},
            {'name': 'ELECTION STATE', 'number': '10'},
            {'name': 'ELECTION DISTRICT', 'number': '11'},
            {'name': 'REPORT CODE', 'number': '12'},
            {'name': 'DATE OF ELECTION', 'number': '13'},
            {'name': 'STATE OF ELECTION', 'number': '14'},
            {'name': 'SEMI-ANNUAL PERIOD - Sect 5(c) or (d)', 'number': '15'},
            {'name': 'COVERAGE FROM DATE', 'number': '16'},
            {'name': 'COVERAGE THROUGH DATE', 'number': '17'},
            {'name': 'SEMI-ANNUAL JAN-JUN - Sect 6(b)', 'number': '18'},
            {'name': 'SEMI-ANNUAL JUL-DEC - Sect 6(b)', 'number': '19'},
            {'name': 'QTR/MON/POST BUNDLED CONTRIBUTIONS', 'number': '20'},
            {'name': 'SEMI-ANNUAL BUNDLED CONTRIBS', 'number': '21'},
            {'name': 'TREASURER LAST NAME', 'number': '22'},
            {'name': 'TREASURER FIRST NAME', 'number': '23'},
            {'name': 'TREASURER MIDDLE NAME', 'number': '24'},
            {'name': 'TREASURER PREFIX', 'number': '25'},
            {'name': 'TREASURER SUFFIX', 'number': '26'},
            {'name': 'DATE SIGNED', 'number': '27'},
    ]
        self.fields_names = self.hash_names(self.fields)
