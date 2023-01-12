#1
select count(*) from koncert where month(data) = 7;

#2 nie mam pojęcia czemu to nie działa, licząc ręcznie wychodzi inaczej niż w odpowiedziach
select count(distinct id_zespolu), miasto from koncert as k join miasta as m on k.kod_miasta = m.kod_miasta 
group by miasto order by count(distinct id_zespolu) desc;

#3
select wojewodztwo, round(count(*)/ count(distinct miasto), 2) as odp from koncert as k join miasta as m on k.kod_miasta = m.kod_miasta 
group by wojewodztwo order by odp desc;

#4
select nazwa from zespoly where id_zespolu not in(
select id_zespolu from koncert where date(data) >= date("2017-07-20") and date(data) <= date("2017-07-25"));

#5
select count(*) c1, c2, nazwa from koncert k1
join (select count(*) c2, id_zespolu from koncert where weekday(data) in (0,1,2,3,4) group by id_zespolu) k2 on k1.id_zespolu = k2.id_zespolu
join zespoly z on k1.id_zespolu = z.id_zespolu
where weekday(data) in (5,6) group by k1.id_zespolu having c1>c2 