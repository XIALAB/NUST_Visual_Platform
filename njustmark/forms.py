#!/usr/bin/env python
# encoding: utf-8


from django import forms


class DocumentForm(forms.Form):
    docfile = forms.FileField(
            label = 'Select A File!',
            help_text = 'Max 100M'
    )
    file_type = forms.CharField(max_length=100)
