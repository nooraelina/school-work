## Tietokannat-tentti

Tentissä on 8 tehtävää. Tentistä voit saada tehtävästä voit saada 20 pistettä. Tentissä voit käyttää kurssin materiaaleja (esitykset, omat vastaukset) Optimasta. 

1. Laadi kysely jolla saat Northwind-tietokannasta kaikki tilaukset, jotka on toimitettu muualle kuin USA:han tai Saksaan. Näytä tulostaulussa vain tilaustunnus ja toimituspäivä.  (2 pts)
```
SELECT OrderID AS 'tilaustunnus', ShippedDate AS 'toimituspäivä', ShipCountry 
FROM orders 
WHERE ShipCountry != 'USA' AND ShipCountry != 'Germany'
```

2. Laadi kysely jolla selvität Northwind-tietokannasta kuinka monta tuotetta on varastossa? (2 pts)
```
SELECT SUM(UnitsInStock) AS 'Tuotteita varastossa:' FROM products
```

3. Selitä käsitteet ”Primary key” ja ”Foreign Key”. Kerro lisäksi miten ne liityvät toisiinsa? (2 pts)

Primary key on jokaisella rivillä uniikki, eli sen avulla rivi voidaan tunnistaa. Foreign keytä voi olla useampia yhdessä taulussa, ja ne yhdistävät taulun jonkin toisen taulun primary keyhin. Primary key ei voi olla null, mutta foreign key voi. Keyt yhdistävät siis tauluja toisiinsa. 

4. Laadi kysely JOIN:a käyttäen jolla saat Northwind-tietokannasta tuotteiden toimittajat. Näytä  tuloslistassa toimittajan nimi ja tuotteen nimi. (2 pts)
```
SELECT suppliers.CompanyName, products.ProductName 
FROM suppliers JOIN products ON suppliers.SupplierID = products.SupplierID
```
5. Mitä tarkoittaa ER-mallissa entiteetti? (2 pts)

Entiteetti on kuin olio-ohjelmoinnissa olio. Entiteetti on jokin asia, joka määrittelee instanssien yhteiset ominaisuudet. Entiteeteiksi määritellään sellaisia asioita, joita voi olla monta, esim. autotietokannassa autoja. Entiteeteissä on lisäksi yksityiskohtia, mitä jokaisesta instanssista halutaan tietää.

6. Laadi ER-malli yleisurheilukilpailun ilmoittautumis- ja tulosjärjestelmän tietokannasta. Kilpailuihin osallistuu useita kilpailijoita useasta seurasta. Yksi kilpailija osallistuu luonnollisesti vähintään yhteen lajiin. Jokaisessa lajissa on päätuomari jonka tehtäviin kuuluu tulosten kirjaaminen. (4 pts)
 
Entiteetit: Ilmoittautumiset, Tulokset, Kilpailijat, Seurat, Lajit, Tuomarit

7. Laadi SQL-lauseet edellisen tehtävän tietokannan luomiseksi (3 pts)
```
CREATE DATABASE Yleisurheilukilpailu;
CREATE TABLE yleisurheilukilpailu.kilpailijat (
    kilpailijaID INT NOT NULL AUTO_INCREMENT,
    nimi VARCHAR(50) NOT NULL,
    seura INT NOT NULL,
    puhelinnro INT(10),
    PRIMARY KEY (kilpailijaID));
CREATE TABLE yleisurheilukilpailu.seurat (
    seuraID INT NOT NULL AUTO_INCREMENT,
    seurannimi VARCHAR(50) NOT NULL,
    paikkakunta VARCHAR(50) NOT NULL,
    PRIMARY KEY (seuraID));
CREATE TABLE yleisurheilukilpailu.lajit (
    lajiID INT NOT NULL AUTO_INCREMENT,
    laji VARCHAR(80) NOT NULL,
    paatuomari INT,
    PRIMARY KEY (lajiID));
CREATE TABLE yleisurheilukilpailu.ilmoittautumiset (
    ilmoID INT NOT NULL AUTO_INCREMENT,
    lajiID INT,
    kilpailijaID INT,
    PRIMARY KEY (ilmoID));
CREATE TABLE yleisurheilukilpailu.tuomarit (
    tuomariID INT NOT NULL AUTO_INCREMENT,
    nimi VARCHAR(60),
    laji VARCHAR(80),
    PRIMARY KEY (tuomariID));
CREATE TABLE yleisurheilukilpailu.tulokset (
    tulosID INT NOT NULL AUTO_INCREMENT,
    lajiID INT(11),
    kilpailijaID INT(11),
    sijoitus INT,
    PRIMARY KEY (tulosID));
ALTER TABLE kilpailijat ADD FOREIGN KEY (seura) REFERENCES seurat(seuraID);
ALTER TABLE ilmoittautumiset 
ADD FOREIGN KEY (lajiID) REFERENCES lajit(lajiID);
ALTER TABLE ilmoittautumiset 
ADD FOREIGN KEY (kilpailijaID) REFERENCES kilpailijat(kilpailijaID);
ALTER TABLE lajit
ADD FOREIGN KEY (paatuomari) REFERENCES tuomarit(tuomariID);
```

8. Varmista että juuri luomasi tietokanta on 3.normaalimuodossa. Perustele miksi näin on.  (3 pts)

1.normaalimuoto: Rivit uniikkeja id:n ansiosta. Sarakkeissa ei toistoa ja arvot ovat yksittäisiä.
2.normaalimuoto: Kaikki sarakkeet kuvautuvat pääavaimella.
3.normaalimuoto: Kaikki sarakkeet, jotka voisivat olla transitiivisesti riippuvaisia pääavaimesta, on siirretty omaksi taulukseen.
