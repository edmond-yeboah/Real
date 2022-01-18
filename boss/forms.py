from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


from.models import listing

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class addlistingForm(forms.ModelForm):
    class Meta:
        model = listing
        fields = [
            'image',
            'title','city',
            'state','zipcode','property_type','property_status',
            'price','description','number_bedrooms',
            'number_rooms','number_bath','number_garage','year_built',
            'floor_size',
        ]
        widgets ={
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Luxurious house at Legon'}),
            # 'address':forms.TextInput(attrs={'class':'form-control filter-input','placeholder':'Oak Street'}),
            # 'neighbouhoood':forms.TextInput(attrs={'class':'form-control filter-input','placeholder':'Cantoment'}),
            # 'country':forms.TextInput(attrs={'class':'form-control filter-input','placeholder':'Ghana'}),
            'city':forms.TextInput(attrs={'class':'form-control','placeholder':'Accra'}),
            'state':forms.TextInput(attrs={'class':'form-control','placeholder':'State'}),
            'zipcode':forms.TextInput(attrs={'class':'form-control','placeholder':'Zip Code'}),
            'property_type':forms.Select(attrs={'class':'form-control'}),
            # 'floor_select':forms.Select(attrs={'class':'listing-input hero__form-input  form-control custom-select'}),
            'property_status':forms.Select(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control','placeholder':'Total(sale)   or   /month(rent)'}),
            'description':forms.Textarea(attrs={'class':'form-control h-120','rows':'4','placeholder':'Enter your text here'}),
            # 'property_id':forms.TextInput(attrs={'class':'form-control filter-input','placeholder':'ZOAC25'}),
            'number_bedrooms':forms.NumberInput(attrs={'class':'form-control','placeholder':'4'}),
            'number_rooms':forms.NumberInput(attrs={'class':'form-control','placeholder':'8'}),
            'number_bath':forms.NumberInput(attrs={'class':'form-control','placeholder':'4'}),
            'number_garage':forms.NumberInput(attrs={'class':'form-control','placeholder':'2'}),
            'year_built':forms.TextInput(attrs={'class':'form-control','placeholder':'17-05-1992'}),
            # 'image':forms.FileInput(attrs={'class':'add-listing__input-file'}),
            # 'amenity':forms.SelectMultiple(attrs={'class':'filter-checkbox'}),
            # 'rooms_size':forms.NumberInput(attrs={'class':'form-control filter-input','placeholder':'440 x 440'}),
            # 'bath_size':forms.NumberInput(attrs={'class':'form-control filter-input','placeholder':'200 x 200'}),
            'floor_size':forms.NumberInput(attrs={'class':'form-control','placeholder':'1240'}),
            
        }