from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from random import * 
from sendEmail.views import *


# Create your views here.
def index(request):
    # 로그인된 사용자만 접근
    # 조건문 : 사용자의 정보가 세션에 존재하면 메인(=서비스) 화면으로 출력
    #          만약, 사용자의 정보가 세션에 없다면 로그인 화면으로 출력 
    if 'user_name' in request.session.keys():
        return render(request, 'main/index.html') # 사용자의 세션 정보가 담겨져 있는 상태에서의 index.html
    else:
        return redirect('main_signin')
    
    # return render(request, "main/index.html") # 아무런 세션 정보가 없는 index.html 

def signup(request):
    return render(request, "main/signup.html")

def join(request):
    print("테스트", request)

    name = request.POST['signupName']
    email = request.POST['signupEmail']
    pw = request.POST['signupPW']
    user = User(user_name = name, user_email = email, user_password = pw)
    user.save()

    # print("사용자 정보 저장 완료됨!! ")

    # 인증코드 하나 생성
    code = randint(1000, 9000)
    print("인증코드 생성-----------------", code) # 서버가 보낸 코드, 쿠키와 세션
    
    response = redirect("main_verifyCode") # 응답을 객체로 저장한다!
    response.set_cookie('code', code) # 인증코드
    response.set_cookie('user_id', user.id)

    print("응답 객체 완성----------------", response)

    # 이메일 발송 하는 함수 만들어보기
    # ExcelCalculate > main > views.py > join 함수 
    # 이메일 주소 2개를 준비를 해주세용
    send_result = send(email, code)
    if send_result:
        print("Main > views.py > 이메일 발송 중 완료된 거 같음....")
        return response
    else:
        return HttpResponse("이메일 발송 실패!")

def signin(request):
    return render(request, "main/signin.html")

def login(request): 
    # 로그인된 사용자만 이용할 수 있도록 구현
    # 이 때, 현재 사용자가 로그인된 사용자인지 판단하기 위해 세션 사용 FROM (verify함수에서 만든 세션)
    # 세션 처리 진행
    print("----------------------------------접근--------")
    loginEmail = request.POST['loginEmail']
    loginPW = request.POST['loginPW']

    # 로그인 시도 시, User 모델에 접근 후, 사용자가 입력한 이메일로 탐색을 시도
    # 회원 미가입 또는 비번 틀릴 경우, 에러가 발생하고 이상한 페이지 나옴
    # 예외 처리
    try:
        user = User.objects.get(user_email=loginEmail)
    except:
        return redirect("main_loginFail")

    if user.user_password == loginPW:
        print("매칭 성공")
        request.session['user_name'] = user.user_name # 사용자가 회원가입 시, 입력한 정보
        request.session['user_email'] = user.user_email # 사용자가 회원가입 시, 입력한 정보
        return redirect('main_index')
    else:
        # 로그인 실패, 정보가 다름
        print("매칭 실패")
        return redirect("main_loginFail")

def loginFail(request):
    return render(request, 'main/loginFail.html')

def verifyCode(request):
    return render(request, "main/verifyCode.html")

def verify(request):
    # 사용자가 입력한 code값을 받아야 함
    user_code = request.POST['verifyCode']

    # 쿠키에 저장되어 있는 code값을 가져온다. (join 함수 확인)
    cookie_code = request.COOKIES.get('code')
    print("코드 확인: ", user_code, cookie_code)

    if user_code == cookie_code:
        user = User.objects.get(id=request.COOKIES.get('user_id')) # SELECT FROM WHERE id = cookie_id 데이터를 가져오는 것, 
        user.user_validate = 1 # True 1 False 0
        user.save()

        print("DB에 user_validate 업데이트-----------------")

        response = redirect('main_index')

        # 저장되어 있는 쿠키를 삭제
        response.delete_cookie('code')
        response.delete_cookie('user_id')
        # response.set_cookie('user', user)

        # 사용자 정보를 세션에 저장
        request.session['user_name'] = user.user_name   ## 로그인 화면 구현 
        request.session['user_email'] = user.user_email ## 로그인 화면 구현

        return response

    else:
        return redirect('main_verifyCode') # verifyCode 화면으로 돌리기 


    # return redirect('main_index') # 인증이 완료되면 메인 화면으로 보내줌

def result(request):
    if 'user_name' in request.session.keys():
        # 현재 상황은 user_name, user_email 정보가 존재함
        # calculate 두개의 정보가 들어 있음
        content = {}
        # 새로운 객체에 저장
        content['grade_calculate_dic'] = request.session['grade_calculate_dic']
        content['email_domain_dic'] = request.session['email_domain_dic']
        content['grade_calculate_pd_dic'] = request.session['grade_calculate_pd_dic']


        # 기존 세션 삭제
        del request.session['grade_calculate_dic']
        del request.session['email_domain_dic']
        del request.session['grade_calculate_pd_dic']

        return render(request, 'main/result.html', content) # 사용자의 세션 정보가 담겨져 있는 상태에서의 index.html
    else:
        return redirect('main_signin')

def logout(request):
    # 로그아웃의 개념 : 세션 정보를 삭제하는 것
    # 파이썬에서 객체를 지울 때 
    del request.session['user_name']
    del request.session['user_email']

    return redirect('main_signin')
