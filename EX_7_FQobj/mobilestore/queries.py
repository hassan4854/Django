from .models import Brand, Mobile
from django.db.models import F, Q


def all_brands_not_in_korea_china():
    query = Brand.objects.filter(~Q(nationality='Korea') & ~Q(nationality='China'))
    return query


def some_brand_mobiles(*brand_names):

    #   1 : my solution
    if brand_names:
        condition = Q(brand__name='nothing')
        for brand in brand_names:
            condition.add(Q(brand__name=brand), Q.OR)
        query = Mobile.objects.filter(condition)
    else:
        query = Mobile.objects.all()
    return query


""""
2
    condition = Q()
    for brand_name in brand_names:
        condition |= Q(brand__name=brand_name)

    return Mobile.objects.filter(condition)
3

    q_object = Q()
    if brand_names:
        q_object = Q(brand__name__in=brand_names)
    return Mobile.objects.filter(q_object)
"""


def mobiles_brand_nation_equals_made_in():
    query = Mobile.objects.filter(brand__nationality=F('made_in'))
    return query
