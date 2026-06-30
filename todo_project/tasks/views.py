from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1> WELCOME TO HAIRDAIRY.NG</h1>')

def about(request):
    return HttpResponse('<h4>Serving premium human hair daily. From flawless bone straights to luxury deep waves, we feed your hair obsession with nothing but quality. ✨</h4>')

def contact(request):
    return HttpResponse("""
        <h3>Contact hairdairy.ng</h3>
        <ul>
            <li><strong>Phone:</strong> +234 806 719 6456</li>
            <li><strong>Email:</strong> info@hairdairy.ng</li>
            <li><strong>Instagram:</strong> @hairdairy.ng</li>
            <li><strong>TikTok:</strong> @hairdairy.ng</li>
        </ul>
    """)
