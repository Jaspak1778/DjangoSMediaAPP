# Django REST API - Windows

Kevyt testiympäristö sosiaalista mediaa muistuttavalle REST API

Tämä projekti on sosiaalisen median tyylinen sovellus, joka tarjoaa REST API -pohjaiset toiminnot. Sovellus on tarkoitettu testikäyttöön ja toimii parhaiten Windows-ympäristössä.

Sovelluksen tarkoituksena on tarjota CRUD-toiminnot postauksille, kommenteille ja käyttäjäprofiileille. Käyttämällä Django REST Frameworkia API toimii testiserverillä, jonka voi avata paikalliselle koneelle.
##
Asennus

Kloonaa repo uuteen kansioon jonka voit nimetä miten vain.
Kansion sisällä osoite kenttään cmd ja anna komento

    git clone <repon-url>

Avaa IDE antamalla komento.
    
    code .

Luo virtuaali ympäristö IDE:n terminaalissa.

    python -m venv venv

Ja aktivoi virtuaaliympäristö IDE:n terminaalissa.

    Windows: venv\Scripts\activate

Asenna riippuvuudet
Varmista, että virtuaaliympäristö on aktivoitu ennen asennusta:

    pip install -r requirements.txt

Tietokannan migraatiot

    python manage.py makemigrations
    python manage.py migrate


Käynnistä kehityspalvelin

    python manage.py runserver`

Käyttöohjeet:

Avaa selain osoitteeseen:

    http://127.0.0.1:8000/api/posts/ tai lisää muita päätepisteitä seuraavan kohdan mukaisesti.

API-päätepisteet

    Posts: http://127.0.0.1:8000/api/posts/
    Comments: http://127.0.0.1:8000/api/comments/
    Users: http://127.0.0.1:8000/api/users/


*Muutoksia tulossa*

*TODO - REST Kirjautuminen.*

*TODO - Poistetaan testi aikaiset koodit, jotta vain REST toimintaan tarvittavat koodit on esillä, selkeyden vuoksi.*