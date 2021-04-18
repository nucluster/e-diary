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
    teacher = Teacher.objects.filter(full_name__contains=teacher_name)
    if len(schoolkid) == 1:
        subject = Subject.objects.filter(title__contains=subject_title, year_of_study=schoolkid[0].year_of_study)
        if len(subject) == 1:
            lesson = Lesson.objects.filter(date=date, subject=subject[0], year_of_study=schoolkid[0].year_of_study, group_letter=schoolkid[0].group_letter)
    if len(teacher) == 1 and len(lesson) == 1:
        print(Commendation.objects.create(text='Хвалю!', created=date, schoolkid=schoolkid[0], subject=subject[0], teacher=teacher[0]))
    elif len(schoolkid) == 0:
        print(f'Ученика с именем {schoolkid_name} нет в базе данных.')
    elif len(subject) == 0:
        print(f'Предмета {subject_title} нет в базе данных или у данного ученика.')
    elif len(teacher) == 0:
        print(f'Учителя с именем {teacher_name} нет в базе данных.')
    elif len(lesson) == 0:
        print(f"По предмету {subject_title} на дату: {date} у ученика {schoolkid_name} не было занятий")
    elif len(schoolkid) > 1:
        print(f'Найдено {len(schoolkid)} учеников с именем {schoolkid_name}:', *schoolkid, sep='\n')
    elif len(subject) > 1:
        print(f'Найдено {len(subject)} предметов с названием {subject_title}:', *subject, sep='\n')
    elif len(teacher) > 1:
        print(f'Найдено {len(teacher)} учителей с именем {teacher_name}:', *teacher_name, sep='\n')

