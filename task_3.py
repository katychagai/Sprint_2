class PointsForPlace:
    def __init__(self):
        self.points = 0
    
    def get_points_for_place(self, place):
        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
            self.points = 0
        elif place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
            self.points = 0
        else:
            self.points = 101 - place
        return self.points

        
class PointsForMeters:
    def __init__(self):
        self.points = 0

    def get_points_for_meters(self, meters):
        if meters < 0:
            print('Количество метров не может быть отрицательным')
            self.points = 0
        else:
            self.points = meters * 0.5
        return self.points
                  

class TotalPoints(PointsForPlace, PointsForMeters):
    def __init__(self):
        PointsForPlace.__init__(self)
        PointsForMeters.__init__(self)
        self.total = 0
       


    def get_total_points(self, meters, place):
        place_points = self.get_points_for_place(place)  # Вызываем метод из PointsForPlace
        meters_points = self.get_points_for_meters(meters)  # Вызываем метод из PointsForMeters
        self.total = place_points + meters_points
        return self.total

    

points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))