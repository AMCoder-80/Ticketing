from utils.contants import Constant
import requests
import json


class HelpicalAdapter:

    def __init__(self):

        """ Initialized required variables and attributes """

        # base variables
        self.secret_key = Constant.HELPICAL_KEY
        self.base_url = Constant.HELPICAL_URL

        # POST related urls
        self.create_ticker_url = self.base_url + 'ticket/customer-new/'
        self.create_attachment_url = self.base_url + 'ticket/attachment/'

        # PUT related urls
        self.close_ticker_url = self.base_url + 'ticket/customer-close/'
        self.create_reply_url = self.base_url + 'ticket/customer-reply/'
        self.create_customer_url = self.base_url + 'customer/'

        # GET related urls
        self.list_tickets_url = self.base_url + 'ticket/customer-tickets/{}/'
        self.ticket_detail_url = self.base_url + 'ticket/customer-ticket/{}/{}/'

    def create_customer(self, user):
        
        data = json.dumps({
            "fname": user.first_name,
            "lname": user.last_name,
            "email": user.email,
            "org_id": "1",
            "mobile": user.mobile,
            "password": user.mobile,
            "level": "2",
            "position": "student"
        })

        
        headers = {
            'X-Api-Key': self.secret_key,
            'Content-Type': 'application/json'
        }

        print(data)
        response = requests.request("POST", self.create_customer_url, headers=headers, data=data)

        is_verified = response.status_code == 201
        print(response.status_code)
        data = response.json()
        print(data)
        return data, is_verified

    def create_ticket(self, user, subject, message, priority):
        data = json.dumps({
            "customer_id": user.helpical_id,
            "customer_username": "",
            "customer_email": "",
            "ticket_cat": 2,
            "subject": subject,
            "target_department_id": 6,
            "message": message,
            "importance": priority
        })

        print(data)
        headers = {
            'X-Api-Key': self.secret_key,
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", self.create_ticker_url, headers=headers, data=data)

        is_verified = response.status_code == 201
        print(response.status_code)
        data = response.json()
        print(data)
        return data, is_verified

    def create_attachment(self, content_id, filename):
        
        data = {
            "content_id": content_id,
        }

        files = [
            ('attachment[]', (filename.name, filename.file, filename.content_type)),
        ]

        print(data, files)
        headers = {
            'X-Api-Key': self.secret_key,
        }

        response = requests.request("POST", self.create_attachment_url, headers=headers, data=data, files=files)

        is_verified = response.status_code == 201
        print(response.status_code)
        data = response.json()
        print(data)
        return data, is_verified

    def create_reply(self, user, ticket_id, message):
        data = json.dumps({
            "customer_id": user.helpical_id,
            "customer_username": "",
            "customer_email": "",
            "ticket_id": ticket_id,
            "message": message,
            "reply_and_close": "0"
        })

        print(data)
        headers = {
            'X-Api-Key': self.secret_key,
            'Content-Type': 'application/json'
        }

        response = requests.request("PUT", self.create_reply_url, headers=headers, data=data)

        is_verified = response.status_code == 202
        print(response.status_code)
        data = response.json()
        print(data)
        return data, is_verified

    def close_ticket(self):
        ...

    def list_tickets(self, user):
        
        headers = {
            'X-Api-Key': self.secret_key,
            'Content-Type': 'application/json'
        }

        response = requests.request("GET", self.list_tickets_url.format(user.helpical_id), headers=headers)

        is_verified = response.status_code == 200
        print(response.status_code)
        data = response.json()
        print(data)
        return data, is_verified

    def ticket_detail(self, user, ticket_id):

        headers = {
            'X-Api-Key': self.secret_key,
            'Content-Type': 'application/json'
        }

        response = requests.request("GET", self.ticket_detail_url.format(ticket_id, user.helpical_id), headers=headers)

        is_verified = response.status_code == 200
        print(response.status_code)
        data = response.json()
        print(data)
        return data, is_verified