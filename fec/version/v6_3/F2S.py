import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER CANDIDATE ID NUMBER', 'number': '2'},
            {'name': 'AUTH COMMITTEE ID NUMBER', 'number': '3'},
            {'name': 'AUTH COMMITTEE NAME', 'number': '4'},
            {'name': 'AUTH STREET 1', 'number': '5'},
            {'name': 'AUTH STREET 2', 'number': '6'},
            {'name': 'AUTH CITY', 'number': '7'},
            {'name': 'AUTH STATE', 'number': '8'},
            {'name': 'AUTH ZIP', 'number': '9'},
    ]
        self.fields_names = self.hash_names(self.fields)
