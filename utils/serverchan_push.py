
import config
import requests


def push_to_wechat(msg):
    """
    通过serverchan将消息推送到微信
    :param secretKey: severchan secretKey
    :param text: 标题
    :param desp: 内容
    :return resp: json
    """
    url = f'https://qmsg.zendee.cn/send/{secretKey}'
    session = requests.Session()
#     data = {'msg':msg,'desp':desp}
    data = {'msg':msg}
    resp = session.post(url,data = data)
    return resp.json()


if __name__ == '__main__':
    resp = push_to_wechat(msg = 'test', secretKey= config.SERVERCHAN_SECRETKEY)
    print(resp)
