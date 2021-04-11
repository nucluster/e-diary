#6551	Фролов Иван Григорьевич	2006-02-26	6	2013	А

from datacenter.models import Chastisement, Mark, Schoolkid, Commendation, Lesson, Subject, Teacher

def fix_marks(schoolkid_name):
    schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    return Mark.objects.filter(schoolkid=schoolkid, points__in=[2,3]).update(points=5)

def remove_chastisements(schoolkid_name):
    schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    return Chastisement.objects.filter(schoolkid=schoolkid).delete()

def create_commendation(schoolkid_name, subject_title, date):
    schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    subject = Subject.objects.get(title__contains=subject_title, year_of_study=schoolkid.year_of_study)
    teacher = Teacher.objects.get(id=697)
    if Lesson.objects.filter(date=date, subject=subject, year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter).count():
        Commendation.objects.create(text='Хвалю!', created=date, schoolkid=schoolkid, subject=subject, teacher=teacher)
        return f"Добавлена похвала ученику {schoolkid.full_name} по предмету {subject.title}, дата: {date}, учитель {teacher.full_name}"
    else:
        return f"По предмету {subject.title} на дату: {date} у ученика {schoolkid.full_name} не было занятий"