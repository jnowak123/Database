select Pojemnosc_dysku, count(*) ilosc from komputery group by Pojemnosc_dysku order by ilosc desc limit 10;

select Numer_komputera, count(*) ilosc_napraw from naprawy 
join awarie using(numer_zgloszenia) join komputery using(numer_komputera) 
where Sekcja = "A" group by Numer_komputera having ilosc_napraw >= 10;

select Sekcja s, count(*) c,
(select count(*) ilosc from awarie join komputery using(numer_komputera) where Sekcja = s 
group by date(Czas_awarii) order by ilosc desc limit 1) pods
from komputery group by Sekcja having c = pods;
select Czas_awarii, count(*) ilosc from awarie join komputery using(numer_komputera) where Sekcja = "Q"
group by date(Czas_awarii) order by ilosc desc limit 1;

select Numer_zgloszenia as n1, Czas_awarii c1, n.c2, timediff(n.c2, awarie.Czas_awarii) dlugosc from awarie
join (select Numer_zgloszenia n2, max(czas_naprawy) c2 from naprawy group by Numer_zgloszenia) n on awarie.Numer_zgloszenia = n.n2
order by dlugosc desc limit 1;

select count(*) from komputery where Numer_komputera not in (select Numer_komputera from awarie where Priorytet >= 8);


