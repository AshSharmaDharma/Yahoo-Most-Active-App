#!/usr/bin/python


#----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Quick Note on CRON:
# Automating the code with cron
# Need 3 seperate crontabs


# In the terminal, type:

# crontab -e
# Press I for Insert:


# In the terminal, type:

# 30-59/5 9 * * * PATH_TO_FILE
# */5 10-15 * * * PATH_TO_FILE
# 0 16 * * * PATH_TO_FILE


# Type ":"" , followed by "wq" to save and exit


# The first handles the case between 09:30 and 09:55
# The second every five minutes between 10:00 and 15:55
# The final one the single job at 16:00.


# Type : , followed by wq to save and exit


#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------


# Part 1: Scraping and saving the data.


import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import glob
import os
import csv
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText


def get_url_data():
	res = requests.get('https://finance.yahoo.com/most-active/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAABxP0qpFfWbhO4hH1dGY2sx6-dTv8n_SYbwySiB7exxrgT36JI483gxNqP7ciC-IFjwhZwJg-LNOUE7fy_swy1ywOHhgbmvAaUTXTc3Fy73E87XHZo7Lim7tuZ3XXSOK4xi02iaGX-2B0QqgY6vPJ9OL1kQ9BwUimIMkLN2s2ug7')
	# Request the Yahoo Most Active URL
	soup = BeautifulSoup(res.text, 'html.parser')
	global data
	global names
	data = soup.find_all('span' , class_ = "Trsdu(0.3s)")
	names = soup.find_all('td', class_ = 'Va(m) Ta(start) Px(10px) Fz(s)')


#----------------------------------------------------------------------------------------------------------------------------------------------------------------


def corp_names(names):
	# Get all the company names in html format
	companies = []
	for corp in names:
		companies.append(corp.text)
		# This gives us the companies in text format and append it to a list
	return companies[0:25]
		# Get the first 25 most active stocks only


def corp_price(data):
	all_current_prices = []
	for current_price in data:
		all_current_prices.append(current_price.text)
	return all_current_prices[32:155:5]
	# Give us all the numbers (including price, change and percentage change)
	# Data includes: intraday price, dollar change, percentage change, volume and market cap
	# So we start from index 32 (starting point of the table) and ending at 155 and skip by 5
	# This way we only get the data for current price for the 25 most active stocks


def corp_dollar_change(data):
	all_dollar_changes = []
	for change in data:
		all_dollar_changes.append(change.text)
	return all_dollar_changes[33:155:5]
	# Start from index 33 (starting point of the table) and ending at 155 and skip by 5
	# This way we only get the data for dollar change


def corp_percentage_change(data):
	all_percentage_changes = []
	for percent_change in data:
		all_percentage_changes.append(percent_change.text)
		all_percentage_changes = [item.replace("%", "") for item in all_percentage_changes]
	return all_percentage_changes[34:155:5]


def corp_volume(data):
	volumes = []
	for volume in data:
		volumes.append(volume.text)
		volumes = [((item.replace("M", "")).replace("B", "")).replace("T", "") for item in volumes]
	return volumes[35:160:5]


def corp_market_Cap(data):
	mcaps = []
	for cap in data:
		mcaps.append(cap.text)
	return mcaps[36:160:5]


#----------------------------------------------------------------------------------------------------------------------------------------------------------------


def organize_data():
	c_names = corp_names(names)
	c_price = corp_price(data)
	c_d_change = corp_dollar_change(data)
	c_p_change = corp_percentage_change(data)
	c_volume = corp_volume(data)
	c_m_cap = corp_market_Cap(data)
	# Assign lists to new variables
	
	global df1
	df1 = pd.DataFrame(list(zip(c_names, c_price, c_d_change, c_p_change, c_volume, c_m_cap)), columns =['Name', 'Price', 'Dollar Change', 'Percentage Change', 'Volume', 'Market Cap'])
	# Calling DataFrame constructor after zipping both lists, with columns specified:
	# State your columns/metrics headers
	# print(df1)

	text = datetime.now().strftime("%I:%M%p on %B %d, %Y")
	# We are going to date and time stamp our files to differentiate them in Part 2

	export_csv = df1.to_csv (r"New_Folder_with_Exported_Data"+text+".csv", index = None, header=True)
	# Export dataframe to a csv with the time stamp
	# Save these files to a brand new folder
	print('Done 1')


get_url_data()
organize_data()



# END OF PART 1


#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------


# Part 2: Compare Data and Email to Oursevles


path = r'CSV_FILE_FOLDER_PATH*.csv'
list_of_files = glob.glob(path) # * Means all if need specific format then *.csv
sorted_files = sorted(list_of_files, key=os.path.getmtime)
# Sort files by most recently modified


newest_file = sorted_files[-1] # Most recent saved file from Part 1 (the "9:35 file" for example)
second_newest_file = sorted_files[-2] # The "9:30 file"
# Get the latest 2 files from our folder


def read_csv_no_index(file):
	df = pd.read_csv(file)
	# Read each csv as a DataFrame:
	return df


