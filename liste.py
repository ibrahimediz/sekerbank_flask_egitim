liste = ["Abdullah","Anıl","Burak","Cem","Cihan","Emre","Dilay",
"Eyuphan","Furkan","İsmail","Nafiz","Özge","Pelin","Sevda","Fırat","Ediz","Serap"]
import os
dosyaismi = "06_02_finally.py"
klasorismi = "app"
for item in liste:
    if not os.path.exists(os.path.join("Egzersizler",item)):
        os.mkdir(os.path.join("Egzersizler",item))
        open(os.path.join("Egzersizler",item,"run.py"),"a+")
    if not os.path.exists(os.path.join("Egzersizler",item,klasorismi)):
        os.mkdir(os.path.join("Egzersizler",item,klasorismi))
        open(os.path.join("Egzersizler",item,klasorismi,"__init__.py"),"a+")