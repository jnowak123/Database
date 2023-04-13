SELECT Klasa, count(*) c FROM uczniowie WHERE Legitymacja IN (SELECT Legitymacja FROM sukcesy_uczniow WHERE sukces = "laureat" GROUP BY Legitymacja) GROUP BY Klasa HAVING c < 2;

SELECT Nazwa, COUNT(*) c FROM sukcesy_uczniow JOIN olimpiady USING(Id_olimpiady)
WHERE sukces = "finalista" or sukces = "laureat" GROUP BY id_olimpiady HAVING c > 5;

SELECT Imię, Nazwisko, SUM(punkty) FROM sukcesy_uczniow JOIN punkty USING(sukces) JOIN nauczyciele on opiekun = id_nauczyciela GROUP BY opiekun;

SELECT Klasa, SUM(punkty) FROM sukcesy_uczniow JOIN punkty USING(sukces) JOIN uczniowie USING(Legitymacja) GROUP BY Klasa;

SELECT Klasa, count(*)/ (SELECT COUNT(*) FROM uczniowie  WHERE Klasa = u.Klasa GROUP BY Klasa) FROM uczniowie u
WHERE Legitymacja IN(SELECT Legitymacja FROM sukcesy_uczniow GROUP BY Legitymacja) 
GROUP BY Klasa;

SELECT Klasa, 1 - (count(*)/ (SELECT COUNT(*) FROM uczniowie  WHERE Klasa = u.Klasa GROUP BY Klasa)) FROM uczniowie u
WHERE Legitymacja IN(SELECT Legitymacja FROM sukcesy_uczniow GROUP BY Legitymacja) 
GROUP BY Klasa;

