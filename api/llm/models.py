import pynamodb
from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute, BooleanAttribute, MapAttribute, ListAttribute
from pynamodb.models import Model as DDBModel
from util.time_utils import get_now
from util.logging_util import logger
from contants import DEFAULT_REGION


class UserModel(DDBModel):
    """
    User Data Model for DDB
    """

    class Meta:
        billing_mode = pynamodb.constants.PAY_PER_REQUEST_BILLING_MODE
        table_name = 'template_user'
        region = DEFAULT_REGION

    class FcmTopic(MapAttribute):
        topic_name = UnicodeAttribute(null=False)
        topic_desc = UnicodeAttribute(null=False)
        subscription = BooleanAttribute()

    # 인증 정보
    email = UnicodeAttribute(hash_key=True)
    password = UnicodeAttribute(null=False)

    # 기본 정보
    name = UnicodeAttribute(null=False)
    mobile = UnicodeAttribute(null=False)
    profile_image = UnicodeAttribute(null=False)

    # 위치 정보
    address = UnicodeAttribute(null=False)
    latitude = UnicodeAttribute(null=False)
    longitude = UnicodeAttribute(null=False)

    # 생성/수정 일자
    created_at = UTCDateTimeAttribute(default=lambda: get_now())
    updated_at = UTCDateTimeAttribute(default=lambda: get_now())

    # 로그인 관련
    scope = UnicodeAttribute(null=True)
    last_login_at = UTCDateTimeAttribute(null=True)

    # 비밀 번호 찾기
    verification_code = UnicodeAttribute(null=True)
    verification_code_create_at = UTCDateTimeAttribute(null=True)

    # PUSH 관련
    fcm_token = UnicodeAttribute(null=True)
    fcm_topics = ListAttribute(of=FcmTopic, default=[])

    def __repr__(self):
        return '<%r %r %r %r %r %r>' % (
            self.Meta.table_name, self.email, self.name, self.mobile, self.scope, self.created_at)


class UserMobileConstraintModel(DDBModel):
    """
    User Mobile Unique Constraint Model for DDB
    """
    class Meta:
        billing_mode = pynamodb.constants.PAY_PER_REQUEST_BILLING_MODE
        table_name = 'template_user_mobile_constraint'
        region = DEFAULT_REGION

    # 다이나모 DB 에서는 hash_key 이외에 unique를 줄수 없다.
    # 하지만 일반적으로 사용자 이메일, 전화번호 두개다 unique를 주어야 하기 때문에 다음과 같이 mobile 을 hash_key
    # 로 잡는 constraint table 을 만든다.
    # 이것과 관련된 논의가 있고 2가지 가이드가 존재하고 그중 하나를 택하였다.
    # 선택한 방법 : https://advancedweb.hu/how-to-properly-implement-unique-constraints-in-dynamodb/
    # 다른 방법 : https://aws.amazon.com/ko/blogs/database/simulating-amazon-dynamodb-unique-constraints-using-transactions/
    mobile = UnicodeAttribute(hash_key=True)
    email = UnicodeAttribute(null=False)

    def __repr__(self):
        return '<%r %r %r>' % (
            self.Meta.table_name, self.mobile, self.email)


if not UserModel.exists():
    UserModel.create_table(wait=True, billing_mode=pynamodb.constants.PAY_PER_REQUEST_BILLING_MODE)
    logger.get_logger('pynamodb').info('UserModel created!')
else:
    logger.get_logger('pynamodb').info('UserModel is already exists!')

if not UserMobileConstraintModel.exists():
    UserMobileConstraintModel.create_table(wait=True, billing_mode=pynamodb.constants.PAY_PER_REQUEST_BILLING_MODE)
    logger.get_logger('pynamodb').info('UserMobileConstraintModel created!')
else:
    logger.get_logger('pynamodb').info('UserMobileConstraintModel is already exists!')


