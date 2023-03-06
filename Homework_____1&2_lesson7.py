# Написать класс Car
# # Конструктор класса принимает атрибуты:
# # color: str (цвет)
# # count_passenger_seats: int (количество пассажирских мест)
# # is_baby_seat: bool (наличие десткого кресла)
# # is_busy: bool (определяется внутри конструктора со значением False, не принимается на
# # вход)
# # 1.1 Написать магический метод __str__ выводящий форматированную строку с информацией
# # об автомобиле

class Car:

    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool, is_busy: bool = False):

        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat
        self.is_busy = is_busy


    def __str__(self):
        return f'Car: {self.color, self.count_passenger_seats, self.is_baby_seat, self.is_busy}'


car_1 = Car("red", 5, True)
car_2 = Car("black", 6, False)
print(str(car_1))
print(str(car_2))

#Написать класс Taxi
# Конструктор класса принимает атрибуты:
# cars: list[Car] (список экземпляров класса Car)
# 2.1 Реализовать метод find_car
# На вход метода поступают атрибуты: count_passengers, is_baby (количество пассажиров,
# наличие ребенка, примечание: количество пассажиров с учетом ребенка если он есть)
# На основании данных, вернуть объект Car из атрибута cars подходящий по параметрам и
# свободный (is_busy = False), у автомобиля сменить атрибут is_busy на значение True, если
# подходящего автомобиля нет, метод должен возвращать None
class Taxi:
    def __init__(self, cars: list[Car]):
        self.cars = cars

    def find_car(self, count_passengers: int, is_baby: bool):
        self.count_passengers = count_passengers
        self.is_baby = is_baby
        for c in self.cars:
            if count_passengers <= car_1.count_passengers_seats:
            return car_1
            print(car_1)
            elif:

            else:
            return None








