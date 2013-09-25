from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'CHANGE OF COMMITTEE NAME', 'number': '3'},
            {'name': 'COMMITTEE NAME', 'number': '4'},
            {'name': 'CHANGE OF ADDRESS', 'number': '5'},
            {'name': 'STREET 1', 'number': '6'},
            {'name': 'STREET 2', 'number': '7'},
            {'name': 'CITY', 'number': '8'},
            {'name': 'STATE', 'number': '9'},
            {'name': 'ZIP', 'number': '10'},
            {'name': 'COMMITTEE EMAIL', 'number': '11'},
            {'name': 'COMMITTEE WEB URL', 'number': '12'},
            {'name': 'COMMITTEE FAX NUMBER', 'number': '13'},
            {'name': 'SUBMISSION DATE', 'number': '14'},
            {'name': 'SIGNATURE LAST NAME', 'number': '15'},
            {'name': 'SIGNATURE FIRST NAME', 'number': '16'},
            {'name': 'SIGNATURE MIDDLE NAME', 'number': '17'},
            {'name': 'SIGNATURE PREFIX', 'number': '18'},
            {'name': 'SIGNATURE SUFFIX', 'number': '19'},
            {'name': 'DATE SIGNED', 'number': '20'},
            {'name': 'COMMITTEE TYPE', 'number': '21-5.'},
            {'name': 'CANDIDATE ID NUMBER', 'number': '22-5.'},
            {'name': 'CANDIDATE LAST NAME', 'number': '23-5.'},
            {'name': 'CANDIDATE FIRST NAME', 'number': '24-5.'},
            {'name': 'CANDIDATE MIDDLE NAME', 'number': '25-5.'},
            {'name': 'CANDIDATE PREFIX', 'number': '26-5.'},
            {'name': 'CANDIDATE SUFFIX', 'number': '27-5.'},
            {'name': 'CANDIDATE OFFICE', 'number': '28-5.'},
            {'name': 'CANDIDATE STATE', 'number': '29-5.'},
            {'name': 'CANDIDATE DISTRICT', 'number': '30-5.'},
            {'name': 'PARTY CODE', 'number': '31-5.'},
            {'name': 'PARTY TYPE', 'number': '32-5.'},
            {'name': 'ORGANIZATION TYPE', 'number': '33-5 (e).'},
            {'name': 'LEADERSHIP PAC', 'number': '34-5 (f).'},
            {'name': 'AFFILIATED Committee ID NUM', 'number': '35-6.'},
            {'name': 'AFFILIATED Committee NAME', 'number': '36-6.'},
            {'name': 'AFFILIATED STREET 1', 'number': '37-6.'},
            {'name': 'AFFILIATED STREET 2', 'number': '38-6.'},
            {'name': 'AFFILIATED CITY', 'number': '39-6.'},
            {'name': 'AFFILIATED STATE', 'number': '40-6.'},
            {'name': 'AFFILIATED ZIP', 'number': '41-6.'},
            {'name': 'AFFILIATED RELATIONSHIP CODE', 'number': '42-6.'},
            {'name': 'CUSTODIAN LAST NAME', 'number': '43-7.'},
            {'name': 'CUSTODIAN FIRST NAME', 'number': '44-7.'},
            {'name': 'CUSTODIAN MIDDLE NAME', 'number': '45-7.'},
            {'name': 'CUSTODIAN PREFIX', 'number': '46-7.'},
            {'name': 'CUSTODIAN SUFFIX', 'number': '47-7.'},
            {'name': 'CUSTODIAN STREET 1', 'number': '48-7.'},
            {'name': 'CUSTODIAN STREET 2', 'number': '49-7.'},
            {'name': 'CUSTODIAN CITY', 'number': '50-7.'},
            {'name': 'CUSTODIAN STATE', 'number': '51-7.'},
            {'name': 'CUSTODIAN ZIP', 'number': '52-7.'},
            {'name': 'CUSTODIAN TITLE', 'number': '53-7.'},
            {'name': 'CUSTODIAN TELEPHONE', 'number': '54-7.'},
            {'name': 'TREASURER LAST NAME', 'number': '55-8.'},
            {'name': 'TREASURER FIRST NAME', 'number': '56-8.'},
            {'name': 'TREASURER MIDDLE NAME', 'number': '57-8.'},
            {'name': 'TREASURER PREFIX', 'number': '58-8.'},
            {'name': 'TREASURER SUFFIX', 'number': '59-8.'},
            {'name': 'TREASURER STREET 1', 'number': '60-8.'},
            {'name': 'TREASURER STREET 2', 'number': '61-8.'},
            {'name': 'TREASURER CITY', 'number': '62-8.'},
            {'name': 'TREASURER STATE', 'number': '63-8.'},
            {'name': 'TREASURER ZIP', 'number': '64-8.'},
            {'name': 'TREASURER TITLE', 'number': '65-8.'},
            {'name': 'TREASURER TELEPHONE', 'number': '66-8.'},
            {'name': 'AGENT LAST NAME', 'number': '67-8.'},
            {'name': 'AGENT FIRST NAME', 'number': '68-8.'},
            {'name': 'AGENT MIDDLE NAME', 'number': '69-8.'},
            {'name': 'AGENT PREFIX', 'number': '70-8.'},
            {'name': 'AGENT SUFFIX', 'number': '71-8.'},
            {'name': 'AGENT STREET 1', 'number': '72-8.'},
            {'name': 'AGENT STREET 2', 'number': '73-8.'},
            {'name': 'AGENT CITY', 'number': '74-8.'},
            {'name': 'AGENT STATE', 'number': '75-8.'},
            {'name': 'AGENT ZIP', 'number': '76-8.'},
            {'name': 'AGENT TITLE', 'number': '77-8.'},
            {'name': 'AGENT TELEPHONE', 'number': '78-8.'},
            {'name': 'BANK NAME', 'number': '79-9. a)'},
            {'name': 'BANK STREET 1', 'number': '80-9. a)'},
            {'name': 'BANK STREET 2', 'number': '81-9. a)'},
            {'name': 'BANK CITY', 'number': '82-9. a)'},
            {'name': 'BANK STATE', 'number': '83-9. a)'},
            {'name': 'BANK ZIP', 'number': '84-9. a)'},
            {'name': 'BANK NAME', 'number': '85-9. b)'},
            {'name': 'BANK STREET 1', 'number': '86-9. b)'},
            {'name': 'BANK STREET 2', 'number': '87-9. b)'},
            {'name': 'BANK CITY', 'number': '88-9. b)'},
            {'name': 'BANK STATE', 'number': '89-9. b)'},
            {'name': 'BANK ZIP', 'number': '90-9. b)'},
    ]
        self.fields_names = self.hash_names(self.fields)
