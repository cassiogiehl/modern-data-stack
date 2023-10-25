select r.id, rr.cost_per_launch from data_warehouse.public.rockets_rockets rr
right join data_warehouse.public.rockets r
    on rr._airbyte_rockets_hashid = r._airbyte_rockets_hashid