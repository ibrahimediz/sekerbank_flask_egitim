liste = ["Abdullah","Anıl","Burak","Cem","Cihan","Emre","Dilay",
"Eyuphan","Furkan","İsmail","Nafiz","Özge","Pelin","Sevda","Fırat","Ediz","Serap"]
import os
dosyaismi = "06_02_finally.py"
klasorismi = "templates"
for item in liste:
    if not os.path.exists(os.path.join("Egzersizler",item,"app")):
        os.mkdir(os.path.join("Egzersizler",item,"app"))
    if not os.path.exists(os.path.join("Egzersizler",item,"app",klasorismi)):
        os.mkdir(os.path.join("Egzersizler",item,"app",klasorismi))
    open(os.path.join("Egzersizler",item,"app",klasorismi,"base.html"),"a+")