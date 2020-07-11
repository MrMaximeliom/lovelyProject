from django.shortcuts import render
from django.utils.translation import gettext as _
# @login_required
def home(request):

    context = {
        'title':  _('HomePage'),
        'home' : 'active',

    }

    return render(request, 'home/home.html', context)

def contact_us(request):
    context={
        'title':'Contact Us',
        'contact':'active',
    }
    return render(request,'home/contact_us.html',context)
def compare(request):
    return render(request, 'home/compare.html')