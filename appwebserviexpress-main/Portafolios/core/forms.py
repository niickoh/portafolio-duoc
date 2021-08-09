from django import forms
from django.forms import widgets
from django.forms.models import fields_for_model
from .models import Reservadehora, Usuarioescritorio, Boleta
from datetime import datetime, timedelta, date, tzinfo
from django.utils import timezone
from .models import Reservadehora
from django.core.exceptions import ValidationError
import pytz


class ReservadeHoraForm(forms.ModelForm):
    
    asunto = forms.CharField(widget=forms.Textarea(attrs={'rows':4}))
    hora = forms.CharField()
    
    def clean_fecha_solicitud(self):
        fecha_solicitud = self.cleaned_data['fecha_solicitud']
        if fecha_solicitud < (timezone.now() + timedelta(days=-1)):
            raise ValidationError("Fecha del pasado.")
        
        return fecha_solicitud
    
    def clean_hora(self):
        horas_permitidas = ['09:00','09:15','09:30','09:45','10:00','10:15','10:30','10:45'
                            ,'11:00','11:15','11:30','11:45','12:00','12:15','12:30','13:00'
                            ,'13:15','13:30','13:45','14:00','14:15','14:30','14:45','15:00'
                            ,'15:15','15:30','15:45','16:00','16:15','16:30','16:45','17:00'
                            ,'17:15','17:30','17:45','18:00','18:15','18:30','18:45','19:00'
                            ,'19:15','19:30','19:45','20:00','20:15','20:30','20:45']

        hora = self.cleaned_data['hora']
        if hora not in horas_permitidas:
            raise ValidationError("Hora no valida.")
        
        return hora
    class Meta:
        model = Reservadehora
        fields = ('fecha_solicitud','asunto','tiposervicio','usuarioescritorio')

    def clean(self):
        data = self.cleaned_data
        if not ('fecha_solicitud' in data.keys() and 'hora' in data.keys()):
            raise forms.ValidationError("Este campo es requerido.")  
        fecha_solicitudd = data['fecha_solicitud']
        fecha_solicitudd = fecha_solicitudd.date()
        hora = data['hora']
        fecha = str(fecha_solicitudd) + ' ' + str(hora)
        print('fecha str:',fecha)
        fecha_f = datetime.strptime(fecha, "%Y-%m-%d %H:%M")
        print('fecha 1er strptime:',fecha_f)
        fecha_formato = fecha_f.strftime("%d/%m/%Y %H:%M")
        print('fecha formato cambiado:',fecha_formato)
        fecha_f = datetime.strptime(fecha_formato,"%d/%m/%Y %H:%M")
        fechas = Reservadehora.objects.filter(fecha_solicitud=fecha_f).count()
        if fechas >= 1:
            raise forms.ValidationError("Fecha no disponible.")
        return data
    
    def __init__(self, *args, **kwargs):

        super(ReservadeHoraForm, self).__init__(*args,**kwargs)
        self.fields['usuarioescritorio'] = forms.ModelChoiceField(queryset=Usuarioescritorio.objects.filter(tipousuario_id=5))

        for field in self.fields:
            
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].widget.attrs.update({'autocomplete': 'off'})

        self.fields['hora'].widget.attrs.update({'class': 'form-control timepicker'})        


class BoletaForm(forms.ModelForm):

    

    class Meta:
        model = Boleta
        fields = '__all__'