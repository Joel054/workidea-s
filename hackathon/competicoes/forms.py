from django.forms import ModelForm, Textarea

from competicoes.models import Activity, Premium, Phase, Hackathon


class FormActivity(ModelForm):
    class Meta:
        model = Activity
        fields = ["name", "description"]
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 20}),
        }


class FormPremium(ModelForm):
    class Meta:
        model = Premium
        fields = ["name", "description"]
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 20}),
        }


class FormPhase(ModelForm):
    class Meta:
        model = Phase
        fields = ["name", "description"]
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 20}),
        }


class FormHackathon(ModelForm):
    class Meta:
        model = Hackathon
        fields = ["name", "description"]
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
