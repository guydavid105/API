import pandas as pd
import requests
import json

soc_codes = [1115, 1116, 1121, 1122, 1123, 1131, 1132, 1133, 1134, 1135, 1136, 1139, 1150, 1161, 1162, 1172, 1173, 1181, 1184, 1190, 1211, 1213, 1221, 1223, 1224, 1225, 1226, 1241, 1242, 1251, 1252, 1253, 1254, 1255, 1259, 2111, 2112, 2113, 2114, 2119, 2121, 2122, 2123, 2124, 2126, 2127, 2129, 2133, 2134, 2135, 2136, 2137, 2139, 2141, 2142, 2150, 2211, 2212, 2213, 2214, 2215, 2216, 2217, 2218, 2219, 2221, 2222, 2223, 2229, 2231, 2232, 2311, 2312, 2314, 2315, 2316, 2317, 2318, 2319, 2412, 2413, 2419, 2421, 2423, 2424, 2425, 2426, 2429, 2431, 2432, 2433, 2434, 2435, 2436, 2442, 2443, 2444, 2449, 2451, 2452, 2461, 2462, 2463, 2471, 2472, 2473, 3111, 3112, 3113, 3114, 3115, 3116, 3119, 3121, 3122, 3131, 3132, 3213, 3216, 3217, 3218, 3219, 3231, 3233, 3234, 3235, 3239, 3312, 3313, 3314, 3315, 3319, 3411, 3412, 3413, 3414, 3415, 3416, 3417, 3421, 3422, 3441, 3442, 3443, 3511, 3512, 3513, 3520, 3531, 3532, 3533, 3534, 3535, 3536, 3537, 3538, 3539, 3541, 3542, 3543, 3544, 3545, 3546, 3550, 3561, 3562, 3563, 3564, 3565, 3567, 4112, 4113, 4114, 4121, 4122, 4123, 4124, 4129, 4131, 4132, 4133, 4134, 4135, 4138, 4151, 4159, 4161, 4162, 4211, 4212, 4213, 4214, 4215, 4216, 4217, 5111, 5112, 5113, 5114, 5119, 5211, 5212, 5213, 5214, 5215, 5216, 5221, 5222, 5223, 5224, 5225, 5231, 5232, 5234, 5235, 5236, 5237, 5241, 5242, 5244, 5245, 5249, 5250, 5311, 5312, 5313, 5314, 5315, 5316, 5319, 5321, 5322, 5323, 5330, 5411, 5412, 5413, 5414, 5419, 5421, 5422, 5423, 5431, 5432, 5433, 5434, 5435, 5436, 5441, 5442, 5443, 5449, 6121, 6122, 6123, 6125, 6126, 6131, 6132, 6139, 6141, 6142, 6143, 6144, 6145, 6146, 6147, 6148, 6211, 6212, 6214, 6215, 6219, 6221, 6222, 6231, 6232, 6240, 7111, 7112, 7113, 7114, 7115, 7121, 7122, 7123, 7124, 7125, 7129, 7130, 7211, 7213, 7214, 7215, 7219, 7220, 8111, 8112, 8113, 8114, 8115, 8116, 8117, 8118, 8119, 8121, 8122, 8123, 8124, 8125, 8126, 8127, 8129, 8131, 8132, 8133, 8134, 8135, 8137, 8139, 8141, 8142, 8143, 8149, 8211, 8212, 8213, 8214, 8215, 8221, 8222, 8223, 8229, 8231, 8232, 8233, 8234, 8239, 9111, 9112, 9119, 9120, 9132, 9134, 9139, 9211, 9219, 9231, 9232, 9233, 9234, 9235, 9236, 9239, 9241, 9242, 9244, 9249, 9251, 9259, 9260, 9271, 9272, 9273, 9274, 9275, 9279]

def hours1(soc): #works out hours based on soc code
  hours_r = requests.get(f"http://api.lmiforall.org.uk/api/v1/ashe/estimateHours?soc={soc}")
  hours_json = hours_r.json()
  sort1 = []
  for i in hours_json["series"]:
    sort1.append(i["year"])
  sort2 = sorted(sort1)
  for i in hours_json["series"]:
    if i["year"] == sort2[-1]:
      hours = i["hours"]
  return hours



def pay1(soc): #works out pay based on soc code
  pay_r = requests.get(f"http://api.lmiforall.org.uk/api/v1/ashe/estimatePay?soc={soc}")
  pay_json = pay_r.json()
  sort1 = []
  for i in pay_json["series"]:
    sort1.append(i["year"])
  sort2 = sorted(sort1)
  for i in pay_json["series"]:
    if i["year"] == sort2[-1]:
      pay = i["estpay"]
  return pay



def change1(soc): #works out change based on soc code
  change_r = requests.get(f"http://api.lmiforall.org.uk/api/v1/ashe/annualChanges?soc={soc}")
  change_json = change_r.json()
  sort1 = []
  for i in change_json["annual_changes"]:
    sort1.append(i["year"])
  sort2 = sorted(sort1)
  for i in change_json["annual_changes"]:
    if i["year"] == sort2[-1]:
      change = i["change"]
  return change


overall1 = []
for socs in soc_codes:
  info1 = []
  soc_hour = hours1(socs)
  soc_pay = pay1(socs)
  soc_change = change1(socs)
  info1.append(socs)
  info1.append(soc_hour)
  info1.append(soc_pay)
  info1.append(soc_change)
  overall1.append(info1)

df1 = pd.DataFrame(overall1, columns = ['soc', 'hours', 'estpay', 'change'])

