from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Producto

class crearFormUsuario(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
    def __init__(self, *args, **kwargs):
        super(crearFormUsuario, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
             {'class': 'main__input', 'placeholder': 'Correo electrónico', 'name': 'mail'})
        self.fields['username'].widget.attrs.update(
            {'class': 'main__input', 'placeholder': 'Nombre de usuario'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'main__input', 'placeholder': 'Contraseña'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'main__input', 'placeholder': 'Confirmar contraseña'})    

class formProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        fields_order = ['nombre_producto', 'descript_producto', 'img_producto', 'valor_compra', 'precio_producto','activo']

    def __init__(self, *args, **kwargs):
        super(formProducto, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

        self.fields['nombre_producto'].widget.attrs.update({'placeholder': 'Nombre del Producto'})
        self.fields['descript_producto'].widget.attrs.update({'placeholder': 'Descripción del Producto'})
        self.fields['img_producto'].widget.attrs.update({'class': 'form-control-file'})
        self.fields['valor_compra'].widget.attrs.update({'placeholder': 'Valor de Compra'})
        self.fields['precio_producto'].widget.attrs.update({'placeholder': 'Precio del Producto'})
        self.fields['activo'].widget = forms.RadioSelect(choices=[(True, 'Activo'), (False, 'Inactivo')])
        self.fields['activo'].empty_label = None  # Para que no haya una opción vacía
    
    