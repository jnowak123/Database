select * from uczen join ewidencja on uczen.IdUcznia = ewidencja.IdUcznia where time(ewidencja.wejscie) <= time("8:00:00") and day(ewidencja.wejscie) = "4";
select * from uczen join ewidencja on uczen.IdUcznia = ewidencja.IdUcznia where time(ewidencja.wejscie) <= time("8:00:00") and day(ewidencja.wejscie) = "5";
select * from uczen join ewidencja on uczen.IdUcznia = ewidencja.IdUcznia where time(ewidencja.wejscie) <= time("8:00:00") and day(ewidencja.wejscie) = "6";
select * from uczen join ewidencja on uczen.IdUcznia = ewidencja.IdUcznia where time(ewidencja.wejscie) <= time("8:00:00") and day(ewidencja.wejscie) = "7";
select * from uczen join ewidencja on uczen.IdUcznia = ewidencja.IdUcznia where time(ewidencja.wejscie) <= time("8:00:00") and day(ewidencja.wejscie) = "8";

select ewidencja.IdUcznia, Imie, Nazwisko from uczen join ewidencja on uczen.IdUcznia = ewidencja.IdUcznia group by ewidencja.IdUcznia order by sum(to_seconds(Wyjscie) - to_seconds(Wejscie)) desc limit 3;

select Imie, Nazwisko from uczen join ewidencja on uczen.IdUcznia = ewidencja.IdUcznia where uczen.IdUcznia not in(
select ewidencja.IdUcznia from uczen join ewidencja on uczen.IdUcznia = ewidencja.IdUcznia where date(Wejscie) = "2022.04.06") group by uczen.IdUcznia

