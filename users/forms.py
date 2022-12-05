from django import forms

from users.models import Account


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('username', 'first_name', 'last_name', 'email', 'phone',
                  'is_superuser', 'avno_user', 'is_active', 'password')
