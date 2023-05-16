from utils.contants import Constant


class HelpicalAdapter:

    def __init__(self):

        """ Initialized required variables and attributes """

        # base variables
        self.secret_key = Constant.HELPICAL_KEY
        self.base_url = Constant.HELPICAL_URL

        # POST related urls
        self.create_ticker_url = self.base_url + 'ticket/customer-new/'
        self.create_attachment = self.base_url + 'ticket/attachment/'

        # PUT related urls
        self.close_ticker = self.base_url + 'ticket/customer-close/'
        self.create_reply_url = self.base_url + 'ticket/customer-reply/'

        # GET related urls
        self.list_tickets = self.base_url + 'ticket/customer-tickets/{}/'
        self.ticket_detail = self.base_url + 'ticket/customer-ticket/{}/{}/'


    def create_ticket(self):
        ...

    def create_attachment(self):
        ...

    def create_reply(self):
        ...

    def close_ticket(self):
        ...

    def list_tickets(self):
        ...

    def ticket_detail(self):
        ...