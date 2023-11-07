from django import forms
from .models import Round


CHOICES = [
        ('NS', 'Not Started'),
        ('CLR', 'Cleared'),
        ('AWR', 'Awaiting Result'),
        ('NC', 'Not Cleared'),
        ('O', 'Ongoing'),
    ]

class DateTimeLocalInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class RoundForm(forms.Form):
    round_1_intime = forms.DateTimeField(widget=DateTimeLocalInput)
    round_1_outtime = forms.DateTimeField(widget=DateTimeLocalInput)
    round_1_status = forms.ChoiceField(choices=CHOICES)
    round_2_intime = forms.DateTimeField(widget=DateTimeLocalInput)
    round_2_outtime = forms.DateTimeField(widget=DateTimeLocalInput)
    round_2_status = forms.ChoiceField(choices=CHOICES)
    round_3_intime = forms.DateTimeField(widget=DateTimeLocalInput)
    round_3_outtime = forms.DateTimeField(widget=DateTimeLocalInput)
    round_3_status = forms.ChoiceField(choices=CHOICES)

    def save(self, students):
        round_1_intime = self.cleaned_data['round_1_intime']
        round_1_outtime = self.cleaned_data['round_1_outtime']
        round_1_status = self.cleaned_data['round_1_status']
        round_2_intime = self.cleaned_data['round_2_intime']
        round_2_outtime = self.cleaned_data['round_2_outtime']
        round_2_status = self.cleaned_data['round_2_status']
        round_3_intime = self.cleaned_data['round_3_intime']
        round_3_outtime = self.cleaned_data['round_3_outtime']
        round_3_status = self.cleaned_data['round_3_status']

        round_1 = Round(shortlist_id= students.shortlist_id, round_number =1, round_start=round_1_intime, round_end=round_1_outtime, status= round_1_status )
        round_2 = Round(shortlist_id= students.shortlist_id, round_number =2, round_start=round_2_intime, round_end=round_2_outtime, status= round_2_status )
        round_3 = Round(shortlist_id= students.shortlist_id, round_number =3, round_start=round_3_intime, round_end=round_3_outtime, status= round_3_status )

        if round_1_intime is not None and round_1_outtime is not None:
            round_1.save()
        if round_2_intime is not None and round_2_outtime is not None:
            round_2.save()
        if round_3_intime is not None and round_3_outtime is not None:
            round_3.save()