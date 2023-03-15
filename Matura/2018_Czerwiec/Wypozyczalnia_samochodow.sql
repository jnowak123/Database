select Imie, Nazwisko, Nr_rej, datediff(zwrot, wypozyczenie) czas_wypozyczenia,
left(Nr_firmowy, 1) mojaklasa, (select cena*czas_wypozyczenia from ceny_za_dobe where klasa = mojaklasa)
from wypozyczenia join klienci using(nr_klienta) join samochody using(nr_ew)
order by Nazwisko, Imie, Nr_rej;

select count(*), left(Nr_firmowy, 1) klasa from wypozyczenia join samochody using(nr_ew) group by klasa;

select Imie, Nazwisko, count(*) ilosc from wypozyczenia join klienci using(nr_klienta) 
group by Nr_klienta order by ilosc desc limit 1;

select Miejscowosc, left(Nr_firmowy, 1) klasa, count(*) ilosc from samochody 
where Nr_ew not in (select Nr_ew from wypozyczenia group by Nr_ew)
group by Miejscowosc, Klasa;

select count(*) from klienci where Nr_klienta not in (select Nr_klienta from wypozyczenia);

select Imie, Nazwisko, Nr_ew, datediff(zwrot, wypozyczenie) czas_wypozyczenia,
left(Nr_firmowy, 1) mojaklasa, (select cena*czas_wypozyczenia from ceny_za_dobe where klasa = mojaklasa)
from wypozyczenia join klienci using(nr_klienta) join samochody using(nr_ew)
order by Nazwisko, Imie, Nr_ew desc