from math import asin, cos, radians, sin, sqrt


CITIES = {
    'bangalore': {
        'name': 'Bangalore',
        'state': 'Karnataka',
        'lat': 12.9716,
        'lon': 77.5946,
        'fuel_price': 103.0,
        'hotel_avg': 3600,
        'food_avg': 1200,
        'vibe': 'craft cafes, tech streets, gardens, and weekend hill detours',
        'road_notes': {
            'fuel': 'Fuel up near Nelamangala or Devanahalli before leaving the city limits.',
            'scenic': 'Nandi Hills sunrise detour or Ramanagara rock views depending on your highway.',
            'break': 'Use a highway Cafe Coffee Day or Adyar Ananda Bhavan stop after the first 90 km.',
        },
        'attractions': [
            {'name': 'ISKCON Temple Bangalore', 'type': 'Temple', 'note': 'Calm evening aarti and city views.'},
            {'name': 'Lalbagh Botanical Garden', 'type': 'Nature', 'note': 'Morning walk before traffic builds.'},
            {'name': 'Bangalore Palace', 'type': 'Heritage', 'note': 'A quick royal-history stop.'},
        ],
        'restaurants': ['MTR', 'Vidyarthi Bhavan', 'Toit'],
        'hotels': ['The Oberoi Bengaluru', 'Bloomrooms Indiranagar', 'Taj MG Road'],
    },
    'goa': {
        'name': 'Goa',
        'state': 'Goa',
        'lat': 15.2993,
        'lon': 74.1240,
        'fuel_price': 97.0,
        'hotel_avg': 4200,
        'food_avg': 1500,
        'vibe': 'beaches, forts, seafood, and slow coastal roads',
        'road_notes': {
            'fuel': 'Top up around Ponda or Mapusa before beach-hopping.',
            'scenic': 'Add Chorla Ghat viewpoints if entering from Karnataka.',
            'break': 'Use a beachside shack pause after check-in, not during peak afternoon heat.',
        },
        'attractions': [
            {'name': 'Baga Beach', 'type': 'Beach', 'note': 'Lively sunset and water sports.'},
            {'name': 'Basilica of Bom Jesus', 'type': 'Heritage', 'note': 'UNESCO-era old Goa architecture.'},
            {'name': 'Aguada Fort', 'type': 'Fort', 'note': 'Coastal views near Candolim.'},
        ],
        'restaurants': ['Ritz Classic', 'Gunpowder', 'Thalassa'],
        'hotels': ['Taj Cidade de Goa', 'BloomSuites Calangute', 'The Hosteller Goa'],
    },
    'manali': {
        'name': 'Manali',
        'state': 'Himachal Pradesh',
        'lat': 32.2432,
        'lon': 77.1892,
        'fuel_price': 96.0,
        'hotel_avg': 3500,
        'food_avg': 1100,
        'vibe': 'mountain drives, snow viewpoints, cafes, and river valleys',
        'road_notes': {
            'fuel': 'Refuel at Mandi or Kullu before the tighter hill climb.',
            'scenic': 'Keep time for Beas river viewpoints and pine-valley photo pullouts.',
            'break': 'Stop every 60 to 80 km on hill roads to cool brakes and stretch.',
        },
        'attractions': [
            {'name': 'Hadimba Devi Temple', 'type': 'Temple', 'note': 'Cedar forest temple stop.'},
            {'name': 'Solang Valley', 'type': 'Adventure', 'note': 'Paragliding and snow-season views.'},
            {'name': 'Old Manali', 'type': 'Cafe', 'note': 'Cafes, shops, and slow evenings.'},
        ],
        'restaurants': ['Johnson Bar and Restaurant', 'Cafe 1947', 'Drifters Cafe'],
        'hotels': ['Span Resort and Spa', 'The Orchard Greens', 'Zostel Manali'],
    },
    'delhi': {
        'name': 'Delhi',
        'state': 'Delhi',
        'lat': 28.6139,
        'lon': 77.2090,
        'fuel_price': 94.8,
        'hotel_avg': 4100,
        'food_avg': 1400,
        'vibe': 'monuments, markets, food lanes, and big highway exits',
        'road_notes': {
            'fuel': 'Start with a full tank before crossing Gurgaon, Noida, or Sonipat exits.',
            'scenic': 'India Gate night drive works best after city traffic drops.',
            'break': 'Use Murthal dhabas or expressway plazas depending on your direction.',
        },
        'attractions': [
            {'name': 'Akshardham Temple', 'type': 'Temple', 'note': 'Large temple complex and evening show.'},
            {'name': 'India Gate', 'type': 'Landmark', 'note': 'Night drive and central vista.'},
            {'name': 'Humayun Tomb', 'type': 'Heritage', 'note': 'Mughal architecture and gardens.'},
        ],
        'restaurants': ['Karim Hotel', 'Indian Accent', 'Saravana Bhavan'],
        'hotels': ['The Lalit New Delhi', 'Bloomrooms Janpath', 'The Imperial'],
    },
    'mumbai': {
        'name': 'Mumbai',
        'state': 'Maharashtra',
        'lat': 19.0760,
        'lon': 72.8777,
        'fuel_price': 104.2,
        'hotel_avg': 5200,
        'food_avg': 1600,
        'vibe': 'sea links, art deco lanes, beaches, and late-night food',
        'road_notes': {
            'fuel': 'Top up before the expressway or Western Express Highway merge.',
            'scenic': 'Marine Drive and Bandra-Worli Sea Link are the cleanest city-drive moments.',
            'break': 'Plan a vada pav or Irani cafe stop before leaving the island city.',
        },
        'attractions': [
            {'name': 'Siddhivinayak Temple', 'type': 'Temple', 'note': 'Important city temple stop.'},
            {'name': 'Juhu Beach', 'type': 'Beach', 'note': 'Street food and sunset.'},
            {'name': 'Gateway of India', 'type': 'Landmark', 'note': 'Classic Mumbai waterfront.'},
        ],
        'restaurants': ['Britannia and Co.', 'Trishna', 'Prakash Upahar Gruha'],
        'hotels': ['Taj Mahal Palace', 'Abode Bombay', 'The Leela Mumbai'],
    },
    'hyderabad': {
        'name': 'Hyderabad',
        'state': 'Telangana',
        'lat': 17.3850,
        'lon': 78.4867,
        'fuel_price': 107.4,
        'hotel_avg': 3400,
        'food_avg': 1200,
        'vibe': 'biryani, forts, lakes, and long expressway stretches',
        'road_notes': {
            'fuel': 'Fill up near ORR exits before committing to the highway.',
            'scenic': 'Hussain Sagar or Golconda sunset makes a strong city pause.',
            'break': 'Use a biryani lunch stop before departure if the next leg is long.',
        },
        'attractions': [
            {'name': 'Birla Mandir', 'type': 'Temple', 'note': 'Marble temple with city views.'},
            {'name': 'Charminar', 'type': 'Heritage', 'note': 'Old city icon and markets.'},
            {'name': 'Golconda Fort', 'type': 'Fort', 'note': 'Evening light-and-sound option.'},
        ],
        'restaurants': ['Paradise Biryani', 'Shah Ghouse', 'Chutneys'],
        'hotels': ['Taj Krishna', 'The Park Hyderabad', 'FabHotel Limestone'],
    },
    'munnar': {
        'name': 'Munnar',
        'state': 'Kerala',
        'lat': 10.0889,
        'lon': 77.0595,
        'fuel_price': 107.6,
        'hotel_avg': 3800,
        'food_avg': 1100,
        'vibe': 'tea estates, misty ghat roads, waterfalls, and viewpoints',
        'road_notes': {
            'fuel': 'Refuel at Adimali or the plains before climbing into Munnar.',
            'scenic': 'Keep camera time for tea-estate bends, waterfalls, and mist breaks.',
            'break': 'Take short ghat-road pauses instead of one long stop.',
        },
        'attractions': [
            {'name': 'Tea Museum', 'type': 'Heritage', 'note': 'Tea history and tasting.'},
            {'name': 'Eravikulam National Park', 'type': 'Nature', 'note': 'Book ahead in peak season.'},
            {'name': 'Attukad Waterfalls', 'type': 'Waterfall', 'note': 'Good monsoon photo stop.'},
        ],
        'restaurants': ['Rapsy Restaurant', 'Saravana Bhavan Munnar', 'Tea Tales Cafe'],
        'hotels': ['Fragrant Nature Munnar', 'Tea County Munnar', 'Zostel Munnar'],
    },
    'surat': {
        'name': 'Surat',
        'state': 'Gujarat',
        'lat': 21.1702,
        'lon': 72.8311,
        'fuel_price': 95.0,
        'hotel_avg': 3000,
        'food_avg': 1000,
        'vibe': 'textile markets, Gujarati snacks, riverfront, and coastal day trips',
        'road_notes': {
            'fuel': 'Top up before the Mumbai-Ahmedabad highway or Dumas side trip.',
            'scenic': 'Tapi riverfront and Dumas Beach are the easiest relaxed breaks.',
            'break': 'Plan a locho or thali stop before getting back on the highway.',
        },
        'attractions': [
            {'name': 'Ambika Niketan Temple', 'type': 'Temple', 'note': 'Popular Tapi river temple.'},
            {'name': 'Dumas Beach', 'type': 'Beach', 'note': 'Evening snack stop near the sea.'},
            {'name': 'Dutch Garden', 'type': 'Heritage', 'note': 'Short city-history pause.'},
        ],
        'restaurants': ['Sasumaa Gujarati Thali', 'Gopal Locho', 'Leonardo Italian'],
        'hotels': ['Courtyard by Marriott Surat', 'Lords Plaza Surat', 'Ginger Surat'],
    },
    'jaipur': {
        'name': 'Jaipur',
        'state': 'Rajasthan',
        'lat': 26.9124,
        'lon': 75.7873,
        'fuel_price': 104.9,
        'hotel_avg': 3900,
        'food_avg': 1200,
        'vibe': 'forts, temples, bazaars, palace hotels, and desert-edge roads',
        'road_notes': {
            'fuel': 'Fuel up before Amber Road or the Delhi-Jaipur highway push.',
            'scenic': 'Nahargarh and Amber Fort approaches give the best drive views.',
            'break': 'Use a dhaba or lassi stop outside city traffic before parking near the old city.',
        },
        'attractions': [
            {'name': 'Govind Dev Ji Temple', 'type': 'Temple', 'note': 'Central devotional stop.'},
            {'name': 'Amber Fort', 'type': 'Fort', 'note': 'Start early for cooler weather.'},
            {'name': 'Hawa Mahal', 'type': 'Heritage', 'note': 'Iconic old-city facade.'},
        ],
        'restaurants': ['Laxmi Misthan Bhandar', 'Rawat Mishtan Bhandar', 'Peacock Rooftop Restaurant'],
        'hotels': ['Alsisar Haveli', 'ITC Rajputana', 'Zostel Jaipur'],
    },
    'chennai': {
        'name': 'Chennai',
        'state': 'Tamil Nadu',
        'lat': 13.0827,
        'lon': 80.2707,
        'fuel_price': 100.8,
        'hotel_avg': 3600,
        'food_avg': 1100,
        'vibe': 'temples, beaches, filter coffee, and East Coast Road drives',
        'road_notes': {
            'fuel': 'Fill up before ECR or GST Road depending on the route.',
            'scenic': 'East Coast Road, Marina, and Besant Nagar are the best coastal drive breaks.',
            'break': 'Start with filter coffee and tiffin before the highway stretch.',
        },
        'attractions': [
            {'name': 'Kapaleeshwarar Temple', 'type': 'Temple', 'note': 'Historic Mylapore temple.'},
            {'name': 'Marina Beach', 'type': 'Beach', 'note': 'Early morning or breezy evening walk.'},
            {'name': 'San Thome Basilica', 'type': 'Heritage', 'note': 'Landmark near the coast.'},
        ],
        'restaurants': ['Murugan Idli Shop', 'Dakshin', 'Ratna Cafe'],
        'hotels': ['Taj Connemara', 'The Residency Towers', 'Zostel Chennai'],
    },
}


