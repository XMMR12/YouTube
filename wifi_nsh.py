import subprocess
x=subprocess.check_output(["netsh","wlan","show","profiles"])
try:
    thefiltered_result=x.split("\r\nProfiles on interface Wi-Fi:\r\n\r\nGroup policy profiles (read only)\r\n---------------------------------\r\n    <None>\r\n\r\nUser profiles\r\n-------------\r\n    ")
    names="".join(thefiltered_result)
    names=names.split("All User Profile     : ")
    names="".join("".join(names).split("\n")).split("\r")
    c=1
except TypeError:
    thefiltered_result="".join(str(x))
    thefiltered_result=thefiltered_result.split("b'\\r\\nProfiles on interface Wi-Fi:\\r\\n\\r\\nGroup policy profiles (read only)\\r\\n---------------------------------\\r\\n    <None>\\r\\n\\r\\nUser profiles\\r\\n-------------\\r\\n    ")
    names="".join(thefiltered_result)
    names=names.split("All User Profile     : ")
    names="".join("".join(names).split("\\n")).split("\\r")
    c=0


list_of_wifi_names=[]
for a in names:
    if len(a) and a!="'":
        list_of_wifi_names.append(a.strip())

list_of_wifi_passwords=[]
for a in list_of_wifi_names:
    result=subprocess.check_output(["netsh","wlan","show","profile",a,'key="clear"'])
    if c: 
        result=result.split("Key Content            :")[1]
        result=result[1:result.find("\r")]
    else:
        result=str(result).split("Key Content            :")[1]
        result=result[1:result.find("\\r")]
    list_of_wifi_passwords.append(result)

#done lol
f=open("Wifi_passwords.txt","w")
f.write(("="*23)+"\n\t@XMMR12\n"+("="*23))
for a in range(len(list_of_wifi_names)):
    f.write("\nWIFI:"+list_of_wifi_names[a]+"\nPASS:"+list_of_wifi_passwords[a])

#Wifi_nsh v0.2
