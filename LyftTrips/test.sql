SELECT trips.id, trips.date, trips.type, riders.username 
FROM trips LEFT JOIN riders 
ON trips.rider_id = riders.id LIMIT 2;

SELECT trips.date, trips.type, cars.model, cars.trips_completed 
FROM trips JOIN cars 
ON trips.car_id = cars.id; 

SELECT * FROM riders UNION SELECT * FROM riders2;
SELECT ROUND(AVG(cost), 2) AS 'average'FROM trips GROUP BY rider_id; 
SELECT * FROM riders WHERE total_trips < 500;
SELECT COUNT(*) FROM cars WHERE status = 'active';
SELECT * FROM cars ORDER BY trips_completed DESC LIMIT 2;