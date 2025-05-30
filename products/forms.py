from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(choices=[(i, i) for i in range(1, 6)]),
            'comment': forms.Textarea(attrs={'rows': 4}),
        }


SKIN_TYPES = [
    ('acne', 'Acne-prone'),
    ('dry', 'Dry'),
    ('sensitive', 'Sensitive'),
    ('ageing', 'Ageing'),
]

SKIN_CONCERNS = [
    ('acne', 'Spots or Acne'),
    ('dry', 'Dry Skin'),
    ('sensitive', 'Sensitive Skin'),
    ('ageing', 'Ageing or Fine Lines'),
]

SKIN_FEEL = [
    ('acne', 'Oily'),
    ('dry', 'Dry or Tight'),
    ('sensitive', 'Red, or Sore'),
    ('normal', 'Normal'),
]


class SkinQuizForm(forms.Form):
    q1 = forms.ChoiceField(
        label="How would you describe your skin?",
        choices=SKIN_TYPES,
        widget=forms.RadioSelect
    )
    q2 = forms.ChoiceField(
        label="What’s your biggest skin concern?",
        choices=SKIN_CONCERNS,
        widget=forms.RadioSelect
    )
    q3 = forms.ChoiceField(
        label="How does your skin feel after cleansing?",
        choices=SKIN_FEEL,
        widget=forms.RadioSelect
    )
