from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER COMMITTEE ID', 'number': '2'},
            {'name': 'TRANSACTION ID NUMBER', 'number': '3'},
            {'name': 'RECORD ID NUMBER (for account name)', 'number': '4'},
            {'name': 'ACCOUNT NAME', 'number': '5'},
            {'name': 'Bank Account ID Number', 'number': '6'},
            {'name': 'COVERAGE FROM DATE', 'number': '7'},
            {'name': 'COVERAGE THROUGH DATE', 'number': '8'},
            {'name': 'Total Receipts', 'number': '9-1.'},
            {'name': 'Transfers to FED or allocation', 'number': '10-2.'},
            {'name': 'Transfers to state/local Party organizations', 'number': '11-3.'},
            {'name': 'Direct state/local candidate support', 'number': '12-4.'},
            {'name': 'Other Disbursements', 'number': '13-5.'},
            {'name': 'Total Disbursements', 'number': '14-6.'},
            {'name': 'Beginning COH', 'number': '15-7.'},
            {'name': 'Receipts', 'number': '16-8.'},
            {'name': 'Subtotal', 'number': '17-9.'},
            {'name': 'Disbursements', 'number': '18-10.'},
            {'name': 'Ending COH', 'number': '19-11.'},
            {'name': 'Total receipts', 'number': '20-1.'},
            {'name': 'Transfers to FED or allocation', 'number': '21-2.'},
            {'name': 'Transfers to state/local Party organizations', 'number': '22-3.'},
            {'name': 'Direct state/local candidate support', 'number': '23-4.'},
            {'name': 'Other Disbursements', 'number': '24-5.'},
            {'name': 'Total Disbursements', 'number': '25-6.'},
            {'name': 'Beginning COH (as of Jan 1)', 'number': '26-7.'},
            {'name': 'Receipts', 'number': '27-8.'},
            {'name': 'Subtotal', 'number': '28-9.'},
            {'name': 'Disbursements', 'number': '29-10.'},
            {'name': 'Ending COH', 'number': '30-11.'},
    ]
        self.fields_names = self.hash_names(self.fields)
