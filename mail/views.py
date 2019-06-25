from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from mail.forms import CreateMailList
from mail.models import MailList
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.views.generic import View, ListView, CreateView

# View for the home Page
def add(request):
    if request.method == 'POST':
        form = CreateMailList(request.POST or None)
        data = {'message': 'Something went wrong with your form data',
                'status': 'failed',
                'error': form.errors,
                }
        if form.is_valid():
            form.save()
            messages.success(request, 'Your data has been added successfully')
            return redirect('add')
        context = {'form': form}
        return render(request, 'mail/add.html', context)
    return render(request, 'mail/add.html')


class MailListView(ListView):
    model = MailList
    template_name = 'mail/list.html'
    context_object_name = 'mail_list'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_request_var'] = "page"
        return context


