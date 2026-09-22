select b.name,a.rentals_date
 from rentals a
 left join customers b on b.id = id_customers
 where a.rentals_date between '2016-09-01' and '2016-09-30'