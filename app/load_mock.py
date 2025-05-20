import datetime
import json
import os

import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()

# Import models after Django setup
from app.models import Game, Platform, Studio


def load_games_data():
    """
    Load game data from JSON into Django models
    """
    # First ensure migrations are applied

    # JSON data - you can also load this from a file
    data = [
        {
            "name": "The Witcher 3 : Wild Hunt",
            "release_date": "2015-05-19",
            "studio": "CD Projekt RED",
            "ratings": 19,
            "platforms": ["PC", "PS4", "PS5", "Switch", "One"],
        },
        {
            "name": "Mario Kart 8 Deluxe",
            "release_date": "2017-04-28",
            "studio": "Nintendo",
            "ratings": 16,
            "platforms": ["Switch"],
        },
        {
            "name": "Don't Starve",
            "release_date": "2013-04-23",
            "studio": "Capybara Games",
            "ratings": 17,
            "platforms": ["PC", "PS4", "Switch", "One", "WiiU", "PS3"],
        },
    ]

    # Process each game entry
    for game_data in data:
        # Create or get the game object

        studio, _ = Studio.objects.get_or_create(name=game_data["studio"])

        game, created = Game.objects.get_or_create(
            name=game_data["name"],
            defaults={
                "release_date": game_data["release_date"],
                "studio": studio,
                "ratings": game_data["ratings"],
            },
        )

        if not created:
            # Update the game if it already exists
            game.release_date = game_data["release_date"]
            game.studio = studio
            game.ratings = game_data["ratings"]
            game.save()

        # Process platforms - create if they don't exist
        for platform_name in game_data["platforms"]:
            platform, _ = Platform.objects.get_or_create(name=platform_name)
            game.platform.add(platform)

        print(f"{'Created' if created else 'Updated'} game: {game.name}")


if __name__ == "__main__":
    # Ensure Platform model has necessary fields
    # This assumes Platform model has a 'name' field
    print("Loading game data...")
    load_games_data()
    print("Data loading complete!")
