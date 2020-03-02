## Tietokannat tehtävä 9

Ohjelmointi. Voit tehdä tehtävät valitsemallasi ohjelmointikielellä. Liitä vastaukseen lähdekoodi ja kuvakaappaus tuloksesta. 

1. Toteuta valitsemallasi kielellä CRUD-operaatiot testikantaan
Create:
```python
import mysql.connector
from mysql.connector import Error

def insertIntoAsiakas(nimi,puhelin):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='testikanta',
                                            user='root',
                                            password='root')

        if connection.is_connected():   
            sqlQuery = "insert into asiakas(nimi, puhelin) values ( %s, %s);"
            values = (nimi, puhelin)
            cursor = connection.cursor()
            cursor.execute(sqlQuery, values)
            connection.commit()
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

insertIntoAsiakas('Asiakas Seitsemän', '12223')
```
Read:
```python
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='testikanta',
                                         user='root',
                                         password='root')

    if connection.is_connected():
        sqlQuery = "select * from asiakas;"
        cursor = connection.cursor()
        cursor.execute(sqlQuery)
        records = cursor.fetchall()
        print("numeber of rows: ", cursor.rowcount)
        print("\nAll rows:")
        for row in records:
            print("ID:",row[0])
            print("Nimi:",row[1])
            print("Puhelin",row[2], "\n")
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
```
Update:
```python
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='testikanta',
                                         user='root',
                                         password='root')

    if connection.is_connected():
        updateQuery = "UPDATE asiakas SET puhelin = '999999' WHERE nimi='Antti Asiakas';"
        cursor = connection.cursor()
        cursor.execute(updateQuery)
        connection.commit()

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

```
Delete:
```python
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='testikanta',
                                         user='root',
                                         password='root')

    if connection.is_connected():
        deleteQuery = "DELETE FROM asiakas WHERE nimi='Ari Ahkera';"
        cursor = connection.cursor()
        cursor.execute(deleteQuery)
        connection.commit()
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

```

2. Toteuta haku testikantaan siten että haulle annetaan parametrina asiakkaan nimi ja näytetään vain kyseinen asiakas

```python
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='testikanta',
                                         user='root',
                                         password='root')

    if connection.is_connected():
        sqlQuery = "select * from asiakas where nimi = 'Kolmas Asiakas';"
        cursor = connection.cursor()
        cursor.execute(sqlQuery)
        records = cursor.fetchall()
        for row in records:
            print("ID:",row[0])
            print("Nimi:",row[1])
            print("Puhelin",row[2], "\n")
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

```
 
3. Toteuta seuraava toiminnallisuus: Jokaisen työntekijän palkkaa nostetaan 100 eurolla.
 
```python
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='testikanta',
                                         user='root',
                                         password='root')

    if connection.is_connected():
        updateQuery = "UPDATE tyontekija SET palkka = palkka + 100;"
        cursor = connection.cursor()
        cursor.execute(updateQuery)
        connection.commit()

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

```
 
4. Teoriaa: Selitä mitä tarkoittavat pythonin mySQL-ajurin commit() ja rollback() -funktiot. Laadi lisäksi esimerkki jossa hyödynnät rollback()-toiminnallisuutta. Koodia ei tarvitse kirjoittaa, esimerkki riittää.

commit()
- Commit-funktio lähettää komentojoukon mySQL serverille ja näin suorittaen sen (tehden muutoksesta pysyvän ja muille näkyvän). Python ei automaattisesti muuta dataa ilman tätä funktiota, joten commitia on tärkeä kutsua jokaisen dataa muuttavan käskyn jälkeen.

rollback()
- Tämän avulla voidaan peruuttaa tapahtuma, ellei sitä olla vielä commit()-funktiolla suoritettu.

esimerkki:
Komentoja voidaan ryhmitellä niin, että otetaan autocommit pois päältä komennolla set autocommit = 0.
Tämän jälkeen annetaan erilaisia käskyjä (esim. INSERT, DELETE jne) ja kun rivit halutaan suorittaa, kirjoitetaan käsky commit, tai jos muutoksia (tai jos vaikka yksi rivi meni eri lailla kuin haluttiin), kirjoitetaan käsky rollback.
