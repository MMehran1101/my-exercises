import re

# 1. Find Iranian phone number

data = "شماره من 09121234567 هست ولی قبلاً 09351234567 داشتم."

phone_pattern = r"09\d{9}"


result = re.finditer(phone_pattern, data)


for i in result:
    print(i.group())

# 1. End
