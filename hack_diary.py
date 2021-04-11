#6551	Фролов Иван Григорьевич	2006-02-26	6	2013	А

from datacenter.models import Chastisement, Mark, Schoolkid, Commendation, Lesson

def fix_marks(schoolkid_id):
    return Mark.objects.filter(schoolkid__id=schoolkid_id, points__in=[2,3]).update(points=5)

def remove_chastisements(schoolkid_name):
    return Chastisement.objects.filter(schoolkid__full_name__contains=schoolkid_name).delete()

def create_commendation(schoolkid_name, subject_title, date):
    if Lesson.objects.filter(date=date, subject__title__contains=subject_title, ):
        Commendation.objects.create(text='Хвалю!', created='2018-10-02', schoolkid__full_name__contains=schoolkid_name, subject__title__contains=subject_title, teacher_id=697)
        return f"Добавлена похвала ученику {schoolkid_name} по предмету {subject_title}, дата: {date}"
    else:
        return f"По предмету {subject_title} на дату: {date} не было занятий"