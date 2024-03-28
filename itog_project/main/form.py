from django import forms
from .models import Offer, WorkerResume, EmployeerResume, Message

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border mb-12'
MESSAGE_INPUT_CLASSES = 'w-2/3 py-4 px-6 rounded-xl border border-teal-400'


class AddOfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ('job_title', 'description', 'salary', 'is_active')
        widgets = {'job_title': forms.TextInput(attrs={'class': INPUT_CLASSES}),
                   'description': forms.Textarea(attrs={'class': INPUT_CLASSES}),
                   'salary': forms.TextInput(attrs={'class': INPUT_CLASSES})}


class WorkerResumeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(WorkerResumeForm, self).__init__(*args, **kwargs)
        self.fields['profile_photo'].required = False
        self.fields['portfolio'].required = False

    class Meta:
        model = WorkerResume
        fields = ('profile_photo', 'name', 'lastname', 'surname', 'age', 'description', 'education',
                  'experience', 'email', 'phone_number', 'portfolio')
        widgets = {'age': forms.NumberInput(),
                   'name': forms.TextInput(),
                   'surname': forms.TextInput(),
                   'lastname': forms.TextInput(),
                   'education': forms.Select(choices=(
                       ('Высшее', 'Высшее'), ('Среднее', 'Среднее'), ('Основное', 'Основное'), ('Другое', 'Другое'))),
                   'experience': forms.Select(choices=(
                       ('Без опыта', 'Без опыта'), ('3-6 месяцев', '3-6 месяцев'), ('6-12 месяцев', '6-12 месяцев'),
                       ('1-2 года', '1-2 года'), ('3-5 лет', '3-5 лет'), ('5-10 лет', '5-10 лет'),
                       ('10+ лет', '10+ лет'))),
                   'phone_number': forms.TextInput(),
                   'portfolio': forms.FileInput(),
                   'description': forms.Textarea()}


class EmployeerResumeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EmployeerResumeForm, self).__init__(*args, **kwargs)
        self.fields['profile_photo'].required = False

    class Meta:
        model = EmployeerResume
        fields = ('profile_photo', 'organization_name', 'email', 'phone_number')
        widgets = {'organization_name': forms.TextInput(),
                   'email': forms.TextInput(),
                   'phone_number': forms.TextInput()}


class MessageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False

    class Meta:
        model = Message
        fields = ('text', 'image')
        widgets = {'text': forms.TextInput(attrs={'class': MESSAGE_INPUT_CLASSES}),
                   'image': forms.FileInput(attrs={'class': MESSAGE_INPUT_CLASSES})}
