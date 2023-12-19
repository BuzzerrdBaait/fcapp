from django import forms

from .models import *


class Registration(forms.Form):

    username = forms.CharField(label='Username', max_length=100)

    email = forms.EmailField(label='Email')

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

class DeckForm(forms.ModelForm):

    class Meta:

        model = Deck

        fields = ['title','description', 'category','public']

        widgets = {

            'public': forms.CheckboxInput(), 

        }


class NoteForm(forms.ModelForm):

        class Meta:

            model = Note

            fields = ['note']

            widgets={
                'note':
                forms.Textarea(attrs={'rows':3})
            }

class CardForm(forms.ModelForm):

    class Meta:

        model = Card

        fields = ['question', 'answer']

class UserProfileForm(forms.ModelForm):

    class Meta:

        model = User_Profile

        fields = ['username', 'email'] 

class DeleteDeckForm(forms.Form):

    deck_id = forms.IntegerField(widget=forms.HiddenInput)

class DeleteCardForm(forms.Form):

    card_id = forms.IntegerField(widget=forms.HiddenInput)



class ContactForm(forms.ModelForm):

    class Meta:

        model = Contact

        fields = ['name', 'email', 'message']


class AuthenticationForm(forms.Form):

    authentication_key = forms.CharField(max_length=50, required=True)

    
