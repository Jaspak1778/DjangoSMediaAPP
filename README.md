Django REST API - Windows
Kevyt testiympäristö sosiaalista mediaa muistuttavalle REST API
Tämä projekti on sosiaalisen median tyylinen sovellus, joka tarjoaa REST API -pohjaiset toiminnot. Sovellus on tarkoitettu testikäyttöön ja toimii parhaiten Windows-ympäristössä.

Kuvaus

Sovelluksen tarkoituksena on tarjota CRUD-toiminnot postauksille, kommenteille ja käyttäjäprofiileille. Käyttämällä Django REST Frameworkia API toimii testiserverillä, jonka voi avata paikalliselle koneelle.
Asennus

Kloonaa repo



git clone <repon-url>
cd <projektin-hakemisto>

Luo virtuaaliympäristö

bash

python -m venv venv

Aktivoi virtuaaliympäristö

    Windows: venv\Scripts\activate


Asenna riippuvuudet
Varmista, että virtuaaliympäristö on aktivoitu ennen asennusta:

bash

pip install -r requirements.txt

Tietokannan migraatiot



python manage.py makemigrations
python manage.py migrate

Käynnistä kehityspalvelin



    python manage.py runserver

Käyttöohjeet

Avaa selain osoitteeseen:

    http://127.0.0.1:8000/api/posts/ tai lisää muita päätepisteitä seuraavan kohdan mukaisesti.

API-päätepisteet

    Posts: http://127.0.0.1:8000/api/posts/
    Comments: http://127.0.0.1:8000/api/comments/
    Users: http://127.0.0.1:8000/api/users/