from django.core.mail import EmailMessage
from django.contrib import messages
from django.shortcuts import render
from .forms import GuestEnquiryForm
from .models import GuestEnquiryModel

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        print('--------------inside post')
        form = GuestEnquiryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            package = form.cleaned_data['package']
            news_letter = form.cleaned_data['news_letter']
            enquiry_message = form.cleaned_data['enquiry_message']
            print('============', form.cleaned_data)
            if GuestEnquiryModel.objects.filter(email=email).exists():
                GuestEnquiryModel.objects.update(email=email, name=name, package=package, news_letter=news_letter,
                                                 enquiry_message=enquiry_message)
            else:
                GuestEnquiryModel.objects.create(email=email, name=name, package=package, news_letter=news_letter,
                                                 enquiry_message=enquiry_message)
            email = EmailMessage(
                subject='{} - Enquiry'.format(package),
                body='{}'.format(enquiry_message),
                from_email=email,
                to=['rashidrmadhan08@gmail.com'],
                reply_to=['rashidrmadhan08@gmail.com'],
                headers={'Content-Type': 'text/plain'},
            )
            email.send()
            messages.success(request, 'Your Enquiry request has been successfully received, we will respond via your email, Thanks')

        else:
            print('*************', form.errors)
    return render(request, 'home2.html', {'messages': messages})

# request form for all packages enquiries
def request_email(request):
    if request.method == 'POST':
        print('--------------inside post')
        form = GuestEnquiryForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data, '---')
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            package = form.cleaned_data['package']
            news_letter = form.cleaned_data['news_letter']
            enquiry_message = form.cleaned_data['enquiry_message']
            print('============', form.cleaned_data)
            if GuestEnquiryModel.objects.filter(email=email).exists():
                GuestEnquiryModel.objects.update(email=email, name=name, package=package, news_letter=news_letter,
                                                 enquiry_message=enquiry_message)
            else:
                GuestEnquiryModel.objects.create(email=email, name=name, package=package, news_letter=news_letter,
                                                 enquiry_message=enquiry_message)
            email = EmailMessage(
                subject='{} - Enquiry'.format(package),
                body='{}'.format(enquiry_message),
                from_email=email,
                to=['rashidrmadhan08@gmail.com'],
                reply_to=['rashidrmadhan08@gmail.com'],
                headers={'Content-Type': 'text/plain'},
            )
            email.send()
            messages.success(request, 'Your Enquiry request has been successfully received, we will respond via your email, Thanks')

        else:
            print('*************', form.errors)
    return render(request, 'pages/request_form.html')

def packages_list(request):
    return render(request, 'pages/packages.html')

# Game Reserves pages displays
def masai_mara(request):
    return render(request, 'pages/masai_mara.html')
def nairobi_nsp(request):
    return render(request, 'pages/nairobi_ns.html')
def lake_nakuru(request):
    return render(request, 'pages/lake_nakuru.html')
def tsavo_east(request):
    return render(request, 'pages/tsavo_east.html')
def tsavo_west(request):
    return render(request, 'pages/tsavo_west.html')
def pejeta(request):
    return render(request, 'pages/pejeta.html')
def mount_kenya(request):
    return render(request, 'pages/mount_kenya.html')
def naivasha(request):
    return render(request, 'pages/naivasha.html')
def amboseli(request):
    return render(request, 'pages/amboseli.html')