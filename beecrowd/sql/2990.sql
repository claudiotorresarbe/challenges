select 
a.cpf,
a.enome,
b.dnome
from empregados a
left join departamentos b on b.dnumero = a.dnumero
where a.cpf_supervisor is null
order by a.cpf asc