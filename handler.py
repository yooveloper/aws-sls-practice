import datetime
import logging
import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def hello(event, context):
    current_time = datetime.datetime.now().time()
    name = context.function_name
    logger.info("Your cron function " + name +
                " ran at " + str(current_time))

    send_message(name, current_time)


# Send a message to the Slack channel
def send_message(name, time):
    hook = ''  # Your Hook URL
    title = '알림 봇 테스트'
    content = '[알림 봇 테스트] \n Python으로 작성된 AWS Lambda 함수가 실행되었습니다.\n' + \
        'name : ' + name + "\n time : " + str(time)

    # 메세지 전송
    requests.post(
        hook,
        headers={
            'Content-Type': 'application/json'
        },
        json={
            'text': title,
            'blocks': [
                {
                    'type': 'section',
                    'text': {
                        'type': 'mrkdwn',
                        'text': content
                    }
                }
            ]
        }
    )
