# https://github.com/NLHEALTHCARE/PERSONAL/tree/master/Costiaan/Zandbak/AdventofCode2016
# http://adventofcode.com/2016/day/7
import re

# OPGAVE DATA #
import os
data = []
with open(os.path.basename(__file__).replace('.py', '.txt'), 'r') as f:
    for line in list(f):
        data.append(line.strip())

# OPLOSSING #
ips = data


def abba(string):
    for i in range(len(string)):
        if string[i:i+2] == string[i+2:i+4][::-1] and string[i:i+2] != string[i+2:i+4]:
            return True
            break


def aba(string):
    aba_list = []
    for i in range(len(string)-2):
        if string[i] == string[i+2]:
            aba_list.append(string[i:i+3])
    return aba_list


def bab(string):
    return string[1]+string[0]+string[1]

tls = 0
ssl = 0

for ip in ips:
    in_bracket = re.findall("\[(.*?)\]", ip)
    ip_stripped = "[%s]" %ip
    for item in in_bracket:
        ip_stripped = ip_stripped.replace("[%s]" %item, "][")
    out_bracket = re.findall("\[(.*?)\]", ip_stripped)
    if abba(str(out_bracket)) and not abba(str(in_bracket)):
        tls += 1
    for item_out in aba(str(out_bracket)):
        if bab(item_out) in aba(str(in_bracket)):
            ssl += 1
            break

print('TLS = %i' %tls)
print('SSL = %i' %ssl)




