from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from article.forms import ContactForm
from article.models import Article, Category, Author
from django.core.mail import send_mail
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

def home(request):
    articles = Article.objects.all()
    return render(request, 'home.html', {'articles': articles})


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


def category(request, pk):
    """
    Get All Article in defined category !
    :param request:
    :param p1:
    :return:
    """
    cat = Category.objects.all(pk=pk)
    if not request.user.is_authenticated():
        return HttpResponse("Error: you need to be logged in to view this Category !")
    return render(request, 'category.html', {cat: cat})


def detail(request, pk):
    """
    get Article
    :param request:
    :param pk:
    :return:
    """
    article = Article.objects.get(pk=pk)
    return render(request, 'detail.html',
                  dict(article=article, user=request.user, backurl=request.META["HTTP_REFERER"]))


def vote(request, author_id):
    """
    Vote to the Author
    :param request:
    :return:
    """
    author = get_object_or_404(Author, pk=author_id)
    if request.method == 'POST':
        author.likes += 1
        author.save()

    return HttpResponseRedirect('/')