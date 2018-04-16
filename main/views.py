# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .forms import ContactForm
from django.views.generic.edit import  FormView

# Create your views here.
class ContactView(FormView):
    template_name = 'main/contact_us.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        import pdb; pdb.set_trace()
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')

        return super(ContactView, self).form_valid(form)
