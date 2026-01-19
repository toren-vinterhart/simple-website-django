from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from website.models import Contact
from website.forms import NameForm

# Create your views here.

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    return render(request, 'website/contact.html')

def test_view(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            print(name, email, subject, message)
            c = Contact(name=name, email=email, subject=subject, message=message)
            c.save()
            return HttpResponse('done!')
        else:
            return HttpResponse('not valid')

    form = NameForm()
    context = {'form': form}
    return render(request, 'test.html', context)

# def test_view(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')
#         c = Contact(name=name, email=email, subject=subject, message=message)
#         # c.name = name
#         # c.email = email
#         # c.subject = subject
#         # c.message = message
#         c.save()

#     return render(request, 'test.html')