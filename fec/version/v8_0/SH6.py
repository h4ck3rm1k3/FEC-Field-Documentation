import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'TRANSACTION ID NUMBER', 'number': '3'},
            {'name': 'BACK REFERENCE TRAN ID NUMBER', 'number': '4'},
            {'name': 'BACK REFERENCE SCHED NAME', 'number': '5'},
            {'name': 'ENTITY TYPE', 'number': '6'},
            {'name': 'PAYEE ORGANIZATION NAME', 'number': '7'},
            {'name': 'PAYEE LAST NAME', 'number': '8'},
            {'name': 'PAYEE FIRST NAME', 'number': '9'},
            {'name': 'PAYEE MIDDLE NAME', 'number': '10'},
            {'name': 'PAYEE PREFIX', 'number': '11'},
            {'name': 'PAYEE SUFFIX', 'number': '12'},
            {'name': 'PAYEE STREET 1', 'number': '13'},
            {'name': 'PAYEE STREET 2', 'number': '14'},
            {'name': 'PAYEE CITY', 'number': '15'},
            {'name': 'PAYEE STATE', 'number': '16'},
            {'name': 'PAYEE ZIP', 'number': '17'},
            {'name': 'ACCOUNT/EVENT IDENTIFIER', 'number': '18'},
            {'name': 'EXPENDITURE DATE', 'number': '19'},
            {'name': 'TOTAL FED-LEVIN AMOUNT', 'number': '20'},
            {'name': 'FEDERAL SHARE', 'number': '21'},
            {'name': 'LEVIN SHARE', 'number': '22'},
            {'name': 'ACTIVITY/EVENT TOTAL YTD', 'number': '23'},
            {'name': 'EXPENDITURE PURPOSE DESCRIP', 'number': '24'},
            {'name': 'CATEGORY CODE', 'number': '25'},
            {'name': 'Activity Is Voter Registration', 'number': '26-'},
            {'name': 'Activity GOTV', 'number': '27-'},
            {'name': 'Activity Is Voter ID', 'number': '28-'},
            {'name': 'Activity is Generic Campaign', 'number': '29-'},
            {'name': 'MEMO CODE', 'number': '30'},
            {'name': 'MEMO TEXT/DESCRIPTION', 'number': '31'},
    ]
        self.fields_names = self.hash_names(self.fields)
