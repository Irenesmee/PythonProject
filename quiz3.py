#퀴즈3
url = "https://netflix.com"
my_url = url.replace("https://","")
print(my_url)
my_url = my_url[:my_url.index(".")]
print(my_url)
password = my_url[:3] + str(len(my_url)) + str(my_url.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url,password))