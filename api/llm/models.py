from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute, BooleanAttribute, MapAttribute, ListAttribute
from pynamodb.models import Model as DDBModel
from utils.logging_util import logger


class AnswerHistoryModel(DDBModel):
    """
    User Data Model for DDB
    """

    class Meta:
        billing_mode = "PAY_PER_REQUEST"
        table_name = 'ai_store_manager_answer_history'
        region = 'ap-northeast-2'

    id = UnicodeAttribute(hash_key=True)
    question = UnicodeAttribute(null=False)
    answer = UnicodeAttribute(null=False)


if not AnswerHistoryModel.exists():
    AnswerHistoryModel.create_table(wait=True, billing_mode="PAY_PER_REQUEST")
    logger.get_logger('pynamodb').info('UserModel created!')
