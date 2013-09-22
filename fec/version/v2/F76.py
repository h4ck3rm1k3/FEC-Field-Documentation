from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC CMTE ID', 'number': '2'},
            {'name': 'COMMUNICATION TYPE', 'number': '3'},
            {'name': 'COMMUN SPECIFICATION', 'number': '4-TRANS'},
            {'name': 'COMMUNICATION CLASS OR CATEGORY', 'number': '5'},
            {'name': 'OF COMMUNICATION', 'number': '6-'},
            {'name': 'SUPPORT/OPPOSE', 'number': '7'},
            {'name': 'FEC CANDIDATE ID NUMBER', 'number': '8'},
            {'name': 'CANDIDATE NAME', 'number': '9'},
            {'name': 'CAN/OFF', 'number': '10'},
            {'name': 'STATE (OF ELECTION)', 'number': '11'},
            {'name': 'CAN/DIST', 'number': '12'},
            {'name': 'RPTPGI', 'number': '13'},
            {'name': 'Cost of communication', 'number': '14'},
            {'name': 'AMENDED-CD', 'number': '15'},
            {'name': 'TRAN_ID', 'number': '16'},
            {'name': 'ORIG_TRAN_ID', 'number': '17'},
            {'name': 'SUPR_TRAN_ID', 'number': '18'},
    ]
