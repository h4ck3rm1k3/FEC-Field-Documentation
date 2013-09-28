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
            {'name': 'REPORT CODE', 'number': '10'},
            {'name': 'AMENDMENT DATE', 'number': '11'},
            {'name': 'COVERAGE FROM DATE', 'number': '12'},
            {'name': 'COVERAGE THROUGH DATE', 'number': '13'},
            {'name': 'TOTAL DONATIONS ACCEPTED', 'number': '14-5'},
            {'name': 'TOTAL DONATIONS REFUNDED', 'number': '15-6'},
            {'name': 'NET DONATIONS', 'number': '16-7'},
            {'name': 'DESIGNATED LAST NAME', 'number': '17'},
            {'name': 'DESIGNATED FIRST NAME', 'number': '18'},
            {'name': 'DESIGNATED MIDDLE NAME', 'number': '19'},
            {'name': 'DESIGNATED PREFIX', 'number': '20'},
            {'name': 'DESIGNATED SUFFIX', 'number': '21'},
            {'name': 'DATE SIGNED', 'number': '22'},
    ]
        self.fields_names = self.hash_names(self.fields)
