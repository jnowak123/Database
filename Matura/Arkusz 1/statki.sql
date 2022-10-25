select year(Data_przybycia) ,count(LP) from przybycia group by year(Data_przybycia);

with 
mladownosc as (select MAX(ladownosc) as lad, Nabrzeze as nab from przybycia join statki on przybycia.Nr_IMO = statki.Nr_IMO group by Nabrzeze),
nazwastatku as (select Ladownosc as lad, Nabrzeze as nab, Nazwa_statku from przybycia join statki on przybycia.Nr_IMO = statki.Nr_IMO group by przybycia.Nr_IMO)
select n.nab, nazwa_statku, n.lad from nazwastatku as n join mladownosc as m on m.lad = n.lad and m.nab = n.nab;

select Nabrzeze from przybycia group by nabrzeze having Nabrzeze not in(
select Nabrzeze from przybycia where Nr_IMO in(
select Nr_IMO from przybycia join kody on przybycia.Bandera = kody.Bandera where Kontynent = "Europa" group by Nr_IMO)
group by Nabrzeze);



