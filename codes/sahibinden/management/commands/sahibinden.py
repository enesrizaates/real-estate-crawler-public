from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import json
from utils import cookies
import shutil
import csv
from sahibinden.models import Property, Post, Detail, Picture
import re
from django.utils import timezone

def url_generator(url):
    response = requests.get(
        url, headers=cookies.headers, cookies=cookies.cookies
    )

    html = response.text
    soup = bs(html, 'lxml')
    links = []
    for link in soup.find_all('a'):
        val = link.get('href')
        if val and val.startswith('/ilan/'):
            links.append(val)
    ann_urls = []
    for link in links:
        ann_url = 'https://www.sahibinden.com' + link
        ann_urls.append(ann_url)
    ann_urls = list(dict.fromkeys(ann_urls))
    return ann_urls


def soup_generator(ann_url):
    response = requests.get(
        ann_url, headers=cookies.headers,
        cookies=cookies.cookies
    )
    html = response.text
    soup = bs(html, 'lxml')
    return soup


def main(soup):
    ann_main = soup.find_all(
        'script', attrs={'id': 'gaPageViewTrackingData'}
    )

    main_text = ann_main[0].text
    main_text = main_text.replace(
        'var pageTrackData = ', ''
    ).replace('\n', '').replace(';', '')

    main_json = json.loads(main_text)
    vals = dict()
    for data in main_json['dmpData']:
        try:
            if data.get('name') and data.get('value'):
                vals[data['name']] = data['value']
        except Exception:
            pass

    for data in main_json['customVars']:
        try:
            if data.get('name') and data.get('value'):
                vals[data['name']] = data['value']
        except Exception:
            pass
    name = soup.find(
        'div', attrs={'class':'classifiedDetailTitle'}
    ).text.split('\n')[1]
    vals.update({'name':name}) 
    return vals


def get_properties(soup):
    properties = soup.find_all(
        'div', attrs={'id': 'classifiedProperties'}
    )
    if properties:
        prop = properties[0]
    properties_all = []
    properties_selected = []
    for i in soup.find_all('li', attrs={'class': 'selected'}):
        properties_selected.append(i.text.replace('\n', '').strip())
    for k in prop.find_all('li'):
        properties_all.append(k.text.replace('\n', '').strip())
    properties_all.append('ilan_no')
    main_json = json.loads(
        soup.find_all(
            'script', attrs={'id': 'gaPageViewTrackingData'}
        )[0].text.replace(
            'var pageTrackData = ', ''
        ).replace('\n', '').replace(';', '')
    )

    ilan_no = [
        s['value'] for s in main_json['customVars'] if s['name'] == 'İlan No'
    ]
    properties_all = list(set(properties_all))
    properties_selected = list(set(properties_selected))
    properties_all.sort()
    properties_selected.sort()
    lookup = [
        x for x, y in enumerate(
            properties_all
        ) if y in properties_selected
    ]
    l1 = [False for i in properties_all]
    for i in lookup:
        l1[i] = True
    zipped = zip(properties_all, l1)
    vals = {item[0]: item[1] for item in zipped}
    vals.update({'ilan_no': ilan_no[0]})
    return vals


def get_details(soup):
    description = soup.find(
        'div', attrs={'id': 'classifiedDescription'}
    )
    map_soup = soup.find('a', attrs={'class':'noprevent'})
    map_link = map_soup['href']
    lat_lon = soup.find('div', attrs={'id': 'gmap'})
    ilan_no = [
        x['value'] for x in json.loads(
            soup.find_all(
                'script', attrs={'id':'gaPageViewTrackingData'}
            )[0].text.replace(
                'var pageTrackData = ', ''
            ).replace('\n', '').replace(';', '')
        )['customVars'] if x['name'] == 'İlan No'
    ][0]
    ls_details = {
        'ilan_no':ilan_no,
        'description': description.text,
        'link': map_link,
        'lat': float(lat_lon['data-lat']),
        'lon': float(lat_lon['data-lon'])
    }
    return ls_details


def get_img_url(soup):
    images = soup.find_all('img')
    ls_images = []
    for image in images:
        try:
            img = image.get('data-src')
            if '.jpg' and 'x5' in img:
                ls_images.append(img)
        except Exception:
            pass
    return ls_images


