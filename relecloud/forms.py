from django import forms
from .models import InfoRequest

class InfoRequestForm(forms.ModelForm):
    class Meta:
        model = InfoRequest
        fields = ['name', 'email', 'notes', 'cruise']  # Asegúrate de incluir todos los campos que el usuario necesita rellenar

    def __init__(self, *args, **kwargs):
        super(InfoRequestForm, self).__init__(*args, **kwargs)
        # Aquí puedes añadir cualquier lógica adicional para inicializar el formulario, como configurar clases CSS, etc.
