from django import forms



class ApiForm(forms.Form):
    NAICS=forms.IntegerField(initial=45)
    Term=forms.IntegerField(initial=60)
    NoEmp=forms.IntegerField(initial=12)
    CreateJob=forms.IntegerField(initial=20)
    FranchiseCode=forms.IntegerField(initial=1)
    UrbanRural=forms.IntegerField(initial=0)
    GrAppv=forms.IntegerField(initial=40000)
    LowDoc=forms.CharField(initial='Y')
    RevLineCr=forms.CharField(initial='Y')