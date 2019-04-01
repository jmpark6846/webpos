from rest_framework import status
from rest_framework.response import Response


class WPResponse(Response):
    templates = {
        "success": "정상처리 되었습니다.",
        "invalid": "잘못된 요청입니다. {message}",
        "not_found": "요청하신 내용을 찾을 수 없습니다.",
        "need_login": "세션이 만료되었습니다. 다시 로그인해 주세요."
    }

    def __init__(self, success, message=None, body=None, status=None, *args, **kwargs):
        data = {
            "success": success,
            "message": message,
            "body": body
        }
        super(WPResponse, self).__init__(status=status, data=data, *args, **kwargs)


class CommonResponse:
    not_found = WPResponse(False, message=WPResponse.templates['not_found'], status=status.HTTP_404_NOT_FOUND)

    def success_with_data(data=None, status=status.HTTP_200_OK, **kwargs):
        return WPResponse(True, message=WPResponse.templates['success'], body=data, status=status, **kwargs)

    def invalid_with_message(message: str = None):
        return WPResponse(False, message=WPResponse.templates['invalid'].format(message=message),
                          status=status.HTTP_400_BAD_REQUEST)

    success = success_with_data()
    invalid = invalid_with_message()

