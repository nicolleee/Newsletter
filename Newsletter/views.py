from django.shortcuts import render
from Newsletter.forms import contactformemail
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html')

def contactsendmail(request):
    if request.method=="GET":
        form = contactformemail()
    else:
        form = contactformemail(request.POST)
        if form.is_valid():
            fromemail=form.cleaned_data['fromemail']
            subject=form.cleaned_data['subject']
            message=form.cleaned_data['message']
            send_mail(subject, message, fromemail,['nicolesbullshifs@gmail.com', fromemail],)
        return render(request, 'formTrial.html', {'form':form})