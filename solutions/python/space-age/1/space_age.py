class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self.earth_year = seconds/31557600
        
    def on_mercury(self):

        age = self.earth_year / 0.2408467

        return round(age,2)

    def on_venus(self):

        age = self.earth_year/0.61519726

        return round(age,2)

    def on_earth(self):

        return round(self.earth_year,2)

    def on_mars(self):

        age = self.earth_year/1.8808158

        return round(age,2)
        
    def on_jupiter(self):

        age = self.earth_year/11.862615

        return round(age,2)
    def on_saturn(self):

        age = self.earth_year/29.447498

        return round(age,2)
    def on_uranus(self):

        age = self.earth_year/84.016846

        return round(age,2)
    def on_neptune(self):

        age = self.earth_year/164.79132

        return round(age,2)

        
