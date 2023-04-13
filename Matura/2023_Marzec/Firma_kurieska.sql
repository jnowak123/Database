SELECT nazwa, COUNT(*) c from serwis join naprawy USING(id_naprawy) GROUP BY id_naprawy ORDER BY c DESC LIMIT 1;

SELECT marka, model, COUNT(*) c from serwis JOIN auta USING(nr_rejestracyjny) GROUP BY model ORDER by c DESC limit 1;

SELECT nr_rejestracyjny FROM auta WHERE nr_rejestracyjny not in 
(SELECT nr_rejestracyjny FROM serwis GROUP BY nr_rejestracyjny);

SELECT nr_rejestracyjny, sec_to_time(sum((hour(czasnaprawy)*60 + minute(czasnaprawy)))*60) czas FROM serwis GROUP by nr_rejestracyjny order by czas desc limit 1;

SELECT nr_rejestracyjny, sum(round(cena_roboczo_h*hour(czasnaprawy) + minute(czasnaprawy)/60*cena_roboczo_h, 2) + cena_materialow) cena FROM serwis 
JOIN naprawy USING(id_naprawy) GROUP BY nr_rejestracyjny ORDER BY cena desc LIMIT 1;


SELECT sum(round(cena_roboczo_h*hour(czasnaprawy) + minute(czasnaprawy)/60*cena_roboczo_h, 2) + cena_materialow) cena FROM serwis 
JOIN naprawy USING(id_naprawy)