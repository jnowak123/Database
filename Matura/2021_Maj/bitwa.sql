select kraj, count(id_gracza) from gracze where year(data_dolaczenia) = 2018 group by kraj order by count(id_gracza) desc limit 5;

select sum(strzal) from klasy where nazwa like "%elf%";

select id_gracza from gracze where id_gracza not in
(select id_gracza from jednostki where nazwa = "artylerzysta");

select j.nazwa, count(id_jednostki) from jednostki as j join klasy as k on j.nazwa = k.nazwa 
where abs(lok_x - 100) + abs(lok_y - 100) <= szybkosc group by j.nazwa;

select * from  jednostki as a join jednostki as b on a.lok_x = b.lok_x and a.lok_y = b.lok_y 
where a.id_gracza != b.id_gracza group by a.lok_x, a.lok_y limit 10000;

select * from  jednostki as a join jednostki as b on a.lok_x = b.lok_x and a.lok_y = b.lok_y 
where a.id_gracza != b.id_gracza and 
(a.id_gracza in(select id_gracza from gracze where kraj = "polska") or b.id_gracza in(select id_gracza from gracze where kraj = "polska"))
group by a.lok_x, a.lok_y limit 10000;
