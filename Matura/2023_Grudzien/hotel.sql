select imie, nazwisko, sum(datediff(data_wyjazdu, data_przyjazdu)) len 
from noclegi join klienci using(nr_dowodu) group by nr_dowodu order by len desc limit 1;

select imie, nazwisko, sum(datediff(data_wyjazdu, data_przyjazdu)*cena) a 
from noclegi join klienci using(nr_dowodu) join pokoje using(nr_pokoju) group by nr_dowodu having a>2000;

select nr_pokoju from pokoje where standard = 'N' and nr_pokoju not in (
select nr_pokoju from noclegi join klienci using(nr_dowodu)
where data_przyjazdu > date("1.07.2022") and data_wyjazdu < date("30.09.2022") and (miejscowosc = "Opole" or miejscowosc = "Katowice")
group by nr_pokoju)


