select
a.name,
CAST( EXTRACT (DAY FROM payday) AS INT  ) AS day
from loan a