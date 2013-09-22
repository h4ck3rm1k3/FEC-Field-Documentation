from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        self.fields = [
            {'name': 'Record Type', 'number': '1'},
            {'name': 'Type', 'number': '2-EF'},
            {'name': 'FEC Ver', 'number': '3'},
            {'name': 'Soft Name', 'number': '4'},
            {'name': 'Soft Ver', 'number': '5'},
            {'name': 'Name Delim', 'number': '6'},
            {'name': 'Rpt ID', 'number': '7'},
            {'name': 'Rpt Number', 'number': '8'},
            {'name': 'HDRcomment', 'number': '9'},
    ]