def download_image(url, directory='./pictures'):
    response = requests.get(
        url, cookies=cookies.cookies,
        headers=cookies.headers, stream=True
                    )
    image_name = url.split('/')[-1]
    image_path = '{}/{}'.format(directory, image_name)

    with open(image_path, 'wb') as out_file:
        # response.raw.decode_content = True
        shutil.copyfileobj(response.raw, out_file)
    del response

    return image_path


class Command(BaseCommand):
    help = 'Closes the specified poll for voiting'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        main_url = 'https://www.sahibinden.com/satilik'
        ann_urls = url_generator(main_url)
        df_main = pd.DataFrame()
        ls_main = []
        ls_properties = []
        ls_details = []
        ls_images = []
        x = 0
        for i in ann_urls:
            soup = soup_generator(i)
            ls_main.append(main(soup))
            ls_properties.append(get_properties(soup))
            ls_details.append(get_details(soup))
            ls_images.append(get_img_url(soup))
            for url in get_img_url(soup):
                download_image(url)
            x += 1
            if x >= 3:
                break
        ls_jpgs = []
        ls_jpgs = [
            [
                'home/enes/Project/Python/sahibinden/pictures/'+i.split('/')[-1] for i in k
            ] for k in ls_images
        ]
      

        for (row_m, row, row_d, local_p, web_p) in zip(ls_main, ls_properties, ls_details, ls_jpgs, ls_images):
            post = Post.objects.filter(ilan_no=row_m['İlan No']).first()
            if not post:
                post = Post()
            post.name = row_m['name']
            post.cat1 = row_m['cat1']
            post.cat2 = row_m['cat2']
            post.cat3 = row_m['cat3']
            post.cat4 = row_m['cat4']
            post.cat0 = row_m['cat0']
            post.country = row_m['loc1']
            post.city = row_m['loc2']
            post.region = row_m['loc3']
            post.district = row_m['loc4']
            post.street = row_m['loc5']
            post.m2_brut = row_m['m2_brut']
            post.m2_net = row_m['m2_net']
            post.oda_sayisi = row_m['oda_sayisi']
            post.bina_yasi = row_m['bina_yasi']
            post.bulundugu_kat = row_m.get('bulundugu_kat', '')
            post.kat_sayisi = row_m['kat_sayisi']
            post.isitma = row_m['isitma']
            post.banyo_sayisi = row_m['banyo_sayisi']
            post.balkon = row_m['balkon']
            post.esyali = row_m['esyali']
            post.kullanim_durumu = row_m['kullanim_durumu']
            post.site_icerisinde = row_m['site_icerisinde']
            post.site_adi = row_m['site_adi']
            post.krediye_uygun = row_m['krediye_uygun']
            post.kimden = row_m['kimden']
            post.fiyat = row_m['fiyat']
            post.ilan_aks = row_m['ilan_aks']
            post.ilan_fiyat = row_m['ilan_fiyat']
            post.ilan_no = row_m['İlan No']
            post.ilan_Tarihi = row_m['İlan Tarihi']
            post.Emlak_Tipi = row_m['Emlak Tipi']
            post.area_brut = row_m['m² (Brüt)']
            post.area_net = row_m['m² (Net)']
            post.oda_sayisi = row_m['Oda Sayısı']
            post.bina_yasi = row_m['Bina Yaşı']
            post.floor = row_m.get('Bulunduğu Kat', '')
            post.total_floor = row_m['Kat Sayısı']
            post.isitma = row_m['Isıtma']
            post.banyo_sayisi = row_m['Banyo Sayısı']
            post.balkon = row_m['Balkon']
            post.esyali = row_m['Eşyalı']
            post.kullanim_durumu = row_m['Kullanım Durumu']
            post.site_icerisinde = row_m['Site İçerisinde']
            post.aidat = row_m['Aidat (TL)']
            post.site_adi = row_m['Site Adı']
            post.krediye_uygun = row_m['Krediye Uygun']
            post.kimden = row_m['Kimden']
            post.takas = row_m['Takas']
            post.gecici_numara_servisi = row_m['Geçici Numara Servisi']
            post.site_preference = row_m['site_preference']
            post.record_date_time = timezone.now()
            post.save()


            properties = Property.objects.filter(ilan_no =
                                                   row['ilan_no']).first()
            if not properties:
                properties = Property()

            properties.post = post
            properties.adsl = row['ADSL']
            properties.ahsap_dograma = row['Ahşap Doğrama']
            properties.akilli_ev = row['Akıllı Ev']
            properties.alarm_hirsiz = row['Alarm (Hırsız)']
            properties.alarm_yangin = row['Alarm (Yangın)']
            properties.alaturka_tuvalet = row['Alaturka Tuvalet']
            properties.aluminyum_dograma = row['Alüminyum Doğrama']
            properties.alisveris_merkezi = row['Alışveriş Merkezi']
            properties.amerikan_kapi = row['Amerikan Kapı']
            properties.amerikan_mutfak = row['Amerikan Mutfak']
            properties.anayol = row['Anayol']
            properties.ankastre_firin = row['Ankastre Fırın']
            properties.ara_kat = row['Ara Kat']
            properties.ara_kat_dubleks = row['Ara Kat Dubleks']
            properties.arac_park_yeri = row['Araç Park Yeri']
            properties.asansor = row['Asansör']
            properties.avrasya_tuneli = row['Avrasya Tüneli']
            properties.bahce_dubleksi = row['Bahçe Dubleksi']
            properties.bahce_kati = row['Bahçe Katı']
            properties.bahceli = row['Bahçeli']
            properties.balkon = row['Balkon']
            properties.banyo = row['Banyo']
            properties.barbeku = row['Barbekü']
            properties.bati = row['Batı']
            properties.belediye = row['Belediye']
            properties.beyaz_esya = row['Beyaz Eşya']
            properties.boyali = row['Boyalı']
            properties.bogaz = row['Boğaz']
            properties.bogaz_kopruleri = row['Boğaz Köprüleri']
            properties.buhar_odasi = row['Buhar Odası']
            properties.bulasik_makinesi = row['Bulaşık Makinesi']
            properties.buzdolabi = row['Buzdolabı']
            properties.cadde = row['Cadde']
            properties.cami = row['Cami']
            properties.cemevi = row['Cemevi']
            properties.deniz = row['Deniz']
            properties.deniz_otobusu = row['Deniz Otobüsü']
            properties.denize_sifir = row['Denize Sıfır']
            properties.dolmus = row['Dolmuş']
            properties.doga = row['Doğa']
            properties.dogu = row['Doğu']
            properties.duvar_kagidi = row['Duvar Kağıdı']
            properties.dusakabin = row['Duşakabin']
            properties.e_5 = row['E-5']
            properties.ebeveyn_banyosu = row['Ebeveyn Banyosu']
            properties.eczane = row['Eczane']
            properties.en_ust_kat = row['En Üst Kat']
            properties.eglence_merkezi = row['Eğlence Merkezi']
            properties.fiber_internet = row['Fiber İnternet']
            properties.fuar = row['Fuar']
            properties.firin = row['Fırın']
            properties.garaj_dukkan_ustu = row['Garaj / Dükkan Üstü']
            properties.genis_koridor = row['Geniş Koridor']
            properties.giris_rampa = row['Giriş / Rampa']
            properties.giris_kati = row['Giriş Katı']
            properties.giyinme_odasi = row['Giyinme Odası']
            properties.gol = row['Göl']
            properties.gomme_dolap = row['Gömme Dolap']
            properties.goruntulu_diafon = row['Görüntülü Diafon']
            properties.guney = row['Güney']
            properties.guvenlik = row['Güvenlik']
            properties.hamam = row['Hamam']
            properties.hastane = row['Hastane']
            properties.havaalani = row['Havaalanı']
            properties.havra = row['Havra']
            properties.havuz = row['Havuz']
            properties.hidrofor = row['Hidrofor']
            properties.hilton_banyo = row['Hilton Banyo']
            properties.intercom_sistemi = row['Intercom Sistemi']
            properties.isi_yalitim = row['Isı Yalıtım']
            properties.isicam = row['Isıcam']
            properties.jakuzi = row['Jakuzi']
            properties.jenerator = row['Jeneratör']
            properties.kablo_tv = row['Kablo TV']
            properties.kapali_garaj = row['Kapalı Garaj']
            properties.kapici = row['Kapıcı']
            properties.kartonpiyer = row['Kartonpiyer']
            properties.kat_dubleksi = row['Kat Dubleksi']
            properties.kiler = row['Kiler']
            properties.kilise = row['Kilise']
            properties.klima = row['Klima']
            properties.kres = row['Kreş']
            properties.kuzey = row['Kuzey']
            properties.kuvet = row['Küvet']
            properties.laminat_zemin = row['Laminat Zemin']
            properties.lise = row['Lise']
            properties.market = row['Market']
            properties.marley = row['Marley']
            properties.marmaray = row['Marmaray']
            properties.merdiven = row['Merdiven']
            properties.metro = row['Metro']
            properties.metrobus = row['Metrobüs']
            properties.minibus = row['Minibüs']
            properties.mobilya = row['Mobilya']
            properties.mutfak = row['Mutfak']
            properties.mutfak_ankastre = row['Mutfak (Ankastre)']
            properties.mutfak_laminat = row['Mutfak (Laminat)']
            properties.mutfak_dogalgazi = row['Mutfak Doğalgazı']
            properties.mustakil_girisli = row['Müstakil Girişli']
            properties.mustakil_havuzlu = row['Müstakil Havuzlu']
            properties.oda_kapisi = row['Oda Kapısı']
            properties.otobus_duragi = row['Otobüs Durağı']
            properties.otopark = row['Otopark']
            properties.oyun_parki = row['Oyun Parkı']
            properties.pvc_dograma = row['PVC Doğrama']
            properties.panjur = row['Panjur']
            properties.park = row['Park']
            properties.parke_zemin = row['Parke Zemin']
            properties.polis_merkezi = row['Polis Merkezi']
            properties.priz_elektrik_anahtari = row['Priz / Elektrik Anahtarı']
            properties.sahil = row['Sahil']
            properties.sauna = row['Sauna']
            properties.saglik_ocagi = row['Sağlık Ocağı']
            properties.semt_pazari = row['Semt Pazarı']
            properties.seramik_zemin = row['Seramik Zemin']
            properties.ses_yalitimi = row['Ses Yalıtımı']
            properties.set_ustu_ocak = row['Set Üstü Ocak']
            properties.siding = row['Siding']
            properties.spor_alani = row['Spor Alanı']
            properties.spor_salonu = row['Spor Salonu']
            properties.spot_aydinlatma = row['Spot Aydınlatma']
            properties.su_deposu = row['Su Deposu']
            properties.tem = row['TEM']
            properties.teleferik = row['Teleferik']
            properties.tenis_kortu = row['Tenis Kortu']
            properties.teras = row['Teras']
            properties.termosifon = row['Termosifon']
            properties.ters_dubleks = row['Ters Dubleks']
            properties.tramvay = row['Tramvay']
            properties.tren_istasyonu = row['Tren İstasyonu']
            properties.tripleks = row['Tripleks']
            properties.troleybus = row['Troleybüs']
            properties.tutamak_korkuluk = row['Tutamak / Korkuluk']
            properties.tuvalet = row['Tuvalet']
            properties.uydu = row['Uydu']
            properties.vestiyer = row['Vestiyer']
            properties.wi_fi = row['Wi-Fi']
            properties.yangin_merdiveni = row['Yangın Merdiveni']
            properties.yuz_tanima_parmak_izi = row['Yüz Tanıma & Parmak İzi']
            properties.yuzme_havuzu = row['Yüzme Havuzu']
            properties.yuzme_havuzu_acik = row['Yüzme Havuzu (Açık)']
            properties.yuzme_havuzu_kapali = row['Yüzme Havuzu (Kapalı)']
            properties.zemin_kat = row['Zemin Kat']
            properties.ilan_no = row['ilan_no']
            properties.camasir_kurutma_makinesi = row['Çamaşır Kurutma Makinesi']
            properties.camasir_makinesi = row['Çamaşır Makinesi']
            properties.camasir_odasi = row['Çamaşır Odası']
            properties.cati_dubleksi = row['Çatı Dubleksi']
            properties.celik_kapi = row['Çelik Kapı']
            properties.universite = row['Üniversite']
            properties.ilkokul_ortaokul = row['İlkokul-Ortaokul']
            properties.iskele = row['İskele']
            properties.itfaiye = row['İtfaiye']
            properties.sehir = row['Şehir']
            properties.sehir_merkezi = row['Şehir Merkezi']
            properties.sofben = row['Şofben']
            properties.somine = row['Şömine']
        
            details = Detail()
            details.post = post
            details.description = row_d['description']
            details.map_link = row_d['link']
            details.lat = row_d['lat']
            details.lon = row_d['lon']
            for (lp, wp) in zip(local_p, web_p):
                picture = Picture.objects.filter(web_url=wp).first()
                if picture:
                    continue
                picture = Picture()
                picture.post = post
                picture.local_url = lp
                picture.web_url = wp
                picture.save()
         

            properties.save()
            details.save()
