from django import forms

class findUserForm(forms.Form):
    usrname = forms.CharField(max_length=100,label="",
                           widget= forms.TextInput
                           (attrs={'placeholder':'Search for a user', 'class':'search-form'}))