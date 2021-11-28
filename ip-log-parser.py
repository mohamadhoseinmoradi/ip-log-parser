ip_dict = {}

with open("file.txt", "r") as file:
    for i in file:
        i = i.split(" ")[0]
        if i not in ip_dict:
            ip_dict[i] = 1
        else:
            ip_dict[i] += 1

new_ip_dict = dict(sorted(ip_dict.items(), key= lambda item: item[1], reverse=True)[:5])
#print (*new_ip_dict.items(), sep="\n")
for i,j in new_ip_dict.items():
    print (f"occurence for the ip address of", i, "is: ", j)
