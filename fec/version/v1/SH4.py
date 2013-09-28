import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FEC COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'PAYEE', 'number': '3-'},
            {'name': 'STREET 1', 'number': '4'},
            {'name': 'STREET 2', 'number': '5'},
            {'name': 'CITY', 'number': '6'},
            {'name': 'STATE', 'number': '7'},
            {'name': 'ZIP', 'number': '8'},
            {'name': 'PURPOSE/EVENT', 'number': '9'},
            {'name': 'EVENT NUMBER', 'number': '10'},
            {'name': 'DATE', 'number': '11'},
            {'name': 'TOTAL AMOUNT', 'number': '12'},
            {'name': 'FEDERAL SHARE', 'number': '13'},
            {'name': 'NON-FEDERAL SHARE', 'number': '14'},
            {'name': 'ACTIVITY IS ADMIN/VOTER DRIVE', 'number': '15-'},
            {'name': 'ACTIVITY IS FUNDRAISING', 'number': '16-'},
            {'name': 'ACTIVITY IS EXEMPT', 'number': '17-'},
            {'name': 'ACT DIRECT CAN SUPPORT', 'number': '18-'},
            {'name': 'EVENT YEAR-TO-DATE', 'number': '19'},
            {'name': 'ADDITIONAL DESCRIPTION', 'number': '20'},
            {'name': 'AMENDED', 'number': '21'},
    ]
        self.fields_names = self.hash_names(self.fields)
