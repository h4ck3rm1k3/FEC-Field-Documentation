import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC COMMITTEE ID', 'number': '2'},
            {'name': 'CANDIDATE NAME', 'number': '3-1.'},
            {'name': 'CANDIDATE ID', 'number': '4-2.'},
            {'name': 'CAN/OFFICE', 'number': '5-3.'},
            {'name': 'CANDIDATE STATE', 'number': '6-4.'},
            {'name': 'CANDIDATE DISTRICT', 'number': '7-5.'},
            {'name': 'COMMITTEE NAME', 'number': '8-6.'},
            {'name': 'STREET 1', 'number': '9-8.'},
            {'name': 'STREET 2', 'number': '10-8.'},
            {'name': 'CITY', 'number': '11-9.'},
            {'name': 'STATE', 'number': '12-9.'},
            {'name': 'ZIP', 'number': '13-9.'},
            {'name': 'NAME OF CANDIDATE', 'number': '14-10.'},
            {'name': 'NAME OF COMMITTEE', 'number': '15-11.'},
            {'name': 'COMMITTEE ID', 'number': '16-12.'},
            {'name': 'COMMITTEE STREET 1', 'number': '17-13.'},
            {'name': 'COMMITTEE STREET 2', 'number': '18-13.'},
            {'name': 'COMMITTEE CITY', 'number': '19-14.'},
            {'name': 'COMMITTEE STATE', 'number': '20-14.'},
            {'name': 'COMMITTEE ZIP', 'number': '21-14.'},
            {'name': 'DATE OF FORM 10 RECEIPT', 'number': '22-15.'},
            {'name': 'OPPOSITION PERS FUNDS AMT', 'number': '23-16.'},
            {'name': 'ITEM ELECT CD', 'number': '24'},
            {'name': 'ITEM ELECT OTHER', 'number': '25'},
            {'name': 'TYPE', 'number': '26'},
            {'name': 'NAME/CANDIDATE/TREAS (as signed)', 'number': '27'},
            {'name': 'Signed', 'number': '28-'},
    ]
        self.fields_names = self.hash_names(self.fields)
