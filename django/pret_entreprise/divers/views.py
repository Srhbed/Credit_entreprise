from django.shortcuts import render
from .form import ApiForm
import requests
import json



def Credit(request):
    
    header = {
        'accept': 'application/json',
    'Content-Type': 'application/json'}
    form1 = ApiForm
    if request.method == 'POST':
        form=form1(request.POST or None)
        if form.is_valid():
            data=json.dumps(form.cleaned_data)
            response=requests.post('http://127.0.0.1:8000/predict',headers=header,data=data)
            print(response)
            return render(request,'formulaire.html',context={'response':response.text, "form" : form1})
    else:
        context={'form' : form1}
        return render(request,'formulaire.html',context=context)