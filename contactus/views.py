from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Message
from .forms import MessageForm


class ContactUsView(View):
    def get(self, request):
        form = MessageForm()
        context = {
            'form': form,
        }
        return render(request, 'contactus/contact_us.html', context)

    def post(self, request):
        form = MessageForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('contact_us:done')

        return render(request, 'contactus/contact_us.html', {'form': form})


class DoneView(View):
    def get(self, request):
        return render(request, 'contactus/done_message.html')
