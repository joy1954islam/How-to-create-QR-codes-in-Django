
from django.shortcuts import render

from QRCodeApps.models import Website


def home_view(request):
    qrcode = Website.objects.all()
    context = {
        'qrcode': qrcode,
    }
    return render(request, 'home.html', context)


