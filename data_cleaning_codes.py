#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import re


rdd=sc.textFile('311.csv')
rdd=rdd.map(lambda x: x.encode("ascii", "ignore"))
rdd = rdd.mapPartitions(lambda x: csv.reader(x))
header = rdd.first()
rdd = rdd.filter(lambda x: x != header)

zipcodes=[u'00083', u'10001', u'10002', u'10003', u'10004', u'10004',
	   u'10004', u'10004', u'10005', u'10006', u'10007', u'10009',
	   u'10010', u'10011', u'10012', u'10013', u'10014', u'10016',
	   u'10017', u'10018', u'10019', u'10020', u'10021', u'10022',
	   u'10023', u'10024', u'10025', u'10026', u'10027', u'10028',
	   u'10029', u'10030', u'10031', u'10032', u'10033', u'10034',
	   u'10035', u'10035', u'10036', u'10037', u'10038', u'10039',
	   u'10040', u'10041', u'10043', u'10044', u'10045', u'10047',
	   u'10047', u'10048', u'10055', u'10065', u'10069', u'10075',
	   u'10080', u'10081', u'10096', u'10097', u'10103', u'10104',
	   u'10105', u'10106', u'10107', u'10110', u'10111', u'10112',
	   u'10115', u'10118', u'10119', u'10120', u'10121', u'10122',
	   u'10123', u'10128', u'10151', u'10152', u'10153', u'10154',
	   u'10155', u'10158', u'10162', u'10165', u'10166', u'10167',
	   u'10168', u'10169', u'10170', u'10171', u'10172', u'10173',
	   u'10174', u'10175', u'10176', u'10177', u'10178', u'10196',
	   u'10196', u'10203', u'10259', u'10260', u'10265', u'10270',
	   u'10271', u'10275', u'10278', u'10279', u'10280', u'10281',
	   u'10282', u'10285', u'10286', u'10301', u'10302', u'10303',
	   u'10304', u'10305', u'10306', u'10307', u'10308', u'10309',
	   u'10310', u'10312', u'10314', u'10451', u'10452', u'10453',
	   u'10454', u'10455', u'10456', u'10457', u'10458', u'10459',
	   u'10460', u'10461', u'10462', u'10463', u'10463', u'10464',
	   u'10464', u'10464', u'10465', u'10466', u'10467', u'10468',
	   u'10469', u'10470', u'10471', u'10472', u'10473', u'10474',
	   u'10475', u'11001', u'11004', u'11005', u'11040', u'11096',
	   u'11096', u'11101', u'11102', u'11103', u'11104', u'11105',
	   u'11106', u'11109', u'11201', u'11203', u'11204', u'11205',
	   u'11206', u'11207', u'11208', u'11209', u'11210', u'11211',
	   u'11212', u'11213', u'11214', u'11215', u'11216', u'11217',
	   u'11218', u'11219', u'11220', u'11221', u'11222', u'11223',
	   u'11224', u'11225', u'11226', u'11228', u'11229', u'11230',
	   u'11231', u'11231', u'11232', u'11233', u'11234', u'11235',
	   u'11236', u'11237', u'11238', u'11239', u'11249', u'11251',
	   u'11354', u'11355', u'11356', u'11357', u'11358', u'11359',
	   u'11360', u'11361', u'11362', u'11363', u'11364', u'11365',
	   u'11366', u'11367', u'11368', u'11369', u'11370', u'11370',
	   u'11371', u'11372', u'11373', u'11374', u'11375', u'11377',
	   u'11378', u'11379', u'11385', u'11411', u'11412', u'11413',
	   u'11414', u'11415', u'11416', u'11417', u'11418', u'11419',
	   u'11420', u'11421', u'11422', u'11423', u'11426', u'11427',
	   u'11428', u'11429', u'11430', u'11432', u'11433', u'11434',
	   u'11435', u'11436', u'11451', u'11691', u'11692', u'11693',
	   u'11693', u'11693', u'11693', u'11694', u'11697']

def cleanZip(x):
	if len(x)==0:
		return 'null'
	clean=x
	clean=re.sub("[^0-9]", "", clean[0:5])
	if clean not in zipcodes:
		return 'invalid'
	else:
		return clean

