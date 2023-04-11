print("Saptamana 1")


CNP = "5001215011153"
print(CNP[:1])


sex = CNP[:1]
birth_year = CNP[1:3]
birth_month = CNP[3:5]
birth_day = CNP[5:7]
county = CNP[7:9]
unique_id_num = CNP[9:11]
end_flag_validator = CNP[-1]

print(sex)
print(birth_year)
print(birth_month)
print(end_flag_validator)

print(CNP[:-1])
print(list(CNP))
CNP_list = map(lambda x: int(x), list(CNP))
print("CNP list:")
for val in CNP_list:
    print(val)
    print()