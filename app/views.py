from django.shortcuts import render
from app import forms
# Create your views here.
def django_forms(request):
    form=forms.NameForm()
    d={'form':form}
    if request.method=='POST':
        form_data=forms.NameForm(request.POST)
        if form_data.is_valid():
            form_checked_data=form_data.cleaned_data
            return render(request,'response.html',form_checked_data)
    return render(request,'django_forms.html',d)