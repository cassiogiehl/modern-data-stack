/*
    Análise de custo de lançamento de foguetes da space x
*/

select 
    l.id, 
    l.success,
    l.failures,
    l.date_local,
    l.rocket,
    r.cost_per_launch
from {{ ref('stg_launches') }} l
left join {{ ref('stg_rockets') }} r
on l.rocket = r.id

-- monthly_launch_cost as (
--     select 
--         l.date_local,
--         sum(r.cost_per_launch)
--     from launches_cost
--     group by l.date_local
-- )