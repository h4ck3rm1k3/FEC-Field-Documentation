from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FEC COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'COMMITTEE NAME', 'number': '3'},
            {'name': 'STREET 1', 'number': '4'},
            {'name': 'STREET 2', 'number': '5'},
            {'name': 'CITY', 'number': '6'},
            {'name': 'STATE', 'number': '7'},
            {'name': 'ZIP', 'number': '8'},
            {'name': 'CASH ON HAND', 'number': '9-1.'},
            {'name': 'as of', 'number': '10-1(a)'},
            {'name': 'Total assets to be liquidated', 'number': '11-2.'},
            {'name': 'Total (assets)', 'number': '12-3.'},
            {'name': 'Year to date receipts', 'number': '13-4.'},
            {'name': 'Year to date disbursements', 'number': '14-5.'},
            {'name': 'Total amount of debts owed by cmte', 'number': '15-6.'},
            {'name': 'Total number of creditors owed', 'number': '16-7.'},
            {'name': 'Number of creditors in part II of this plan', 'number': '17-8.'},
            {'name': 'Total amount of debts owed to creditors in part II of plan', 'number': '18-9.'},
            {'name': 'Total amount to be paid to creditors in part II of this plan', 'number': '19-10.'},
            {'name': 'Is the cmte terminating activities', 'number': '20-11. '},
            {'name': 'PLANNED FOR TERMINATION RPT', 'number': '21-11.Y '},
            {'name': 'If this is an authorized committee are there other authorized committees.', 'number': '22-12. '},
            {'name': 'Y IF YES list AUTH CMTE ID/NAMES', 'number': '23-12. '},
            {'name': 'have sufficient funds to pay total amount indicated in this plan', 'number': '24-13. '},
            {'name': 'N If NO what steps will be taken to obtain the funds', 'number': '25-13. '},
            {'name': 'Has the committee filed previous debt settlement plans', 'number': '26-14. '},
            {'name': "After disposing of all the committee's debts and obligations; will there be any residual funds?", 'number': '27-15. '},
            {'name': 'IF YES how will the funds be disbursed', 'number': '28-15. '},
            {'name': 'PART IIIYESNO (Does committee have sufficient funds to pay the remaining amts to be paid or offered.', 'number': '29'},
            {'name': 'N If no, what steps will be taken to obtain the funds.', 'number': '30-PART III '},
            {'name': 'Treasurer\xe2\x80\x99s NAME', 'number': '31'},
            {'name': 'SIGNED', 'number': '32-'},
    ]
        self.fields_names = self.hash_names(self.fields)
