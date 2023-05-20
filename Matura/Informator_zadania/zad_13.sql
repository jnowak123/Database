SELECT nazwa_aktywnosci, COUNT(id_aktywnosci) c FROM rejestr_aktywnosci JOIN rodzaj_aktywnosci USING(id_aktywnosci) GROUP BY id_aktywnosci ORDER BY c DESC limit 5;

SELECT *, sum(hour(timediff(godzina_zak, godzina_rozp)) + minute(timediff(godzina_zak, godzina_rozp))/60) FROM rejestr_aktywnosci
JOIN rodzaj_aktywnosci USING(id_aktywnosci) join pracownicy USING(pesel)
WHERE miejscowosc = "Gliwice" and nazwa_aktywnosci = "scianka wspinaczkowa" GROUP BY id_aktywnosci;

SELECT Imie, nazwisko FROM rejestr_aktywnosci JOIN pracownicy USING(PESEL)
GROUP BY data, PESEL HAVING COUNT(PESEL) > 1 ORDER BY nazwisko;


SELECT MOD(RIGHT(PESEL, 1), 2) plec, avg(wiek) FROM pracownicy JOIN(
SELECT PESEL, MOD(2018 - 1900 - LEFT(PESEL, 2), 100) wiek FROM pracownicy 
JOIN rejestr_aktywnosci USING(PESEL) JOIN rodzaj_aktywnosci USING(ID_aktywnosci) WHERE nazwa_aktywnosci = "rolki" GROUP by PESEL) x USING(PESEL)
GROUP BY plec


SELECT PESEL FROM pracownicy JOIN rejestr_aktywnosci USING(PESEL) JOIN rodzaj_aktywnosci USING(Id_aktywnosci) 
WHERE Nazwa_aktywnosci = "masaz" AND PESEL NOT IN(
SELECT PESEL FROM rejestr_aktywnosci JOIN rodzaj_aktywnosci USING(Id_aktywnosci) 
WHERE Nazwa_aktywnosci = "joga" or Nazwa_aktywnosci = "silownia" GROUP BY PESEL) GROUP BY PESEL ORDER BY PESEL


