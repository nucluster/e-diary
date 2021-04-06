# fix_marks
#6551	Фролов Иван Григорьевич	2006-02-26	6	2013	А
from datacenter.models import Chastisement, Mark, Schoolkid

def fix_marks(schoolkid_id):
    return Mark.objects.filter(schoolkid__id=schoolkid_id, points__in=[2,3]).update(points=5)

def remove_chastisements(schoolkid_name):
    return Chastisement.objects.filter(schoolkid__full_name__contains=schoolkid_name).count()