import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'TRANSACTION ID NUMBER', 'number': '3'},
            {'name': 'COMMUNICATION TYPE', 'number': '4'},
            {'name': 'COMMUNICATION TYPE - OTHER DESCRIPTION', 'number': '5'},
            {'name': 'COMMUNICATION CLASS', 'number': '6'},
            {'name': 'COMMUNICATION DATE', 'number': '7'},
            {'name': 'COMMUNICATION COST (per candidate)', 'number': '8'},
            {'name': 'ELECTION CODE', 'number': '9'},
            {'name': 'ELECTION OTHER DESCRIPTION', 'number': '10'},
            {'name': 'SUPPORT/OPPOSE', 'number': '11'},
            {'name': 'S/O CANDIDATE ID NUMBER', 'number': '12'},
            {'name': 'S/O CANDIDATE LAST NAME', 'number': '13'},
            {'name': 'S/O CANDIDATE FIRST NAME', 'number': '14'},
            {'name': 'S/O CANDIDATE MIDDLE NAME', 'number': '15'},
            {'name': 'S/O CANDIDATE PREFIX', 'number': '16'},
            {'name': 'S/O CANDIDATE SUFFIX', 'number': '17'},
            {'name': 'S/O CANDIDATE OFFICE', 'number': '18'},
            {'name': 'S/O CANDIDATE STATE', 'number': '19'},
            {'name': 'S/O CANDIDATE DISTRICT', 'number': '20'},
    ]
        self.fields_names = self.hash_names(self.fields)
