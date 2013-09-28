import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC CMTE ID', 'number': '2'},
            {'name': 'NAT PARTY COMMITTEES %', 'number': '3'},
            {'name': 'HSE/SEN PTY COMMITTEES MINIMUM FED %', 'number': '4'},
            {'name': 'HSE/SEN PTY COMMITTEES PERCENTAGE ESTIMATED FEDERAL CAN SUPPORT', 'number': '5'},
            {'name': 'HSE/SEN PTY COMMITTEES PERCENTAGE ESTIMATED NON FEDERAL CAN SUPPORT', 'number': '6'},
            {'name': 'HSE/SEN PTY COMMITTEES ACTUAL FEDERAL CAN SUPPORT', 'number': '7'},
            {'name': 'HSE/SEN PTY COMMITTEES ACTUAL NON FEDERAL CAN SUPPORT', 'number': '8'},
            {'name': 'HSE/SEN PTY COMMITTEES PERCENTAGE ACTUAL FEDERAL', 'number': '9'},
            {'name': 'SEP. SEG FUNDS & PERCENTAGE NON CONNECTED COMMITTEES ESTIMATED FEDERAL CANDIDATE SUPPORT', 'number': '10'},
            {'name': 'SEP. SEG FUNDS & PERCENTAGE NON CONNECTED COMMITTEES ESTIMATED NON FEDERAL CANDIDATE SUPPORT', 'number': '11'},
            {'name': 'SEP. SEG FUNDS & NON CONNECTED COMMITTEES ACTUAL FEDERAL CANDIDATE SUPPORT', 'number': '12'},
            {'name': 'SEP. SEG FUNDS & NON CONNECTED COMMITTEES ACTUAL NON FEDERAL CANDIDATE SUPPORT', 'number': '13'},
            {'name': 'SEP. SEG FUNDS & PERCENTAGE NON CONNECTED COMMITTEES ACTUAL FEDERAL CANDIDATE SUPPORT', 'number': '14'},
            {'name': 'BALLOT COMP PRES BLANK OR 1', 'number': '15-1.'},
            {'name': 'BALLOT COMP SEN BLANK OR 1', 'number': '16-2.'},
            {'name': 'BALLOT COMP HSE BLANK OR 1', 'number': '17-3.'},
            {'name': 'SUBTOTAL FED', 'number': '18-4.'},
            {'name': 'BALLOT COMP GOV BLANK OR 1', 'number': '19-5.'},
            {'name': 'OTHER STATEWIDE', 'number': '20-6.'},
            {'name': 'STATE SENATE', 'number': '21-7.'},
            {'name': 'STATE REP.', 'number': '22-8.'},
            {'name': 'LOCAL CANDIDATES BLANK, 1 OR 2', 'number': '23-9.'},
            {'name': 'EXTRA NON-FED POINT BLANK OR 1', 'number': '24-10.'},
            {'name': 'SUBTOTAL', 'number': '25-11.'},
            {'name': 'TOTAL POINTS', 'number': '26-12.'},
            {'name': 'FEDERAL ALLOCATION PERCENTAGE', 'number': '27'},
            {'name': 'AMENDED CD', 'number': '28'},
            {'name': 'TRAN ID', 'number': '29'},
    ]
        self.fields_names = self.hash_names(self.fields)
