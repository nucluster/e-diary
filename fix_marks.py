# fix_marks

def fix_marks(schoolkid_id):
    return Mark.objects.filter(schoolkid__id=schoolkid_id, points__in=[2,3]).update(points=5)