select TYTUL, count(w.id_filmu) c from wypozyczenia w join filmy f on w.id_filmu = f.id_filmu
 group by w.id_filmu order by c desc;
 
 select count(*) from filmy where ODCINKI > 1;
 select count(*) from filmy where ODCINKI = 1;


select imie, NAZWISKO,count(*) from osoby o join wypozyczenia w on w.ID_OSOBY = o.ID_OSOBY where o.ID_OSOBY not in(
select ID_OSOBY from wypozyczenia w join filmy f on f.ID_FILMU = w.ID_FILMU where f.ODCINKI = 1)
group by o.ID_OSOBY;

select IMIE, NAZWISKO from osoby o join wypozyczenia w on w.ID_OSOBY = o.ID_OSOBY where o.ID_OSOBY not in(
select ID_OSOBY from wypozyczenia w join filmy f on w.ID_FILMU = f.ID_FILMU where w.ODCINKI <> f.ODCINKI)
and ODCINKI <> 1 group by o.ID_OSOBY having count(id_filmu) = 40;

select * from filmy where ID_FILMU not in (
select id_filmu from wypozyczenia group by id_filmu);


