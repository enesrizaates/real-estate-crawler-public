from django.http import Http404
from django.shortcuts import render
from .models import Post, Property, Detail, Picture
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, UpdateView


# Create your views here.

class SahibindenListView(ListView):
    model = Post
    template_name ='home.html'

class SahibindenDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html' 

class SahibindenCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['name', 'cat1', 'cat2', 'cat3', 'cat4',  'cat0', 'country', 'city', 'region', 'district', 'street', 'm2_brut', 'm2_net', 'oda_sayisi', 'bina_yasi', 'bulundugu_kat', 'kat_sayisi', 'isitma', 'banyo_sayisi', 'balkon', 'esyali', 'kullanim_durumu', 'site_icerisinde', 'site_adi', 'krediye_uygun', 'kimden', 'fiyat', 'ilan_aks', 'ilan_fiyat', 'ilan_no', 'ilan_Tarihi', 'Emlak_Tipi', 'area_brut', 'area_net', 'oda_sayisi', 'bina_yasi', 'floor', 'total_floor', 'isitma', 'banyo_sayisi', 'balkon', 'esyali', 'kullanim_durumu', 'site_icerisinde', 'aidat', 'site_adi', 'krediye_uygun', 'kimden', 'takas', 'gecici_numara_servisi', 'site_preference', 'record_date_time']



class SahibindenUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['name', 'cat1', 'cat2', 'cat3', 'cat4',  'cat0', 'country', 'city', 'region', 'district', 'street', 'm2_brut', 'm2_net', 'oda_sayisi', 'bina_yasi', 'bulundugu_kat', 'kat_sayisi', 'isitma', 'banyo_sayisi', 'balkon', 'esyali', 'kullanim_durumu', 'site_icerisinde', 'site_adi', 'krediye_uygun', 'kimden', 'fiyat', 'ilan_aks', 'ilan_fiyat', 'ilan_no', 'ilan_Tarihi', 'Emlak_Tipi', 'area_brut', 'area_net', 'oda_sayisi', 'bina_yasi', 'floor', 'total_floor', 'isitma', 'banyo_sayisi', 'balkon', 'esyali', 'kullanim_durumu', 'site_icerisinde', 'aidat', 'site_adi', 'krediye_uygun', 'kimden', 'takas', 'gecici_numara_servisi', 'site_preference', 'record_date_time']


def post(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    if not post:
        raise Http404
    post_val = dict(post.get_fields())
    prop = Property.objects.filter(post=post).first()
    prop_val = {}

    for field in Property._meta.get_fields():
        prop_val[field.name] = getattr(prop, field.name)


    detail = Detail.objects.filter(post=post).first()
    detail_val = {}

    for field in Detail._meta.get_fields():
        detail_val[field.name] = getattr(detail, field.name)

    pictures = Picture.objects.filter(post=post)
    pict_val = {}

    for picture_no, picture in enumerate(pictures):
        pict_val[picture_no] = picture.local_url.name.split("/")[-1]

   
    context = {'post': post_val, 'prop': prop_val, 'detail': detail_val, 'pictures': pict_val} 

    return render(request, 'post_detail.html', context)
