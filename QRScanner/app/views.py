from django.shortcuts import render
import qrcode
from .models import User

# Create your views here.

def index(request):
    return render(request, 'page.html')

def get_qr_code(request):
    if request.user.is_authenticated:
        user = User.objects.get(email=request.user.email)
        context = {
            'qr_code': user.qr_code
        }
        render(request, 'page.html', context)
    else:
        return render(request, 'page.html')