rdd_map=rdd.map(lambda line: (cleanZip(line[8]),line[0]))
rdd_reduce=rdd_map.reduceByKey(lambda x,y: x+','+y)
rdd_reduce.map(lambda (k, v): "{0} \t {1}".format(k, v)).saveAsTextFile('311_clean_zip')


import datetime

def clean_time(date_text,resolution):
	if len(date_text)==0:
		return 'null'
	format = '%m/%d/%Y %I:%M:%S %p %Z'
	try:
		dt=datetime.datetime.strptime(date_text+' EST', format)
		if resolution=='hour':
			dt=dt.replace(minute=0, second=0, microsecond=0)
		elif resolution == 'day':
			dt=dt.replace(hour=0,minute=0, second=0, microsecond=0)
		elif resolution == 'week':
			dt=dt.replace(hour=0,minute=0, second=0, microsecond=0)
			weekday=dt.strftime("%U")
			dt=datetime.datetime.strptime(str(dt.year)+'-'+weekday + '-0', "%Y-%W-%w")
		elif resolution=='month':
			dt=dt.replace(day=0,hour=0,minute=0, second=0, microsecond=0)
		elif resolution =='year':
			dt=dt.replace(month=0,day=0,hour=0,minute=0, second=0, microsecond=0)
		return dt.strftime("%s")
	except ValueError:
		return 'invalid'

resolutions=['hour','day','week','month','year']

for val in resolutions:
	rdd_map=rdd.map(lambda line: (clean_time(line[1],val),line[0]))
	rdd_reduce=rdd_map.reduceByKey(lambda x,y: x+','+y)
	rdd_reduce.map(lambda (k, v): "{0} \t {1}".format(k, v)).saveAsTextFile('311_clean_create_date_'+val)



def checkNull(df,type):
	if type == 'Landmark':
		if len(df[17])==0:
			return 'no'
		else:
			return 'yes'
	if type == 'Park':
		if len(df[26])==0:
			return 'no'
		else:
			return 'yes'
	if type == 'School':
		if len(df[28])==0:
			return 'no'
		else:
			return 'yes'
	if type == 'Taxi':
		if len(df[40])==0:
			return 'no'
		else:
			return 'yes'
	if type == 'Bridge':
		if len(df[42])==0:
			return 'no'
		else:
			return 'yes'
	if type == 'Ferry':
		if len(df[48])==0:
			return 'no'
		else:
			return 'yes'


types=['Landmark','Park','School','Taxi','Bridge','Ferry']

for val in types:
	rdd_map=rdd.map(lambda line: (checkNull(line,val),line[0]))
	rdd_reduce=rdd_map.reduceByKey(lambda x,y: x+','+y)
	rdd_reduce.map(lambda (k, v): "{0} \t {1}".format(k, v)).saveAsTextFile('311_clean_type_'+val)

def unpackDf(line):
	lines=[3,4,5,6,7,17,18,22,23,26,28,39,40,42,48]
	# i=13
	vals=[]
	for val in lines:
		vals.append((line[0],line[val]))
		# i+=1
	return tuple(vals)


rdd_merge=rdd.flatMap(lambda line: unpackDf(line))

rdd_merge=None
files=[
		'311_clean_create_date_hour.txt',
		'311_clean_create_date_day.txt',
		'311_clean_create_date_week.txt',
		'311_clean_create_date_month.txt',
		'311_clean_create_date_year.txt',
		'311_clean_type_Bridge.txt',
		'311_clean_type_Ferry.txt',
		'311_clean_type_Landmark.txt',
		'311_clean_type_Park.txt',
		'311_clean_type_School.txt',
		'311_clean_type_Taxi.txt',
		'311_clean_zip.txt']

def unpackRows(line):
	x,y=line.split('\t')
	return ((v,x) for v in y.split(','))

# i=1
for val in files:
	rdd_dummy=sc.textFile(val)
	rdd_dummy=rdd_dummy.flatMap(lambda line: unpackRows(line))
	if rdd_merge ==None:
		rdd_merge=rdd_dummy
	else:
		rdd_merge=rdd_merge.join(rdd_dummy)
	# i+=1


rdd_reduce=rdd_merge.reduceByKey(lambda x,y: x+','+y)
rdd_reduce.map(lambda (k, v): "{0},{1}".format(k, v)).saveAsTextFile('311_clean_merge')






