from django import forms
from employee.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['eid', 'ename', 'elname', 'eemail', 'econtact']

