import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': "FILER'S FEC ID NUMBER", 'number': '2'},
            {'name': 'ENTITY TYPE', 'number': '3'},
            {'name': 'ORGANIZATION NAME', 'number': '4'},
            {'name': 'INDIVIDUAL LAST NAME', 'number': '5'},
            {'name': 'INDIVIDUAL FIRST NAME', 'number': '6'},
            {'name': 'INDIVIDUAL MIDDLE NAME', 'number': '7'},
            {'name': 'INDIVIDUAL PREFIX', 'number': '8'},
            {'name': 'INDIVIDUAL SUFFIX', 'number': '9'},
            {'name': 'CHANGE OF ADDRESS', 'number': '10'},
            {'name': 'STREET 1', 'number': '11'},
            {'name': 'STREET 2', 'number': '12'},
            {'name': 'CITY', 'number': '13'},
            {'name': 'STATE', 'number': '14'},
            {'name': 'ZIP', 'number': '15'},
            {'name': 'Qualified Non-Profit Corporation', 'number': '16-'},
            {'name': 'INDIVIDUAL EMPLOYER', 'number': '17'},
            {'name': 'INDIVIDUAL OCCUPATION', 'number': '18'},
            {'name': 'REPORT CODE', 'number': '19'},
            {'name': 'HOUR 48HOUR CODE', 'number': '20-24'},
            {'name': 'COVERAGE FROM DATE', 'number': '21'},
            {'name': 'COVERAGE THROUGH DATE', 'number': '22'},
            {'name': 'TOTAL CONTRIBUTION', 'number': '23'},
            {'name': 'TOTAL INDEPENDENT EXPENDITURE', 'number': '24'},
            {'name': 'PERSON COMPLETING LAST NAME', 'number': '25'},
            {'name': 'PERSON COMPLETING FIRST NAME', 'number': '26'},
            {'name': 'PERSON COMPLETING MIDDLE NAME', 'number': '27'},
            {'name': 'PERSON COMPLETING PREFIX', 'number': '28'},
            {'name': 'PERSON COMPLETING SUFFIX', 'number': '29'},
            {'name': 'DATE SIGNED', 'number': '30'},
    ]
        self.fields_names = self.hash_names(self.fields)
