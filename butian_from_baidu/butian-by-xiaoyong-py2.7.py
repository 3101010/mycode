#coding=utf-8

import requests,re,json

class butian(object):

    def __init__(self, page):
        self.page = page
        self.butian_url = "http://loudong.360.cn/Reward/pub"
        #self.proxies = {"http":"113.214.13.1:8000"}
        self.data = {
            "s":1,
            "p":self.page,
            "token":""
        }

    def bananer(self):
        page = self.page
        self.header = {
            "Cookie":"__huid=10xaEtmUCMoI06kNrXNKXNyzX2RaER%2BoGSbKG5tPlC10c%3D; __guid=91251416.888412062766036000.1509958669404.2043; Q=u%3Dwhwv320374794%26n%3DYvbqre%26le%3DZmVjZmp0Amx0WGDjpKRhL29g%26m%3DZGt3WGWOWGWOWGWOWGWOWGWOBGD5%26qid%3D2623405447%26im%3D1_t01a0666e4df0c405f9%26src%3Dpcw_webscan%26t%3D1; T=s%3Daa64c8fcf5ede555ff4f44140185a3fb%26t%3D1510279337%26lm%3D%26lf%3D2%26sk%3D254af8b4de79e226dbceba1702526893%26mt%3D1510279337%26rc%3D%26v%3D2.0%26a%3D1; smidV2=201711101002007ee03404e393cd45c97cdaadc1199ae2009802ad813b2b330; PHPSESSID=j43buncg79afvgnoq9dhs02r02; __q__=1510300224745; __DC_monitor_count=88; __DC_gid=90162694.994766671.1510279312148.1510300224993.221; __DC_sid=90162694.1811885298615175200.1510298887994.0684",
            "Host":"loudong.360.cn",
            "Referer":"http://loudong.360.cn/Service",
            "User-Agent":"Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; m1 metal Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36",
            "Origin":"http://loudong.360.cn",
            "Accept":"application/json, text/javascript, */*; q=0.01",
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With":"XMLHttpRequest",
            "Accept-Encoding":"gzip, deflate",
            "Content-Length":'14',
            "Connection":"keep-alive",
            "Accept-Language":"zh-CN,zh;q=0.8"
        }
        return self.header

    def butianjson(self):
        self.res = requests.post("http://loudong.360.cn/Reward/pub", headers = self.bananer(), data = self.data)
        self.content = json.loads(self.res.content)
        result = []
        for i in range(0, len(self.content["data"]["list"])-1):
            result.append(self.content["data"]["list"][i]["company_name"])
        return result


class baidu(object):

    def __init__(self):
        self.url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%B9%BF%E5%B7%9E%E8%A7%86%E6%BA%90%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8"

        self.bananer = {
            "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
            "Cookie":"BAIDUID=A8AC42B1F46CDE7379A037C75CB62819:FG=1; BIDUPSID=A8AC42B1F46CDE7379A037C75CB62819; PSTM=1509928743; BDSFRCVID=W2AsJeCCxG3wqIbA3H_73bWlRYwArbZtRVBJ3J; H_BDCLCKID_SF=tRk8oDDafCvbfP0k54r-hICShUFX5-CsQbrCQhcH0hOWsIO6KfrDLjtnBNte5qbQLH5f54otytbCSlo_DUC0-nDSHHK8Jj8O3J; BD_UPN=123353; H_PS_645EC=87d0k6j1zJCm9Ri%2Fyz1u3cOEnpeK5T6s2yB7SB5VJZU3itkGx%2FAeu%2BGEwAs; BD_CK_SAM=1; PSINO=2; BDSVRTM=159; H_PS_PSSID=1426_12896_21106_17001_24879; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598"

        }
        self.proxies = {"http": "113.214.13.1:8000"}
    def save_txt(self, url):
        file = open("tests.txt", "a+")
        file.write("%s\r\n"%url)
        file.close()

    def connect_baidu(self, url):
        self.url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%s"%url
        self.res = requests.get(self.url, headers = self.bananer, proxies = self.proxies, timeout=10)
        self.result = re.findall(r'<div class="f13"><a target="_blank" href="(.*?)"', self.res.content)
        baidulink = self.result[0]
        print baidulink
        try:
            res_url = requests.get(self.result[0], allow_redirects=True, timeout=10)
            _url = res_url.url
        except:
            end_url = ""
            return end_url
        end_url = _url.split("/")[0] + "//" + _url.split("/")[2]
        return end_url


if __name__ == "__main__":

    #butian = butian(1).butianjson()
    #for t in butian:
    #    xxs = baidu()
    #    baiduspider = xxs.connect_baidu(t)
    #    xxs.save_txt(baiduspider)
    #    print "FILE OK! %s"%baiduspider
    for page in xrange(32, 100):
        xxs = butian(page)
        print xxs.butianjson()
        for t in xxs.butianjson():
            xxa = baidu()
            baiduspider = xxa.connect_baidu(t)
            xxa.save_txt(baiduspider)
            print "FILE OK! %s" % baiduspider
        #butian = xxs.butianjson()
        #for t in butian:
            #xxs = baidu()
            #baiduspider = xxs.connect_baidu(t)
            #xxs.save_txt(baiduspider)
            #print "FILE OK! %s" % baiduspider
