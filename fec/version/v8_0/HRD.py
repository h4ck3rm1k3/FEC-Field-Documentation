import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'Record Type', 'number': '1'},
            {'name': 'Type', 'number': '2-EF'},
            {'name': 'FEC Version #', 'number': '3'},
            {'name': 'Soft Name', 'number': '4'},
            {'name': 'Soft Ver', 'number': '5'},
            {'name': 'Rpt ID', 'number': '6'},
            {'name': 'Rpt Number', 'number': '7'},
            {'name': 'HDRcomment', 'number': '8'},
    ]
        self.fields_names = self.hash_names(self.fields)
