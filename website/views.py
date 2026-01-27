from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.contrib import messages
from website.models import Contact
from website.forms import ContactModelForm, NewsletterModelForm,  NameForm, TestContactModelForm

# Create your views here.

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.add_message(request, messages.SUCCESS, 'Your ticket submited successfully') # this line and next line do the same
            messages.success(request, 'Your ticket submited successfully')
        else:
            # messages.add_message(request, messages.ERROR, "Your ticket didn't submited") # this line and next line do the same
            messages.error(request, "Your ticket didn't submited")

    form = ContactModelForm()
    context = {'form': form} 
    return render(request, 'website/contact.html', context)

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterModelForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponseRedirect('/')
            return redirect(reverse('website:index'))
        
    return redirect(reverse('website:index'))



# test for forms.ModelForm
def test_view(request):
    if request.method == 'POST':
        form = TestContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('not valid')

    form = TestContactModelForm()
    context = {'form': form}
    return render(request, 'test.html', context)


# test for forms.Form
# def test_view(request):
#     if request.method == 'POST':
#         form = NameForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']
#             print(name, email, subject, message)
#             c = Contact(name=name, email=email, subject=subject, message=message)
#             c.save()
#             return HttpResponse('done!')
#         else:
#             return HttpResponse('not valid')

#     form = NameForm()
#     context = {'form': form}
#     return render(request, 'test.html', context)

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