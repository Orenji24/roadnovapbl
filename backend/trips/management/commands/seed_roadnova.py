from datetime import date

from django.core.management.base import BaseCommand

from trips.models import Stop, Trip


class Command(BaseCommand):
    help = 'Seed RoadNova with demo trips and stops.'

    def handle(self, *args, **options):
        Trip.objects.all().delete()

        routes = [
            {
                'title': 'Pacific Ember Run',
                'origin': 'San Francisco',
                'destination': 'Big Sur',
                'tagline': 'Cliffside drives, tide pools, redwoods, and slow coastal mornings.',
                'mood': 'coastal',
                'start_date': date(2026, 6, 12),
                'days': 4,
                'distance_km': 510,
                'budget': 620,
                'cover_color': '#0f766e',
                'is_featured': True,
                'stops': [
                    ('San Francisco', 'Cross the bridge after breakfast and stock the cooler.', 'Start', False),
                    ('Half Moon Bay', 'Walk the bluffs and grab a seafood lunch.', '55m', False),
                    ('Santa Cruz', 'Boardwalk pause and sunset coffee near West Cliff.', '1h 10m', True),
                    ('Big Sur', 'Redwood hikes, coastal overlooks, and a no-rush final night.', '1h 35m', True),
                ],
            },
            {
                'title': 'Blue Ridge Switchback',
                'origin': 'Asheville',
                'destination': 'Shenandoah',
                'tagline': 'A ridgeline crawl through overlooks, cabins, and tiny mountain towns.',
                'mood': 'mountain',
                'start_date': date(2026, 7, 3),
                'days': 6,
                'distance_km': 760,
                'budget': 810,
                'cover_color': '#4338ca',
                'stops': [
                    ('Asheville', 'Coffee, gallery stroll, and route prep.', 'Start', False),
                    ('Boone', 'Waterfall detour and a relaxed dinner downtown.', '2h 20m', True),
                    ('Roanoke', 'Overlook-heavy day with a late check-in.', '3h 10m', True),
                    ('Shenandoah', 'Skyline Drive, trailheads, and a final cabin night.', '2h 45m', True),
                ],
            },
            {
                'title': 'Desert Neon Loop',
                'origin': 'Las Vegas',
                'destination': 'Joshua Tree',
                'tagline': 'Retro motels, desert skies, art stops, and night drives under stars.',
                'mood': 'wild',
                'start_date': date(2026, 8, 21),
                'days': 5,
                'distance_km': 890,
                'budget': 740,
                'cover_color': '#c2410c',
                'stops': [
                    ('Las Vegas', 'Leave the strip early and point toward open desert.', 'Start', False),
                    ('Mojave Preserve', 'Kelso dunes, wide roads, and packed water.', '2h 30m', True),
                    ('Palm Springs', 'Architecture walk and poolside recovery.', '2h 15m', True),
                    ('Joshua Tree', 'Sunrise boulders and a stargazing finale.', '55m', True),
                ],
            },
        ]

        for route in routes:
            stops = route.pop('stops')
            trip = Trip.objects.create(**route)
            Stop.objects.bulk_create(
                Stop(trip=trip, order=index, name=name, note=note, drive_time=drive_time, overnight=overnight)
                for index, (name, note, drive_time, overnight) in enumerate(stops, start=1)
            )

        self.stdout.write(self.style.SUCCESS('Seeded RoadNova demo trips.'))
