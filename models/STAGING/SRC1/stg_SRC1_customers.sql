select
    id as customer_id,
    first_name,
    last_name
from {{ source('SRC1','customers_src') }}