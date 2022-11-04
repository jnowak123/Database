select count(*) from uczen join ewidencja on uczen.IdUcznia = ewidencja.IdUcznia 
join klasa on uczen.IdKlasy = klasa.IdKlasy where imie like '%a' and ProfilKlasy = 'biologiczno-chemiczny'; 

select count(*), day(ewidencja.wejscie) as dzien from uczen join ewidencja on uczen.IdUcznia = ewidencja.IdUcznia 
where time(ewidencja.wejscie) <= time("8:00:00") group by dzien order by dzien1;

select ewidencja.IdUcznia, Imie, Nazwisko from uczen join ewidencja on uczen.IdUcznia = ewidencja.IdUcznia group by ewidencja.IdUcznia order by sum(to_seconds(Wyjscie) - to_seconds(Wejscie)) desc limit 3;

select Imie, Nazwisko from uczen join ewidencja on uczen.IdUcznia = ewidencja.IdUcznia where uczen.IdUcznia not in(
select ewidencja.IdUcznia from uczen join ewidencja on uczen.IdUcznia = ewidencja.IdUcznia where date(Wejscie) = "2022.04.06") group by uczen.IdUcznia

