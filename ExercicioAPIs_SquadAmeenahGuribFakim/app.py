from flask import Flask, render_template
import urllib.request as ur
import json
import ssl

# Disables SSL to bypass the "certificate_verify_failed" error
ssl._create_default_https_context = ssl._create_unverified_context

app = Flask(__name__)


# Main page
@app.route("/")
def index():
    return render_template("index.html")


# Characters' JSON
@app.route("/lista")
def get_characters_json():
    with ur.urlopen("https://rickandmortyapi.com/api/character/") as url:
        response = url.read()
        characters_list = json.loads(response)
        characters = []

        for character in characters_list["results"]:
            character = {
                "name": character["name"],
                "status": character["status"],
            }
            characters.append(character)

    return {"characters": characters}


# Characters' Page
@app.route("/characters")
def get_characters():
    url = "https://rickandmortyapi.com/api/character/"
    response = ur.urlopen(url)
    data = response.read()
    characters_data = json.loads(data)

    return render_template("characters.html", characters=characters_data["results"])


# Character's Profile Page
@app.route("/profile/<id>")
def get_single_profile(id):
    url = f"https://rickandmortyapi.com/api/character/{id}"
    response = ur.urlopen(url)
    data = response.read()
    character_profile = json.loads(data)

    return render_template("profile.html", profile=character_profile)


# Episodes Page
@app.route("/episodes")
def get_episode_data():
    url = f"https://rickandmortyapi.com/api/episode/"
    response = ur.urlopen(url)
    data = response.read()
    episode_data = json.loads(data)

    return render_template("episodes.html", episodes=episode_data["results"])


# Single Episode Page
@app.route("/episode/<id>")
def get_single_episode(id):
    url = f"https://rickandmortyapi.com/api/episode/{id}"
    try:
        response = ur.urlopen(url)
        data = response.read()
        episode_profile = json.loads(data)

        # Fetches the characters list from each episode
        characters = []
        for character_url in episode_profile["characters"]:
            with ur.urlopen(character_url) as character_response:
                character_data = json.loads(character_response.read())
                characters.append(
                    {"id": character_data["id"], "name": character_data["name"]}
                )

        return render_template(
            "episode.html", episode=episode_profile, characters=characters
        )

    except Exception as e:
        return f"Unexpected error: {str(e)}"


# Locations' Page
@app.route("/locations")
def get_location():
    url_for = "https://rickandmortyapi.com/api/location"
    response = ur.urlopen(url_for)
    data = response.read()
    location_data = json.loads(data)

    return render_template("locations.html", locations=location_data["results"])


# Single Location Page
@app.route("/location/<int:id>")
def get_single_location(id):
    url = f"https://rickandmortyapi.com/api/location/{id}"
    try:
        with ur.urlopen(url) as response:
            data = response.read()
            location_profile = json.loads(data)

            # Fetches the residents list from each location
            residents = []
            for resident_url in location_profile["residents"]:
                with ur.urlopen(resident_url) as resident_response:
                    resident_data = json.loads(resident_response.read())
                    residents.append(
                        {"id": resident_data["id"], "name": resident_data["name"]}
                    )

            return render_template(
                "location.html", location=location_profile, residents=residents
            )

    except Exception as e:
        return f"Unexpected error: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)
