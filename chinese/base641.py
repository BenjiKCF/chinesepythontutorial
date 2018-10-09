# coding:utf-8
import base64

# 如果要編碼的二進制數據不是3的倍數，最後會剩下1個或2個字節怎麼辦？
# Base64用\x00字節在末尾補足後，再在編碼的末尾加上1個或2個=號，表示補了多少字節，
# 解碼的時候，會自動去掉。
print base64.b64encode('binary\x00string')
print base64.b64decode('YmluYXJ5AHN0cmluZw==')

# 由於標準的Base64編碼後可能出現字符+和/，在URL中就不能直接作為參數，
# 所以又有一種"url safe"的base64編碼，其實就是把字符+和/分別變成-和_：
print base64.b64encode('i\xb7\x1d\xfb\xef\xff')
# abcd++//
print base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff')
# abcd--__
print base64.urlsafe_b64decode('abcd--__')
# i\xb7\x1d\xfb\xef\xff

# 由於=字符也可能出現在Base64編碼中，但=用在URL、Cookie裡面會造成歧義，
# 所以，很多Base64編碼後會把=去掉：
# 標準Base64:
#'abcd' -> 'YWJjZA=='
# 自動去掉=:
#'abcd' -> 'YWJjZA'

# 因為Base64是把3個字節變為4個字節，所以，Base64編碼的長度永遠是4的倍數
# 因此，需要加上=把Base64字符串的長度變為4的倍數，就可以正常解碼了。
