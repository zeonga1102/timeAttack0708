from rest_framework.permissions import BasePermission
from rest_framework.exceptions import APIException
from rest_framework import status


class GenericAPIException(APIException):
    def __init__(self, status_code, detail=None, code=None):
        self.status_code=status_code
        super().__init__(detail=detail, code=code)


class IsCandidateUser(BasePermission):
    message = 'candidate 유저만 사용할 수 있습니다.'

    def has_permisstion(self, request, view):
        user = request.user

        if not user.is_authenticated:
            response ={
                    "detail": "로그인 해주세요.",
                }
            raise GenericAPIException(status_code=status.HTTP_401_UNAUTHORIZED, detail=response)
        
        if user.user_type.user_type == 'candidate':
            return True

        return False
