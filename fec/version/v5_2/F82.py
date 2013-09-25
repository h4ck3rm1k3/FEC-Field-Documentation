from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC CMTE ID', 'number': '2'},
            {'name': 'CREDITOR CODE', 'number': '3'},
            {'name': 'NAME (Contributor/Lender)', 'number': '4'},
            {'name': 'STREET 1', 'number': '5'},
            {'name': 'STREET 2', 'number': '6'},
            {'name': 'CITY', 'number': '7'},
            {'name': 'STATE', 'number': '8'},
            {'name': 'ZIP', 'number': '9'},
            {'name': 'Incurred', 'number': '10-'},
            {'name': 'AMOUNT OWED TO', 'number': '11'},
            {'name': 'AMOUNT OFFERED IN', 'number': '12'},
            {'name': 'Initial Terms And Nature Of Debt', 'number': '13-A. '},
            {'name': 'Efforts Made By Cmte To Pay Debt', 'number': '14-B. '},
            {'name': 'Steps Taken By Creditor To Collect', 'number': '15-C. '},
            {'name': 'effort made by creditor to collect...', 'number': '16-D. '},
            {'name': 'N If No Explain', 'number': '17-D. '},
            {'name': 'terms of debt settlement comparable...', 'number': '18-E. '},
            {'name': 'N If No Explain', 'number': '19-E. '},
            {'name': 'FEC COMMITTEE ID NUMBER', 'number': '20'},
            {'name': 'FEC CANDIDATE ID NUMBER', 'number': '21'},
            {'name': 'CANDIDATE NAME', 'number': '22'},
            {'name': 'CAN/OFFICE', 'number': '23'},
            {'name': 'CAN/STATE', 'number': '24'},
            {'name': 'CAN/DIST', 'number': '25'},
            {'name': 'NAME of creditor or representative', 'number': '26'},
            {'name': 'Signed', 'number': '27-'},
            {'name': 'AMENDED CD', 'number': '28'},
            {'name': 'TRAN ID', 'number': '29'},
    ]
        self.fields_names = self.hash_names(self.fields)
