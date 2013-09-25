from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM-TYPE', 'number': '1'},
            {'name': 'FILER FEC CMTE ID', 'number': '2'},
            {'name': 'ENTITY-TYPE', 'number': '3'},
            {'name': 'CONTRIBUTOR-NAME', 'number': '4'},
            {'name': 'STREET 1', 'number': '5'},
            {'name': 'STREET 2', 'number': '6'},
            {'name': 'CITY', 'number': '7'},
            {'name': 'STATE', 'number': '8'},
            {'name': 'ZIP', 'number': '9'},
            {'name': 'ITEM-ELECT-CD', 'number': '10'},
            {'name': 'ITEM-ELECT-OTHER', 'number': '11'},
            {'name': 'IND-EMPLOYER', 'number': '12'},
            {'name': 'IND-OCCUP', 'number': '13'},
            {'name': 'AGGREGATE-AMT-YTD', 'number': '14'},
            {'name': 'DATE-RECEIVED', 'number': '15'},
            {'name': 'AMOUNT-RECEIVED', 'number': '16'},
            {'name': 'TRANS-CODE', 'number': '17'},
            {'name': 'TRANS-DESCRIP', 'number': '18'},
            {'name': 'FEC-COMMITTEE-ID-NUMBER', 'number': '19'},
            {'name': 'FEC-CANDIDATE-ID-NUMBER', 'number': '20'},
            {'name': 'CANDIDATE-NAME', 'number': '21'},
            {'name': 'CAND-OFFICE', 'number': '22'},
            {'name': 'CAND-STATE (OF ELECTION)', 'number': '23'},
            {'name': 'CAND-DISTRICT', 'number': '24'},
            {'name': 'CONDUIT-NAME', 'number': '25'},
            {'name': 'CONDUIT-STREET-1', 'number': '26'},
            {'name': 'CONDUIT-STREET-2', 'number': '27'},
            {'name': 'CONDUIT-CITY', 'number': '28'},
            {'name': 'CONDUIT-STATE', 'number': '29'},
            {'name': 'CONDUIT-ZIP', 'number': '30'},
            {'name': 'MEMO-CODE', 'number': '31'},
            {'name': 'MEMO-TEXT', 'number': '32'},
            {'name': 'AMENDED-CD', 'number': '33'},
            {'name': 'TRAN-ID', 'number': '34'},
            {'name': 'ORIG-TRAN-ID', 'number': '35'},
            {'name': 'SUPR-TRAN-ID', 'number': '36'},
    ]
        self.fields_names = self.hash_names(self.fields)
