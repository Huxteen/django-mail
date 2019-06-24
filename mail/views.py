from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from mail.forms import CreateMailList
from mail.models import MailList
from django.http import JsonResponse, HttpResponse

# View for the home Page
def add(request):
    if request.method == 'POST':
        form = CreateMailList(request.POST or None)
        data = {'message': 'Something went wrong with your form data',
                'status': 'failed',
                'error': form.errors,
                }
        if form.is_valid():
            status = form.save()
            data = {
                'message':'New data has been added successfully',
                'status':'success', 
            }
        return JsonResponse(data)
    return render(request, 'mail/add.html')


def mail_list(request):
    mail_list = MailList.objects.all()
    context = {'mail_list':mail_list}
    return render(request, 'mail/list.html', context)