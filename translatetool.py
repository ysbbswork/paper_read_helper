
import urllib.request
import urllib.parse
import json


def zipdict(l1, l2):
    return dict(map(lambda x, y: [x, y], l1, l2))


def translateit(content):
    content = str(content)
    # if len(content) <= 7:
    #     return content
    # else:
    # print(content)
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
    data = {}
    data['type'] = 'AUTO'
    data['i'] = content
    data['doctype'] = 'json'
    data['xmlVersion'] = '1.8'
    data['keyfrom'] = 'fanyi.web'
    data['ue'] = 'UTF-8'
    data['typoResult'] = 'true'
    data = urllib.parse.urlencode(data).encode('UTF-8')
    req = urllib.request.Request(url, data, head)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    target = json.loads(html)

    output = target['translateResult'][0][0]['tgt']
    # print(target)
    # print(target['smartResult']['entries'])
    return output
if __name__ == "__main__":
    l1 = 'It then uses signal strength variations in the averaged signal to extract a lower rate backscattered signal. '

    print(translateit(l1))
