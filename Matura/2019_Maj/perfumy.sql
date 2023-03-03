select nazwa_p from perfumy join sklad using(id_perfum) where nazwa_skladnika = "absolut jasminu";

select r, p.nazwa_p, c from perfumy p join 
(select rodzina_zapachow r, min(cena) c from perfumy group by rodzina_zapachow) ps
on r = p.rodzina_zapachow and c = p.cena;

select nazwa_m from marki where id_marki not in(
select id_marki from sklad join perfumy using(id_perfum) join marki using(id_marki) 
where nazwa_skladnika like "%paczula%" group by id_marki) order by nazwa_m;

select nazwa_p, cena*0.85 from perfumy join marki using(id_marki)
where nazwa_m = "Mou De Rosine" and rodzina_zapachow = "orientalno-drzewna"
order by cena asc;

select nazwa_m, rodzina_zapachow from perfumy join marki using(id_marki)
group by id_marki having count(rodzina_zapachow) = 1;

select nazwa_p from perfumy where cena = 113;


