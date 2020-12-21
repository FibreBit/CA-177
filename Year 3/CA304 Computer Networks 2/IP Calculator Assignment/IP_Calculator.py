classes={
         'A':{
                'prefix':'0',
                'network_bits':7,
                'host_bits':24,
            },
         'B':{
                'prefix':'10',
                'network_bits':14,
                'host_bits':16
         },
         'C':{
                'prefix':'110',
                'network_bits':21,
                'host_bits':8
         },
         'D':{
                'prefix':'1110',
                'network_bits':'N/A',
                'host_bits':'N/A'                      
         },
         'E':{
                'prefix':'1111',
                'network_bits':'N/A',
                'host_bits':'N/A'
         }
        }



def to_binary_string(ip_addr):
    byte_split = ip_addr.split(".")
    return ['{0:08b}'.format(int(x)) for x in byte_split]

def to_decimal_dot(ip_addr_list):
    return ".".join([str(int(x,2)) for x in ip_addr_list])

def to_split_binary(binary):
    "Takes a string of binary and sections it into a list of four bytes"
    new = []
    new.append(binary[0:8])
    new.append(binary[8:16])
    new.append(binary[16:24])
    new.append(binary[24:])
    return to_decimal_dot(new)
def get_class_letter(ip_addr):
    class_letters = 'ABCDE'
    total = 0
    #Checking prefix to see which class letter it applies to.
    for digit in to_binary_string(ip_addr)[0]:
        if total > 5:
            return class_letters[4]
        elif digit == '1':
            total += 1
        else:
            return class_letters[total]

def get_first_and_last(ip_addr):
    "Finds the prefix for the corresponding class letter and returns first and last address range."
    class_letter = get_class_letter(ip_addr)
    binary_ip = to_binary_string(ip_addr)
    #To get first and last address range, replace all bits after class prefix with 0's and 1's respectively
    first =['00000000', '00000000', '00000000']
    last = ['11111111', '11111111', '11111111']
    first.insert(0, (classes[class_letter]['prefix'] + '0' * (8 - len(classes[class_letter]['prefix']))))
    last.insert(0, (classes[class_letter]['prefix'] + '1' * (8 - len(classes[class_letter]['prefix']))))
    return to_decimal_dot(first), to_decimal_dot(last)

def get_class_stats(ip_addr):
    class_letter = get_class_letter(ip_addr)
    #Class D is reserved for multicasting, Class E is reserved for future use
    if class_letter == 'D' or class_letter == 'E':
        networks = 'N/A'
        hosts = 'N/A'
    else:
        #Per slides 10 & 13, networks and hosts are found with 2 ** network bits and 2 ** host bits
        networks = 2 ** int((classes[class_letter]['network_bits']))
        hosts = 2 ** (classes[class_letter]['host_bits'])
        
    first_address, last_address = get_first_and_last(ip_addr)
    print ('Class: {} \nNetwork: {}\nHost: {}\nFirst Address: {}\nLast Address: {}'.format(class_letter,
                                                                                           networks, hosts,
                                                                                           first_address,
                                                                                           last_address))
        
    

def get_supernet_stats(ip_addr_list):
    first = "".join(to_binary_string(ip_addr_list[0]))
    last = "".join(to_binary_string(ip_addr_list[len(ip_addr_list) - 1]))
    bit_being_checked = 0
    bit_total = 0
    #Checking bits to see if they match, should they not the index of bit is noted and made the network mask
    while bit_being_checked < len(first):
        while bit_total < 1:
            if first[bit_being_checked] == last[bit_being_checked]:
                bit_being_checked += 1
            else:
                bit_total = bit_being_checked
        bit_being_checked += 1
    network_mask = to_split_binary(('1' * bit_total) + ('0' * (32 - bit_total)))
    print('Address {}/{}\nNetwork Mask {}'.format(ip_addr_list[0], bit_total, network_mask))
    




def get_subnet_bits(subnet_mask):
    "Counts the number of 1's in the subnet_mask to return subnet bit count"
    subnet = "".join(to_binary_string(subnet_mask))
    bit_count = 0
    for digit in subnet:
        if digit == '1':
            bit_count += 1
    return bit_count

def get_subnets(ip_addr, subnet_mask, class_letter):
    "Retrieves subnets by counting 1's in the coresponding byte"
    total = 0
    split_subnet = to_binary_string(subnet_mask)
    class_letters = ' ABC'
    i = class_letters.index(class_letter)
    for digit in split_subnet[i]:
        if digit == '1':
            total += 1
    return total

def get_valid_subnets(ip_addr, subnet_mask):
    class_letter = get_class_letter(ip_addr)
    split_subnet = subnet_mask.split(".")
    split_ip = ip_addr.split(".")
    valid = []
    broadcast = []
    first = []
    last = []
    if get_class_letter(ip_addr) == 'C':
        del split_ip[3]
        changing_slot = 3
    elif get_class_letter(ip_addr) == 'B':
        del split_ip[2]
        changing_slot = 2
    elif get_class_letter(ip_addr) == 'A':
        del split_ip[1]
        changing_slot = 1

    block_size = 256 - int(split_subnet[changing_slot])
    increment = 0

    while increment <= int(split_subnet[changing_slot]):
        split_ip.insert(changing_slot, str(increment))
        valid.append(".".join(split_ip))
        del split_ip[changing_slot]
        split_ip.insert(changing_slot, str(increment + 1))
        first.append(".".join(split_ip))
        del split_ip[changing_slot]

        if increment != 0:
            split_ip.insert(changing_slot, str(increment - 1))
            broadcast.append(".".join(split_ip))
            del split_ip[changing_slot]
            split_ip.insert(changing_slot, str(increment - 2))
            last.append(".".join(split_ip))
            del split_ip[changing_slot]
        increment = increment + block_size

    split_ip.insert(changing_slot, '255')
    broadcast.append(".".join(split_ip))
    del split_ip[changing_slot]
    split_ip.insert(changing_slot, '254')
    last.append(".".join(split_ip))
    return valid, broadcast, first, last

def get_subnet_stats(ip_addr, subnet_mask):
    class_letter = get_class_letter(ip_addr)
    CIDR = get_subnet_bits(subnet_mask)
    subnet_total = 2 ** get_subnets(ip_addr, subnet_mask, class_letter)
    #2 host addresses reserved for network and broadcast address
    host_total = 2 ** (32 - get_subnet_bits(subnet_mask)) - 2
    valid, broadcast, first, last = get_valid_subnets(ip_addr, subnet_mask)
    print ('Address: {}/{}\nSubnets: {}\nAdressable hosts per subnet: {}\nValid Subnets: {}\nBroadcast addresses: {}\nFirst addresses: {}\nLast Addresses: {}'.format(
        ip_addr, 
        CIDR, 
        subnet_total, 
        host_total, 
        valid, 
        broadcast, 
        first, 
        last))
