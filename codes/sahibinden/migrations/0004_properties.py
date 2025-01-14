# Generated by Django 2.2.5 on 2019-10-08 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sahibinden', '0003_post_record_date_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adsl', models.CharField(blank=True, max_length=256, null=True)),
                ('ahsap_dograma', models.CharField(blank=True, max_length=256, null=True)),
                ('akilli_ev', models.CharField(blank=True, max_length=256, null=True)),
                ('alarm_hirsiz', models.CharField(blank=True, max_length=256, null=True)),
                ('alarm_yangin', models.CharField(blank=True, max_length=256, null=True)),
                ('alaturka_tuvalet', models.CharField(blank=True, max_length=256, null=True)),
                ('aluminyum_dograma', models.CharField(blank=True, max_length=256, null=True)),
                ('alisveris_merkezi', models.CharField(blank=True, max_length=256, null=True)),
                ('amerikan_kapi', models.CharField(blank=True, max_length=256, null=True)),
                ('amerikan_mutfak', models.CharField(blank=True, max_length=256, null=True)),
                ('anayol', models.CharField(blank=True, max_length=256, null=True)),
                ('ankastre_firin', models.CharField(blank=True, max_length=256, null=True)),
                ('ara_kat', models.CharField(blank=True, max_length=256, null=True)),
                ('ara_kat_dubleks', models.CharField(blank=True, max_length=256, null=True)),
                ('arac_park_yeri', models.CharField(blank=True, max_length=256, null=True)),
                ('asansor', models.CharField(blank=True, max_length=256, null=True)),
                ('avrasya_tuneli', models.CharField(blank=True, max_length=256, null=True)),
                ('bahce_dubleksi', models.CharField(blank=True, max_length=256, null=True)),
                ('bahce_kati', models.CharField(blank=True, max_length=256, null=True)),
                ('bahceli', models.CharField(blank=True, max_length=256, null=True)),
                ('balkon', models.CharField(blank=True, max_length=256, null=True)),
                ('banyo', models.CharField(blank=True, max_length=256, null=True)),
                ('barbeku', models.CharField(blank=True, max_length=256, null=True)),
                ('bati', models.CharField(blank=True, max_length=256, null=True)),
                ('belediye', models.CharField(blank=True, max_length=256, null=True)),
                ('beyaz_esya', models.CharField(blank=True, max_length=256, null=True)),
                ('boyali', models.CharField(blank=True, max_length=256, null=True)),
                ('bogaz', models.CharField(blank=True, max_length=256, null=True)),
                ('bogaz_kopruleri', models.CharField(blank=True, max_length=256, null=True)),
                ('buhar_odasi', models.CharField(blank=True, max_length=256, null=True)),
                ('bulasik_makinesi', models.CharField(blank=True, max_length=256, null=True)),
                ('buzdolabi', models.CharField(blank=True, max_length=256, null=True)),
                ('cadde', models.CharField(blank=True, max_length=256, null=True)),
                ('cami', models.CharField(blank=True, max_length=256, null=True)),
                ('cemevi', models.CharField(blank=True, max_length=256, null=True)),
                ('deniz', models.CharField(blank=True, max_length=256, null=True)),
                ('deniz_otobusu', models.CharField(blank=True, max_length=256, null=True)),
                ('denize_sifir', models.CharField(blank=True, max_length=256, null=True)),
                ('dolmus', models.CharField(blank=True, max_length=256, null=True)),
                ('doga', models.CharField(blank=True, max_length=256, null=True)),
                ('dogu', models.CharField(blank=True, max_length=256, null=True)),
                ('duvar_kagidi', models.CharField(blank=True, max_length=256, null=True)),
                ('dusakabin', models.CharField(blank=True, max_length=256, null=True)),
                ('e_5', models.CharField(blank=True, max_length=256, null=True)),
                ('ebeveyn_banyosu', models.CharField(blank=True, max_length=256, null=True)),
                ('eczane', models.CharField(blank=True, max_length=256, null=True)),
                ('en_ust_kat', models.CharField(blank=True, max_length=256, null=True)),
                ('eglence_merkezi', models.CharField(blank=True, max_length=256, null=True)),
                ('fiber_internet', models.CharField(blank=True, max_length=256, null=True)),
                ('fuar', models.CharField(blank=True, max_length=256, null=True)),
                ('firin', models.CharField(blank=True, max_length=256, null=True)),
                ('garaj_dukkan_ustu', models.CharField(blank=True, max_length=256, null=True)),
                ('genis_koridor', models.CharField(blank=True, max_length=256, null=True)),
                ('giris_rampa', models.CharField(blank=True, max_length=256, null=True)),
                ('giris_kati', models.CharField(blank=True, max_length=256, null=True)),
                ('giyinme_odasi', models.CharField(blank=True, max_length=256, null=True)),
                ('gol', models.CharField(blank=True, max_length=256, null=True)),
                ('gomme_dolap', models.CharField(blank=True, max_length=256, null=True)),
                ('goruntulu_diafon', models.CharField(blank=True, max_length=256, null=True)),
                ('guney', models.CharField(blank=True, max_length=256, null=True)),
                ('guvenlik', models.CharField(blank=True, max_length=256, null=True)),
                ('hamam', models.CharField(blank=True, max_length=256, null=True)),
                ('hastane', models.CharField(blank=True, max_length=256, null=True)),
                ('havaalani', models.CharField(blank=True, max_length=256, null=True)),
                ('havra', models.CharField(blank=True, max_length=256, null=True)),
                ('havuz', models.CharField(blank=True, max_length=256, null=True)),
                ('hidrofor', models.CharField(blank=True, max_length=256, null=True)),
                ('hilton_banyo', models.CharField(blank=True, max_length=256, null=True)),
                ('intercom_sistemi', models.CharField(blank=True, max_length=256, null=True)),
                ('isi_yalitim', models.CharField(blank=True, max_length=256, null=True)),
                ('isicam', models.CharField(blank=True, max_length=256, null=True)),
                ('jakuzi', models.CharField(blank=True, max_length=256, null=True)),
                ('jenerator', models.CharField(blank=True, max_length=256, null=True)),
                ('kablo_tv', models.CharField(blank=True, max_length=256, null=True)),
                ('kapali_garaj', models.CharField(blank=True, max_length=256, null=True)),
                ('kapici', models.CharField(blank=True, max_length=256, null=True)),
                ('kartonpiyer', models.CharField(blank=True, max_length=256, null=True)),
                ('kat_dubleksi', models.CharField(blank=True, max_length=256, null=True)),
                ('kiler', models.CharField(blank=True, max_length=256, null=True)),
                ('kilise', models.CharField(blank=True, max_length=256, null=True)),
                ('klima', models.CharField(blank=True, max_length=256, null=True)),
                ('kres', models.CharField(blank=True, max_length=256, null=True)),
                ('kuzey', models.CharField(blank=True, max_length=256, null=True)),
                ('kuvet', models.CharField(blank=True, max_length=256, null=True)),
                ('laminat_zemin', models.CharField(blank=True, max_length=256, null=True)),
                ('lise', models.CharField(blank=True, max_length=256, null=True)),
                ('market', models.CharField(blank=True, max_length=256, null=True)),
                ('marley', models.CharField(blank=True, max_length=256, null=True)),
                ('marmaray', models.CharField(blank=True, max_length=256, null=True)),
                ('merdiven', models.CharField(blank=True, max_length=256, null=True)),
                ('metro', models.CharField(blank=True, max_length=256, null=True)),
                ('metrobus', models.CharField(blank=True, max_length=256, null=True)),
                ('minibus', models.CharField(blank=True, max_length=256, null=True)),
                ('mobilya', models.CharField(blank=True, max_length=256, null=True)),
                ('mutfak', models.CharField(blank=True, max_length=256, null=True)),
                ('mutfak_ankastre', models.CharField(blank=True, max_length=256, null=True)),
                ('mutfak_laminat', models.CharField(blank=True, max_length=256, null=True)),
                ('mutfak_dogalgazi', models.CharField(blank=True, max_length=256, null=True)),
                ('mustakil_girisli', models.CharField(blank=True, max_length=256, null=True)),
                ('mustakil_havuzlu', models.CharField(blank=True, max_length=256, null=True)),
                ('oda_kapisi', models.CharField(blank=True, max_length=256, null=True)),
                ('otobus_duragi', models.CharField(blank=True, max_length=256, null=True)),
                ('otopark', models.CharField(blank=True, max_length=256, null=True)),
                ('oyun_parki', models.CharField(blank=True, max_length=256, null=True)),
                ('pvc_dograma', models.CharField(blank=True, max_length=256, null=True)),
                ('panjur', models.CharField(blank=True, max_length=256, null=True)),
                ('park', models.CharField(blank=True, max_length=256, null=True)),
                ('parke_zemin', models.CharField(blank=True, max_length=256, null=True)),
                ('polis_merkezi', models.CharField(blank=True, max_length=256, null=True)),
                ('priz_elektrik_anahtari', models.CharField(blank=True, max_length=256, null=True)),
                ('sahil', models.CharField(blank=True, max_length=256, null=True)),
                ('sauna', models.CharField(blank=True, max_length=256, null=True)),
                ('saglik_ocagi', models.CharField(blank=True, max_length=256, null=True)),
                ('semt_pazari', models.CharField(blank=True, max_length=256, null=True)),
                ('seramik_zemin', models.CharField(blank=True, max_length=256, null=True)),
                ('ses_yalitimi', models.CharField(blank=True, max_length=256, null=True)),
                ('set_ustu_ocak', models.CharField(blank=True, max_length=256, null=True)),
                ('siding', models.CharField(blank=True, max_length=256, null=True)),
                ('spor_alani', models.CharField(blank=True, max_length=256, null=True)),
                ('spor_salonu', models.CharField(blank=True, max_length=256, null=True)),
                ('spot_aydinlatma', models.CharField(blank=True, max_length=256, null=True)),
                ('su_deposu', models.CharField(blank=True, max_length=256, null=True)),
                ('tem', models.CharField(blank=True, max_length=256, null=True)),
                ('teleferik', models.CharField(blank=True, max_length=256, null=True)),
                ('tenis_kortu', models.CharField(blank=True, max_length=256, null=True)),
                ('teras', models.CharField(blank=True, max_length=256, null=True)),
                ('termosifon', models.CharField(blank=True, max_length=256, null=True)),
                ('ters_dubleks', models.CharField(blank=True, max_length=256, null=True)),
                ('tramvay', models.CharField(blank=True, max_length=256, null=True)),
                ('tren_istasyonu', models.CharField(blank=True, max_length=256, null=True)),
                ('tripleks', models.CharField(blank=True, max_length=256, null=True)),
                ('troleybus', models.CharField(blank=True, max_length=256, null=True)),
                ('tutamak_korkuluk', models.CharField(blank=True, max_length=256, null=True)),
                ('tuvalet', models.CharField(blank=True, max_length=256, null=True)),
                ('uydu', models.CharField(blank=True, max_length=256, null=True)),
                ('vestiyer', models.CharField(blank=True, max_length=256, null=True)),
                ('wi_fi', models.CharField(blank=True, max_length=256, null=True)),
                ('yangin_merdiveni', models.CharField(blank=True, max_length=256, null=True)),
                ('yuz_tanima_parmak_izi', models.CharField(blank=True, max_length=256, null=True)),
                ('yuzme_havuzu', models.CharField(blank=True, max_length=256, null=True)),
                ('yuzme_havuzu_acik', models.CharField(blank=True, max_length=256, null=True)),
                ('yuzme_havuzu_kapali', models.CharField(blank=True, max_length=256, null=True)),
                ('zemin_kat', models.CharField(blank=True, max_length=256, null=True)),
                ('ilan_no', models.CharField(blank=True, max_length=256, null=True, unique=True)),
                ('camasir_kurutma_makinesi', models.CharField(blank=True, max_length=256, null=True)),
                ('camasir_makinesi', models.CharField(blank=True, max_length=256, null=True)),
                ('camasir_odasi', models.CharField(blank=True, max_length=256, null=True)),
                ('cati_dubleksi', models.CharField(blank=True, max_length=256, null=True)),
                ('celik_kapi', models.CharField(blank=True, max_length=256, null=True)),
                ('universite', models.CharField(blank=True, max_length=256, null=True)),
                ('ilkokul_ortaokul', models.CharField(blank=True, max_length=256, null=True)),
                ('iskele', models.CharField(blank=True, max_length=256, null=True)),
                ('itfaiye', models.CharField(blank=True, max_length=256, null=True)),
                ('sehir', models.CharField(blank=True, max_length=256, null=True)),
                ('sehir_merkezi', models.CharField(blank=True, max_length=256, null=True)),
                ('sofben', models.CharField(blank=True, max_length=256, null=True)),
                ('somine', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
    ]
