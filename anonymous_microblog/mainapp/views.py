from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Message


class MessageCreateView(CreateView):
    model = Message
    template_name = 'mainapp/base.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(MessageCreateView, self).get_context_data(**kwargs)
        context['title'] = "Анонимный микроблог"
        all_messages = Message.objects.all().order_by('-created')
        context['all_messages'] = all_messages
        return context

    def get_success_url(self):
        return reverse_lazy('main')
