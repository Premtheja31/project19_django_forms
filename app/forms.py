from django import forms
g=[['MALE','male'],['FEMALE','female'],['OTHERS','others']]
cour=[['PYTHON','python'],['SQL','sql'],['DJANGO','django']]
class NameForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField(min_value=18)
    email=forms.EmailField()
    password=forms.CharField(max_length=20,widget=forms.PasswordInput)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    courses=forms.MultipleChoiceField(choices=cour,widget=forms.CheckboxSelectMultiple)