ip_dict = {}

with open("ip.log", "r") as file:
    for line in file:
        ip = line.split(" ")[0]
        if ip not in ip_dict:
            ip_dict[ip] = 0
        ip_dict[ip] += 1

ip_dict_top_5 = dict(sorted(ip_dict.items(), key=lambda item: item[1], reverse=True)[:5])
for i,j in ip_dict_top_5.items():
    print (f"occurence for the ip address of", i, "is: ", j)
