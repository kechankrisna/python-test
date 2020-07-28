from django.http import JsonResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.core import serializers

from .models import Client
from .filters import ClientFilter


class ClientList(ListView):
    model = Client
    template_name = "list.html"


class ClientCreate(CreateView):
    model = Client
    fields = [
        "username",
        "contact_name",
        "email",
        "phone_number",
        "street_name",
        "suburb",
        "postcode",
        "state",
    ]
    template_name = "create.html"
    success_url = reverse_lazy("client_list")


class ClientUpdate(UpdateView):
    model = Client
    fields = [
        "username",
        "contact_name",
        "email",
        "phone_number",
        "street_name",
        "suburb",
        "postcode",
        "state",
    ]
    template_name = "create.html"
    success_url = reverse_lazy("client_list")


def clientFilter(request):
    client_filter = ClientFilter(request.GET, queryset=Client.objects.all())
    return JsonResponse(serializers.serialize('json', client_filter.qs), safe=False)
