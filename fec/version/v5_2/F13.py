import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC CMTE ID', 'number': '2'},
            {'name': 'COMMITTEE NAME', 'number': '3'},
            {'name': 'STREET 1', 'number': '4'},
            {'name': 'STREET 2', 'number': '5'},
            {'name': 'CITY', 'number': '6'},
            {'name': 'STATE', 'number': '7'},
            {'name': 'ZIP', 'number': '8'},
            {'name': 'CHG OF ADDRESS', 'number': '9'},
            {'name': 'RPTCODE', 'number': '10'},
            {'name': 'Of Amendment', 'number': '11-'},
            {'name': 'Coverage From', 'number': '12-'},
            {'name': 'Coverage To', 'number': '13-'},
            {'name': 'Total Donations Accepted', 'number': '14-5.'},
            {'name': 'Total Donations Refund', 'number': '15-6.'},
            {'name': 'Net Donations', 'number': '16-7.'},
            {'name': 'DESIGNATED OFFICER --LAST NAME (as signed)', 'number': '17'},
            {'name': 'DESIGNATED OFFICER -- FIRST NAME (as signed)', 'number': '18'},
            {'name': 'DESIGNATED OFFICER --MIDDLE NAME (as signed)', 'number': '19'},
            {'name': 'DESIGNATED OFFICER -- PREFIX (as signed)', 'number': '20'},
            {'name': 'DESIGNATED OFFICER -- SUFFIX (as signed)', 'number': '21'},
            {'name': 'Signed', 'number': '22-'},
    ]
        self.fields_names = self.hash_names(self.fields)
