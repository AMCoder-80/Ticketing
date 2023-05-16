from adapters.helpical_adapter import HelpicalAdapter


class TicketService:

    def __init__(self, user):
        self.helpical_adapter = HelpicalAdapter()
        self.user = user

    
    def create_ticket(self):
        ...

    def reply_ticket(self):
        ...

    def list_tickets(self):
        
        data, is_verified = self.helpical_adapter.list_tickets(self.user)
        if not is_verified:
            return 'someting went wrong', is_verified
        
        result = list()

        print(data, '\n\n')
        print(data['returned_values'], '\n\n')

        for parameter in data['returned_values']:

            param = {
                'owner_name': parameter['owner_user_name'],
                'created_date': parameter['create_date_time'],
                'department_name': parameter['target_department_name'],
                'id': parameter['ticket_id'],
                'subject': parameter['title'],
                'importance': parameter['importance'],
            }
            result.append(param)
        
        print(result)
        return result, is_verified

    def ticket_detail(self):
        ...
    