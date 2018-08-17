from django import forms

class URLForm(forms.Form):
	url = forms.CharField(
		max_length=250, 
		label='',
		widget=forms.TextInput(
			attrs={
				'class':'form-control main-input',
				'placeholder':'Enter URL',
				'required': 'required',
			}
		)
	)