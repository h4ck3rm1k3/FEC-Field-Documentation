import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'COMMITTEE NAME', 'number': '3'},
            {'name': 'STREET 1', 'number': '4'},
            {'name': 'STREET 2', 'number': '5'},
            {'name': 'CITY', 'number': '6'},
            {'name': 'STATE', 'number': '7'},
            {'name': 'ZIP', 'number': '8'},
            {'name': 'CANDIDATE ID NUMBER', 'number': '9'},
            {'name': 'CANDIDATE LAST NAME', 'number': '10'},
            {'name': 'CANDIDATE FIRST NAME', 'number': '11'},
            {'name': 'CANDIDATE MIDDLE NAME', 'number': '12'},
            {'name': 'CANDIDATE PREFIX', 'number': '13'},
            {'name': 'CANDIDATE SUFFIX', 'number': '14'},
            {'name': 'CANDIDATE OFFICE', 'number': '15'},
            {'name': 'CANDIDATE STATE', 'number': '16'},
            {'name': 'CANDIDATE DISTRICT', 'number': '17'},
            {'name': 'SIGNER LAST NAME', 'number': '18'},
            {'name': 'SIGNER FIRST NAME', 'number': '19'},
            {'name': 'SIGNER MIDDLE NAME', 'number': '20'},
            {'name': 'SIGNER PREFIX', 'number': '21'},
            {'name': 'SIGNER SUFFIX', 'number': '22'},
            {'name': 'DATE SIGNED', 'number': '23'},
    ]
        self.fields_names = self.hash_names(self.fields)
