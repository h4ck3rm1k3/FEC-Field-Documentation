import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'TRANSACTION ID NUMBER', 'number': '3'},
            {'name': 'BACK REFERENCE TRAN ID', 'number': '4'},
            {'name': 'BACK REFERENCE SCHED NAME', 'number': '5'},
            {'name': 'CANDIDATE ID NUMBER', 'number': '6'},
            {'name': 'CANDIDATE LAST NAME', 'number': '7'},
            {'name': 'CANDIDATE FIRST NAME', 'number': '8'},
            {'name': 'CANDIDATE MIDDLE NAME', 'number': '9'},
            {'name': 'CANDIDATE PREFIX', 'number': '10'},
            {'name': 'CANDIDATE SUFFIX', 'number': '11'},
            {'name': 'CANDIDATE OFFICE', 'number': '12'},
            {'name': 'CANDIDATE STATE', 'number': '13'},
            {'name': 'CANDIDATE DIST', 'number': '14'},
            {'name': 'ELECTION CODE', 'number': '15'},
            {'name': 'ELECTION OTHER DESCRIPTION', 'number': '16'},
    ]
        self.fields_names = self.hash_names(self.fields)
