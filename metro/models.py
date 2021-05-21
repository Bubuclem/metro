from django.db import models

class Station(models.Model):
    nom     = models.CharField(max_length=200)
    x_coord = models.IntegerField(null=True)
    y_coord = models.IntegerField(null=True)

    def __str__(self):
        return self.nom
    def coordinates(self):
        return (self.x_coord,self.y_coord)

class Ligne(models.Model):
    nom         = models.CharField(max_length=200)
    stations    = models.ManyToManyField(Station)
    def __str__(self):
        return self.nom
    def get_stations(self):
        return ", ".join([str(s) for s in self.stations.all()])

class Trajet(models.Model):
    FromStation = models.ForeignKey(Station, on_delete=models.CASCADE, related_name="from_station")
    ToStation   = models.ForeignKey(Station, on_delete=models.CASCADE, related_name="to_station")
    distance    = models.FloatField(default=0.0)
    time        = models.TimeField(auto_now=False, blank=True)

    def __str__(self):
        return 'Trajet: %s -> %s' % (
            self.FromStation.nom,
            self.ToStation.nom
        )