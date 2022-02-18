"""MAIN FILE OF LAB TWITTER MAP"""


from flask import Flask, render_template, request
import folium
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderUnavailable
import twitter


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    """
    Function that returns the index.html template and processes
    the given value.
    """
    username = ''
    if request.method == "POST":
        info = request.form
        username = info['username']
        print(username)

        locations = twitter.locations(username)
        print(locations)
        geocoder = Nominatim(user_agent="mykhailo.trushch@gmail.com")
        user_location = twitter.user_loc(username)
        if user_location is not None:
            map1 = folium.Map(zoom_start=10, location=[user_location.lat, user_location.lon])
        else:
            map1 = folium.Map(zoom_start=10)
        main_group = folium.FeatureGroup()
        counter = 0
        for i in locations: # pylint: disable=C0206
            if counter >= 60:
                break
            location = locations[i]
            location = location.strip("!")
            try:
                loc = geocoder.geocode(location)
            except GeocoderUnavailable:
                loc = None
            if loc is None:
                continue
            counter += 1
            loc = loc.latitude, loc.longitude
            print(loc)
            main_group.add_child(folium.Marker(location=list(loc),
                                               popup=i,
                                               icon=folium.Icon(color="red")))
        map1.add_child(main_group)
        map1.fit_bounds(map1.get_bounds())
        return map1._repr_html_() # pylint: disable=W0212
    return render_template("index.html", username=username)


if __name__ == "__main__":
    app.run(debug=True)
