from enum import Enum
from http import HTTPStatus


class CustomException(Exception):
    def __init__(
        self,
        error_code: str,
        message: str,
        status_code: HTTPStatus = HTTPStatus.BAD_REQUEST
    ) -> None:
        self.error_code = error_code
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class CustomError(Enum):
    # 400 Bad Request
    INVALID_REQUEST_PARAMETER = CustomException('INVALID_REQUEST_PARAMETER', '파라미터 유효성 검사 오류입니다.', HTTPStatus.BAD_REQUEST)
    REQUIRED_PARAMETER_MISSED = CustomException('REQUIRED_PARAMETER_MISSED', '필수값을 입력해주세요.', HTTPStatus.BAD_REQUEST)
    USER_ALREADY_EXISTS = CustomException('USER_ALREADY_EXISTS', '이미 존재하는 유저 아이디 입니다.', HTTPStatus.BAD_REQUEST)
    REPORT_NOT_MODIFIABLE = CustomException('REPORT_NOT_MODIFIABLE', '작성 중인 점검일지 리포트만 수정하거나 삭제할 수 있습니다.', HTTPStatus.BAD_REQUEST)
    REPORT_STILL_IN_PROGRESS = CustomException('REPORT_STILL_IN_PROGRESS', '아직 작성 중인 점검일지 리포트입니다.', HTTPStatus.BAD_REQUEST)
    ORIGIN_PASSWORD_NOT_MATCHED = CustomException('ORIGIN_PASSWORD_NOT_MATCHED', '기존 비밀번호가 일치하지 않습니다.', HTTPStatus.BAD_REQUEST)
    NEW_PASSWORD_NOT_MATCHED = CustomException('NEW_PASSWORD_NOT_MATCHED', '신규 비밀번호가 일치하지 않습니다.', HTTPStatus.BAD_REQUEST)

    # 401 Unauthorized
    INVALID_TOKEN = CustomException('INVALID_TOKEN', '유효하지 않는 토큰입니다.', HTTPStatus.UNAUTHORIZED)
    INVALID_PASSWORD = CustomException('INVALID_PASSWORD', '비밀번호가 일치하지 않습니다.', HTTPStatus.UNAUTHORIZED)

    # 403 Forbidden
    ADMIN_AUTHORITY_REQUIRED = CustomException('ADMIN_AUTHORITY_REQUIRED', '어드민 권한이 필요합니다.', HTTPStatus.FORBIDDEN)
    TEAM_LEADER_AUTHORITY_REQUIRED = CustomException('TEAM_LEADER_AUTHORITY_REQUIRED', '팀장 권한이 필요합니다.', HTTPStatus.FORBIDDEN)
    TEAM_MEMBER_AUTHORITY_REQUIRED = CustomException('TEAM_MEMBER_AUTHORITY_REQUIRED', '팀원 권한이 필요합니다.', HTTPStatus.FORBIDDEN)
    TEAM_AUTHORITY_REQUIRED = CustomException('TEAM_AUTHORITY_REQUIRED', '해당 팀에 소속된 유저만 사용 가능합니다.', HTTPStatus.FORBIDDEN)
    REPORTER_AUTHORITY_REQUIRED = CustomException('REPORTER_AUTHORITY_REQUIRED', '점검일지 리포트 작성자 권한이 필요합니다.', HTTPStatus.FORBIDDEN)
    REPORT_ALREADY_APPROVED = CustomException('REPORT_ALREADY_APPROVED', '이미 결재 완료된 점검일지 리포트입니다.', HTTPStatus.FORBIDDEN)
    APPROVER_AUTHORITY_REQUIRED = CustomException('APPROVER_AUTHORITY_REQUIRED', '점검일지 리포트 결재자 권한이 필요합니다.', HTTPStatus.FORBIDDEN)

    # 404 Not Found
    USER_NOT_FOUND = CustomException('USER_NOT_FOUND', '존재하지 않는 유저 입니다.', HTTPStatus.NOT_FOUND)
    TEMPLATE_NOT_FOUND = CustomException('TEMPLATE_NOT_FOUND', '존재하지 않는 점검일지 템플릿 입니다.', HTTPStatus.NOT_FOUND)
    REPORT_NOT_FOUND = CustomException('REPORT_NOT_FOUND', '존재하지 않는 점검일지 리포트 입니다.', HTTPStatus.NOT_FOUND)
