from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'COMMITTEE NAME', 'number': '3'},
            {'name': 'STREET 1', 'number': '4'},
            {'name': 'STREET 2', 'number': '5'},
            {'name': 'CITY', 'number': '6'},
            {'name': 'STATE', 'number': '7'},
            {'name': 'ZIP', 'number': '8'},
            {'name': 'TREASURER LAST NAME', 'number': '9'},
            {'name': 'TREASURER FIRST NAME', 'number': '10'},
            {'name': 'TREASURER MIDDLE NAME', 'number': '11'},
            {'name': 'TREASURER PREFIX', 'number': '12'},
            {'name': 'TREASURER SUFFIX', 'number': '13'},
            {'name': 'DATE SIGNED', 'number': '14'},
            {'name': 'TEXT CODE', 'number': '15'},
    ]
