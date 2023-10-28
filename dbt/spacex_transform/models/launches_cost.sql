/*
    Análise de custo de lançamento de foguetes da space x
*/
{{
    config(
        materialized='table'
    )
}}

select 
    l.id, 
    l.success,
    l.failures,
    sum(r.cost_per_launch) as cost_per_launch
from {{ ref('stg_launches') }} l
left join {{ ref('stg_rockets') }} r
on l.rocket = r.id
group by 
    l.id, 
    l.success,
    l.failures