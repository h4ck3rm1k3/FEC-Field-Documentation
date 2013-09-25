from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'JOINT FUND PARTICIPANT Committee NAME', 'number': '3-5.'},
            {'name': 'JOINT FUND PARTICIPANT Committee FEC-ID', 'number': '4-5.'},
            {'name': 'AFFILIATED Committee ID NUM', 'number': '5-6.'},
            {'name': 'AFFILIATED Committee NAME', 'number': '6-6.'},
            {'name': 'AFFILIATED STREET 1', 'number': '7-6.'},
            {'name': 'AFFILIATED STREET 2', 'number': '8-6.'},
            {'name': 'AFFILIATED CITY', 'number': '9-6.'},
            {'name': 'AFFILIATED STATE', 'number': '10-6.'},
            {'name': 'AFFILIATED ZIP', 'number': '11-6.'},
            {'name': 'AFFILIATED RELATIONSHIP CODE', 'number': '12-6.'},
            {'name': 'AGENT LAST NAME', 'number': '13-8.'},
            {'name': 'AGENT FIRST NAME', 'number': '14-8.'},
            {'name': 'AGENT MIDDLE NAME', 'number': '15-8.'},
            {'name': 'AGENT PREFIX', 'number': '16-8.'},
            {'name': 'AGENT SUFFIX', 'number': '17-8.'},
            {'name': 'AGENT STREET 1', 'number': '18-8.'},
            {'name': 'AGENT STREET 2', 'number': '19-8.'},
            {'name': 'AGENT CITY', 'number': '20-8.'},
            {'name': 'AGENT STATE', 'number': '21-8.'},
            {'name': 'AGENT ZIP', 'number': '22-8.'},
            {'name': 'AGENT TITLE', 'number': '23-8.'},
            {'name': 'AGENT TELEPHONE', 'number': '24-8.'},
            {'name': 'BANK NAME', 'number': '25-9.'},
            {'name': 'BANK STREET 1', 'number': '26-9.'},
            {'name': 'BANK STREET 2', 'number': '26-9.'},
            {'name': 'BANK CITY', 'number': '28-9.'},
            {'name': 'BANK STATE', 'number': '29-9.'},
            {'name': 'BANK ZIP', 'number': '30-9.'},
    ]
        self.fields_names = self.hash_names(self.fields)