df2 = read_csv_no_index(newest_file)
# The most recently saved csv file from Part 1 (9:35)

df1 = read_csv_no_index(second_newest_file)
# The 9:30 file


#----------------------------------------------------------------------------------------------------------------------------------------------------------------


# Loop through the 2 dataframes and whatever "Name" is not in BOTH dataframes, append those company names to a list

def get_diff_names_from_df2():
	new_names = []
	# All names found in dataframe 2
	old_names = []
	# All names found in dataframe 1
	diff_names_from_df2 = []
	# Names exclusive to dataframe 2

	for i in df2["Name"]:
		new_names.append(i)

	for i in df1["Name"]:
		old_names.append(i)

	for i in new_names:
		if i not in old_names:
			diff_names_from_df2.append(i)

	return diff_names_from_df2


list_of_diff_corps_from_df2 = get_diff_names_from_df2()


def get_diff_names_from_df1():
	new_names = []
	old_names = []
	diff_names_from_df1 = []
	for i in df2["Name"]:
		new_names.append(i)

	for i in df1["Name"]:
		old_names.append(i)

	for i in old_names:
		if i not in new_names:
			diff_names_from_df1.append(i)

	return diff_names_from_df1


list_of_diff_corps_from_df1 = get_diff_names_from_df1()


#----------------------------------------------------------------------------------------------------------------------------------------------------------------


def read_csv_with_index(file):
	df = pd.read_csv(file, index_col ='Name')
	# Need to read the file again and get rid of the index numbers (0, 1, 2, etc.)
	# This will allow us to drop certain "Names" from the dataframes so that we can compare those that are similar
	return df


df4 = read_csv_with_index(newest_file)
df3 = read_csv_with_index(second_newest_file)


def drop_diff_rows(ls, dfx):
	for i in ls:
		dfx.drop(i, inplace = True)
		# Remove the company names in the list from the dataframe
	return dfx


df4 = drop_diff_rows(list_of_diff_corps_from_df2, df4)
df3 = drop_diff_rows(list_of_diff_corps_from_df1, df3)
# We now have 2 dataframes with the same company names


# We can now order them alphabetically to have the same order from top to bottom (for comparison):

df4.sort_values(by=['Name'], inplace=True)
df3.sort_values(by=['Name'], inplace=True)


# Subtract the price column from each other and put the diff into a new column called Price Diff within df4 (also for DolLar Change Diff, Percentage Change Diff and Volume Diff)

df4['Price Diff'] = df4['Price'] - df3['Price']
df4['Dollar Change Diff'] = df4['Dollar Change'] - df3['Dollar Change']
df4['Percentage Change Diff'] = df4['Percentage Change'] - df3['Percentage Change']
df4['Volume Diff'] = df4['Volume'] - df3['Volume']


# Sort the dataframe by Volume Diff (or any metric you'd like to analyze)
# Personally I am a volume trader and like to have the liquidty and flexibility in trades
# We can also see which companies are picking up in volume quickly every 5 minutes or so


df5 = df4.sort_values(by='Volume Diff', ascending=False)


#----------------------------------------------------------------------------------------------------------------------------------------------------------------


# Convert df5 into a new csv file with a time stamp and save to a new folder (The folder which holds the files we want to email)


text2 = datetime.now().strftime("%I:%M%p on %B %d, %Y")
export_csv = df5.to_csv (r"New_Final_CSV_Folder"+text2+".csv", index = True, header=True)
print('Done 2')


# ----------------------------------------------------------------------


# Email said file


path2 = r'File_Path*.csv'
list_of_files2 = glob.glob(path2) 
sorted_files2 = sorted(list_of_files2, key=os.path.getmtime)
email_file = sorted_files2[-1]


emailfrom = "your email"
emailto = "receiver's email"
fileToSend = email_file
username = "your email"
password = "your email's password"

msg = MIMEMultipart()
msg["From"] = emailfrom
msg["To"] = emailto
msg["Subject"] = "Yahoo Most Active Stocks @: " + text2
msg.preamble = "Yahoo Most Active Stocks @: " + text2

ctype, encoding = mimetypes.guess_type(fileToSend)
if ctype is None or encoding is not None:
    ctype = "application/octet-stream"

maintype, subtype = ctype.split("/", 1)

if maintype == "text":
    fp = open(fileToSend)
    # Note: we should handle calculating the charset
    attachment = MIMEText(fp.read(), _subtype=subtype)
    fp.close()
elif maintype == "image":
    fp = open(fileToSend, "rb")
    attachment = MIMEImage(fp.read(), _subtype=subtype)
    fp.close()
else:
    fp = open(fileToSend, "rb")
    attachment = MIMEBase(maintype, subtype)
    attachment.set_payload(fp.read())
    fp.close()
    encoders.encode_base64(attachment)
attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
msg.attach(attachment)

server = smtplib.SMTP("smtp.gmail.com:587")
server.starttls()
server.login(username,password)
server.sendmail(emailfrom, emailto, msg.as_string())
server.quit()
print('Done 4')