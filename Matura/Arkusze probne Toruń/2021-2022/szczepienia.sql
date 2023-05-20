/*
SELECT count(*) FROM szczepienia WHERE indeks NOT IN (
SELECT indeks FROM szczepienia JOIN szczepionki ON id_szczepionki = szczepionka WHERE dat_II OR nazwa = "Johnson & Johnson")

SELECT *, floor(datediff(data_urodzenia, "2021-12-1")/-365) as wiek FROM mieszkancy WHERE floor(datediff(data_urodzenia, "2021-12-1")/-365) > 50 AND
identyfikator NOT IN (SELECT indeks FROM szczepienia) ORDER BY identyfikator ASC

SELECT count(*) FROM szczepienia JOIN szczepionki ON id_szczepionki = szczepionka JOIN mieszkancy ON indeks = identyfikator
WHERE (dat_II OR nazwa = "Johnson & Johnson") AND RIGHT(imie, 1) = "a"
*/
SELECT *, RIGHT( FROM szczepienia JOIN szczepionki on szczepionka = id_szczepionki