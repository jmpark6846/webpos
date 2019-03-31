from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.views import APIView

from webpos_account.account_methods import create_token
from webpos_account.models import Account, RefreshToken
from webpos_account.serializers import AccountSerializer, LoginSerializer
from webpos_common.responses import WPResponse, CommonResponse
from webpos_common.utils import get_now
from webpos_common.views import BaseViewSet


class AccountViewSet(BaseViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = AccountSerializer
    queryset = Account.objects.filter(deleted_at=None)


class AccountView(APIView):
    def post(self, request:Request):
        serializer = AccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if Account.objects.filter(email=serializer.validated_data['email']).exists():
            return CommonResponse.invalid_with_message('이미 가입된 이메일 입니다.')

        account = serializer.save()
        account.set_password(serializer.validated_data['password'])
        account.save()
        return CommonResponse.success


class TokenView(APIView):
    def post(self, request: Request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        account = Account.objects.filter(email=serializer.validated_data['email'], deleted_at=None).last()

        if not account:
            return WPResponse(False, "아이디가 존재하지 않습니다.", status=status.HTTP_404_NOT_FOUND)

        if not account.check_password(serializer.validated_data['password']):
            return WPResponse(False, "비밀번호가 올바르지 않습니다.", status=status.HTTP_400_BAD_REQUEST)

        access_token, refresh_token = create_token(account)
        res = CommonResponse.success_with_data(data={"token":access_token.value})

        account.last_login = get_now()
        account.save()

        res.set_cookie(
            'webpos_refreshtoken',
            value=refresh_token.value,
            expires=refresh_token.expire_at.timestamp(),
            path='/',
            httponly=False, # todo: https 연결 사용하여 True 로 변경
        )
        return res

    def put(self, request: Request):
        RefreshToken.objects.filter()


# 로그인
# 이메일, 비밀번호 입력
# 이메일, 만료일시 로 토큰 생성
# 토큰을 response 로 전송

# 로그아웃
# 헤더의 토큰값 삭제

# 인증
# 헤더에서 토큰을 들고옴
# 만료 됬는지 검사, 만료됬으면 응답 전송
# 이메일로 유저 조회 있으면 request.user = User, (user, None) 리턴
# 유저 정보 없으면 request.user = None, None, None 리턴


# 클라이언트가 api 사용
# 헤더에 해당 access token 을 담아 전송
