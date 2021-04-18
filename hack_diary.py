from datacenter.models import Chastisement, Mark, Schoolkid, Commendation, Lesson, Subject, Teacher


def fix_marks(schoolkid_name):
    schoolkid = Schoolkid.objects.filter(full_name__contains=schoolkid_name)
    if len(schoolkid) == 1:
        print('Исправлены оценки 2 и 3:', Mark.objects.filter(schoolkid=schoolkid[0], points__in=[2,3]).update(points=5))
    elif len(schoolkid) == 0:
        print(f'Ученика с именем {schoolkid_name} нет в базе данных.')
    else:
        print(f'Найдено {len(schoolkid)} учеников с именем {schoolkid_name}:', *schoolkid, sep='\n')


def remove_chastisements(schoolkid_name):
    schoolkid = Schoolkid.objects.filter(full_name__contains=schoolkid_name)
    if len(schoolkid) == 1:
        print('Удалены замечания:', Chastisement.objects.filter(schoolkid=schoolkid[0]).delete())
    elif len(schoolkid) == 0:
        print(f'Ученика с именем {schoolkid_name} нет в базе данных.')
    else:
        print(f'Найдено {len(schoolkid)} учеников с именем {schoolkid_name}:', *schoolkid, sep='\n')


def create_commendation(schoolkid_name, subject_title, teacher_name, date):
    schoolkid = Schoolkid.objects.filter(full_name__contains=schoolkid_name)
    subject = Subject.objects.filter(title__contains=subject_title, year_of_study=schoolkid.year_of_study)
    teacher = Teacher.objects.filter(full_name__contains=teacher_name)
    lesson = Lesson.objects.filter(date=date, subject=subject, year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter)
    if len(schoolkid) == 1 and len(subject) == 1 and len(teacher) == 1 and len(lesson) == 1:
        Commendation.objects.create(text='Хвалю!', created=date, schoolkid=schoolkid, subject=subject, teacher=teacher)
        print(f"Добавлена похвала ученику {schoolkid.full_name} по предмету {subject.title}, дата: {date}, учитель {teacher.full_name}")
    elif len(schoolkid) == 0:
        print(f'Ученика с именем {schoolkid_name} нет в базе данных.')
    elif len(subject) == 0:
        print(f'Предмета {subject_name} нет в базе данных.')
    elif len(teacher) == 0:
        print(f'Учителя с именем {teacher_name} нет в базе данных.')
    elif len(lesson) == 0:
        print(f"По предмету {subject_name} на дату: {date} у ученика {schoolkid_name} не было занятий")
    elif len(schoolkid) > 1:
        print(f'Найдено {len(schoolkid)} учеников с именем {schoolkid_name}:', *schoolkid, sep='\n')
    elif len(subject) > 1:
        print(f'Найдено {len(subject)} предметов с названием {subject_name}:', *subject, sep='\n')
    elif len(teacher) > 1:
        print(f'Найдено {len(teacher)} учителей с именем {teacher_name}:', *teacher_name, sep='\n')

