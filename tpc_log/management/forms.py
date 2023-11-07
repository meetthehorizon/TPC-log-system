from django import forms
from .models import Company, Process

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        
class ProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'step': 60}),
        }

    def __init__(self, *args, **kwargs):
        super(ProcessForm, self).__init__(*args, **kwargs)

        self.fields['company_id'].label_from_instance = lambda obj: f"{obj.company_name}"
        self.fields['company_id'].empty_label = "Select a company"
        self.fields['spoc_id'].label_from_instance = lambda obj: f"{obj.roll_number} - {obj.name}"
        self.fields['spoc_id'].empty_label = "Select an SPOC"

    def clean_time(self):
        # Get the time value from the cleaned data
        cleaned_data = super().clean()
        time = cleaned_data.get('time')

        # Extract the hour and minute
        if time:
            hour = time.hour
            minute = time.minute
            return f"{hour:02}:{minute:02}"  # Format as HH:MM
        return None

