from backend.database import SessionLocal
from backend.model import Destination, DestinationFeature

db = SessionLocal()

try:

    destinations_data = [

        {
            "name": "Maasai Mara National Reserve",
            "country": "Kenya",
            "description": "A world-famous wildlife reserve known for lions, elephants, and the Great Migration.",
            "estimated_cost": 1500,
            "climate": "Tropical",
            "best_season": "July-October",
            "latitude": -1.406,
            "longitude": 35.008,
            "image_url": "maasai_mara.jpg",
            "destination_type": "Wildlife",
            "wildlife_score": 5,
            "adventure_score": 4,
            "beach_score": 0,
            "family_score": 4,
            "history_score": 2,
            "culture_score": 4
        },

        {
            "name": "Zanzibar Beaches",
            "country": "Tanzania",
            "description": "Beautiful beaches with rich Swahili culture and historical attractions.",
            "estimated_cost": 1200,
            "climate": "Tropical",
            "best_season": "June-October",
            "latitude": -6.165,
            "longitude": 39.202,
            "image_url": "zanzibar.jpg",
            "destination_type": "Beach",
            "wildlife_score": 2,
            "adventure_score": 3,
            "beach_score": 5,
            "family_score": 4,
            "history_score": 3,
            "culture_score": 5
        },

        {
            "name": "Cape Coast Castle",
            "country": "Ghana",
            "description": "A historical coastal fortress representing Ghana's colonial history.",
            "estimated_cost": 500,
            "climate": "Coastal",
            "best_season": "November-March",
            "latitude": 5.131,
            "longitude": -1.279,
            "image_url": "cape_coast.jpg",
            "destination_type": "Historical",
            "wildlife_score": 1,
            "adventure_score": 2,
            "beach_score": 2,
            "family_score": 3,
            "history_score": 5,
            "culture_score": 5
        },

        {
            "name": "Victoria Falls",
            "country": "Zambia",
            "description": "One of the largest waterfalls in the world with adventure activities.",
            "estimated_cost": 900,
            "climate": "Tropical",
            "best_season": "May-August",
            "latitude": -17.924,
            "longitude": 25.857,
            "image_url": "victoria_falls.jpg",
            "destination_type": "Adventure",
            "wildlife_score": 4,
            "adventure_score": 5,
            "beach_score": 0,
            "family_score": 4,
            "history_score": 2,
            "culture_score": 3
        },

        {
            "name": "Pyramids of Giza",
            "country": "Egypt",
            "description": "Ancient pyramids and archaeological landmarks.",
            "estimated_cost": 1000,
            "climate": "Desert",
            "best_season": "October-April",
            "latitude": 29.979,
            "longitude": 31.134,
            "image_url": "giza.jpg",
            "destination_type": "Historical",
            "wildlife_score": 1,
            "adventure_score": 3,
            "beach_score": 0,
            "family_score": 4,
            "history_score": 5,
            "culture_score": 5
        },


            {
            "name": "Serengeti National Park",
            "country": "Tanzania",
            "description": "A vast national park famous for wildlife, the Great Migration, and large populations of predators.",
            "estimated_cost": 1600,
            "climate": "Tropical",
            "best_season": "June-October",
            "latitude": -2.333,
            "longitude": 34.833,
            "image_url": "serengeti.jpg",
            "destination_type": "Wildlife",
            "wildlife_score": 5,
            "adventure_score": 5,
            "beach_score": 0,
            "family_score": 4,
            "history_score": 2,
            "culture_score": 4
            },


            {
            "name": "Ngorongoro Crater",
            "country": "Tanzania",
            "description": "A spectacular volcanic crater containing a dense concentration of wildlife.",
            "estimated_cost": 1500,
            "climate": "Temperate",
            "best_season": "June-October",
            "latitude": -3.067,
            "longitude": 35.533,
            "image_url": "ngorongoro.jpg",
            "destination_type": "Wildlife",
            "wildlife_score": 5,
            "adventure_score": 4,
            "beach_score": 0,
            "family_score": 4,
            "history_score": 2,
            "culture_score": 4
            },

            {
            "name": "Amboseli National Park",
            "country": "Kenya",
            "description": "A scenic wildlife park known for elephants and spectacular views of Mount Kilimanjaro.",
            "estimated_cost": 1300,
            "climate": "Tropical",
            "best_season": "June-October",
            "latitude": -2.652,
            "longitude": 37.260,
            "image_url": "amboseli.jpg",
            "destination_type": "Wildlife",
            "wildlife_score": 5,
            "adventure_score": 4,
            "beach_score": 0,
            "family_score": 4,
            "history_score": 2,
            "culture_score": 4
        },

        {
            "name": "Kruger National Park",
            "country": "South Africa",
            "description": "One of Africa's largest game reserves and home to diverse wildlife including the Big Five.",
            "estimated_cost": 1400,
            "climate": "Tropical",
            "best_season": "May-September",
            "latitude": -23.988,
            "longitude": 31.554,
            "image_url": "kruger.jpg",
            "destination_type": "Wildlife",
            "wildlife_score": 5,
            "adventure_score": 4,
            "beach_score": 0,
            "family_score": 5,
            "history_score": 2,
            "culture_score": 3
        },

        {
            "name": "Chobe National Park",
            "country": "Botswana",
            "description": "A wildlife destination famous for its large elephant population and river safaris.",
            "estimated_cost": 1500,
            "climate": "Tropical",
            "best_season": "May-October",
            "latitude": -18.650,
            "longitude": 24.750,
            "image_url": "chobe.jpg",
            "destination_type": "Wildlife",
            "wildlife_score": 5,
            "adventure_score": 4,
            "beach_score": 0,
            "family_score": 4,
            "history_score": 2,
            "culture_score": 3
        },

        {
            "name": "Okavango Delta",
            "country": "Botswana",
            "description": "A unique inland delta offering spectacular wildlife viewing and traditional mokoro excursions.",
            "estimated_cost": 1800,
            "climate": "Tropical",
            "best_season": "June-October",
            "latitude": -19.283,
            "longitude": 22.900,
            "image_url": "okavango.jpg",
            "destination_type": "Wildlife",
            "wildlife_score": 5,
            "adventure_score": 5,
            "beach_score": 0,
            "family_score": 3,
            "history_score": 1,
            "culture_score": 4
        },

        {
            "name": "Etosha National Park",
            "country": "Namibia",
            "description": "A large protected area surrounding a salt pan and known for abundant wildlife.",
            "estimated_cost": 1200,
            "climate": "Desert",
            "best_season": "May-October",
            "latitude": -19.033,
            "longitude": 16.000,
            "image_url": "etosha.jpg",
            "destination_type": "Wildlife",
            "wildlife_score": 5,
            "adventure_score": 4,
            "beach_score": 0,
            "family_score": 4,
            "history_score": 2,
            "culture_score": 3
        },

        {
            "name": "Bwindi Impenetrable Forest",
            "country": "Uganda",
            "description": "A UNESCO-listed forest famous for mountain gorilla trekking and rich biodiversity.",
            "estimated_cost": 1700,
            "climate": "Tropical",
            "best_season": "June-September",
            "latitude": -1.052,
            "longitude": 29.718,
            "image_url": "bwindi.jpg",
            "destination_type": "Wildlife",
            "wildlife_score": 5,
            "adventure_score": 5,
            "beach_score": 0,
            "family_score": 3,
            "history_score": 1,
            "culture_score": 4
        },

        {
            "name": "Volcanoes National Park",
            "country": "Rwanda",
            "description": "A mountainous park renowned for gorilla trekking and volcanic landscapes.",
            "estimated_cost": 1800,
            "climate": "Tropical",
            "best_season": "June-September",
            "latitude": -1.483,
            "longitude": 29.533,
            "image_url": "volcanoes.jpg",
            "destination_type": "Wildlife",
            "wildlife_score": 5,
            "adventure_score": 5,
            "beach_score": 0,
            "family_score": 3,
            "history_score": 1,
            "culture_score": 4
        },

        {
            "name": "Lake Nakuru National Park",
            "country": "Kenya",
            "description": "A scenic national park known for flamingos, rhinos, and diverse wildlife.",
            "estimated_cost": 1100,
            "climate": "Temperate",
            "best_season": "June-October",
            "latitude": -0.303,
            "longitude": 36.080,
            "image_url": "lake_nakuru.jpg",
            "destination_type": "Wildlife",
            "wildlife_score": 5,
            "adventure_score": 3,
            "beach_score": 0,
            "family_score": 4,
            "history_score": 2,
            "culture_score": 3
        },

        {
            "name": "Bazaruto Archipelago",
            "country": "Mozambique",
            "description": "A tropical island group known for beaches, coral reefs, marine life, and water activities.",
            "estimated_cost": 1700,
            "climate": "Coastal",
            "best_season": "May-October",
            "latitude": -21.650,
            "longitude": 35.450,
            "image_url": "bazaruto.jpg",
            "destination_type": "Beach",
            "wildlife_score": 3,
            "adventure_score": 4,
            "beach_score": 5,
            "family_score": 4,
            "history_score": 2,
            "culture_score": 4
        },

        {
            "name": "Seychelles",
            "country": "Seychelles",
            "description": "An island nation famous for pristine beaches, turquoise waters, and tropical scenery.",
            "estimated_cost": 2000,
            "climate": "Coastal",
            "best_season": "April-May",
            "latitude": -4.679,
            "longitude": 55.492,
            "image_url": "seychelles.jpg",
            "destination_type": "Beach",
            "wildlife_score": 3,
            "adventure_score": 4,
            "beach_score": 5,
            "family_score": 4,
            "history_score": 2,
            "culture_score": 4
        },

        {
            "name": "Mauritius",
            "country": "Mauritius",
            "description": "A popular island destination offering beaches, water sports, nature, and cultural experiences.",
            "estimated_cost": 1600,
            "climate": "Coastal",
            "best_season": "May-October",
            "latitude": -20.348,
            "longitude": 57.552,
            "image_url": "mauritius.jpg",
            "destination_type": "Beach",
            "wildlife_score": 2,
            "adventure_score": 4,
            "beach_score": 5,
            "family_score": 5,
            "history_score": 3,
            "culture_score": 5
        },

        {
            "name": "Diani Beach",
            "country": "Kenya",
            "description": "A popular Kenyan coastal destination known for white sand beaches and water activities.",
            "estimated_cost": 900,
            "climate": "Coastal",
            "best_season": "June-October",
            "latitude": -4.284,
            "longitude": 39.594,
            "image_url": "diani.jpg",
            "destination_type": "Beach",
            "wildlife_score": 2,
            "adventure_score": 4,
            "beach_score": 5,
            "family_score": 5,
            "history_score": 2,
            "culture_score": 4
        },

        {
            "name": "Lamu Island",
            "country": "Kenya",
            "description": "A historic island destination combining Swahili culture, traditional architecture, and beaches.",
            "estimated_cost": 1000,
            "climate": "Coastal",
            "best_season": "June-October",
            "latitude": -2.269,
            "longitude": 40.900,
            "image_url": "lamu.jpg",
            "destination_type": "Cultural",
            "wildlife_score": 2,
            "adventure_score": 3,
            "beach_score": 5,
            "family_score": 4,
            "history_score": 5,
            "culture_score": 5
        },

        {
            "name": "Robben Island",
            "country": "South Africa",
            "description": "A historic island near Cape Town known for its museum and political history.",
            "estimated_cost": 700,
            "climate": "Coastal",
            "best_season": "November-March",
            "latitude": -33.806,
            "longitude": 18.371,
            "image_url": "robben_island.jpg",
            "destination_type": "Historical",
            "wildlife_score": 1,
            "adventure_score": 2,
            "beach_score": 2,
            "family_score": 4,
            "history_score": 5,
            "culture_score": 5
        },

        {
            "name": "Table Mountain",
            "country": "South Africa",
            "description": "A famous mountain overlooking Cape Town with hiking, sightseeing, and panoramic views.",
            "estimated_cost": 800,
            "climate": "Coastal",
            "best_season": "November-March",
            "latitude": -33.962,
            "longitude": 18.409,
            "image_url": "table_mountain.jpg",
            "destination_type": "Adventure",
            "wildlife_score": 2,
            "adventure_score": 5,
            "beach_score": 3,
            "family_score": 4,
            "history_score": 3,
            "culture_score": 4
        },

        {
            "name": "Sossusvlei",
            "country": "Namibia",
            "description": "A spectacular desert landscape featuring towering red dunes and salt-and-clay pans.",
            "estimated_cost": 1200,
            "climate": "Desert",
            "best_season": "May-October",
            "latitude": -24.733,
            "longitude": 15.333,
            "image_url": "sossusvlei.jpg",
            "destination_type": "Adventure",
            "wildlife_score": 2,
            "adventure_score": 5,
            "beach_score": 0,
            "family_score": 3,
            "history_score": 2,
            "culture_score": 3
        },

        {
            "name": "Namib Desert",
            "country": "Namibia",
            "description": "An ancient desert known for dramatic landscapes, sand dunes, and unique desert wildlife.",
            "estimated_cost": 1100,
            "climate": "Desert",
            "best_season": "May-October",
            "latitude": -24.500,
            "longitude": 15.500,
            "image_url": "namib_desert.jpg",
            "destination_type": "Adventure",
            "wildlife_score": 2,
            "adventure_score": 5,
            "beach_score": 0,
            "family_score": 3,
            "history_score": 2,
            "culture_score": 3
        },

        {
            "name": "Mount Kilimanjaro",
            "country": "Tanzania",
            "description": "Africa's highest mountain and a major destination for trekking and adventure tourism.",
            "estimated_cost": 1800,
            "climate": "Temperate",
            "best_season": "June-October",
            "latitude": -3.067,
            "longitude": 37.355,
            "image_url": "kilimanjaro.jpg",
            "destination_type": "Adventure",
            "wildlife_score": 3,
            "adventure_score": 5,
            "beach_score": 0,
            "family_score": 2,
            "history_score": 2,
            "culture_score": 4
        },

        {
            "name": "Rwenzori Mountains",
            "country": "Uganda",
            "description": "A dramatic mountain range offering challenging trekking and spectacular alpine scenery.",
            "estimated_cost": 1400,
            "climate": "Temperate",
            "best_season": "June-September",
            "latitude": 0.367,
            "longitude": 29.983,
            "image_url": "rwenzori.jpg",
            "destination_type": "Adventure",
            "wildlife_score": 3,
            "adventure_score": 5,
            "beach_score": 0,
            "family_score": 2,
            "history_score": 2,
            "culture_score": 4
        },

        {
            "name": "Marrakech",
            "country": "Morocco",
            "description": "A historic Moroccan city known for markets, palaces, gardens, and vibrant cultural traditions.",
            "estimated_cost": 900,
            "climate": "Desert",
            "best_season": "March-May",
            "latitude": 31.629,
            "longitude": -7.981,
            "image_url": "marrakech.jpg",
            "destination_type": "Cultural",
            "wildlife_score": 1,
            "adventure_score": 3,
            "beach_score": 1,
            "family_score": 4,
            "history_score": 5,
            "culture_score": 5
        },

        {
            "name": "Fes Medina",
            "country": "Morocco",
            "description": "A historic urban center famous for traditional architecture, markets, crafts, and Islamic heritage.",
            "estimated_cost": 800,
            "climate": "Temperate",
            "best_season": "March-May",
            "latitude": 34.018,
            "longitude": -5.007,
            "image_url": "fes.jpg",
            "destination_type": "Cultural",
            "wildlife_score": 1,
            "adventure_score": 2,
            "beach_score": 0,
            "family_score": 4,
            "history_score": 5,
            "culture_score": 5
        },

        {
            "name": "Karnak Temple",
            "country": "Egypt",
            "description": "A vast ancient temple complex showcasing the architectural achievements of ancient Egypt.",
            "estimated_cost": 700,
            "climate": "Desert",
            "best_season": "October-April",
            "latitude": 25.718,
            "longitude": 32.657,
            "image_url": "karnak.jpg",
            "destination_type": "Historical",
            "wildlife_score": 0,
            "adventure_score": 2,
            "beach_score": 0,
            "family_score": 4,
            "history_score": 5,
            "culture_score": 5
        },

        {
            "name": "Luxor",
            "country": "Egypt",
            "description": "An ancient Egyptian city containing major archaeological sites and temples along the Nile.",
            "estimated_cost": 800,
            "climate": "Desert",
            "best_season": "October-April",
            "latitude": 25.687,
            "longitude": 32.639,
            "image_url": "luxor.jpg",
            "destination_type": "Historical",
            "wildlife_score": 0,
            "adventure_score": 2,
            "beach_score": 0,
            "family_score": 4,
            "history_score": 5,
            "culture_score": 5
        },

        {
            "name": "Abu Simbel",
            "country": "Egypt",
            "description": "A remarkable ancient temple complex famous for its monumental statues and archaeological significance.",
            "estimated_cost": 900,
            "climate": "Desert",
            "best_season": "October-April",
            "latitude": 22.337,
            "longitude": 31.625,
            "image_url": "abu_simbel.jpg",
            "destination_type": "Historical",
            "wildlife_score": 0,
            "adventure_score": 2,
            "beach_score": 0,
            "family_score": 4,
            "history_score": 5,
            "culture_score": 5
        },

        {
            "name": "Gorée Island",
            "country": "Senegal",
            "description": "A historic island off Dakar known for its colonial architecture and cultural heritage.",
            "estimated_cost": 700,
            "climate": "Coastal",
            "best_season": "November-March",
            "latitude": 14.667,
            "longitude": -17.399,
            "image_url": "goree_island.jpg",
            "destination_type": "Historical",
            "wildlife_score": 1,
            "adventure_score": 2,
            "beach_score": 3,
            "family_score": 4,
            "history_score": 5,
            "culture_score": 5
        },

        {
            "name": "Djenné",
            "country": "Mali",
            "description": "An ancient city famous for its distinctive mud-brick architecture and historic mosque.",
            "estimated_cost": 600,
            "climate": "Desert",
            "best_season": "November-February",
            "latitude": 13.907,
            "longitude": -4.553,
            "image_url": "djenne.jpg",
            "destination_type": "Historical",
            "wildlife_score": 1,
            "adventure_score": 2,
            "beach_score": 0,
            "family_score": 3,
            "history_score": 5,
            "culture_score": 5
        },

        {
            "name": "Accra",
            "country": "Ghana",
            "description": "Ghana's capital city offering beaches, cultural attractions, markets, museums, and nightlife.",
            "estimated_cost": 600,
            "climate": "Coastal",
            "best_season": "November-March",
            "latitude": 5.603,
            "longitude": -0.187,
            "image_url": "accra.jpg",
            "destination_type": "Cultural",
            "wildlife_score": 1,
            "adventure_score": 3,
            "beach_score": 4,
            "family_score": 5,
            "history_score": 4,
            "culture_score": 5
        },

        {
            "name": "Kumasi",
            "country": "Ghana",
            "description": "A cultural center associated with Ashanti heritage, traditional crafts, markets, and history.",
            "estimated_cost": 500,
            "climate": "Tropical",
            "best_season": "November-March",
            "latitude": 6.688,
            "longitude": -1.624,
            "image_url": "kumasi.jpg",
            "destination_type": "Cultural",
            "wildlife_score": 1,
            "adventure_score": 2,
            "beach_score": 0,
            "family_score": 5,
            "history_score": 5,
            "culture_score": 5
        },

        {
            "name": "Kakum National Park",
            "country": "Ghana",
            "description": "A tropical rainforest park famous for its canopy walkway and diverse forest ecosystem.",
            "estimated_cost": 500,
            "climate": "Tropical",
            "best_season": "November-March",
            "latitude": 5.350,
            "longitude": -1.382,
            "image_url": "kakum.jpg",
            "destination_type": "Adventure",
            "wildlife_score": 4,
            "adventure_score": 5,
            "beach_score": 0,
            "family_score": 4,
            "history_score": 2,
            "culture_score": 3
        },

        {
            "name": "Aksum",
            "country": "Ethiopia",
            "description": "An ancient Ethiopian city known for archaeological monuments, obelisks, and historical heritage.",
            "estimated_cost": 700,
            "climate": "Temperate",
            "best_season": "October-February",
            "latitude": 14.130,
            "longitude": 38.720,
            "image_url": "aksum.jpg",
            "destination_type": "Historical",
            "wildlife_score": 1,
            "adventure_score": 2,
            "beach_score": 0,
            "family_score": 4,
            "history_score": 5,
            "culture_score": 5
        },

        {
            "name": "Lalibela",
            "country": "Ethiopia",
            "description": "A historic Ethiopian destination famous for its remarkable rock-hewn churches.",
            "estimated_cost": 800,
            "climate": "Temperate",
            "best_season": "October-February",
            "latitude": 12.031,
            "longitude": 39.047,
            "image_url": "lalibela.jpg",
            "destination_type": "Historical",
            "wildlife_score": 1,
            "adventure_score": 3,
            "beach_score": 0,
            "family_score": 4,
            "history_score": 5,
            "culture_score": 5
        },

        {
            "name": "Lake Malawi",
            "country": "Malawi",
            "description": "A beautiful freshwater lake offering beaches, water activities, wildlife, and scenic landscapes.",
            "estimated_cost": 900,
            "climate": "Tropical",
            "best_season": "May-October",
            "latitude": -12.000,
            "longitude": 34.000,
            "image_url": "lake_malawi.jpg",
            "destination_type": "Beach",
            "wildlife_score": 3,
            "adventure_score": 4,
            "beach_score": 5,
            "family_score": 5,
            "history_score": 2,
            "culture_score": 4
        },

        {
            "name": "Stone Town",
            "country": "Tanzania",
            "description": "The historic heart of Zanzibar featuring Swahili architecture, markets, and cultural attractions.",
            "estimated_cost": 900,
            "climate": "Coastal",
            "best_season": "June-October",
            "latitude": -6.162,
            "longitude": 39.191,
            "image_url": "stone_town.jpg",
            "destination_type": "Cultural",
            "wildlife_score": 1,
            "adventure_score": 2,
            "beach_score": 4,
            "family_score": 4,
            "history_score": 5,
            "culture_score": 5
        },

        {
            "name": "Maputo",
            "country": "Mozambique",
            "description": "A coastal capital known for Portuguese-influenced architecture, beaches, food, and cultural attractions.",
            "estimated_cost": 800,
            "climate": "Coastal",
            "best_season": "May-October",
            "latitude": -25.969,
            "longitude": 32.573,
            "image_url": "maputo.jpg",
            "destination_type": "Cultural",
            "wildlife_score": 1,
            "adventure_score": 3,
            "beach_score": 4,
            "family_score": 4,
            "history_score": 4,
            "culture_score": 5
        },

        {
            "name": "Victoria Falls",
            "country": "Zimbabwe",
            "description": "One of the world's most spectacular waterfalls offering sightseeing and adventure activities.",
            "estimated_cost": 1000,
            "climate": "Tropical",
            "best_season": "May-August",
            "latitude": -17.924,
            "longitude": 25.857,
            "image_url": "victoria_falls_zimbabwe.jpg",
            "destination_type": "Adventure",
            "wildlife_score": 4,
            "adventure_score": 5,
            "beach_score": 0,
            "family_score": 4,
            "history_score": 2,
            "culture_score": 3
        },

        {
            "name": "Addis Ababa",
            "country": "Ethiopia",
            "description": "Ethiopia's capital city offering museums, cultural attractions, markets, and historic sites.",
            "estimated_cost": 700,
            "climate": "Temperate",
            "best_season": "October-February",
            "latitude": 9.032,
            "longitude": 38.746,
            "image_url": "addis_ababa.jpg",
            "destination_type": "Cultural",
            "wildlife_score": 1,
            "adventure_score": 2,
            "beach_score": 0,
            "family_score": 4,
            "history_score": 4,
            "culture_score": 5
        },

        {
            "name": "Chefchaouen",
            "country": "Morocco",
            "description": "A picturesque mountain town famous for its blue-painted buildings and traditional Moroccan culture.",
            "estimated_cost": 700,
            "climate": "Temperate",
            "best_season": "March-May",
            "latitude": 35.171,
            "longitude": -5.269,
            "image_url": "chefchaouen.jpg",
            "destination_type": "Cultural",
            "wildlife_score": 1,
            "adventure_score": 3,
            "beach_score": 1,
            "family_score": 4,
            "history_score": 4,
            "culture_score": 5
        }

        

    ]

    #  destinations first
    destinations = []

    for data in destinations_data:

        destination = Destination(
            name=data["name"],
            country=data["country"],
            description=data["description"],
            estimated_cost=data["estimated_cost"],
            climate=data["climate"],
            best_season=data["best_season"],
            latitude=data["latitude"],
            longitude=data["longitude"],
            image_url=data["image_url"]
        )

        destinations.append(destination)

    db.add_all(destinations)
    db.commit()

    # Refresh IDs
    for destination in destinations:
        db.refresh(destination)

    # Create feature records
    features = []

    for destination, data in zip(destinations, destinations_data):

        feature = DestinationFeature(
            destination_id=destination.destination_id,
            destination_type=data["destination_type"],
            wildlife_score=data["wildlife_score"],
            adventure_score=data["adventure_score"],
            beach_score=data["beach_score"],
            family_score=data["family_score"],
            history_score=data["history_score"],
            culture_score=data["culture_score"]
        )

        features.append(feature)

    db.add_all(features)
    db.commit()

    print("Destination data seeded successfully!")
    print(f"Destinations inserted: {len(destinations)}")
    print(f"Features inserted: {len(features)}")


except Exception as e:

    db.rollback()
    print("Error:", e)

finally:

    db.close()