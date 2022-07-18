from django.shortcuts import get_object_or_404
from .models import *
from django.http.response import JsonResponse
import json

# Create your views here.
def create_profile(request):
    # 생성 과정은 post 요청에만 일어나도록!
    if request.method == "POST":

        # requests에 담겨서 온 데이터를 디코딩하기!(사용할 수 있도록 json 화)
        body =  json.loads(request.body.decode('utf-8'))
        
        # 장고 orm 을 통해 가져온 데이터의 자료형은 "queryset"이라는 특별한 자료형입니다.
        new_profile = Profile.objects.create(
            # requests에서 넘어온 데이터로 새로운 profile 생성)
            name       =  body['name'],
            age        =  body['age'],
            phone      =  body['phone']
        )

        # queryset 자료를 json 모양으로 데이터를 이쁘게 정리해주기
        new_profile_json={
            "id"        : new_profile.id,
            "name"      : new_profile.name,
            "age"       : new_profile.age,
            "phone"     : new_profile.phone,
            "pup_date"  : new_profile.pup_date,
        }

        # 성공 할 경우 client가 받을 데이터 모양
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': 'new_profile_success',
                'data': new_profile_json    # 이쁘게 만든 데이터를 respons['data']에 담아 보내줌
            })

    # request.method에 대한 분기처리(post 가 아닌경우)
    return JsonResponse({
                'status': 405,
                'success': False,
                'message': 'method error',
                'data': None
        })

## profile 로 생성된 모든 데이터를 가져오는 함수
def get_profile_all(requests):
    # 생성 과정은 get 요청에만 일어나도록!
    if requests.method == 'GET':
        # 쿼리셋 모양으로 가져옴(쿼리셋 모양은 for문 적용 가능)
        profile_all = Profile.objects.all() 

        ### 특정 속성의 profile 여러개를 가져오고 싶을 때 ### 
        Profile.objects.filter(age = 0) # 여러개
        ###

        # 이쁘게 만들기
        # 여기에 최종 json 모양의 데이터가 담겨서 전달될 예정
        profile_json_all=[] 
        for profile in profile_all:
            profile_json={
                "id"        : profile.id,
                "name"      : profile.name,
                "age"       : profile.age,
                "phone"     : profile.phone,
                "pup_date"  : profile.pup_date,
            }
            profile_json_all.append(profile_json) # 나중에 serializer 배우면 생략 가능한 부분!!
        
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': 'profile_all_success',
                'data': profile_json_all
            })

    return JsonResponse({
                'status': 405,
                'success': False,
                'message': 'method error',
                'data': None
            })

# 많은 profile 중 특정 id값(다른 속성도 가능하지만 보통 id)을 갖고 있는 profile 를 가져오는 함수 
# 매개변수로 id 값도 받는다(url을 통해 전달)
def get_profile(request, id):
    if request.method == "GET":
        
        # 특정한 profile 하나를 가져오는 함수
        # pk는 실제로 모델이 id 값을 저장하고 있는 필드
        # => profile 모델로 저장된 애들중 pk 값이 id인 놈 가져와!! 아니면 404
        profile = get_object_or_404(Profile, pk = id)

        # 가져와서 이쁘게 만들기
        profile_json={
                "id"        : profile.id,
                "name"      : profile.name,
                "age"       : profile.age,
                "phone"     : profile.phone,
                "pup_date"  : profile.pup_date,
        }
        
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': 'profile_success',
                'data': profile_json
            })

    return JsonResponse({
                'status': 405,
                'success': False,
                'message': 'method error',
                'data': None
            })

def create_url(request, profile_id):
    if request.method == "POST":
        
        body = request.POST

        new_url = Url.objects.create(
            profile = get_object_or_404(Profile, pk = profile_id),
            title = body["title"],
            link = body["link"]
        )
   
        new_url_json={
            "id" : new_url.id,
            "title" : new_url.title,
            "link" : new_url.link,
            "is_completed" : new_url.is_completed,
            "pup_date" : new_url.pup_date
        }
        
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': 'url_success',
                'data': new_url_json
            })

    return JsonResponse({
                'status': 405,
                'success': False,
                'message': 'method error',
                'data': None
        })

def get_url_all(request, profile_id):
    if request.method == "GET":
        profile_url = Url.objects.filter(profile = profile_id)
        
        profile_url_json=[]
        for url in profile_url:
            new_set={
                "url_id" : url.id,
                "title" : url.title,
                "link" : url.link,
                "is_completed" : url.is_completed,
                "pup_date" : url.pup_date
            }
            profile_url_json.append(new_set)
        
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': 'url_all_success',
                'data': profile_url_json
            })

    return JsonResponse({
            'status': 405,
            'success': False,
            'message': 'method error',
            'data': None
        })