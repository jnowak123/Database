select * from dane_ankiet having imie like "%a";
select * from dane_ankiet having imie not like "%a";

select Srod_lok, count(d.id) from dane_ankiet d join lok l on l.Id = d.id 
where Wojewodztwo = "Mazowieckie" and Pora_roku = "lato" group by Srod_lok;

select Wojewodztwo, count(id) c from dane_ankiet group by Wojewodztwo having c >= 20;

select Imie, Nazwisko, Wojewodztwo from dane_ankiet 
where Wyksztalcenie in ("wyzsze", "srednie") and Wiek > 50 and id not in
(select id from zain where Zainteresowania in ("informatyka", "gry komputerowe"))
group by id order by Nazwisko asc;

select avg(Dochod) from dane_ankiet where imie like "%a" and Wojewodztwo = "Zachodniopomorskie" and id in 
(select id from lok where Srod_lok = "rower" group by id)