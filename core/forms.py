from django import forms
from .models import Message, Project

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['recipient', 'subject', 'body']

    def save(self, sender=None, commit=True):
        message = super().save(commit=False)  # Get the instance without committing
        message.sender = sender  # Manually set the sender
        if commit:
            message.save()  # Save the message to the database
        return message

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date', 'status', 'stakeholders']
