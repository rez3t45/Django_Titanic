from django import forms

class PredictionForm(forms.Form):
     
    pclass = forms.IntegerField(label='pclass', min_value=1)
    sex = forms.IntegerField(label='sex', min_value=0,max_value=1) 
    age = forms.DecimalField(label='age', min_value=0, decimal_places=1)
    sibsp = forms.IntegerField(label='sibsp', min_value=0)
    parch = forms.IntegerField(label='parch', )
    #fare = forms.DecimalField(label='fare', min_value=0, decimal_places=1 )
    fare = forms.DecimalField(label='fare', min_value=0, decimal_places=2)
    embarked = forms.IntegerField(label='embarked', min_value=0)