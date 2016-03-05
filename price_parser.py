import csv
import json

StateCode_dict = {
"Alabama":"AL",	
"Alaska":"AK",	
"Arizona":"AZ",	
"Arkansas":"AR",	
"California":"CA",	
"Colorado":"CO",	
"Connecticut":"CT",	
"Delaware":"DE",	
"District of Columbia":"DC",
"Florida":"FL",	
"Georgia":"GA",
"Hawaii":"HI",	
"Idaho":"ID",	
"Illinois":"IL",	
"Indiana":"IN",	
"Iowa":"IA",	
"Kansas":"KS",	
"Kentucky":"KY",	
"Louisiana":"LA",	
"Maine":"ME",	
"Maryland":"MD",	
"Massachusetts":"MA",	
"Michigan":"MI",	
"Minnesota":"MN",	
"Mississippi":"MS",	
"Missouri":"MO",	
"Montana":"MT",	
"Nebraska":"NE",
"Nevada":"NV",	
"New Hampshire":"NH",	
"New Jersey":"NJ",	
"New Mexico":"NM",	
"New York":"NY",	
"North Carolina":"NC",	
"North Dakota":"ND",	
"Ohio":"OH",	
"Oklahoma":"OK",
"Oregon":"OR",	
"Pennsylvania":"PA",	
"Rhode Island":"RI",	
"South Carolina":"SC",	
"South Dakota":"SD",	
"Tennessee":"TN",	
"Texas":"TX",	
"Utah":"UT",	
"Vermont":"VT",	
"Virginia":"VA",	
"West Virginia":"WV",	
"Wyoming": "WY",
"Wisconsin" : "WI",
"Washington" : "WA"
}

Data_dict = {
	'HI': {}, 
	'AK': {}, 
	'FL': {}, 
	'SC': {}, 
	'GA': {}, 
	'AL': {}, 
	'NC': {}, 
	'TN': {}, 
	'RI': {}, 
	'CT': {}, 
	'MA': {},
	'ME': {}, 
	'NH': {}, 
	'VT': {}, 
	'NY': {}, 
	'NJ': {}, 
	'PA': {}, 
	'DE': {},
	'MD': {},
	'WV': {},
	'KY': {}, 
	'OH': {}, 
	'MI': {}, 
	'WY': {}, 
	'MT': {},
	'ID': {},
	'WA': {},
	'DC': {},
	'TX': {},
	'CA': {},
	'AZ': {},
	'NV': {}, 
	'UT': {}, 
	'CO': {}, 
	'NM': {}, 
	'OR': {}, 
	'ND': {}, 
	'SD': {}, 
	'NE': {}, 
	'IA': {}, 
	'MS': {}, 	
	'IN': {}, 
	'IL': {}, 
	'MN': {}, 
	'WI': {}, 
	'MO': {}, 
	'AR': {}, 
	'OK': {}, 
	'KS': {}, 
	'LA': {}, 
	'VA': {}
}	


def min_max_med(L):
	min_val  = '5000'
	m = sorted(L)
	max_val  = m[len(L) - 1]
	min_val = m[0]
	med = m[6]
	# for items in m:
	# 	if items < min_val and items != '0':
	# 		min_val = items
	# 		break
	# if min_val == '5000':
	# 	min_val = '0'
	# med  =  m[7]
	L.extend([min_val, max_val, med])
	return L





def empty_string_replacer(L):
	while "" in L:
		index = L.index("")
		L[index] = '0'
	return L



