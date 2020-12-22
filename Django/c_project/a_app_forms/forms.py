from django import forms
from django.core import validators

choices_list = (
    ('1','option 1'),
    ('2','option 2'),
    ('3','option 3'),
)

# the 1,2,3 in choices_list are the values that will be printed ref views.py
# option 1, option 2, option 3 will display in web

def check_for_valids(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name need to start with Z")

class Formname(forms.Form):
    # select many fields using ctrl
    option_select = forms.MultipleChoiceField(choices = choices_list)
    # select only one field
    option_select_2 = forms.ChoiceField(choices=choices_list)

    name=forms.CharField(min_length=3,max_length=5,label='Custom',validators=[check_for_valids],
                         widget=forms.TextInput(attrs={'placeholder':'Enter name starts with "Z"'}))
    emailId=forms.EmailField(required=True)
    text_name=forms.CharField(widget=forms.Textarea)
    verify_email = forms.EmailField(label='Enter Email Again')

    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0,message='GOTCHA BOT!!!!'),])
# we don't always use the below method for validation there is built-in method
    # def clean_botcatcher(self):
    #     botcatcher=self.cleaned_data['botcatcher']
    #     if len(botcatcher)>0:
    #         raise forms.ValidationError("Gotcha BOT!!!")
    #     return botcatcher

# this clean(self) is for all data in forms so we don;t need to clean data's seperately and this function must be under class
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['emailId']
        vmail = all_clean_data['verify_email']
        if email!=vmail:
            raise forms.ValidationError("Make Sure Email Match!!")
