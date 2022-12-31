from django import forms
from employee.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['eid'].widget.attrs.update({'class': 'form-control'})
        self.fields['ename'].widget.attrs.update({'class': 'form-control'})
        self.fields['elname'].widget.attrs.update({'class': 'form-control'})
        self.fields['eemail'].widget.attrs.update({'class': 'form-control'})
        self.fields['econtact'].widget.attrs.update({'class': 'form-control'})
