#6551	Фролов Иван Григорьевич	2006-02-26	6	2013	А

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
    if Lesson.objects.filter(date=date, subject=subject, year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter).count():
        Commendation.objects.create(text='Хвалю!', created=date, schoolkid=schoolkid, subject=subject, teacher=teacher)
        return f"Добавлена похвала ученику {schoolkid.full_name} по предмету {subject.title}, дата: {date}, учитель {teacher.full_name}"
    else:
        return f"По предмету {subject.title} на дату: {date} у ученика {schoolkid.full_name} не было занятий"