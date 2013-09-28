import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'REPORT TYPE (24/48 Hour)', 'number': '3'},
            {'name': 'COMMITTEE NAME', 'number': '4'},
            {'name': 'STREET 1', 'number': '5'},
            {'name': 'STREET 2', 'number': '6'},
            {'name': 'CITY', 'number': '7'},
            {'name': 'STATE', 'number': '8'},
            {'name': 'ZIP', 'number': '9'},
            {'name': 'TREASURER LAST NAME', 'number': '10'},
            {'name': 'TREASURER FIRST NAME', 'number': '11'},
            {'name': 'TREASURER MIDDLE NAME', 'number': '12'},
            {'name': 'TREASURER PREFIX', 'number': '13'},
            {'name': 'TREASURER SUFFIX', 'number': '14'},
            {'name': 'DATE SIGNED', 'number': '15'},
    ]
        self.fields_names = self.hash_names(self.fields)
