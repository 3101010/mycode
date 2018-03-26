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
            "Cookie":"__huid=11iG2Lxm6+ZYcs3gZYffTpfY3hSL9DFgEOVB2IVGdrCSY=; __guid=132730903.3081300459025730600.1511068627877.4731; __gid=156009789.597625749.1511068940809.1511069060148.3; __hsid=607590b042738ffc; Q=u%3D%25PQ%25S8%25O6%25R1%25PP%25RP%25PS%25P2%26n%3D%26le%3Drv53o2ScLzIcnzyhMl53WGDjZGLmYzAioD%3D%3D%26m%3D%26qid%3D108357034%26im%3D1_t0110241e46b6243004%26src%3D360chrome%26t%3D1; T=s%3Def372f4f334b11bd509f9be7171ef9db%26t%3D1511071681%26lm%3D%26lf%3D1%26sk%3Ddc28e065bfccfa0ef16cd0a4c95ef983%26mt%3D1511071681%26rc%3D%26v%3D2.0%26a%3D1; PHPSESSID=qucsabthphh4g2mt5am2020gi1; __q__=1511686950193; __DC_monitor_count=2; __DC_gid=156009789.597625749.1511068940809.1511686949655.5; __DC_sid=90162694.2805026889702643000.1511686924976.1587",
            "Cookie":"__huid=11iG2Lxm6+ZYcs3gZYffTpfY3hSL9DFgEOVB2IVGdrCSY=; __guid=132730903.3081300459025730600.1511068627877.4731; __gid=156009789.597625749.1511068940809.1511069060148.3; __hsid=607590b042738ffc; Q=u%3D%25PQ%25S8%25O6%25R1%25PP%25RP%25PS%25P2%26n%3D%26le%3Drv53o2ScLzIcnzyhMl53WGDjZGLmYzAioD%3D%3D%26m%3D%26qid%3D108357034%26im%3D1_t0110241e46b6243004%26src%3D360chrome%26t%3D1; T=s%3Def372f4f334b11bd509f9be7171ef9db%26t%3D1511071681%26lm%3D%26lf%3D1%26sk%3Ddc28e065bfccfa0ef16cd0a4c95ef983%26mt%3D1511071681%26rc%3D%26v%3D2.0%26a%3D1; PHPSESSID=qucsabthphh4g2mt5am2020gi1; __q__=1511686950193; __DC_monitor_count=2; __DC_gid=156009789.597625749.1511068940809.1511686949655.5; __DC_sid=90162694.2805026889702643000.1511686924976.1587",
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
        self.result = re.findall(r'<div class="f13"><a target="_blank" href="(.*?)"', self.res.content.decode("utf-8" ))
        baidulink = self.result[0]
        print (baidulink)
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
    for page in range(32, 100):
        xxs = butian(page)
        print (xxs.butianjson())
        for t in xxs.butianjson():
            xxa = baidu()
            baiduspider = xxa.connect_baidu(t)
            xxa.save_txt(baiduspider)
            print ("FILE OK! %s" % baiduspider)
        #butian = xxs.butianjson()
        #for t in butian:
            #xxs = baidu()
            #baiduspider = xxs.connect_baidu(t)
            #xxs.save_txt(baiduspider)
            #print "FILE OK! %s" % baiduspider
