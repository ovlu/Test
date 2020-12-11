# 引入包
import requests
import requests.json

url='请求地址'
# 传参
data={
    '值':'zhi',
    '值2':'zhi2'
}#字典，转换成json字符串
data=json.dumps()
res=requests.request(method="post",url=url,data=data)
# 获取响应值
print(res.text)