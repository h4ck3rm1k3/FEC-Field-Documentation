import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'TRANSACTION ID NUMBER', 'number': '3'},
            {'name': 'BACK REFERENCE TRAN ID NUMBER', 'number': '4'},
            {'name': 'GUARANTOR LAST NAME', 'number': '5'},
            {'name': 'GUARANTOR FIRST NAME', 'number': '6'},
            {'name': 'GUARANTOR MIDDLE NAME', 'number': '7'},
            {'name': 'GUARANTOR PREFIX', 'number': '8'},
            {'name': 'GUARANTOR SUFFIX', 'number': '9'},
            {'name': 'GUARANTOR STREET 1', 'number': '10'},
            {'name': 'GUARANTOR STREET 2', 'number': '11'},
            {'name': 'GUARANTOR CITY', 'number': '12'},
            {'name': 'GUARANTOR STATE', 'number': '13'},
            {'name': 'GUARANTOR ZIP', 'number': '14'},
            {'name': 'GUARANTOR EMPLOYER', 'number': '15'},
            {'name': 'GUARANTOR OCCUPATION', 'number': '16'},
            {'name': 'GUARANTEED AMOUNT', 'number': '17'},
    ]
        self.fields_names = self.hash_names(self.fields)
