from django.shortcuts import render
import razorpay
from django.conf import settings

# Create your views here.

# def home(request):
#     return render(request, 'index.html')


def home(request):
        client = razorpay.Client(
        auth=(settings.RAZOR_PAY_KEY_ID, settings.RAZOR_PAY_KEY_SECRET))
        payment = client.order.create(
        {'amount': 1000*100, 'currency': 'INR', 'payment_capture': 1, })
        return render(request, 'index.html', {'amount': payment['amount'], 'id': payment['id'], 'key': settings.RAZOR_PAY_KEY_ID})
