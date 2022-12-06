from app import app

@app.route('/')
@app.route('/index')
def index():
    kullanici = {"kullaniciAdi":"Şekerbank"}
    return '''
    <html>
    <head>
        <title>Ana Sayfa</title>
    </head>
    <body>
    <h1> Merhaba ''' + kullanici["kullaniciAdi"] +'''
    </h1>
    </body>
    </html>
    '''