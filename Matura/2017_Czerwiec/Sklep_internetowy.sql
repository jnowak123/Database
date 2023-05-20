SELECT program from programy WHERE rodzaj = "edytor dokumentow tekstowych" and id_programu in (
SELECT id_programu from zestawy GROUP by id_programu HAVING count(*) >= 2);

SELECT nazwa_pakietu from zestawy JOIN pakiety USING(id_pakietu) where Id_programu in(
SELECT id_programu FROM programy WHERE rodzaj like "%zarzadzanie%") GROUP by id_pakietu;

SELECT nazwa_pakietu, firma, sum(cena) c from zestawy JOIN programy USING(Id_programu) JOIN pakiety using(id_pakietu)
GROUP by Id_pakietu order by c desc limit 3;

SELECT program FROM programy WHERE Id_programu not in (
SELECT Id_programu FROM zestawy GROUP by Id_programu);

SELECT nazwa_pakietu, c1 ilosc_darmowych, c2 ilosc_platnych FROM pakiety JOIN
(SELECT Id_pakietu, COUNT(*) c1 from zestawy JOIN programy USING(id_programu) WHERE cena = 0 GROUP BY Id_pakietu) s1
USING(Id_pakietu) JOIN
(SELECT Id_pakietu, COUNT(*) c2 from zestawy JOIN programy USING(id_programu) WHERE cena > 0 GROUP BY Id_pakietu) s2
USING(Id_pakietu);