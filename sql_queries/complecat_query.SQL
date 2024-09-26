CREATE INDEX idx_mission_mission_date ON mission(EXTRACT(YEAR FROM mission_date));

EXPLAIN ANALYZE
SELECT m.air_force, m.target_city, COUNT(m.mission_id) AS mission_count
FROM mission m
WHERE EXTRACT(YEAR FROM mission_date) = 1944
GROUP BY m.air_force, m.target_city
ORDER BY mission_count DESC;

select target_country, bomb_damage_assessment, count(target_country) from mission
where bomb_damage_assessment is not null
and airborne_aircraft > 5
group by target_country, bomb_damage_assessment
order by count(bomb_damage_assessment) desc limit 1;
