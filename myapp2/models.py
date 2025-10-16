from django.db import models

class User(models.Model):
    nickname = models.CharField("Никнейм", max_length=50)
    surname = models.CharField("Фамилия", max_length=50)
    name = models.CharField("Имя", max_length=50)
    patronymic = models.CharField("Отчество", max_length=50)
    mail = models.EmailField("Почта", max_length=100)
    phone_number = models.CharField("Номер телефона", max_length=100)
    registration_date = models.DateField("Дата регистрации")
    map_id = models.ForeignKey('Map', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Карта')
    booking_id = models.ForeignKey('Booking', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Бронирование')
    
    def __str__(self):
        return f"{self.surname} ({self.mail})"

    class Meta:
        verbose_name = "Пользователь" 
        verbose_name_plural = "Пользователи"
        
        

class Additional_service(models.Model):
    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    cost = models.DecimalField("Стоимость", max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Дополнительная услуга" 
        verbose_name_plural = "Дополнительные услуги"

    def __str__(self):
        return f"{self.name} ({self.cost}"


class Tour(models.Model):
    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    cost = models.DecimalField("Стоимость", max_digits=10, decimal_places=2)
    duration_of_the_tour = models.IntegerField("Продолжительность тура", default=0)
    start_date = models.DateField("Дата начала")
    end_date = models.DateField("Дата окончания")

    class Meta:
        verbose_name = "Тур" 
        verbose_name_plural = "Туры"

    def __str__(self):
        return f"{self.name} ({self.start_date} - {self.end_date})"
    


class Booking(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    booking_date = models.DateField("Дата бронирования")
    tour_id = models.ForeignKey(Tour, on_delete=models.CASCADE, verbose_name='Тур')
    Additional_services_id = models.ForeignKey('Additional_service', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Дополнительные услуги')
    number_of_participants = models.IntegerField(default=0, verbose_name='Количество участников')
    cost = models.DecimalField("Стоимость", max_digits=10, decimal_places=2)
    def __str__(self):
        return f"Бронирование №{self.id} для {self.user_id.surname} на тур '{self.tour_id.name}'"
    class Meta:
        verbose_name = "Бронирование" 
       

class Feedback(models.Model):
    tour_id = models.ForeignKey('Tour', on_delete=models.CASCADE, verbose_name='Тур')
    review_text = models.TextField("Текст отзыва")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    date_reference = models.DateField("Дата отзыва")
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')
    def __str__(self):
        return f" '{self.tour_id.name}' от {self.date_reference.strftime('%Y-%m-%d')}"
    class Meta:
        verbose_name = "Отзыв" 
        verbose_name_plural = "Отзывы"



class Article(models.Model):  
    name = models.CharField("Название", max_length=100)
    author = models.CharField("Автор", max_length=100)
    Date_of_publicationи = models.DateField("Дата публикации")
    content = models.TextField("Содержание")
    tour_id = models.ForeignKey(Tour, on_delete=models.CASCADE, verbose_name='Тур')
    category = models.CharField("Категория", max_length=50)

    class Meta:
        verbose_name = "Статья" 
        verbose_name_plural = "Статьи"

    def __str__(self):
        return f"{self.name} (Author: {self.author})"
    

class Stock(models.Model):
    name = models.CharField("Название", max_length=100)
    start_date = models.DateField("Дата начала")
    end_date = models.DateField("Дата окончания")

    class Meta:
        verbose_name = "Акция" 
        verbose_name_plural = "Акции"

    def __str__(self):
        return f"{self.name} (с {self.start_date} по {self.end_date})"

class Event(models.Model):
    name = models.CharField("Название", max_length=100)
    location_of_the_event = models.CharField("Место проведения", max_length=100)
    date_and_time = models.DateTimeField("Дата и время")
    type_of_event = models.CharField("Тип мероприятия", max_length=50)

    class Meta:
        verbose_name = "Событие" 
        verbose_name_plural = "События"

    def __str__(self):
        return f"{self.name} ({self.date_and_time.strftime('%Y-%m-%d %H:%M')})"

class Map(models.Model):
    tour_id = models.ForeignKey(Tour,on_delete=models.CASCADE, verbose_name='Тур')
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Событие')
    
    class Meta:
        verbose_name = "Карта" 
        verbose_name_plural = "Карты"

    def __str__(self):
        return f"map: tour '{self.tour_id.name}'; Event '{self.event_id.name}'"
