import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FEC COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'COMMITTEE NAME', 'number': '3'},
            {'name': 'STREET 1', 'number': '4'},
            {'name': 'STREET 2', 'number': '5'},
            {'name': 'CITY', 'number': '6'},
            {'name': 'STATE', 'number': '7'},
            {'name': 'ZIP', 'number': '8'},
            {'name': 'CHG OF ADDRESS', 'number': '9'},
            {'name': 'ELECTION STATE', 'number': '10'},
            {'name': 'ELECTION DISTRICT', 'number': '11'},
            {'name': 'RPTCODE', 'number': '12'},
            {'name': 'RPTPGI', 'number': '13'},
            {'name': 'OF ELECTION', 'number': '14-'},
            {'name': 'STATE (OF ELECTION)', 'number': '15'},
            {'name': 'ACTIVITY PRIMARY', 'number': '16'},
            {'name': 'ACTIVITY GENERAL', 'number': '17'},
            {'name': 'ACTIVITY SPECIAL', 'number': '18'},
            {'name': 'ACTIVITY RUNOFF', 'number': '19'},
            {'name': 'COVERAGE FROM', 'number': '20-'},
            {'name': 'COVERAGE TO', 'number': '21-'},
            {'name': 'Total Contributions (NO Loans)', 'number': '22-(6a)'},
            {'name': 'Total Contribution Refunds', 'number': '23-(6b)'},
            {'name': 'Net Contributions', 'number': '24-(6c)'},
            {'name': 'Total Operating Expenditures', 'number': '25-(7a)'},
            {'name': 'Total Offset to Operating Expenditures', 'number': '26-(7b)'},
            {'name': 'NET Operating Expenditures', 'number': '27-(7c)'},
            {'name': 'Cash on Hand Close of reporting period', 'number': '28-8'},
            {'name': 'DEBTS TO ( Totals from SCH C and/or D)', 'number': '29-9'},
            {'name': 'DEBTS BY (Totals from SCH C and/or D)', 'number': '30-10'},
            {'name': 'Individuals Itemized', 'number': '31-11(ai)'},
            {'name': 'Individuals UnItemized', 'number': '32-11(aii)'},
            {'name': 'Individual Contribution Total', 'number': '33-11(aiii)'},
            {'name': 'Political Party Committees', 'number': '34-11(b)'},
            {'name': 'Other Political Committees', 'number': '35-11(c)'},
            {'name': 'The Candidate', 'number': '36-11(d)'},
            {'name': 'Total Contributions', 'number': '37-11(e)'},
            {'name': 'Transfers from Other Authorized Committees', 'number': '38-12'},
            {'name': 'Loans made or guarn. by the Candidate', 'number': '39-13(a)'},
            {'name': 'All Other Loans', 'number': '40-13(b)'},
            {'name': 'Total Loans', 'number': '41-13(c)'},
            {'name': 'Offsets to Operating Expenditures', 'number': '42-14'},
            {'name': 'Other Receipts', 'number': '43-15'},
            {'name': 'Total Receipts', 'number': '44-16.'},
            {'name': 'Operating Expenditures', 'number': '45-17'},
            {'name': 'Transfers to Other Authorized Committees', 'number': '46-18'},
            {'name': 'Of Loans made or guar by the Candidate', 'number': '47-19(a)'},
            {'name': 'Loan Repayments, All Other Loans', 'number': '48-19(b)'},
            {'name': 'Total Loan Repayments', 'number': '49-19(c)'},
            {'name': 'Refund/Individuals Other than Political Committees', 'number': '50-20(a)'},
            {'name': 'Refund Political Party Committees', 'number': '51-20(b)'},
            {'name': 'Refund Other Political Committees', 'number': '52-20(c)'},
            {'name': 'Total Contributions Refunds', 'number': '53-20(d)'},
            {'name': 'Other Disbursements', 'number': '54-21'},
            {'name': 'Total Disbursements', 'number': '55-22'},
            {'name': 'Cash Beginning Reporting Period', 'number': '56-23'},
            {'name': 'Total Receipts this Period', 'number': '57-24'},
            {'name': 'SubTotal)', 'number': '58-25'},
            {'name': 'Total Disbursements this Period', 'number': '59-26'},
            {'name': 'Cash on hand at Close Period', 'number': '60-27'},
            {'name': 'Total Contributions (No Loans)', 'number': '61-(6a)'},
            {'name': 'Total Contribution Refunds', 'number': '62-(6b)'},
            {'name': 'Net Contributions', 'number': '63-(6c)'},
            {'name': 'Total Operating Expenditures', 'number': '64-(7a)'},
            {'name': 'Total Offsets to Operating Expenditures', 'number': '65-(7b)'},
            {'name': 'NET Operating Expenditures', 'number': '66-(7c)'},
            {'name': 'Individuals Itemized', 'number': '67-11(ai)'},
            {'name': 'Individuals UnItemized', 'number': '68-11(aii)'},
            {'name': 'Individuals Total', 'number': '69-11(aiii)'},
            {'name': 'Political Party Committees', 'number': '70-11(b)'},
            {'name': 'All Other Political Committees (PACS)', 'number': '71-11(c)'},
            {'name': 'THE CANDIDATE', 'number': '72-11(d)'},
            {'name': 'Total Contributions', 'number': '73-11(e)'},
            {'name': 'Transfers from Other AUTH Committees', 'number': '74-12'},
            {'name': 'Loans made or guarn. by the Candidate', 'number': '75-13(a)'},
            {'name': 'All Other Loans', 'number': '76-13(b)'},
            {'name': 'Total Loans', 'number': '77-13(c)'},
            {'name': 'Offsets to Operating Expenditures', 'number': '78-14'},
            {'name': 'Other Receipts', 'number': '79-15'},
            {'name': 'Total Receipts', 'number': '80-16.'},
            {'name': 'Operating Expenditures', 'number': '81-17'},
            {'name': 'Transfers To Other AUTH Committees', 'number': '82-18'},
            {'name': 'Loan Repayment to Candidate', 'number': '83-19(a)'},
            {'name': 'Loan Repayments, ALL Other Loans', 'number': '84-19(b)'},
            {'name': 'Total Loan Repayments', 'number': '85-19(c)'},
            {'name': 'Refund/Individuals Other than Political Committees', 'number': '86-20(a)'},
            {'name': 'Refund, Political Party Committees', 'number': '87-20(b)'},
            {'name': 'Refund, Other Political Committees', 'number': '88-20(c)'},
            {'name': 'Total Contributions Refunds', 'number': '89-20(d)'},
            {'name': 'Other Disbursements', 'number': '90-21'},
            {'name': 'Total Disbursements', 'number': '91-22'},
            {'name': 'TREASURER', 'number': '92-'},
            {'name': 'SIGNED', 'number': '93-'},
    ]
        self.fields_names = self.hash_names(self.fields)
