from rest_framework import status
from rest_framework.response import Response


class WPResponse(Response):
    def __init__(self, success, message=None, body=None, status=None, *args, **kwargs):
        data={
            "success": success,
            "message": message,
            "body": body
        }
        super(WPResponse, self).__init__(status=status, data=data, *args, **kwargs)


class CommonResponse:
    success = WPResponse(True, message="정상처리 되었습니다.", status=status.HTTP_200_OK)

    @staticmethod
    def success_with_data(data, status=status.HTTP_200_OK, **kwargs):
        return WPResponse(True, message="정상처리 되었습니다.", body=data, status=status, **kwargs)
