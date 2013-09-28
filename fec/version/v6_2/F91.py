import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'TRANSACTION ID NUMBER', 'number': '3'},
            {'name': 'CONTROLLER LAST NAME (Share/Exer Control)', 'number': '4'},
            {'name': 'CONTROLLER FIRST NAME', 'number': '5'},
            {'name': 'CONTROLLER MIDDLE NAME', 'number': '6'},
            {'name': 'CONTROLLER PREFIX', 'number': '7'},
            {'name': 'CONTROLLER SUFFIX', 'number': '8'},
            {'name': 'CONTROLLER STREET 1', 'number': '9'},
            {'name': 'CONTROLLER STREET 2', 'number': '10'},
            {'name': 'CONTROLLER CITY', 'number': '11'},
            {'name': 'CONTROLLER STATE', 'number': '12'},
            {'name': 'CONTROLLER ZIP', 'number': '13'},
            {'name': 'CONTROLLER EMPLOYER', 'number': '14'},
            {'name': 'CONTROLLER OCCUPATION', 'number': '15'},
    ]
        self.fields_names = self.hash_names(self.fields)
