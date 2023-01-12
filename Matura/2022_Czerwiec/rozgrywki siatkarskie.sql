select count(*) from mecze where Sety_wygrane + Sety_przegrane = 5;

select Miasto, count(Id_meczu) from mecze join kluby on mecze.Id_klubu = kluby.Id_klubu group by Miasto order by count(Id_meczu) desc;

select imie, nazwisko, count(mecze.Id_meczu) from mecze join sedziowie on mecze.Id_sedziego = sedziowie.Id_sedziego group by sedziowie.Id_sedziego having count(mecze.Id_meczu) >
(select count(Id_meczu) from mecze) /(select count(Id_sedziego) from sedziowie);

select Imie, Nazwisko from sedziowie where id_sedziego not in(
select sedziowie.Id_sedziego from mecze join sedziowie on mecze.Id_sedziego = sedziowie.Id_sedziego join kluby on mecze.Id_klubu = kluby.Id_klubu
where (date(data) >= "2019-10-15" and date(data) <= "2019-12-15") and (Miasto = "Szymbark" or  Miasto = "Licowo ")
group by sedziowie.Id_sedziego);

with 
wyg as (select count(Id_meczu), Id_klubu from mecze where Sety_wygrane > Sety_przegrane group by Id_klubu),
przeg as (select count(Id_meczu), Id_klubu from mecze where Sety_wygrane > Sety_przegrane group by Id_klubu)
select * from wyg join przeg on wyg.id_klubu = przeg.id_klubu;
