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

    def ticket_detail(self, pk):
        
        data, is_verified = self.helpical_adapter.ticket_detail(self.user, pk)
        if not is_verified:
            return 'someting went wrong', is_verified
        
        print(data, '\n\n')
        print(data['returned_values'][0]['contents'], '\n\n')

        result = list()

        for parameter in data['returned_values'][0]['contents']:

            param = {
                'writer_name': parameter['writer_user_name'],
                'writer_image': parameter['writer_photo_url'],
                'created_date': parameter['update_date_time'],
                'message': parameter['message'],
            }
            if parameter['attachments']:
                param['attachment'] = parameter['attachments'][0]
            result.append(param)
        
        print(result)
        return result, is_verified
    