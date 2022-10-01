from pytz import timezone
import requests
import time
from datetime import datetime
from django.conf import settings
import os
import django

tz = timezone('Africa/Nairobi')


def date_obj(date_string):
    try:
        ff = date_string[-19:][:15]
        year = ff[:4][2:]
        month = ff[:6][4:]
        day = ff[:8][6:]
        hour = ff[:11][9:]
        minute = ff[:13][11:]
        second = ff[:15][13:]
        time_string = f"{day}/{month}/{year} {hour}:{minute}:{second}"
        date_time_obj = datetime.strptime(time_string, '%d/%m/%y %H:%M:%S')
        normalized_date = tz.localize(date_time_obj).astimezone(tz)
        print(normalized_date)
        return normalized_date
    except Exception as e:
        print(e)
        return None


def fetch():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tafuta.settings")
    django.setup()
    from form34web.models import Region, Pdfpath

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
    total_region = 46229
    count = 999

    for i in range(total_region):
        count += 1
        site_number = str(count)[0]
        print(site_number)
        url_path = f"https://forms.iebc.or.ke/assets/data/totalized_results/sites/{site_number}/{count}_F.json"
        print(count)
        response = requests.get(url_path, headers=headers)
        if response.status_code == 200:
            data = response.json()

            form_34a_path = data[0]["forms"][0]["nl"]

            for path in form_34a_path:
                final_path = path["path"]
                polling_station_code = str(final_path)[18:][0:15]

                # purchase = Order(bought_by=current_user, product=Product.query.filter_by(product_id=form.product_id.data).first())
                try:
                    region = Region(iebc_region=f"{count}_F")
                    instance = Region.objects.filter(iebc_region=f"{count}_F").first()
                    if instance:
                        print("")
                    else:
                        region.save()
                    instance2 = Pdfpath.objects.filter(form_34_path=final_path).first()
                    date_added = date_obj(final_path)
                    path_pdf = Pdfpath(polling_station_code=polling_station_code,
                                       form_34_path=f"https://forms.iebc.or.ke/{final_path}",
                                       date_posted=date_added,
                                       iebc_region=Region.objects.get(iebc_region=f"{count}_F"))
                    if instance2 and date_added is None:
                        print("")
                    else:
                        path_pdf.save()
                except Exception as e:
                    print(e)
        else:
            print("not yet")


def run():
    fetch()
