from django import forms
from .models import Category, News
import re
from django.core.exceptions import ValidationError


class SearchForm(forms.Form):
    title = forms.CharField(label='search', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))


class NewForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'content': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'category': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Xato')
        return title

    title = forms.CharField(max_length=150, label='Cars', widget=forms.TextInput(
        attrs=({'class': 'form-control'})
    ))
    content = forms.CharField(label='Text', widget=(forms.Textarea(
        attrs=({'class': 'form-control'})
    )))
    is_published = forms.CharField(label='Bool', initial=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Categories',
                                      widget=forms.Select(
                                          attrs=({'class': 'form-control'})
                                      ))


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }

# class SearchForm(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields = ['title']
#         widgets = {
#             'title': forms.TextInput(
#                 attrs={
#                     'class': 'form-control'
#                 }
#             )
#         }
#     def clean_title(self):
#         title = self.cleaned_data['title']
#         if re.match(r'\d', title):
#             raise ValidationError('error')
#         return title
#

# class Search(forms.ModelForm):
#     class Meta:
#         fields = ['title']
#         widgets = {
#             'title': forms.TextInput(
#                 attrs={
#                     'class': 'form-control'
#                 }
#             )
#         }
#
