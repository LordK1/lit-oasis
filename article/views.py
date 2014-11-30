from article.forms import ContactForm
from django.core.mail import send_mail
from django.http.response import HttpResponseRedirect
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})


def contact(request):
    """
    For Sign in the Web site and send Email for Users
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject': 'I Love your Site , Thanks list Oasis !!!'}
        )
        return render(request, 'contact_form.html', {'form': form})