

def get_subject(subject_name, year_of_study=None):
    from datacenter.models import Subject
    try:
        subject = Subject.objects.get(title=subject_name, year_of_study=year_of_study)
    except Subject.DoesNotExist:
        print(f'Предмет {subject_name} {year_of_study} класс не найден')
        return
    except Subject.MultipleObjectsReturned:
        print(f'Найдено много предметов {subject_name} {year_of_study} класс')
        return
    return subject


def get_student(student_name):
    from datacenter.models import Schoolkid
    students = Schoolkid.objects.filter(full_name__contains=student_name)
    if students.count() == 0:
        print('Student not found')
        return
    elif students.count() > 1:
        print('Found a lot of students')
        return
    else:
        return students.first()


def create_commendation(student_name, subject_name):
    import random
    from datacenter.models import Commendation
    from datacenter.models import Lesson
    words = ['Молодец!', 'Отлично!', 'Хорошо!', 'Гораздо лучше, чем я ожидал!', 'Ты меня приятно удивил!', 'Великолепно!', 'Прекрасно!', 'Ты меня очень обрадовал!', 'Именно этого я давно ждал от тебя!', 'Сказано здорово – просто и ясно!', 'Ты, как всегда, точен!', 'Очень хороший ответ!', 'Талантливо!', 'Ты сегодня прыгнул выше головы!', 'Я поражен!', 'Уже существенно лучше!', 'Потрясающе!', 'Замечательно!', 'Прекрасное начало!', 'Так держать!', 'Ты на верном пути!', 'Здорово!', 'Это как раз то, что нужно!', 'Я тобой горжусь!', 'С каждым разом у тебя получается всё лучше!', 'Мы с тобой не зря поработали!', 'Я вижу, как ты стараешься!', 'Ты растешь над собой!', 'Ты многое сделал, я это вижу!', 'Теперь у тебя точно все получится!']
    student = get_student(student_name)
    subject = get_subject(subject_name, student.year_of_study)
    lesson = random.choice(Lesson.objects.filter(subject=subject))
    Commendation.objects.create(text=random.choice(words), created=lesson.date, schoolkid=student, subject=subject, teacher=lesson.teacher)


def update_mark(student_name, subject_name):
    from datacenter.models import Mark
    student = get_student(student_name)
    subject = get_subject(subject_name, student.year_of_study)
    Mark.objects.filter(schoolkid=student, subject=subject, points__in=[2, 3]).update(points=5)


def delete_chastisements(student_name):
    from datacenter.models import Chastisement
    Chastisement.objects.filter(schoolkid=get_student(student_name)).delete()
