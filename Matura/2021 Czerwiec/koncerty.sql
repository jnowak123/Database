select count(*) from koncert where month(data) = 7;

select miasto, count(id_zespolu) from koncert as k join miasta as m on k.kod_miasta = m.kod_miasta
group by k.kod_miasta order by count(id_zespolu) desc;

select count(miasto), count(id) from miasta as m join koncert as k on m.kod_miasta = k.kod_miasta group by wojewodztwo;

select nazwa from zespoly where id_zespolu not in(
select id_zespolu from koncert where date(data) >= date("2017-07-20") and date(data) <= date("2017-07-25"));

select count(weekday(data) = 1), count(weekday(data) in (1,2,3,4,5)) from koncert group by id_zespolu
