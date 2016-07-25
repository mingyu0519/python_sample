# coding=utf-8
import requests

response = requests.get("http://106.75.28.160/UCloud.txt#rd?nsukey=%2BAhDBz%2BtXRAZc4U7S0%2Ft2S8cPsPtXunmzmNO6ZSv5ZlpeQsJcvugDj229VsRgkk7g71IE8TxdiVQJDf4aIQ0aQ%3D%3D")
print response.text.count('UCanUup')