INTERESTS = {
    'temples': 'Temples',
    'beaches': 'Beaches',
    'heritage': 'Heritage',
    'food': 'Food',
    'nature': 'Nature',
    'adventure': 'Adventure',
}


HIGHWAY_STOPS = [
    {'slug': 'tumakuru', 'name': 'Tumakuru', 'state': 'Karnataka', 'lat': 13.3379, 'lon': 77.1173, 'hotel_avg': 2200, 'food_avg': 700, 'fuel_price': 103.0, 'scenic': 'Devarayanadurga hill views and clean highway exits.', 'food': 'Kamat Upachar Tumakuru', 'hotel': 'Naveen Regency'},
    {'slug': 'chitradurga', 'name': 'Chitradurga', 'state': 'Karnataka', 'lat': 14.2251, 'lon': 76.3980, 'hotel_avg': 2400, 'food_avg': 750, 'fuel_price': 103.0, 'scenic': 'Chitradurga Fort, windmill roads, and rocky hill scenery.', 'food': 'Aishwarya Fort Restaurant', 'hotel': 'KSTDC Mayura Durg'},
    {'slug': 'hubballi', 'name': 'Hubballi', 'state': 'Karnataka', 'lat': 15.3647, 'lon': 75.1240, 'hotel_avg': 2800, 'food_avg': 850, 'fuel_price': 103.0, 'scenic': 'Unkal Lake evening walk and wide NH48 service plazas.', 'food': 'Basaveshwar Khanavali', 'hotel': 'The President Hotel'},
    {'slug': 'dandeli', 'name': 'Dandeli', 'state': 'Karnataka', 'lat': 15.2477, 'lon': 74.6297, 'hotel_avg': 3200, 'food_avg': 900, 'fuel_price': 103.0, 'scenic': 'Forest roads, Kali river viewpoints, and calm nature stays.', 'food': 'Bison River Resort Restaurant', 'hotel': 'Dandeli Jungle Camp'},
    {'slug': 'belagavi', 'name': 'Belagavi', 'state': 'Karnataka', 'lat': 15.8497, 'lon': 74.4977, 'hotel_avg': 2900, 'food_avg': 850, 'fuel_price': 103.0, 'scenic': 'Fort area, Kittur stretch, and ghats toward Goa.', 'food': 'Niyaaz Belagavi', 'hotel': 'Fairfield by Marriott Belagavi'},
    {'slug': 'kolhapur', 'name': 'Kolhapur', 'state': 'Maharashtra', 'lat': 16.7050, 'lon': 74.2433, 'hotel_avg': 3000, 'food_avg': 900, 'fuel_price': 104.2, 'scenic': 'Mahalaxmi Temple, Rankala Lake, and NH48 food stops.', 'food': 'Dehati Kolhapur', 'hotel': 'Sayaji Kolhapur'},
    {'slug': 'pune', 'name': 'Pune', 'state': 'Maharashtra', 'lat': 18.5204, 'lon': 73.8567, 'hotel_avg': 3600, 'food_avg': 1100, 'fuel_price': 104.2, 'scenic': 'Sinhagad side roads, old city food, and expressway access.', 'food': 'Vaishali FC Road', 'hotel': 'The Central Park Pune'},
    {'slug': 'lonavala', 'name': 'Lonavala', 'state': 'Maharashtra', 'lat': 18.7546, 'lon': 73.4062, 'hotel_avg': 3800, 'food_avg': 1000, 'fuel_price': 104.2, 'scenic': 'Bhushi Dam, Tiger Point, and misty expressway views.', 'food': 'Rama Krishna Lonavala', 'hotel': 'Fariyas Resort Lonavala'},
    {'slug': 'nashik', 'name': 'Nashik', 'state': 'Maharashtra', 'lat': 19.9975, 'lon': 73.7898, 'hotel_avg': 3000, 'food_avg': 900, 'fuel_price': 104.2, 'scenic': 'Sula side roads, Panchavati temples, and vineyard views.', 'food': 'Sadhana Restaurant', 'hotel': 'Ibis Nashik'},
    {'slug': 'vapi', 'name': 'Vapi', 'state': 'Gujarat', 'lat': 20.3893, 'lon': 72.9106, 'hotel_avg': 2600, 'food_avg': 800, 'fuel_price': 95.0, 'scenic': 'Daman beach detour and Mumbai-Ahmedabad highway plazas.', 'food': 'Woodlands Vapi', 'hotel': 'Fortune Park Galaxy'},
    {'slug': 'vadodara', 'name': 'Vadodara', 'state': 'Gujarat', 'lat': 22.3072, 'lon': 73.1812, 'hotel_avg': 3000, 'food_avg': 850, 'fuel_price': 95.0, 'scenic': 'Laxmi Vilas Palace and expressway access toward Ahmedabad.', 'food': 'Mandap Gujarati Thali', 'hotel': 'Sayaji Vadodara'},
    {'slug': 'ahmedabad', 'name': 'Ahmedabad', 'state': 'Gujarat', 'lat': 23.0225, 'lon': 72.5714, 'hotel_avg': 3200, 'food_avg': 900, 'fuel_price': 95.0, 'scenic': 'Sabarmati Riverfront, old city pols, and stepwell detours.', 'food': 'Agashiye', 'hotel': 'Four Points by Sheraton Ahmedabad'},
    {'slug': 'udaipur', 'name': 'Udaipur', 'state': 'Rajasthan', 'lat': 24.5854, 'lon': 73.7125, 'hotel_avg': 3700, 'food_avg': 1000, 'fuel_price': 104.9, 'scenic': 'Lake Pichola, Aravalli curves, and palace viewpoints.', 'food': 'Natraj Dining Hall', 'hotel': 'Jagat Niwas Palace'},
    {'slug': 'ajmer', 'name': 'Ajmer', 'state': 'Rajasthan', 'lat': 26.4499, 'lon': 74.6399, 'hotel_avg': 2600, 'food_avg': 800, 'fuel_price': 104.9, 'scenic': 'Ana Sagar Lake and Pushkar side detour.', 'food': 'Mango Masala Ajmer', 'hotel': 'Hotel LN Courtyard'},
    {'slug': 'agra', 'name': 'Agra', 'state': 'Uttar Pradesh', 'lat': 27.1767, 'lon': 78.0081, 'hotel_avg': 3300, 'food_avg': 950, 'fuel_price': 96.5, 'scenic': 'Yamuna Expressway plazas and Taj Mahal sunrise option.', 'food': 'Pinch of Spice', 'hotel': 'Crystal Sarovar Premiere'},
    {'slug': 'chandigarh', 'name': 'Chandigarh', 'state': 'Chandigarh', 'lat': 30.7333, 'lon': 76.7794, 'hotel_avg': 3500, 'food_avg': 1000, 'fuel_price': 96.0, 'scenic': 'Sukhna Lake, Rock Garden, and clean mountain-road staging.', 'food': 'Pal Dhaba', 'hotel': 'Hotel Mountview'},
    {'slug': 'mandi', 'name': 'Mandi', 'state': 'Himachal Pradesh', 'lat': 31.7087, 'lon': 76.9320, 'hotel_avg': 2600, 'food_avg': 800, 'fuel_price': 96.0, 'scenic': 'Beas river bends and hill-road rest points.', 'food': 'Mandi Treat', 'hotel': 'Hotel Valley View'},
    {'slug': 'kullu', 'name': 'Kullu', 'state': 'Himachal Pradesh', 'lat': 31.9579, 'lon': 77.1095, 'hotel_avg': 2800, 'food_avg': 850, 'fuel_price': 96.0, 'scenic': 'River rafting stretch, valley roads, and apple-orchard views.', 'food': 'Sapna Sweets Kullu', 'hotel': 'Hotel Sandhya Palace'},
    {'slug': 'anantapur', 'name': 'Anantapur', 'state': 'Andhra Pradesh', 'lat': 14.6819, 'lon': 77.6006, 'hotel_avg': 2300, 'food_avg': 700, 'fuel_price': 107.4, 'scenic': 'Dryland highway views and clean fuel plazas.', 'food': 'Blue Moon Highway Restaurant', 'hotel': 'Hotel Masineni Grand'},
    {'slug': 'kurnool', 'name': 'Kurnool', 'state': 'Andhra Pradesh', 'lat': 15.8281, 'lon': 78.0373, 'hotel_avg': 2500, 'food_avg': 750, 'fuel_price': 107.4, 'scenic': 'Tungabhadra river belt and Orvakal rock garden detour.', 'food': 'Aahar Restaurant Kurnool', 'hotel': 'Triguna Clarks Inn'},
    {'slug': 'vijayawada', 'name': 'Vijayawada', 'state': 'Andhra Pradesh', 'lat': 16.5062, 'lon': 80.6480, 'hotel_avg': 3000, 'food_avg': 900, 'fuel_price': 107.4, 'scenic': 'Kanaka Durga hill road and Krishna river views.', 'food': 'Babai Hotel', 'hotel': 'Quality Hotel DV Manor'},
    {'slug': 'salem', 'name': 'Salem', 'state': 'Tamil Nadu', 'lat': 11.6643, 'lon': 78.1460, 'hotel_avg': 2600, 'food_avg': 800, 'fuel_price': 100.8, 'scenic': 'Yercaud ghat detour and clean highway exits.', 'food': 'Selvi Mess Salem', 'hotel': 'CJ Pallazzio'},
    {'slug': 'coimbatore', 'name': 'Coimbatore', 'state': 'Tamil Nadu', 'lat': 11.0168, 'lon': 76.9558, 'hotel_avg': 3100, 'food_avg': 900, 'fuel_price': 100.8, 'scenic': 'Western Ghats entry roads and coconut belt views.', 'food': 'Annapoorna Gowrishankar', 'hotel': 'Zone by The Park Coimbatore'},
    {'slug': 'madurai', 'name': 'Madurai', 'state': 'Tamil Nadu', 'lat': 9.9252, 'lon': 78.1198, 'hotel_avg': 2800, 'food_avg': 850, 'fuel_price': 100.8, 'scenic': 'Meenakshi Temple area and Vaigai river roads.', 'food': 'Murugan Idli Shop Madurai', 'hotel': 'JC Residency Madurai'},
    {'slug': 'kochi', 'name': 'Kochi', 'state': 'Kerala', 'lat': 9.9312, 'lon': 76.2673, 'hotel_avg': 3800, 'food_avg': 1100, 'fuel_price': 107.6, 'scenic': 'Fort Kochi, backwater edges, and coastal food stops.', 'food': 'Grand Hotel Restaurant', 'hotel': 'Abad Atrium Kochi'},
    {'slug': 'kozhikode', 'name': 'Kozhikode', 'state': 'Kerala', 'lat': 11.2588, 'lon': 75.7804, 'hotel_avg': 3000, 'food_avg': 900, 'fuel_price': 107.6, 'scenic': 'Beach road, Malabar food stops, and coastal highway rhythm.', 'food': 'Paragon Kozhikode', 'hotel': 'The Raviz Calicut'},
    {'slug': 'nagpur', 'name': 'Nagpur', 'state': 'Maharashtra', 'lat': 21.1458, 'lon': 79.0882, 'hotel_avg': 3000, 'food_avg': 850, 'fuel_price': 104.2, 'scenic': 'Zero Mile marker and central-India highway plazas.', 'food': 'Haldiram Nagpur', 'hotel': 'Centre Point Hotel'},
    {'slug': 'indore', 'name': 'Indore', 'state': 'Madhya Pradesh', 'lat': 22.7196, 'lon': 75.8577, 'hotel_avg': 3000, 'food_avg': 850, 'fuel_price': 107.0, 'scenic': 'Sarafa food lane and Malwa highway breaks.', 'food': 'Guru Kripa Indore', 'hotel': 'Effotel Indore'},
]


