SELECT * FROM destinations;
SELECT * FROM destination_features;

SELECT * 
FROM training_data;
SELECT *
FROM training_data
LIMIT 10;
SELECT recommended, COUNT(*)
FROM training_data
GROUP BY recommended;
select count(*) FROM training_data;
SELECT COUNT(*) FROM training_data;
ALTER TABLE user_preferences
ADD COLUMN destination_type VARCHAR(100);


SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'user_preferences';


ALTER TABLE user_preferences
DROP COLUMN preferred_type,
DROP COLUMN wildlife,
DROP COLUMN adventure,
DROP COLUMN beach,
DROP COLUMN family;

SELECT * FROM users;
select * from destinations;
select * from training_data;



SELECT
    d.destination_id,
    d.name,
    d.country,
    d.estimated_cost,
    d.climate,
    f.destination_type,
    f.wildlife_score,
    f.adventure_score,
    f.beach_score,
    f.family_score,
    f.history_score,
    f.culture_score
FROM destinations d
JOIN destination_features f
    ON d.destination_id = f.destination_id
ORDER BY d.destination_id;

SELECT COUNT(*) AS destination_count
FROM destinations;


SELECT destination_id, name, country
FROM destinations
ORDER BY destination_id;




INSERT INTO destinations
(name, country, description, estimated_cost, climate, best_season)
VALUES

 
('Kakum National Park', 'Ghana',
 'A rainforest park famous for its canopy walkway and biodiversity.',
 500, 'Tropical', 'November-April'),

('Mole National Park', 'Ghana',
 'Ghana''s largest wildlife park, known for elephants and other savanna wildlife.',
 650, 'Tropical', 'November-March'),

('Elmina Castle', 'Ghana',
 'Historic coastal castle and UNESCO World Heritage site.',
 400, 'Coastal', 'November-March'),

('Lake Volta', 'Ghana',
 'Large inland lake offering boating, fishing and scenic experiences.',
 450, 'Tropical', 'November-March'),


('Amboseli National Park', 'Kenya',
 'Wildlife destination famous for elephants and views of Mount Kilimanjaro.',
 900, 'Tropical', 'June-October'),

('Lake Nakuru National Park', 'Kenya',
 'Rift Valley park known for wildlife and birdlife.',
 800, 'Temperate', 'June-October'),

('Diani Beach', 'Kenya',
 'Popular Indian Ocean beach destination with white sand and marine activities.',
 850, 'Coastal', 'June-October'),

('Mount Kenya', 'Kenya',
 'Mountain destination offering hiking, climbing and scenic landscapes.',
 950, 'Temperate', 'January-February'),


('Serengeti National Park', 'Tanzania',
 'World-famous wildlife destination known for the Great Migration.',
 1200, 'Tropical', 'June-October'),

('Ngorongoro Crater', 'Tanzania',
 'Large volcanic crater containing a remarkable concentration of wildlife.',
 1100, 'Temperate', 'June-October'),

('Mount Kilimanjaro', 'Tanzania',
 'Africa''s highest mountain and a major trekking destination.',
 1500, 'Temperate', 'January-February'),

('Arusha National Park', 'Tanzania',
 'Scenic park featuring Mount Meru, forests, lakes and wildlife.',
 750, 'Temperate', 'June-October'),


('Kruger National Park', 'South Africa',
 'One of Africa''s largest game reserves and a major safari destination.',
 1000, 'Temperate', 'May-September'),

('Table Mountain', 'South Africa',
 'Iconic Cape Town mountain offering hiking and panoramic views.',
 600, 'Temperate', 'November-March'),

('Boulders Beach', 'South Africa',
 'Coastal attraction famous for its African penguin colony.',
 500, 'Coastal', 'November-March'),

('Garden Route', 'South Africa',
 'Scenic coastal route featuring forests, beaches and outdoor activities.',
 900, 'Coastal', 'November-March'),

('Bwindi Impenetrable National Park', 'Uganda',
 'Rainforest destination famous for mountain gorilla trekking.',
 1300, 'Tropical', 'June-September'),

('Queen Elizabeth National Park', 'Uganda',
 'Wildlife park known for tree-climbing lions, elephants and boat safaris.',
 850, 'Tropical', 'June-September'),

('Murchison Falls National Park', 'Uganda',
 'Large national park featuring the powerful Murchison Falls.',
 800, 'Tropical', 'June-September'),


('Volcanoes National Park', 'Rwanda',
 'Mountainous park famous for gorilla trekking and volcanic scenery.',
 1400, 'Temperate', 'June-September'),

('Lake Kivu', 'Rwanda',
 'Scenic freshwater lake offering relaxation, boating and cultural experiences.',
 600, 'Temperate', 'June-September'),

('Kigali', 'Rwanda',
 'Modern and culturally rich capital city known for cleanliness and history.',
 550, 'Temperate', 'June-September'),


('Sossusvlei', 'Namibia',
 'Iconic desert landscape featuring towering red sand dunes.',
 900, 'Desert', 'May-October'),

('Etosha National Park', 'Namibia',
 'Major wildlife park centered around a large salt pan.',
 850, 'Desert', 'May-October'),

('Swakopmund', 'Namibia',
 'Coastal adventure destination combining desert landscapes with ocean activities.',
 750, 'Coastal', 'May-October'),


('Okavango Delta', 'Botswana',
 'Unique inland delta famous for wildlife, waterways and safari experiences.',
 1400, 'Tropical', 'June-October'),

('Chobe National Park', 'Botswana',
 'Wildlife destination particularly famous for large elephant populations.',
 1000, 'Tropical', 'June-October'),


('South Luangwa National Park', 'Zambia',
 'Renowned wildlife destination known for walking safaris and diverse wildlife.',
 950, 'Tropical', 'June-October'),

('Lower Zambezi National Park', 'Zambia',
 'Wildlife and adventure destination along the Zambezi River.',
 1000, 'Tropical', 'June-October'),

('Hwange National Park', 'Zimbabwe',
 'Zimbabwe''s largest national park and a major elephant habitat.',
 800, 'Tropical', 'June-October'),

('Great Zimbabwe', 'Zimbabwe',
 'Ancient stone city and important archaeological and cultural site.',
 500, 'Tropical', 'May-October'),


('Marrakech Medina', 'Morocco',
 'Historic city center featuring markets, architecture and cultural attractions.',
 650, 'Desert', 'March-May'),

('Chefchaouen', 'Morocco',
 'Mountain town famous for its distinctive blue-painted buildings.',
 550, 'Temperate', 'March-May'),

('Gorée Island', 'Senegal',
 'Historic island known for its architecture and role in West African history.',
 500, 'Coastal', 'November-March');


SELECT destination_id, name, country
FROM destinations
ORDER BY destination_id;


SELECT destination_id, name
FROM destinations
ORDER BY destination_id;
DELETE FROM destination_features;
DELETE FROM destinations;


SELECT COUNT(*) FROM user_preferences;
