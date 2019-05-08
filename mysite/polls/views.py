import datetime
import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group
from django.forms import formset_factory
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.views import View

from .models import Review, Shop, ShopArea, UserProfile

from .forms import ReviewForm, EditProfileForm, RegistrationForm, BookingForm, UserProfileForm

@login_required()
@permission_required('polls.change_shop')
def shop_detail(request):
    shoplink = Shop.objects.filter(shop_owner=request.user.id)
    print(shoplink)
    if shoplink:
        context = {
            'shoplink' : shoplink
        }
    else:
        context = {
            'shoplink' : 'Nodata'
        }
    return render(request, 'polls/shop_detail.html', context=context)

@login_required()
def profile(request):
    args = {'user' : request.user}

    return render(request, 'polls/profile.html', args)

@login_required()
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST,request.FILES, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form' : form}
        return render(request, template_name='polls/edit_profile.html', context=args)


@login_required()
def edit_pic(request):
    a = UserProfile.objects.get(user_id=request.user.id)
    b = UserProfile.objects.filter(user_id=request.user.id)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=a)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=a)

    context = {
    'form': form,
    'shop': b
     }
    return render(request, template_name='polls/edit_pic.html', context=context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(request.POST.get('choices'))
            if request.POST.get('choices') == '01':

                group = Group.objects.get(name='User')
                user.groups.add(group)
            else:
                group = Group.objects.get(name='Merchant')
                user.groups.add(group)
            return redirect('index2')
    else:
        form = RegistrationForm()

    args = {'form': form}
    return render(request, template_name='polls/register.html', context=args)



def my_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            next_url = request.POST.get('next_url')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('index2')
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'Wrong username or password'

    next_url = request.GET.get('next')
    if next_url:
        context['next_url'] = next_url

    return render(request, template_name='polls/login.html', context=context)

def my_logout(request):
    logout(request)
    return redirect('login')

def index2(request):

    # query_set = Group.objects.filter(user=request.user)
    # group_name = ''
    # for g in query_set:
    #     group_name = g.name


    shop_list = ShopArea.objects.all()
    shop_listz = ShopArea.objects.all()[0:1]

    line_1 = ShopArea.objects.all()[0:34:-1]
    line_2 = ShopArea.objects.all()[76:101:-1]
    line_3 = ShopArea.objects.all()[101:126:-1]
    line_4 = ShopArea.objects.all()[127:144:-1]
    line_5 = ShopArea.objects.all()[38:45]
    line_6 = ShopArea.objects.all()[145:160:-1]
    line_7 = ShopArea.objects.all()[45:62]


    line_extra = ShopArea.objects.all()[62:72]
    line_extra2 = ShopArea.objects.all()[72:76]

    shop = Shop.objects.all()


    context = {
        'shop_list' : shop_list,
        'shop_listz' : shop_listz,
        'line_1' : line_1,
        'line_2' : line_2,
        'line_3' : line_3,
        'line_4' : line_4,
        'line_5' : line_5,
        'line_6' : line_6,
        'line_7' : line_7,
        'line_extra' : line_extra,
        'line_extra2' : line_extra2,
        'user' : request.user,
        'shopr': shop,
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            return redirect('index')
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'Wrong username or password'



    return render(request, template_name='polls/index2.html', context=context)

def review(request, shop_area):
    area = ShopArea.objects.get(pk=shop_area)
    shoplink = Shop.objects.get(shop_area=shop_area)
    now = datetime.date.today()

    print(now)
    # การเอาข้อมูลมาแสดง
    # review_list = Review.objects.all()

    ##ส่วนของฐานข้อมูล

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        user = User.objects.get(id=request.user.id)
        if form.is_valid():
            review = Review.objects.create(
                review_title = form.cleaned_data.get('review_title'),
                review_message = form.cleaned_data.get('review_message'),
                review_shop_id = shoplink.id,
                day = now,
                review_user = user
            )
    else:
        form = ReviewForm()


    context = {
        'page_title' : 'wellcome to my poll page',
        'area' : area,
        'form' : form,
        'user' : request.user
    }

    return render(request, template_name='polls/review.html', context=context)


@login_required()
@permission_required('polls.add_shop')
def booking(request, shop_area):
    area = ShopArea.objects.get(pk=shop_area)
    now = datetime.date.today()
    print(now)
    # การเอาข้อมูลมาแสดง
    # review_list = Review.objects.all()

    ##ส่วนของฐานข้อมูล

    if request.method == 'POST':
        form = BookingForm(request.POST, request.FILES)
        user = User.objects.get(id=request.user.id)
        shopArea = ShopArea.objects.get(id=shop_area)
        shop_list = []

        for i in Shop.objects.filter(shop_owner_id=request.user.id):
            shop_list.append(i.shop_name)

        if len(shop_list) != 0:
            if request.POST.get('shop_name') in shop_list:
                shop_data = Shop.objects.get(shop_name=request.POST.get('shop_name'))
                print('ohm')

                for i in Shop.objects.filter(shop_owner_id=request.user.id):

                    if shop_data.shop_name == i.shop_name and shop_data.shop_owner_id == request.user.id:
                        shop_data.shop_area = area
                        shopArea.isBooking = 1
                        shopArea.shop_owner = user

                        shopArea.save()
                        shop_data.save()
                        print(shopArea.isBooking)
                        return redirect('booked')
                        break

            else:
                print('dorn')
                if form.is_valid() and shopArea.isBooking != 1:
                    print('earth')
                    shop = Shop.objects.create(
                        shop_name=form.cleaned_data.get('shop_name'),
                        shop_open=form.cleaned_data.get('shop_open'),
                        shop_close=form.cleaned_data.get('shop_close'),
                        shop_detail=form.cleaned_data.get('shop_detail'),
                        image=request.FILES.get('image'),
                        shop_area=area,
                        shop_owner=user,
                        shop_booking= now,


                    )
                    shopArea.isBooking = 1
                    shopArea.approve_status = 'รอการอนุมัติ'
                    shopArea.shop_owner = user
                    shopArea.save()
                    print(shopArea.isBooking)
                    return redirect('booked')


        else:
            if form.is_valid() and shopArea.isBooking != 1:
                print('earth')
                shop = Shop.objects.create(
                    shop_name=form.cleaned_data.get('shop_name'),
                    shop_open=form.cleaned_data.get('shop_open'),
                    shop_close=form.cleaned_data.get('shop_close'),
                    shop_detail=form.cleaned_data.get('shop_detail'),
                    image=request.FILES.get('image'),
                    shop_area=area,
                    shop_owner=user,
                    shop_booking=now

                )
                shopArea.isBooking = 1
                shopArea.approve_status = 'รอการอนุมัติ'
                shopArea.shop_owner = user
                shopArea.save()

                print(shopArea.isBooking)
                return redirect('booked')


    else:
        form = BookingForm()

    context = {
        'page_title': 'welcome to my poll page',
        'area': area,
        'form': form,

    }

    return render(request, template_name='polls/booking.html', context=context)



@login_required()
@permission_required('polls.add_shop')
def booked(request):

    # query_set = Group.objects.filter(user=request.user)
    # group_name = ''
    # for g in query_set:
    #     group_name = g.name


    shop_list = ShopArea.objects.all()
    shop_listz = ShopArea.objects.all()[0:1]

    line_1 = ShopArea.objects.all()[0:34:-1]
    line_2 = ShopArea.objects.all()[76:101:-1]
    line_3 = ShopArea.objects.all()[101:126:-1]
    line_4 = ShopArea.objects.all()[127:144:-1]
    line_5 = ShopArea.objects.all()[38:45]
    line_6 = ShopArea.objects.all()[145:160:-1]
    line_7 = ShopArea.objects.all()[45:62]


    line_extra = ShopArea.objects.all()[62:72]
    line_extra2 = ShopArea.objects.all()[72:76]

    shop = Shop.objects.all()


    context = {
        'shop_list' : shop_list,
        'shop_listz' : shop_listz,
        'line_1' : line_1,
        'line_2' : line_2,
        'line_3' : line_3,
        'line_4' : line_4,
        'line_5' : line_5,
        'line_6' : line_6,
        'line_7' : line_7,
        'line_extra' : line_extra,
        'line_extra2' : line_extra2,
        'user' : request.user,
        'shopr': shop,
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            return redirect('index')
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'Wrong username or password'



    return render(request, template_name='polls/booked.html', context=context)

@login_required()
@permission_required('polls.change_shop')
def edit_shop(request, shop_id):
    a = Shop.objects.get(id=shop_id)
    b = Shop.objects.filter(id=shop_id)
    if request.method == 'POST':
        form = BookingForm(request.POST,request.FILES, instance=a)
        if form.is_valid():
            form.save()
    else:
        form = BookingForm(instance=a)
    context = {
                'form' : form,
                'shop' : b
                }

    return render(request, template_name='polls/edit_shop.html', context=context)




@login_required()
@permission_required('polls.delete_shop')
def delete_shop(request, shop_area):
    area = ShopArea.objects.get(id=shop_area)
    area.isBooking = 0
    area.shop_owner_id = None
    area.approve_status = "ไม่อนุมัติ"
    area.save()
    Shop.objects.filter(shop_area=shop_area).delete()
    # SomeModel.objects.filter(id=id).delete()

    return redirect('delete')



@login_required()
@permission_required('polls.delete_shop')
def delete(request):

    # query_set = Group.objects.filter(user=request.user)
    # group_name = ''
    # for g in query_set:
    #     group_name = g.name


    shop_list = ShopArea.objects.all()
    shop_listz = ShopArea.objects.all()[0:1]

    line_1 = ShopArea.objects.all()[0:34:-1]
    line_2 = ShopArea.objects.all()[76:101:-1]
    line_3 = ShopArea.objects.all()[101:126:-1]
    line_4 = ShopArea.objects.all()[127:144:-1]
    line_5 = ShopArea.objects.all()[38:45]
    line_6 = ShopArea.objects.all()[145:160:-1]
    line_7 = ShopArea.objects.all()[45:62]


    line_extra = ShopArea.objects.all()[62:72]
    line_extra2 = ShopArea.objects.all()[72:76]

    shop = Shop.objects.all()


    context = {
        'shop_list' : shop_list,
        'shop_listz' : shop_listz,
        'line_1' : line_1,
        'line_2' : line_2,
        'line_3' : line_3,
        'line_4' : line_4,
        'line_5' : line_5,
        'line_6' : line_6,
        'line_7' : line_7,
        'line_extra' : line_extra,
        'line_extra2' : line_extra2,
        'user' : request.user,
        'shopr': shop,
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            return redirect('index')
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'Wrong username or password'

    return render(request, template_name='polls/delete.html', context=context)