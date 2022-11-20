select imie, nazwisko, czas from czasy c join startujacy s on s.id_startu = c.id_startu join zawodnicy z on z.id_zawodnika = s.id_zawodnika 
order by czas limit 1;

select imie, nazwisko, count(id_startu) x from startujacy s join zawodnicy z on z.id_zawodnika = s.id_zawodnika
where obywatel_kraju = 'Polska' group by s.id_zawodnika order by x desc limit 1;

select *, (rok - year(data)) wiek from startujacy s join zawodnicy z on z.id_zawodnika = s.id_zawodnika order by wiek;