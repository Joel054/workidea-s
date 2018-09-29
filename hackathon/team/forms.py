from django.forms import ModelForm, Textarea

from hackathon.team.models import Team, Member


class FormTeam(ModelForm):
    class Meta:
        model = Team
        fields = ["name", "description"]
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 20}),
        }


class FormMember(ModelForm):
    class Meta:
        model = Member
        fields = ["level_asses", "id_user"]
