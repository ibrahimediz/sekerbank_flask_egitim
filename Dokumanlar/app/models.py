from app import db

class Kullanici(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    kullaniciadi = db.Column(db.String(64),index=True, unique=True)
    eposta = db.Column(db.String(120),index=True,unique=True)
    sifre_hash = db.Column(db.String(120))


    def __repr__(self):
        return '<Kullanici {}>'.format(self.kullaniciadi)
