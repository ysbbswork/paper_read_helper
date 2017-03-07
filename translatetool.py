
import urllib.request
import urllib.parse
import json


def zipdict(l1, l2):
    return dict(map(lambda x, y: [x, y], l1, l2))


def translateit(content):
    content = str(content)
    if len(content) <= 7:
        pass
    else:
        print(content)
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
        response = urllib.request.urlopen(url, data)
        html = response.read().decode('utf-8')
        target = json.loads(html)

        print(target['translateResult'][0][0]['tgt'])
        # print(target)
        # print(target['smartResult']['entries'])

if __name__ == "__main__":
    l1 = 'happy new year'
    translateit(l1)
