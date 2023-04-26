import requests
def English_Chinese():
	url = "https://fanyi.baidu.com/sug"
	s = input("请输入要翻译的词(中/英):")
	dat = {
		"kw":s
		}
	resp = requests.post(url,data = dat)# 发送post请求
	ch = resp.json() # 将服务器返回的内容直接处理成json => dict
	resp.close()
	dic_lenth = len(ch['data'])
	for i in range(dic_lenth):
		print("词:"+ch['data'][i]['k']+" "+"单词意思:"+ch['data'][i]['v'])
English_Chinese()
