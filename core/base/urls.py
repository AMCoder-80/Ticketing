from django.urls import path
from base import views


urlpatterns = [
    path('tickets/', views.ListTickets.as_view(), name='list_tickets'),
    path('ticket/<int:pk>/', views.TicketDetail.as_view(), name='ticket_detail'),
    path('ticket/create/', views.CreateTicket.as_view(), name='create_ticket'),
]