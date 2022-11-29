from django import forms

from users.models import Account


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active',
                  'phone', 'password')
