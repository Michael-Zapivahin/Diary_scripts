

def create_Commendation(student_name, subject_name):
    import random
    from datacenter.models import Commendation
    from datacenter.models import Schoolkid
    from datacenter.models import Lesson
    from datacenter.models import Subject
    words = ['Молодец!', 'Отлично!', 'Хорошо!', 'Гораздо лучше, чем я ожидал!', 'Ты меня приятно удивил!', 'Великолепно!', 'Прекрасно!', 'Ты меня очень обрадовал!', 'Именно этого я давно ждал от тебя!', 'Сказано здорово – просто и ясно!', 'Ты, как всегда, точен!', 'Очень хороший ответ!', 'Талантливо!', 'Ты сегодня прыгнул выше головы!', 'Я поражен!', 'Уже существенно лучше!', 'Потрясающе!', 'Замечательно!', 'Прекрасное начало!', 'Так держать!', 'Ты на верном пути!', 'Здорово!', 'Это как раз то, что нужно!', 'Я тобой горжусь!', 'С каждым разом у тебя получается всё лучше!', 'Мы с тобой не зря поработали!', 'Я вижу, как ты стараешься!', 'Ты растешь над собой!', 'Ты многое сделал, я это вижу!', 'Теперь у тебя точно все получится!']
    class_number = 6
    students = Schoolkid.objects.filter(full_name__contains=student_name)
    if students.count() == 0:
        print('Student not found')
        return
    if students.count() > 1:
        print('Found a lot of students')
        return
    subject = Subject.objects.get(title=subject_name, year_of_study=class_number)
    lesson = random.choice(Lesson.objects.filter(subject=subject))
    Commendation.objects.create(text=random.choice(words), created=lesson.date, schoolkid=students[0], subject=subject, teacher=lesson.teacher)



def update_mark(student_name, subject_name, class_number):
    from datacenter.models import Schoolkid
    from datacenter.models import Subject
    from datacenter.models import Mark
    students = Schoolkid.objects.filter(full_name__contains=student_name)
    subject = Subject.objects.get(title=subject_name, year_of_study=class_number)
    if students.count() == 0:
        print('Student not found')
        return
    if students.count() > 1:
        print('Found a lot of students')
        return
    Mark.objects.filter(schoolkid=students[0], subject=subject, points=2).update(points=5)
    Mark.objects.filter(schoolkid=students[0], subject=subject, points=3).update(points=5)



def delete_Chastisements(student_name):
    from datacenter.models import Schoolkid
    from datacenter.models import Chastisement
    student = Schoolkid.objects.get(full_name=student_name)
    Chastisement.objects.filter(schoolkid=student).delete()


