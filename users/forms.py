from django import forms

from users.models import Account, UserAdmin


class UserAdminForm(forms.ModelForm):
    avno_user = forms.ModelChoiceField(
        queryset=Account.objects.filter(is_avno=True),
        to_field_name='first_name',
        required=True,
        initial='avno_user',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = UserAdmin
        fields = (
            'username', 'first_name', 'last_name', 'email', 'phone',
            'avno_user', 'is_active', 'password'
        )


class AvnoAdminForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('username', 'first_name', 'last_name', 'email', 'phone',
                  'is_superuser', 'is_avno', 'is_active', 'password')
