select *, count(*) c from klienci k join noclegi n on n.nr_dowodu = k.nr_dowodu group by k.nr_dowodu order by c desc limit 1;

select* from noclegi n 
join pokoje p on p.nr_pokoju = n.nr_pokoju group by nr_dowodu having sum( datediff(data_wyjazdu, data_przyjazdu)*cena) > 2000 
