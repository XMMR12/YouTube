import subprocess
x=subprocess.check_output(["netsh","wlan","show","profiles"])
thefiltered_result=x.split("\r\nProfiles on interface Wi-Fi:\r\n\r\nGroup policy profiles (read only)\r\n---------------------------------\r\n    <None>\r\n\r\nUser profiles\r\n-------------\r\n    ")
names="".join(thefiltered_result)
names=names.split("All User Profile     : ")
names="".join("".join(names).split("\n")).split("\r")

list_of_wifi_names=[]
for a in names:
    if len(a):
        list_of_wifi_names.append(a.strip())

list_of_wifi_passwords=[]
for a in list_of_wifi_names:
    result=subprocess.check_output(["netsh","wlan","show","profile",a,'key="clear"'])
    result=result.split("Key Content            :")[1]
    result=result[1:result.find("\r")]
    list_of_wifi_passwords.append(result)

"done lol"

#Thanks for watching ^.^