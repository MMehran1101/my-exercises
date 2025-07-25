import re

# 1. Find Iranian phone number

# data = "شماره من 09121234567 هست ولی قبلاً 09351234567 داشتم."

# phone_pattern = r"09\d{9}"


# result = re.finditer(phone_pattern, data)


# for i in result:
#     print(i.group())

# 1. End


# 2. Find emails

# emails = "برای تماس: ali@gmail.com، sara_2020@yahoo.com و test-user@outlook.com و mehran@sds2.cs"

# email_pattern = r"[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}"

# result = re.finditer(email_pattern, emails)

# for i in result:
#     print(i.group())

# 2. End

# 3. English Word from 4 to 6 letters

# data = "We are learning regex with python. Easy? Maybe, maybe not!"

# eng_pattern = r"[a-zA-Z]{4,6}"

# result = re.finditer(eng_pattern, data)

# for i in result:
#     print(i.group())

# 3. End


# 4. Export Dates

data = "Our meetings are on 2025-07-23, 1998-12-04 and 2050-01-01."

date_pattern = r"([1-2][0-9][0-9][0-9])-(0[1-9]|1[1-2]|12)-([0-2][0-9]|3[0-1])"

result = re.finditer(date_pattern, data)

for i in result:
    print(i.group())

# 4. End
