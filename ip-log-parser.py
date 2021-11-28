ip_dict = {}

with open("ip.log", "r") as file:
    for file in file:
        ip = file.split(" ")[0]
        if ip not in ip_dict:
            ip_dict[ip] = 1
        else:
            ip_dict[ip] += 1

new_ip_dict = dict(sorted(ip_dict.items(), key= lambda item: item[1], reverse=True)[:5])
#print (*new_ip_dict.items(), sep="\n")
for i,j in new_ip_dict.items():
    print (f"occurence for the ip address of", i, "is: ", j)
