select count(*) c, Rodzina from jezyki group by Rodzina order by c desc;

select * from uzytkownicy group by jezyk having jezyk not in(
select Jezyk from uzytkownicy where Urzedowy = 'tak');

select Jezyk from uzytkownicy u join panstwa p on p.Panstwo = u.Panstwo group by Jezyk having count(distinct Kontynent) >= 4;

select u.Jezyk, rodzina, round(sum(uzytkownicy),1) suma from uzytkownicy u join panstwa p on p.Panstwo = u.Panstwo 
join jezyki j on j.Jezyk = u.Jezyk  
where Rodzina <> 'indoeuropejska' and Kontynent in ('Ameryka Polnocna', 'Ameryka Poludniowa')
group by u.Jezyk order by suma desc limit 6;

select u.Panstwo, Jezyk, round((Uzytkownicy/Populacja)*100, 2) from uzytkownicy u join panstwa p on p.Panstwo = u.Panstwo 
where Urzedowy = 'nie' and Populacja*0.3 <= uzytkownicy
