import csv

from datetime import datetime

from app.models import App, AppTypeDetails
from website.models import Category, Label, Type, Website

app_names = list(set(App.objects.filter(website_id=1).values_list('name', flat=True)))
"""
len(app_names)
417
"""
app_names_with_duplicate_data = []
app_ids = []  # app data with the same name
for app_name in app_names:
    if App.objects.filter(name=app_name, website_id=1).count() > 1:
        print(app_name)
        app_names_with_duplicate_data.append(app_name)
        app_ids.extend(list(App.objects.filter(name=app_name, website_id=1).values_list('id', flat=True)))
"""
len(app_names_with_duplicate_data)
79
len(app_ids)
228
[3009, 1340, 3534, 1815, 3519, 1800, 2799, 2659, 2544, 2469, 900, 2744, 2604, 2509, 845, 3584, 1865, 3569, 1850, 3029, 1400, 3589, 1870, 2824, 2684, 2554, 925, 2944, 1270, 3554, 1840, 2759, 2619, 860, 2934, 1265, 2809, 2674, 910, 3019, 1355, 3539, 1820, 2814, 2669, 915, 2789, 2649, 2534, 890, 3034, 1395, 2784, 2644, 2529, 885, 3524, 1805, 2994, 2909, 1325, 2984, 1315, 2989, 2904, 1320, 3644, 3479, 3384, 2375, 3024, 1345, 3559, 1835, 3064, 1365, 2939, 2874, 1275, 2839, 2699, 940, 3514, 1795, 2739, 2599, 2504, 840, 3574, 1855, 2979, 2899, 1310, 3674, 3579, 3494, 3414, 1860, 2819, 2679, 2549, 920, 3529, 1810, 2764, 2624, 865, 3049, 2919, 1380, 2794, 2654, 2539, 895, 3039, 1390, 2754, 2609, 2514, 850, 2844, 2704, 2569, 945, 3544, 1825, 2829, 2689, 2559, 2479, 930, 2959, 2884, 1290, 2859, 2724, 2584, 960, 2734, 2594, 835, 2484, 10, 2779, 2639, 880, 2774, 2634, 875, 2869, 2729, 830, 2999, 2914, 1335, 2854, 2714, 2579, 2474, 955, 3564, 1845, 2969, 1295, 3074, 2929, 1260, 3014, 1350, 2769, 2629, 2524, 870, 3054, 2924, 1375, 3079, 3059, 1370, 2964, 2894, 1300, 2974, 1305, 3004, 1330, 2864, 2719, 2589, 2459, 965, 2464, 975, 2949, 2879, 1280, 2489, 135, 2954, 2889, 1285, 3654, 3474, 3379, 2365, 2849, 2709, 2574, 950, 2494, 270, 2749, 2614, 2519, 855, 3044, 1385, 2834, 2694, 2564, 935, 3069, 1360, 3549, 1830, 2804, 2664, 905]
"""

fields = ['id', 'app_file', 'ios_file', 'name', 'code', 'slug', 'website', 'app_type', 'category', 'icon', 'release_at', 'version', 'star', 'download_link', 'size_mb', 'basic_introduction', 'introduction', 'features', 'created_at', 'created_by', 'updated_at', 'updated_by', 'keywords', 'editors_comment', 'rank', 'recommended_rank', 'is_rank', 'is_recommended', 'is_active', 'ios_download_link', 'use_android_link', 'types', 'categories', 'labels']

fieldnames = ['id', 'app_file_id', 'ios_file_id', 'name', 'code', 'slug', 'website_id', 'app_type_id', 'category_id', 'icon', 'release_at', 'version', 'star', 'download_link', 'size_mb', 'basic_introduction', 'introduction', 'features', 'created_at', 'created_by_id', 'updated_at', 'updated_by_id', 'keywords', 'editors_comment', 'rank', 'recommended_rank', 'is_rank', 'is_recommended', 'is_active', 'ios_download_link', 'use_android_link', 'types', 'categories', 'labels']

apps = App.objects.filter(id__in=app_ids).order_by('name').only(*fields).values()
for app in apps:
    print(app)

