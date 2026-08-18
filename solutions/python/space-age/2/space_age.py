
class SpaceAge:
    _PLANET_YEARS = {'Mercury' : 0.2408467,
                    'Venus' : 0.61519726,
                    'Earth' : 1.0,
                    'Mars' : 1.8808158,
                    'Jupiter' : 11.862615,
                    'Saturn' : 29.447498,
                    'Uranus' : 84.016846,
                    'Neptune' : 164.79132
                   }

    _SECONDS_PER_EARTH_YEAR = 31557600
    
    def __init__(self, seconds):
        self.age_on_earth = seconds / self._SECONDS_PER_EARTH_YEAR

    def on_mercury(self):
        return round(self.age_on_earth / self._PLANET_YEARS['Mercury'], 2)

    def on_venus(self):
        return round(self.age_on_earth / self._PLANET_YEARS['Venus'], 2)

    def on_earth(self):
        return round(self.age_on_earth / self._PLANET_YEARS['Earth'], 2)

    def on_mars(self):
        return round(self.age_on_earth / self._PLANET_YEARS['Mars'], 2)

    def on_jupiter(self):
        return round(self.age_on_earth / self._PLANET_YEARS['Jupiter'], 2)

    def on_saturn(self):
        return round(self.age_on_earth / self._PLANET_YEARS['Saturn'], 2)

    def on_uranus(self):
        return round(self.age_on_earth / self._PLANET_YEARS['Uranus'], 2)

    def on_neptune(self):
        return round(self.age_on_earth / self._PLANET_YEARS['Neptune'], 2)