def city_options():
    return [{'slug': slug, **city} for slug, city in CITIES.items()]


def haversine_km(a, b):
    earth_radius = 6371
    lat1, lon1, lat2, lon2 = map(radians, [a['lat'], a['lon'], b['lat'], b['lon']])
    d_lat = lat2 - lat1
    d_lon = lon2 - lon1
    h = sin(d_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(d_lon / 2) ** 2
    return 2 * earth_radius * asin(sqrt(h))


def road_distance_km(origin, destination):
    return round(haversine_km(origin, destination) * 1.28)


def corridor_waypoints(origin_slug, destination_slug, days):
    if days <= 1:
        return []

    origin = CITIES[origin_slug]
    destination = CITIES[destination_slug]
    lat_span = destination['lat'] - origin['lat']
    lon_span = destination['lon'] - origin['lon']
    span_sq = lat_span ** 2 + lon_span ** 2 or 1
    candidates = []

    for stop in HIGHWAY_STOPS:
        if haversine_km(origin, stop) < 40 or haversine_km(destination, stop) < 40:
            continue
        t = ((stop['lat'] - origin['lat']) * lat_span + (stop['lon'] - origin['lon']) * lon_span) / span_sq
        if not 0.08 < t < 0.92:
            continue
        projected = {'lat': origin['lat'] + lat_span * t, 'lon': origin['lon'] + lon_span * t}
        off_route_km = haversine_km(stop, projected)
        if off_route_km > 160:
            continue
        candidates.append({**stop, 'projection': t, 'off_route_km': off_route_km})

    selected = []
    for slot in range(1, days):
        ideal = slot / days
        available = [stop for stop in candidates if stop['slug'] not in {item['slug'] for item in selected}]
        if not available:
            generated = {
                'slug': f'corridor-{slot}',
                'name': f"Highway Halt {slot}",
                'state': 'Route corridor',
                'lat': origin['lat'] + lat_span * ideal,
                'lon': origin['lon'] + lon_span * ideal,
                'hotel_avg': 2600,
                'food_avg': 800,
                'fuel_price': origin['fuel_price'],
                'scenic': 'Use a marked service plaza, lake viewpoint, or safe town bypass for this halt.',
                'food': 'Highway dhaba or food court',
                'hotel': 'Route-side business hotel',
                'projection': ideal,
            }
            selected.append(generated)
            continue
        selected.append(min(available, key=lambda stop: abs(stop['projection'] - ideal) * 320 + stop['off_route_km'] * 2.2))

    return sorted(selected, key=lambda stop: stop['projection'])


def route_stops(origin_slug, destination_slug):
    origin = CITIES[origin_slug]
    destination = CITIES[destination_slug]
    direct_distance = road_distance_km(origin, destination)
    candidates = []

    for slug, city in CITIES.items():
        if slug in {origin_slug, destination_slug}:
            continue
        via_distance = road_distance_km(origin, city) + road_distance_km(city, destination)
        if via_distance <= direct_distance * 1.38:
            candidates.append((via_distance, slug))

    candidates.sort()
    chosen = [slug for _, slug in candidates[:2]]
    return [origin_slug, *chosen, destination_slug]


def places_for_city(city_slug, interests):
    city = CITIES[city_slug]
    selected = []
    wanted = {interest.lower() for interest in interests}

    for place in city['attractions']:
        place_type = place['type'].lower()
        if not wanted or place_type in wanted or (place_type == 'fort' and 'heritage' in wanted):
            selected.append(place)

    if not selected:
        selected = city['attractions'][:2]
    return selected