today = datetime.now()
with open(f'apps-{today:%Y%m%d-%H%M%S}.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for app in apps:
        app_obj = App.objects.get(id=app['id'])
        if app_obj.types.exists():
            app_types = list(app_obj.types.all().order_by('id').values_list('id', flat=True))
            app['types'] = app_types
        if app_obj.categories.exists():
            categories = list(app_obj.categories.all().order_by('id').values_list('id', flat=True))
            app['categories'] = categories
        if app_obj.labels.exists():
            labels = list(app_obj.labels.all().order_by('id').values_list('id', flat=True))
            app['labels'] = labels
        writer.writerow(app)

for app_name in app_names[:5]:
    apps = App.objects.filter(website_id=1, name=app_name)
    app_ids = []
    type_ids = []
    category_ids = []
    label_ids = []
    for app in apps:
        app_ids.append(app.id)
        if app.types.exists():
            type_ids.extend(list(app.types.all().values_list('id', flat=True)))
        if app.categories.exists():
            category_ids.extend(list(app.categories.all().values_list('id', flat=True)))
        if app.labels.exists():
            label_ids.extend(list(app.labels.all().values_list('id', flat=True)))
    type_ids = list(set(type_ids))
    category_ids = list(set(category_ids))
    label_ids = list(set(label_ids))
    max_id = max(app_ids)
    app_ids.remove(max_id)
    print('TO DELETE')
    for delete_app in App.objects.filter(id__in=app_ids):
        print(delete_app)
        print(delete_app.types.all().values_list('id', flat=True))
        print(delete_app.categories.all().values_list('id', flat=True))
        print(delete_app.labels.all().values_list('id', flat=True))
    print('')
    print('TO UPDATE:')
    update_app = App.objects.get(id=max_id)
    print(update_app)
    print(update_app.types.all().values_list('id', flat=True))
    print(update_app.categories.all().values_list('id', flat=True))
    print(update_app.labels.all().values_list('id', flat=True))
    print('NEW VALUE')
    print(type_ids)
    print(category_ids)
    print(label_ids)

for app_name in app_names_with_duplicate_data[1:2]:
    print(app_name)
    apps = App.objects.filter(website_id=1, name=app_name)
    app_ids = []
    type_ids = []
    category_ids = []
    label_ids = []
    for app in apps:
        app_ids.append(app.id)
        if app.types.exists():
            type_ids.extend(list(app.types.all().values_list('id', flat=True)))
        if app.categories.exists():
            category_ids.extend(list(app.categories.all().values_list('name', flat=True)))
        if app.labels.exists():
            label_ids.extend(list(app.labels.all().values_list('name', flat=True)))
    # categories = Category.objects.filter(id__in=list(set(category_ids)))
    # labels = Label.objects.filter(id__in=list(set(label_ids)))
    types = Type.objects.filter(id__in=list(set(type_ids)), website_id=1)
    max_id = apps.latest('updated_at').id
    app_ids.remove(max_id)
    update_app = App.objects.get(id=max_id)
    update_app.types.clear()
    update_app.types.set(types)
    update_app.categories.clear()
    print(set(category_ids))
    for category_name in set(category_ids):
        for app_type in types:
            if Category.objects.filter(types=app_type, name=category_name).exists():
                category = Category.objects.filter(types=app_type, name=category_name).latest('updated_at', 'pk')
                update_app.categories.add(category)
    update_app.labels.clear()
    print(set(label_ids))
    for label_name in set(label_ids):
        for app_type in types:
            if Label.objects.filter(types=app_type, name=label_name).exists():
                label = Label.objects.filter(types=app_type, name=label_name).latest('updated_at', 'pk')
                if not update_app.labels.filter(name=label).exists():
                    update_app.labels.add(label)
    print(update_app)
    delete_apps = App.objects.filter(id__in=app_ids)
    for a in delete_apps:
        print(a)
        if a.types.exists():
            for apptype in a.types.all():
                apptype_details, created = AppTypeDetails.objects.get_or_create(app=update_app, app_type=apptype)
                if created:
                    try:
                        delete_app_apptype_details = AppTypeDetails.objects.get(app=a, app_type=apptype)
                        apptype_details.is_active = delete_app_apptype_details.is_active
                        apptype_details.is_rank = delete_app_apptype_details.is_rank
                        apptype_details.is_recommended = delete_app_apptype_details.is_recommended
                        apptype_details.rank = delete_app_apptype_details.rank
                        apptype_details.recommended_rank = delete_app_apptype_details.recommended_rank
                        apptype_details.save()
                    except Exception as exc:
                        print(f'No app type details: {a.id} -- {apptype.id} ({exc})')
    #     AppTypeDetails.objects.filter(app=a).delete()
    # delete_apps.delete()


label_names = list(set(Label.objects.filter(types__website_id=1).distinct().values_list('name', flat=True)))
label_names_with_duplicate_data = []
label_ids = []  # app data with the same name
for label_name in label_names:
    if Label.objects.filter(name=label_name, types__website_id=1).distinct().count() > 1:
        print(label_name)
        label_names_with_duplicate_data.append(label_name)
        label_ids.extend(list(Label.objects.filter(name=label_name, types__website_id=1).distinct().values_list('id', flat=True)))

for label_name in label_names_with_duplicate_data:
    if not label_name == '阅读':
        continue
    print(label_name)
    labels = Label.objects.filter(types__website_id=1, name=label_name).distinct()
    latest_label = labels.latest('updated_at')
    print(labels.count())
    print(f'LATEST: {latest_label.id} APPS: {App.objects.filter(labels__id=latest_label.id).count()}')
    print(labels)
    for label in labels.exclude(id=latest_label.id):
        print(label.id, label.name)
        print(f'APPS COUNT WITH THIS LABEL: {label.website_applabels.count()}')
        counter_exists = 0
        counter_not_exists = 0
        for label_app in label.website_applabels.all():
            if label_app.labels.filter(id=latest_label.id).exists():
                counter_exists += 1
            else:
                counter_not_exists += 1
        print(f'APPS ALREADY HAVE LATEST LABEL: {label.website_applabels.filter(labels__id=latest_label.id).count()}')
    print('')

"""
阅读
2
LATEST: 349 APPS: 13
2014 阅读
APPS COUNT WITH THIS LABEL: 16
APPS ALREADY HAVE LATEST LABEL: 2
APPS NOT HAVE  LABEL: 14

阅读
2
LATEST: 349 APPS: 13
2014 阅读
APPS COUNT WITH THIS LABEL: 16
APPS ALREADY HAVE LATEST LABEL: 0
"""

website_1 = Website.objects.get(id=1)
types = Type.objects.filter(website=website_1)
labels = Label.objects.filter(types__in=types).distinct()
"""
labels.count()
453
"""
for label in labels:
    if label.types.exists():
        for app_type in label.types.all():
            if not app_type.website == website_1:
                print(label, label.name)
"""
None
"""
label_names = list(set(labels.values_list('name', flat=True)))
"""
print(len(label_names))
357
"""
for label_name in label_names:
    if not label_names.count(label_name) == 1:
        print(label_name)

duplicate_label_names_with_same_name = []  # len(duplicate_label_names_with_same_name)  90
duplicate_labels_with_same_name = []
for label_name in label_names:
    check_duplicate_labels = labels.filter(name=label_name).distinct()
    if check_duplicate_labels.count() > 1:
        duplicate_label_names_with_same_name.append(label_name)
        # print('TO UPDATE')
        # updated_label = check_duplicate_labels.latest('updated_at')
        # print(updated_label)
        # duplicate_labels = check_duplicate_labels.exclude(pk=updated_label.pk)
        # print('TO DELETE')
        # for duplicate_label in duplicate_labels:
        #     print(duplicate_label)
        # print('')

# MERGE TYPES OF UPDATED LABEL WITH OTHER LABELS WITH SAME NAME BUT DIFFERENT TYPES
for duplicate_label_name in duplicate_label_names_with_same_name:
    check_duplicate_labels = labels.filter(name=duplicate_label_name).distinct()
    if check_duplicate_labels.count() > 1:
        # print('TO UPDATE')
        updated_label = check_duplicate_labels.latest('updated_at')
        # print(updated_label, updated_label.types.all())
        updated_label_types = updated_label.types.all()
        duplicate_labels = check_duplicate_labels.exclude(pk=updated_label.pk)
        # print('TO DELETE')
        for duplicate_label in duplicate_labels:
            print('TO DELETE: ', duplicate_label, duplicate_label.types.all(), App.objects.filter(labels=duplicate_label).count())
            duplicate_label_types = duplicate_label.types.exclude(pk__in=list(updated_label_types.values_list('pk', flat=True)))
            # if duplicate_label_types.exists():
                # print('TYPES TO ADD IN UPDATED LABEL')
                # for duplicate_label_type in duplicate_label_types:
                    # print(duplicate_label_type)
                    # updated_label.types.add(duplicate_label_type)
        duplicate_labels.delete()  # TO DELETE LABEL DATA
        print('')

# CHANGE APPS LABEL TO UPDATED LABEL
apps = App.objects.filter(website_id=1)
"""
apps.count()
565
"""
for app in apps[5:]:
    print(app)
    if app.labels.exists():
        app_labels = app.labels.filter(name__in=duplicate_label_names_with_same_name)
        for app_label in app_labels:
            print(f'SET LABEL: {app_label} -- {app_label.types.all()}')
            labels_with_same_name = labels.filter(name=app_label.name)
            if labels_with_same_name.exists():
                print(labels_with_same_name)
                latest_label_with_same_name = labels_with_same_name.latest('updated_at')
                for l in labels_with_same_name:
                    print(l, l.types.all())
                if latest_label_with_same_name == app_label:
                    continue
                print(f'CHANGE TO {latest_label_with_same_name}')
                app.labels.remove(app_label)
                app.labels.add(latest_label_with_same_name)
    print('')
