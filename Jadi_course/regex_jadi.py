import re

# 1. Find Iranian phone number

# data = "شماره من 09121234567 هست ولی قبلاً 09351234567 داشتم."

# phone_pattern = r"09\d{9}"


# result = re.finditer(phone_pattern, data)


# for i in result:
#     print(i.group())

# 1. End


# 2. Find emails

emails = "برای تماس: ali@gmail.com، sara_2020@yahoo.com و test-user@outlook.com و mehran@sds2.cs"

email_pattern = r"[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}"

result = re.finditer(email_pattern, emails)

for i in result:
    print(i.group())

# 1. End
# 2. End

