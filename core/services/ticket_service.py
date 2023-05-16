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
        ...

    def ticket_detail(self):
        ...
    