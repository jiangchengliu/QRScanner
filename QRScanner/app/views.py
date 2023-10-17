from django.shortcuts import render
import qrcode

# Create your views here.

def index(request):
    return render(request, 'index.html')

"""
def generate_qr(request):
    if request.method == 'POST':
        data = request.POST['qr_data']
        img = qrcode.make(data)
        img.save('app/static/app/qr.png')
        return render(request, 'app/index.html')
    else:
        return render(request, 'app/index.html')
"""




