# https://github.com/NLHEALTHCARE/PERSONAL/tree/master/Costiaan/Zandbak/AdventofCode2016
# http://adventofcode.com/2016/day/4


# OPGAVE DATA #
import os
data = []
with open(os.path.basename(__file__).replace('.py', '.txt'), 'r') as f:
    for line in list(f):
        data.append(line.strip())

# OPLOSSING #
codes = data
sector_sum = 0

for code in codes:
    checksum_code = code[code.find('[')+1:code.find(']')]
    sector_id = code.replace('[%s]'%checksum_code, '')[-3:]
    room = code.replace('[%s]'%checksum_code, '')[:-3]

    checksum_dict = {chr(key): (256-key) for key in range(97, 123)}
    checksum_room = ''

    for i in range(len(room)):
        if room[i] != '-':
            checksum_dict[room[i]] += 128

    for c in sorted(checksum_dict, key=checksum_dict.get, reverse=True)[:5]:
        checksum_room += c

    if checksum_room == checksum_code:
        sector_sum += int(sector_id)

    room_name = ''
    for i in range(len(room)):
        if room[i] == '-':
            room_name += ' '
        else:
            room_name += chr((((ord(room[i]) - 96) + int(sector_id)) % 26) + 96)

    if room_name.find('object storage')>0:
        print('room = {0}, sector = {1}'.format(room_name, sector_id))

print('sector sum = %s' % sector_sum)

