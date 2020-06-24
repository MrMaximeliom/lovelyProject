from django.shortcuts import render
from django.utils.translation import gettext as _
# @login_required
def home(request):

    context = {
        'title':  _('HomePage'),
        'home' : 'active',

    }

    return render(request, 'home/home.html', context)