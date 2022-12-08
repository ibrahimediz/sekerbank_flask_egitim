from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired

class GirisForm(FlaskForm):
    kullaniciAdi = StringField('Kullanıcı Adı',validators=[DataRequired()])
    sifre = PasswordField('Şifre',validators=[DataRequired()])
    beni_hatirla = BooleanField('Beni Hatırla')
    onay = SubmitField('Kayıt Yap')