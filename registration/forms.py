from django import forms
from django.core.exceptions import ValidationError
from datetime import date

from .models import RegisteredPerson


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = RegisteredPerson

        fields = [
            'full_name',
            'father_name',
            'mother_name',
            'date_of_birth',
            'gender',
            'mobile',
            'alternate_mobile',
            'email',
            'gotra',
            'pur',
            'native_place',
            'address',
            'city',
            'district',
            'state',
            'pincode',
            'occupation',
            'education',
            'marital_status',
        ]

        widgets = {

            'full_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter full name',
                    'maxlength': '150',
                }
            ),

            'father_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter father name',
                    'maxlength': '150',
                }
            ),

            'mother_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter mother name',
                    'maxlength': '150',
                }
            ),

            'date_of_birth': forms.DateInput(
                attrs={
                    'type': 'date',
                }
            ),

            'mobile': forms.TextInput(
                attrs={
                    'placeholder': 'Enter 10-digit mobile number',
                    'maxlength': '10',
                    'inputmode': 'numeric',
                }
            ),

            'alternate_mobile': forms.TextInput(
                attrs={
                    'placeholder': 'Enter alternate mobile number',
                    'maxlength': '10',
                    'inputmode': 'numeric',
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter email address',
                }
            ),

            'gotra': forms.TextInput(
                attrs={
                    'placeholder': 'Enter gotra',
                    'maxlength': '100',
                }
            ),

            'pur': forms.TextInput(
                attrs={
                    'placeholder': 'Enter pur',
                    'maxlength': '150',
                }
            ),

            'native_place': forms.TextInput(
                attrs={
                    'placeholder': 'Enter native place',
                    'maxlength': '150',
                }
            ),

            'address': forms.Textarea(
                attrs={
                    'placeholder': 'Enter complete address',
                    'rows': 4,
                }
            ),

            'city': forms.TextInput(
                attrs={
                    'placeholder': 'Enter city',
                    'maxlength': '100',
                }
            ),

            'district': forms.TextInput(
                attrs={
                    'placeholder': 'Enter district',
                    'maxlength': '100',
                }
            ),

            'state': forms.TextInput(
                attrs={
                    'placeholder': 'Enter state',
                    'maxlength': '100',
                }
            ),

            'pincode': forms.TextInput(
                attrs={
                    'placeholder': 'Enter 6-digit pincode',
                    'maxlength': '6',
                    'inputmode': 'numeric',
                }
            ),

            'occupation': forms.TextInput(
                attrs={
                    'placeholder': 'Enter occupation',
                    'maxlength': '150',
                }
            ),

            'education': forms.TextInput(
                attrs={
                    'placeholder': 'Enter education',
                    'maxlength': '150',
                }
            ),
        }

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')

        if not mobile:
            return mobile

        if not mobile.isdigit():
            raise ValidationError(
                'Mobile number must contain only digits.'
            )

        if len(mobile) != 10:
            raise ValidationError(
                'Mobile number must be exactly 10 digits.'
            )

        return mobile

    def clean_alternate_mobile(self):
        mobile = self.cleaned_data.get('alternate_mobile')

        if not mobile:
            return mobile

        if not mobile.isdigit():
            raise ValidationError(
                'Alternate mobile number must contain only digits.'
            )

        if len(mobile) != 10:
            raise ValidationError(
                'Alternate mobile number must be exactly 10 digits.'
            )

        return mobile

    def clean_pincode(self):
        pincode = self.cleaned_data.get('pincode')

        if not pincode:
            return pincode

        if not pincode.isdigit():
            raise ValidationError(
                'Pincode must contain only digits.'
            )

        if len(pincode) != 6:
            raise ValidationError(
                'Pincode must be exactly 6 digits.'
            )

        return pincode

    def clean_date_of_birth(self):
        dob = self.cleaned_data.get('date_of_birth')

        if dob and dob > date.today():
            raise ValidationError(
                'Date of birth cannot be in the future.'
            )

        return dob