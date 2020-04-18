from django import forms
from .models import List,ListAllDefects

class ListForm(forms.ModelForm):
	class Meta:
		model = List
		fields = ["item", "completed"]

class ListDefectForm(forms.ModelForm):
	class Meta:
		model = ListAllDefects
		fields = ["issuename","originator","priority","addinfo","expecteddate","createddate","oremailid","status"]
		#fields = ["issuename","originator","priority","createddate","addinfo","expecteddate"]