with open('house_price.csv') as csvfile:
	ignore_row = True
	for row in csvfile:
		if ignore_row :
			ignore_row = False
			continue
		row = row.split(',')

		state = StateCode_dict[row[1]]
		print state
		housing_1997 = row[12:24]
		housing_1998 = row[24:36]
		housing_1999 = row[36:48]
		housing_2000 = row[48:60]
		housing_2001 = row[60:72]
		housing_2002 = row[72:84]
		housing_2003 = row[84:96]
		housing_2004 = row[96:108]
		housing_2005 = row[108:120]
		housing_2006 = row[120:132]
		housing_2007 = row[132:144]
		housing_2008 = row[144:156]
		housing_2009 = row[156:168]
		housing_2010 = row[168:180]
		housing_2011 = row[180:192]
		housing_2012 = row[192:204]
		housing_2013 = row[204:216]
		housing_2014 = row[216:228]
		housing_2015 = row[228:240]	

		if row[1] in ['Texas', 'New York', 'Louisiana', 'West Virginia', 'Montana', 'Alaska', 'North Dakota', 'District of Columbia', 'Wyoming']:
			if "" in housing_1997:
				housing_1997 = empty_string_replacer(housing_1997)
			if "" in housing_1998:
				housing_1999 = empty_string_replacer(housing_1998)
			if "" in housing_1999:
				housing_1999 = empty_string_replacer(housing_1999)
			if "" in housing_2000:
				housing_2000 = empty_string_replacer(housing_2000)
			if "" in housing_2001:
				housing_2001 = empty_string_replacer(housing_2001)
			if "" in housing_2002:
				housing_2002 = empty_string_replacer(housing_2002)
			if "" in housing_2003:
				housing_2003 = empty_string_replacer(housing_2003)
			if "" in housing_2004:
				housing_2004 = empty_string_replacer(housing_2004)
			if "" in housing_2005:
				housing_2005 = empty_string_replacer(housing_2005)
			if "" in housing_2006:
				housing_2006 = empty_string_replacer(housing_2006)	
			if "" in housing_2007:
				housing_2007 = empty_string_replacer(housing_2007)
			if "" in housing_2008:
				housing_2008 = empty_string_replacer(housing_2008)
			if "" in housing_2009:
				housing_2009 = empty_string_replacer(housing_2009)
		Data_dict[state]['housing_1997'] = min_max_med(housing_1997)
		Data_dict[state]['housing_1998'] = min_max_med(housing_1998)
		Data_dict[state]['housing_1999'] = min_max_med(housing_1999)
		Data_dict[state]['housing_2000'] = min_max_med(housing_2000)
		Data_dict[state]['housing_2001'] = min_max_med(housing_2001)
		Data_dict[state]['housing_2002'] = min_max_med(housing_2002)
		Data_dict[state]['housing_2003'] = min_max_med(housing_2003)
		Data_dict[state]['housing_2004'] = min_max_med(housing_2004)
		Data_dict[state]['housing_2005'] = min_max_med(housing_2005)
		Data_dict[state]['housing_2006'] = min_max_med(housing_2006)
		Data_dict[state]['housing_2007'] = min_max_med(housing_2007)
		Data_dict[state]['housing_2008'] = min_max_med(housing_2008)
		Data_dict[state]['housing_2009'] = min_max_med(housing_2009)
		Data_dict[state]['housing_2010'] = min_max_med(housing_2010)
		Data_dict[state]['housing_2011'] = min_max_med(housing_2011)
		Data_dict[state]['housing_2012'] = min_max_med(housing_2012)
		Data_dict[state]['housing_2013'] = min_max_med(housing_2013)
		Data_dict[state]['housing_2014'] = min_max_med(housing_2014)
		Data_dict[state]['housing_2015'] = min_max_med(housing_2015)

		#For Kansas and Maine
		zero_list = ['0'] * 15
		Data_dict['KS']['housing_1997'] = zero_list 
		Data_dict["KS"]['housing_1998'] = zero_list
		Data_dict["KS"]['housing_1999'] = zero_list
		Data_dict["KS"]['housing_2000'] = zero_list
		Data_dict["KS"]['housing_2001'] = zero_list
		Data_dict["KS"]['housing_2002'] = zero_list
		Data_dict["KS"]['housing_2003'] = zero_list
		Data_dict["KS"]['housing_2004'] = zero_list
		Data_dict["KS"]['housing_2005'] = zero_list
		Data_dict["KS"]['housing_2006'] = zero_list
		Data_dict["KS"]['housing_2007'] = zero_list
		Data_dict["KS"]['housing_2008'] = zero_list
		Data_dict["KS"]['housing_2009'] = zero_list
		Data_dict["KS"]['housing_2010'] = zero_list
		Data_dict["KS"]['housing_2011'] = zero_list
		Data_dict["KS"]['housing_2012'] = zero_list
		Data_dict["KS"]['housing_2013'] = zero_list
		Data_dict["KS"]['housing_2014'] = zero_list
		Data_dict["KS"]['housing_2015'] = zero_list

		Data_dict["ME"]['housing_1997'] = zero_list
		Data_dict["ME"]['housing_1998'] = zero_list
		Data_dict["ME"]['housing_1999'] = zero_list
		Data_dict["ME"]['housing_2000'] = zero_list
		Data_dict["ME"]['housing_2001'] = zero_list
		Data_dict["ME"]['housing_2002'] = zero_list
		Data_dict["ME"]['housing_2003'] = zero_list
		Data_dict["ME"]['housing_2004'] = zero_list
		Data_dict["ME"]['housing_2005'] = zero_list
		Data_dict["ME"]['housing_2006'] = zero_list
		Data_dict["ME"]['housing_2007'] = zero_list
		Data_dict["ME"]['housing_2008'] = zero_list
		Data_dict["ME"]['housing_2009'] = zero_list
		Data_dict["ME"]['housing_2010'] = zero_list
		Data_dict["ME"]['housing_2011'] = zero_list
		Data_dict["ME"]['housing_2012'] = zero_list
		Data_dict["ME"]['housing_2013'] = zero_list
		Data_dict["ME"]['housing_2014'] = zero_list
		Data_dict["ME"]['housing_2015'] = zero_list

	print len(Data_dict)
		
with open("data.json","w") as f:
		json.dump(Data_dict, f)

print "Done"