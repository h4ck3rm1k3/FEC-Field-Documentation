from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'REPORT TYPE (24/48 Hour)', 'number': '3'},
            {'name': 'ORIGINAL AMENDMENT DATE', 'number': '4'},
            {'name': 'COMMITTEE NAME', 'number': '5'},
            {'name': 'STREET 1', 'number': '6'},
            {'name': 'STREET 2', 'number': '7'},
            {'name': 'CITY', 'number': '8'},
            {'name': 'STATE', 'number': '9'},
            {'name': 'ZIP', 'number': '10'},
            {'name': 'TREASURER LAST NAME', 'number': '11'},
            {'name': 'TREASURER FIRST NAME', 'number': '12'},
            {'name': 'TREASURER MIDDLE NAME', 'number': '13'},
            {'name': 'TREASURER PREFIX', 'number': '14'},
            {'name': 'TREASURER SUFFIX', 'number': '15'},
            {'name': 'DATE SIGNED', 'number': '16'},
    ]
        self.fields_names = self.hash_names(self.fields)
