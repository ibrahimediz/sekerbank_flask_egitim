from flask import render_template, flash, redirect
from app import app
from app.forms import GirisForm

@app.route('/')
@app.route('/index')
def index():
    kullanici = {"kullaniciAdi":"Dijital Akademi"}
    veriler = [{
        'adi':"Ali",
        'soyadi':"Veli"
    },
    {
        'adi':"Ayşe",
        'soyadi':"Fatma"
    },
    ]
    return render_template('index.html',baslik="Şekerbank",kullanici=kullanici,veriler=veriler)

@app.route('/giris', methods=['GET','POST'])
def giris():
    form = GirisForm()
    if form.validate_on_submit():
        flash('Giriş yapılması için sorgulanan kullanıcı bilgileri: Kullanıcı Adı:{} Beni Hatırla:{}'.format(form.kullaniciAdi.data,form.beni_hatirla.data))
        # print('Giriş yapılması için sorgulanan kullanıcı bilgileri: Kullanıcı Adı:{} Beni Hatırla:{}'.format(form.kullaniciAdi.data,form.beni_hatirla.data))
        return redirect('/index')
    return render_template('giris.html',baslik="giriş form",form=form)