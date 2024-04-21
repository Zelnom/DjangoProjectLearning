from django import forms

from student.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Please enter your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Please enter your last name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your age'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Please enter your description'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'trainer': forms.Select(attrs={'class': 'form-select'}),
        }

        """
        Metoda clean in formularele Django este o parte centrala a sistemului de validare a datelor
        Atunci cand creati sau personalizati un formular in Django puteti implementa validari personalizate care
        se va aplica pe intregul formular
        
        Acesta
        """


    def clean(self):
        cleaned_data = super().clean()  # obtineti access la datele din formular

        # o validare pentru unicitatea adresei de email

        # Varianta
        # get_email = cleaned_data.get('email')
        # all_students = Student.objects.all()
        # for student in all_students:
        #     if get_email == student.email:
        #         msg = 'Email already'
        #         self._errors['email'] = self.error_class([msg])

        # Varianta
        get_email = cleaned_data.get("email")
        check_email = Student.objects.filter(email=get_email)
        # if check_email.exists(): sau
        if len(check_email) > 0:
            msg = 'Email already registered'
            self._errors['email'] = self.error_class([msg])

        # o unicitate pe first_name si last_name. Nu putem salva un student cu acelsi nume si prenume de 2 ori
        get_first_name = cleaned_data.get("first_name")
        get_last_name = cleaned_data.get("last_name")
        check_stud = Student.objects.filter(first_name=get_first_name, last_name=get_last_name)

        if check_stud.exists():
            msg = "The first name or last name is invalid"
            self._errors["first_name"] = self.error_class([msg])
        # o validare pe campul description in care utilizatorul TREBUIE sa adauge minim 10 caractere
        get_description = cleaned_data.get("description")
        if len(get_description) < 10:
            msg = "The description is too short"
            self._errors["description"] = self.error_class([msg])

        # o validare pe campurile start_date si end_date. Daca start_date este > end_date sa genereze o eroare.
        get_start_date = cleaned_data.get("start_date")
        get_end_date = cleaned_data.get("end_start")
        if get_start_date > get_end_date:
            msg = "The start date is greater than the end date"
            self._errors["start_date"] = self.error_class([msg])

        return cleaned_data


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Please enter your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Please enter your last name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your age'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Please enter your description'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'trainer': forms.Select(attrs={'class': 'form-select'}),
        }