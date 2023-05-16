from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from services.ticket_service import TicketService
from base.forms import TicketForm

# Create your views here.


class ListTickets(View, LoginRequiredMixin):

    def get(self, request, *args, **kwargs):

        user = request.user

        ticket_service = TicketService(user)
        data, is_verified = ticket_service.list_tickets()

        if is_verified:
            context = {
                'tickets': data,
                'errors': None
            }
        else:
            context = {
                'tickets': None,
                'errors': data
            }
        return render(request, 'base/list.html', context=context)


class CreateTicket(View, LoginRequiredMixin):

    def get(self, request, *args, **kwargs):
        
        ticket_form = TicketForm()
        return render(request, 'base/create.html', context={'form': ticket_form})

    def post(self, request, *args, **kwargs):

        user = request.user

        ticket_form = TicketForm(request.POST)

        if not ticket_form.is_valid():
            return render(request, 'base/create.html', context={'form': ticket_form})
        
        subject = ticket_form.cleaned_data['subject']
        message = ticket_form.cleaned_data['message']
        priority = ticket_form.cleaned_data['priority']
        
        ticket_service = TicketService(user)
        data, is_verified = ticket_service.create_ticket(
            subject=subject,
            message=message,
            priority=priority
        )

        context = {
            'data': data,
            'is_verified': is_verified
        }
        return render(request, 'base/list.html', context=context)


class TicketDetail(View, LoginRequiredMixin):

    def get(self, request, pk, *args, **kwargs):

        user = request.user

        ticket_service = TicketService(user)
        data, is_verified = ticket_service.ticket_detail(
            pk=pk
        )

        ticket_form = TicketForm()

        if is_verified:
            context = {
                'form': ticket_form,
                'tickets': data,
                'errros': None
            }
        else:
            context = {
                'form': ticket_form,
                'tickets': None,
                'errros': data
            }

        return render(request, 'base/detail.html', context=context)

    def post(self, request, pk, *args, **kwargs):

        user = request.user

        ticket_form = TicketForm(request.POST)

        if not ticket_form.is_valid():
            return render(request, 'base/detail.html', context={'form': ticket_form})
        
        message = ticket_form.cleaned_data['message']
        
        ticket_service = TicketService(user)
        data, is_verified = ticket_service.reply_ticket(
            pk=pk,
            message=message,
        )

        context = {
            'data': data,
            'is_verified': is_verified
        }
        return render(request, 'base/detail.html', context=context)