import os
import shutil

#Abfrage des Kunden
print("Für welchen Kunden soll das Projekt angelegt werden?")
Kunde = input()

#Festlegung des Speicherortes
#dirPath = ("C:\\Users\\shima\\OneDrive\\Python OneDrive\\" + Kunde)
cwd = (os.getcwd())

#Abfrage ob der Ordner "Kunde" schon vorhanden ist?!
if not os.path.isdir(cwd): #Wenn der Ordner "Kunde" nicht existiert, wird der Ordner erstellt
    print('Der Ordner existiert nicht und wird erstellt') #Stautusmeldung
    os.makedirs(Kunde, mode=0o777, exist_ok=False)  
else: #Wenn der Ordner bereits existierte wird dieser direkt geöffnet
    os.chdir(cwd)
    print('Ordner existiert und wird geöffnet') #Statusmeldung   


#Wenn der Ordner erst erstellt werden musste, wird mit folgendem Befehl in den Ordner gewechselt.
os.chdir(cwd + '\\' + Kunde)

#Abfrage des Projektnames und Erstellung des Projektordners
print("Wie lautet der Projektname?")
Projektname = input()
os.makedirs(Projektname, mode=0o777, exist_ok=False) #Erstellung des Projektordners
os.chdir(Projektname) #Öffnen des Projektordners

#Erstellung der gewünschten Unterordner
os.makedirs('Angebote', mode=0o777, exist_ok=False)
print("Der Ordner Angebote wurde erstellt")#Statusmeldung

os.makedirs('Bilder', mode=0o777, exist_ok=False)
print("Der Ordner Bilder wurde erstellt")#Statusmeldung

os.makedirs('Dokumente', mode=0o777, exist_ok=False)
print("Der Ordner Dokumente wurde erstellt")#Statusmeldung

os.makedirs('Kalkulation', mode=0o777, exist_ok=False)
print("Der Ordner Kalkulation wurde erstellt")#Statusmeldung

os.makedirs('Konstruktion', mode=0o777, exist_ok=False)
print("Der Ordner Konstruktion wurde erstellt")#Statusmeldung

os.makedirs('Zeichnungen', mode=0o777, exist_ok=False)
print("Der Ordner Zeichnungen wurde erstellt")#Statusmeldung


os.chdir(cwd)

shutil.copy(cwd + '\\Root.ipj', cwd + '\\' + Kunde + '\\' + Projektname + '\\Konstruktion\\' + '\\Root.ipj')
print('Inventor-Projektdatei wurde im Konstruktionsordner erstellt') #Statusmeldung

shutil.copy(cwd + '\\Kalkulation.xlsx', cwd + '\\' + Kunde + '\\' + Projektname + '\\Kalkulation\\' + '\\Kalkulation.xlsx')
print('Kalkulationdatei wurde im Ordner Kalkulation erstellt') #Statusmeldung

shutil.copy(cwd + '\\Root.csv', cwd + '\\' + Kunde + '\\' + Projektname + '\\Kalkulation\\' + '\\Root.csv')
print('Kalkulationdatenbank wurde im Ordner Kalkulation erstellt') #Statusmeldung