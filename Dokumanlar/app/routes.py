from flask import render_template
from app import app

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