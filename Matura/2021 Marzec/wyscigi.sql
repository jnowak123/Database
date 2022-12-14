select imie, nazwisko, czas 
from czasy c join startujacy s on c.id_startu = s.id_startu join zawodnicy z on z.id_zawodnika = s.id_zawodnika order by czas limit 1;

select imie, nazwisko, count(*) c from startujacy s join zawodnicy z on s.id_zawodnika = z.id_zawodnika
where obywatel_kraju = 'POLSKA' group by s.id_zawodnika order by c desc limit 1;

select imie, nazwisko, rok - year(data) wiek from startujacy s join zawodnicy z on z.id_zawodnika = s.id_zawodnika 
where rok = '2008' order by wiek;
select imie, nazwisko, rok - year(data) wiek from startujacy s join zawodnicy z on z.id_zawodnika = s.id_zawodnika 
where rok = '2009' order by wiek;
select imie, nazwisko, rok - year(data) wiek from startujacy s join zawodnicy z on z.id_zawodnika = s.id_zawodnika 
where rok = '2010' order by wiek;
select imie, nazwisko, rok - year(data) wiek from startujacy s join zawodnicy z on z.id_zawodnika = s.id_zawodnika 
where rok = '2011' order by wiek;
select imie, nazwisko, rok - year(data) wiek from startujacy s join zawodnicy z on z.id_zawodnika = s.id_zawodnika 
where rok = '2012' order by wiek;
select imie, nazwisko, rok - year(data) wiek from startujacy s join zawodnicy z on z.id_zawodnika = s.id_zawodnika 
where rok = '2013' order by wiek;
select imie, nazwisko, rok - year(data) wiek from startujacy s join zawodnicy z on z.id_zawodnika = s.id_zawodnika 
where rok = '2014' order by wiek;
select imie, nazwisko, rok - year(data) wiek from startujacy s join zawodnicy z on z.id_zawodnika = s.id_zawodnika 
where rok = '2015' order by wiek;
select imie, nazwisko, rok - year(data) wiek from startujacy s join zawodnicy z on z.id_zawodnika = s.id_zawodnika 
where rok = '2016' order by wiek;
select imie, nazwisko, rok - year(data) wiek from startujacy s join zawodnicy z on z.id_zawodnika = s.id_zawodnika 
where rok = '2017' order by wiek;

select rok, count(id_startu) c from startujacy 
where id_startu not in (select id_startu from czasy) group by rok order by c desc limit 1;

select *, count(distinct obywatel_kraju) c from startujacy group by id_zawodnika order by c desc;
select id_zawodnika, obywatel_kraju from startujacy where id_zawodnika in (199, 252) group by obywatel_kraju order by id_zawodnika;

select s.rok, imie, nazwisko from startujacy s join zawodnicy z using(id_zawodnika) join
(select rok, max(year(data)) mrok from startujacy s join zawodnicy z on z.id_zawodnika = s.id_zawodnika group by rok) a
on a.rok = s.rok and mrok = year(data)


