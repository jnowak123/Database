select year(Data_przybycia) ,count(LP) from przybycia group by year(Data_przybycia);

select Nabrzeze from przybycia group by nabrzeze having Nabrzeze not in(
select Nabrzeze from przybycia where Nr_IMO in(
select Nr_IMO from przybycia join kody on przybycia.Bandera = kody.Bandera where Kontynent = "Europa" group by Nr_IMO)
group by Nabrzeze);

select MAX(ladownosc), Nabrzeze from przybycia join statki on przybycia.Nr_IMO = statki.Nr_IMO group by Nabrzeze

