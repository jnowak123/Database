select Rodzaj_meczu, count(*) from wyniki where Id_druzyny in (select Id_druzyny from druzyny where Miasto = "Kucykowo") group by Rodzaj_meczu;

select year(data_meczu) rok, count(*) ilosc from wyniki 
where Id_druzyny in (select Id_druzyny from druzyny where Miasto = "Kucykowo") group by rok
order by ilosc desc limit 1;

select Nazwa, sum(Bramki_zdobyte) - sum(Bramki_stracone) bilans from wyniki join druzyny using(id_druzyny)
group by Id_druzyny having bilans = 0;

select count(*) from wyniki where Gdzie = "W" and Bramki_zdobyte > Bramki_stracone;
select count(*) from wyniki where Gdzie = "W" and Bramki_zdobyte = Bramki_stracone;
select count(*) from wyniki where Gdzie = "W" and Bramki_zdobyte < Bramki_stracone;


select count(*) from sedziowie where Nr_licencji not in (select Nr_licencji from wyniki group by Nr_licencji);
