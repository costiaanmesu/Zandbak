import hashlib

door_id = 'wtnhxymk'
loop_count = 0
pass_count = 0
simple_password = ''
advanced_password = ''
advanced_list = ['.']*8

while pass_count < 8:
    loop_count += 1
    hash_code = hashlib.md5(str(door_id+str(loop_count)).encode('UTF8')).hexdigest()
    if hash_code[:5] == '00000':
        simple_password += hash_code[5]
        print(hash_code, hash_code[5], hash_code[6], '0' <= hash_code[5] <= '7', str(advanced_list), str(pass_count))
        if '0' <= hash_code[5] <= '7':
            if advanced_list[int(hash_code[5])] == '.':
                advanced_list[int(hash_code[5])] = str(hash_code[6])
                pass_count += 1

simple_password = simple_password[0:8]
for c in advanced_list:
    advanced_password += c

print('simple password = '+simple_password)
print('advanced password = '+advanced_password)
