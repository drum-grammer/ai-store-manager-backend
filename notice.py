from api.llm.service import insert_to_vector_store


def hook_dynamodb(event, context):
    print("hook_dynamodb")
    print(event)
    print(context)


def hook_s3(event, context):
    print("hook_s3")
    print(event)
    print(context)

    records = event['Records']
    if len(records) <= 0:
        print('Records is empty')
        return

    record = records[0]
    event_name = record['eventName']

    # 신규 생성이고
    if event_name != 'ObjectCreated:Put' and event_name != 'ObjectCreated:Copy':
        print('event_name is not ObjectCreated:Put or ObjectCreated:Copy')
        return

    if 's3' not in record:
        print('s3 is not in record')
        return

    s3 = record['s3']
    if 'bucket' not in s3:
        print('bucket is not in s3')
        return

    if 'object' not in s3:
        print('object is not in bucket')
        return

    s3_object = s3['object']
    key = s3_object['key']
    insert_to_vector_store(key)




