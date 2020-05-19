#!/usr/bin/env python
# coding: utf-8
# Author : Swetabh


# In[1]:


import pandas as pd
from datetime import datetime

# In[2]:


match_dict = {'NOMATCH TO MATCH': 1, 'MATCH TO NOMATCH': 0}


# In[3]:


def clean_date_ranges(df):
    for i, item in enumerate(df.Date):
        if isinstance(item, datetime):
            df.Date[i] = datetime.strftime(item, '%m/%d/%Y')
        if isinstance(df.Date[i], str):
            if df.Date[i].strip() is not '':
                df.Date[i] = datetime.strptime(df.Date[i], '%d/%m/%Y')
            else:
                df.Date[i] = None


# In[4]:


def get_metrics(df):
    data_out = {"total_count": 0,
                "in_time": {"false_positives": 0, "false_negatives": 0, "total_count": 0, "comments": 0},
                "out_time": {"false_positives": 0, "false_negatives": 0, "total_count": 0, "comments": 0}}
    for idx, item in df.iterrows():
        data_out["total_count"] += 1
        if not pd.isna(item["In Time"]):
            d_in = data_out["in_time"]
            d_in["total_count"] += 1
            if not pd.isna(item["Status"]):
                if match_dict[item["Status"]]:
                    d_in["false_positives"] += 1
                else:
                    d_in["false_negatives"] += 1
                if not pd.isna(item["Comment"]):
                    #    print(item["Comment"])
                    if item["Comment"] in ["pic picture", "object picture"]:
                        d_in["comments"] += 1
                    elif not pd.isna(item["Detail"]) and item["Comment"] != "system failed":
                        d_in["comments"] += 1
        if not pd.isna(item["Out Time"]):
            d_out = data_out["out_time"]
            d_out["total_count"] += 1
            if not pd.isna(item["Status.1"]):
                if match_dict[item["Status.1"]]:
                    d_out["false_positives"] += 1
                else:
                    d_out["false_negatives"] += 1
                if not pd.isna(item["Comment.1"]):
                    #   print(item["Comment.1"])
                    if item["Comment.1"] in ["pic picture", "object picture"]:
                        d_out["comments"] += 1
                    elif not pd.isna(item["Detail"]) and item["Comment.1"] != "system failed":
                        d_in["comments"] += 1
    return data_out


# In[5]:


smarteye_excel = pd.read_excel('SMARTEYE.xlsx', sheet_name=None)

# In[6]:


rel_df = smarteye_excel["SEPTEMBER"]

# In[7]:


clean_date_ranges(rel_df)

# In[8]:


d = get_metrics(rel_df[rel_df["Date"] == datetime.strptime('15/09/2019', '%d/%m/%Y')])


# In[9]:


ind = d["in_time"]
out = d["out_time"]
total_corr = ind["total_count"] - ind["false_positives"] - ind["false_negatives"] + out["total_count"] - out["false_positives"] - out["false_negatives"]


# In[10]:


prec_in = (ind["total_count"] - ind["false_positives"] - ind["false_negatives"]) / (ind["total_count"] - ind["false_negatives"])
prec_out = (out["total_count"] - out["false_positives"] - out["false_negatives"]) / (out["total_count"] - out["false_negatives"])
prec = total_corr / (ind["total_count"] + out["total_count"] - ind["false_negatives"] - out["false_negatives"])


# In[11]:


rec_in = (ind["total_count"] - ind["false_positives"] - ind["false_negatives"]) / (ind["total_count"] - ind["false_positives"])
rec_out = (out["total_count"] - out["false_positives"] - out["false_negatives"]) / (out["total_count"] - out["false_positives"])
rec = total_corr / (ind["total_count"] + out["total_count"] - ind["false_positives"] - out["false_positives"])


# In[12]:


print(f"Total proxies identified by SmartEye: {total_corr + ind['false_positives'] + out['false_positives']}")
print(f"Proxies missed by SmartEye (False Negatives): {ind['false_negatives'] + out['false_negatives']}")
print(f"Incorrectly identified proxies (False Positives): {ind['false_positives'] + out['false_positives']}")
print(f"Correct proxy markings (True Positives): {total_corr}")
print(f"Failures due to image issues: {ind['comments'] + out['comments']}")


# In[13]:

print(f"Precision: {prec:.3f}")
print(f"Recall: {rec:.3f}")

# In[14]:

# date_list = [i for i in list(xl_df.Date.unique()) if not pd.isna(i)]
xl_workbook = pd.ExcelFile("SMARTEYE.xlsx")
df = xl_workbook.parse("SEPTEMBER")
_list = df['Date'].tolist()
_set = set(_list)
date_list = list(_set)
date_list.pop(0)
_sorted = sorted(date_list)
date_list.sort(key=lambda date1: datetime.strptime(date1, '%d/%m/%Y'))
csv = []
for i in date_list:
    d = get_metrics(rel_df[rel_df["Date"] == datetime.strptime(i, '%d/%m/%Y')])

    ind = d["in_time"]
    out = d["out_time"]
    total_corr = ind["total_count"] - ind["false_positives"] - ind["false_negatives"] + out["total_count"] - out[
        "false_positives"] - out["false_negatives"]

    prec_in = (ind["total_count"] - ind["false_positives"] - ind["false_negatives"]) / (
                ind["total_count"] - ind["false_negatives"])
    prec_out = (out["total_count"] - out["false_positives"] - out["false_negatives"]) / (
                out["total_count"] - out["false_negatives"])
    prec = total_corr / (ind["total_count"] + out["total_count"] - ind["false_negatives"] - out["false_negatives"])

    rec_in = (ind["total_count"] - ind["false_positives"] - ind["false_negatives"]) / (
                ind["total_count"] - ind["false_positives"])
    rec_out = (out["total_count"] - out["false_positives"] - out["false_negatives"]) / (
                out["total_count"] - out["false_positives"])
    rec = total_corr / (ind["total_count"] + out["total_count"] - ind["false_positives"] - out["false_positives"])

    date = i
    total_proxies = total_corr + ind['false_positives'] + out['false_positives']
    false_neg = ind['false_negatives'] + out['false_negatives']
    false_pos = ind['false_positives'] + out['false_positives']
    true_positives = total_corr
    failures = ind['comments'] + out['comments']
    precision = f"{prec:.3f}"
    recall = f"{rec:.3f}"
    csv.append({'Date': date, 'Proxies Identified': total_proxies, 'Precision': precision, 'Recall': recall})

df = pd.DataFrame(csv)
df.to_csv('result.csv', index=False)
print('**** CSV file created ****')
