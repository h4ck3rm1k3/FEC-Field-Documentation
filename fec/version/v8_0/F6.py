import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'ORIGINAL AMENDMENT DATE', 'number': '3'},
            {'name': 'COMMITTEE NAME', 'number': '4'},
            {'name': 'STREET 1', 'number': '5'},
            {'name': 'STREET 2', 'number': '6'},
            {'name': 'CITY', 'number': '7'},
            {'name': 'STATE', 'number': '8'},
            {'name': 'ZIP', 'number': '9'},
            {'name': 'CANDIDATE ID NUMBER', 'number': '10'},
            {'name': 'CANDIDATE LAST NAME', 'number': '11'},
            {'name': 'CANDIDATE FIRST NAME', 'number': '12'},
            {'name': 'CANDIDATE MIDDLE NAME', 'number': '13'},
            {'name': 'CANDIDATE PREFIX', 'number': '14'},
            {'name': 'CANDIDATE SUFFIX', 'number': '15'},
            {'name': 'CANDIDATE OFFICE', 'number': '16'},
            {'name': 'CANDIDATE STATE', 'number': '17'},
            {'name': 'CANDIDATE DISTRICT', 'number': '18'},
            {'name': 'SIGNER LAST NAME', 'number': '19'},
            {'name': 'SIGNER FIRST NAME', 'number': '20'},
            {'name': 'SIGNER MIDDLE NAME', 'number': '21'},
            {'name': 'SIGNER PREFIX', 'number': '22'},
            {'name': 'SIGNER SUFFIX', 'number': '23'},
            {'name': 'DATE SIGNED', 'number': '24'},
    ]
        self.fields_names = self.hash_names(self.fields)
