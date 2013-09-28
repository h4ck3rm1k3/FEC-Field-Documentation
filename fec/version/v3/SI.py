import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC CMTE ID', 'number': '2'},
            {'name': 'Bank Account ID Number', 'number': '3'},
            {'name': 'NAME (Of Account)', 'number': '4'},
            {'name': 'Coverage From', 'number': '5-'},
            {'name': 'Coverage To', 'number': '6-'},
            {'name': 'Total Receipts', 'number': '7-1.'},
            {'name': 'Transfers to FED or allocation', 'number': '8-2.'},
            {'name': 'Transfers to state/local Party organizations', 'number': '9-3.'},
            {'name': 'Direct state/local candidate support', 'number': '10-4.'},
            {'name': 'Other Disbursements', 'number': '11-5.'},
            {'name': 'Total Disbursements', 'number': '12-6.'},
            {'name': 'Beginning COH', 'number': '13-7.'},
            {'name': 'Receipts', 'number': '15-8.'},
            {'name': 'Subtotal', 'number': '15-9.'},
            {'name': 'Disbursements', 'number': '16-10.'},
            {'name': 'Ending COH', 'number': '17-11.'},
            {'name': 'Total receipts', 'number': '18-1.'},
            {'name': 'Transfers to FED or allocation', 'number': '19-2.'},
            {'name': 'Transfers to state/local Party organizations', 'number': '20-3.'},
            {'name': 'Direct state/local candidate support', 'number': '21-4.'},
            {'name': 'Other Disbursements', 'number': '22-5.'},
            {'name': 'Total Disbursements', 'number': '23-6.'},
            {'name': 'Beginning COH (as of Jan 1)', 'number': '24-7.'},
            {'name': 'Receipts', 'number': '25-8.'},
            {'name': 'Subtotal', 'number': '26-9.'},
            {'name': 'Disbursements', 'number': '27-10.'},
            {'name': 'Ending COH', 'number': '28-11.'},
            {'name': 'AMENDED CD', 'number': '29'},
            {'name': 'TRAN ID', 'number': '30'},
            {'name': 'Account Number for Account named in Field #4', 'number': '31'},
    ]
        self.fields_names = self.hash_names(self.fields)
