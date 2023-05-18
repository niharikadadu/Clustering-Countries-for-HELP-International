# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template,request

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
#fetch json from website

country_to_code = {'Andorra': 'ad', 'United Arab Emirates': 'ae', 'Afghanistan': 'af', 'Antigua and Barbuda': 'ag', 'Anguilla': 'ai', 'Albania': 'al', 'Armenia': 'am', 'Angola': 'ao', 'Antarctica': 'aq', 'Argentina': 'ar', 'American Samoa': 'as', 'Austria': 'at', 'Australia': 'au', 'Aruba': 'aw', 'Åland Islands': 'ax', 'Azerbaijan': 'az', 'Bosnia and Herzegovina': 'ba', 'Barbados': 'bb', 'Bangladesh': 'bd', 'Belgium': 'be', 'Burkina Faso': 'bf', 'Bulgaria': 'bg', 'Bahrain': 'bh', 'Burundi': 'bi', 'Benin': 'bj', 'Saint Barthélemy': 'bl', 'Bermuda': 'bm', 'Brunei': 'bn', 'Bolivia': 'bo', 'Caribbean Netherlands': 'bq', 'Brazil': 'br', 'Bahamas': 'bs', 'Bhutan': 'bt', 'Bouvet Island': 'bv', 'Botswana': 'bw', 'Belarus': 'by', 'Belize': 'bz', 'Canada': 'ca', 'Cocos (Keeling) Islands': 'cc', 'DR Congo': 'cd', 'Central African Republic': 'cf', 'Republic of the Congo': 'cg', 'Switzerland': 'ch', "Côte d'Ivoire (Ivory Coast)": 'ci', 'Cook Islands': 'ck', 'Chile': 'cl', 'Cameroon': 'cm', 'China': 'cn', 'Colombia': 'co', 'Costa Rica': 'cr', 'Cuba': 'cu', 'Cape Verde': 'cv', 'Curaçao': 'cw', 'Christmas Island': 'cx', 'Cyprus': 'cy', 'Czechia': 'cz', 'Germany': 'de', 'Djibouti': 'dj', 'Denmark': 'dk', 'Dominica': 'dm', 'Dominican Republic': 'do', 'Algeria': 'dz', 'Ecuador': 'ec', 'Estonia': 'ee', 'Egypt': 'eg', 'Western Sahara': 'eh', 'Eritrea': 'er', 'Spain': 'es', 'Ethiopia': 'et', 'European Union': 'eu', 'Finland': 'fi', 'Fiji': 'fj', 'Falkland Islands': 'fk', 'Micronesia': 'fm', 'Faroe Islands': 'fo', 'France': 'fr', 'Gabon': 'ga', 'United Kingdom': 'gb', 'England': 'gb-eng', 'Northern Ireland': 'gb-nir', 'Scotland': 'gb-sct', 'Wales': 'gb-wls', 'Grenada': 'gd', 'Georgia': 'us-ga', 'French Guiana': 'gf', 'Guernsey': 'gg', 'Ghana': 'gh', 'Gibraltar': 'gi', 'Greenland': 'gl', 'Gambia': 'gm', 'Guinea': 'gn', 'Guadeloupe': 'gp', 'Equatorial Guinea': 'gq', 'Greece': 'gr', 'South Georgia': 'gs', 'Guatemala': 'gt', 'Guam': 'gu', 'Guinea-Bissau': 'gw', 'Guyana': 'gy', 'Hong Kong': 'hk', 'Heard Island and McDonald Islands': 'hm', 'Honduras': 'hn', 'Croatia': 'hr', 'Haiti': 'ht', 'Hungary': 'hu', 'Indonesia': 'id', 'Ireland': 'ie', 'Israel': 'il', 'Isle of Man': 'im', 'India': 'in', 'British Indian Ocean Territory': 'io', 'Iraq': 'iq', 'Iran': 'ir', 'Iceland': 'is', 'Italy': 'it', 'Jersey': 'je', 'Jamaica': 'jm', 'Jordan': 'jo', 'Japan': 'jp', 'Kenya': 'ke', 'Kyrgyzstan': 'kg', 'Cambodia': 'kh', 'Kiribati': 'ki', 'Comoros': 'km', 'Saint Kitts and Nevis': 'kn', 'North Korea': 'kp', 'South Korea': 'kr', 'Kuwait': 'kw', 'Cayman Islands': 'ky', 'Kazakhstan': 'kz', 'Laos': 'la', 'Lebanon': 'lb', 'Saint Lucia': 'lc', 'Liechtenstein': 'li', 'Sri Lanka': 'lk', 'Liberia': 'lr', 'Lesotho': 'ls', 'Lithuania': 'lt', 'Luxembourg': 'lu', 'Latvia': 'lv', 'Libya': 'ly', 'Morocco': 'ma', 'Monaco': 'mc', 'Moldova': 'md', 'Montenegro': 'me', 'Saint Martin': 'mf', 'Madagascar': 'mg', 'Marshall Islands': 'mh', 'North Macedonia': 'mk', 'Mali': 'ml', 'Myanmar': 'mm', 'Mongolia': 'mn', 'Macau': 'mo', 'Northern Mariana Islands': 'mp', 'Martinique': 'mq', 'Mauritania': 'mr', 'Montserrat': 'ms', 'Malta': 'mt', 'Mauritius': 'mu', 'Maldives': 'mv', 'Malawi': 'mw', 'Mexico': 'mx', 'Malaysia': 'my', 'Mozambique': 'mz', 'Namibia': 'na', 'New Caledonia': 'nc', 'Niger': 'ne', 'Norfolk Island': 'nf', 'Nigeria': 'ng', 'Nicaragua': 'ni', 'Netherlands': 'nl', 'Norway': 'no', 'Nepal': 'np', 'Nauru': 'nr', 'Niue': 'nu', 'New Zealand': 'nz', 'Oman': 'om', 'Panama': 'pa', 'Peru': 'pe', 'French Polynesia': 'pf', 'Papua New Guinea': 'pg', 'Philippines': 'ph', 'Pakistan': 'pk', 'Poland': 'pl', 'Saint Pierre and Miquelon': 'pm', 'Pitcairn Islands': 'pn', 'Puerto Rico': 'pr', 'Palestine': 'ps', 'Portugal': 'pt', 'Palau': 'pw', 'Paraguay': 'py', 'Qatar': 'qa', 'Réunion': 're', 'Romania': 'ro', 'Serbia': 'rs', 'Russia': 'ru', 'Rwanda': 'rw', 'Saudi Arabia': 'sa', 'Solomon Islands': 'sb', 'Seychelles': 'sc', 'Sudan': 'sd', 'Sweden': 'se', 'Singapore': 'sg', 'Saint Helena, Ascension and Tristan da Cunha': 'sh', 'Slovenia': 'si', 'Svalbard and Jan Mayen': 'sj', 'Slovakia': 'sk', 'Sierra Leone': 'sl', 'San Marino': 'sm', 'Senegal': 'sn', 'Somalia': 'so', 'Suriname': 'sr', 'South Sudan': 'ss', 'São Tomé and Príncipe': 'st', 'El Salvador': 'sv', 'Sint Maarten': 'sx', 'Syria': 'sy', 'Eswatini (Swaziland)': 'sz', 'Turks and Caicos Islands': 'tc', 'Chad': 'td', 'French Southern and Antarctic Lands': 'tf', 'Togo': 'tg', 'Thailand': 'th', 'Tajikistan': 'tj', 'Tokelau': 'tk', 'Timor-Leste': 'tl', 'Turkmenistan': 'tm', 'Tunisia': 'tn', 'Tonga': 'to', 'Turkey': 'tr', 'Trinidad and Tobago': 'tt', 'Tuvalu': 'tv', 'Taiwan': 'tw', 'Tanzania': 'tz', 'Ukraine': 'ua', 'Uganda': 'ug', 'United States Minor Outlying Islands': 'um', 'United Nations': 'un', 'United States': 'us', 'Alaska': 'us-ak', 'Alabama': 'us-al', 'Arkansas': 'us-ar', 'Arizona': 'us-az', 'California': 'us-ca', 'Colorado': 'us-co', 'Connecticut': 'us-ct', 'Delaware': 'us-de', 'Florida': 'us-fl', 'Hawaii': 'us-hi', 'Iowa': 'us-ia', 'Idaho': 'us-id', 'Illinois': 'us-il', 'Indiana': 'us-in', 'Kansas': 'us-ks', 'Kentucky': 'us-ky', 'Louisiana': 'us-la', 'Massachusetts': 'us-ma', 'Maryland': 'us-md', 'Maine': 'us-me', 'Michigan': 'us-mi', 'Minnesota': 'us-mn', 'Missouri': 'us-mo', 'Mississippi': 'us-ms', 'Montana': 'us-mt', 'North Carolina': 'us-nc', 'North Dakota': 'us-nd', 'Nebraska': 'us-ne', 'New Hampshire': 'us-nh', 'New Jersey': 'us-nj', 'New Mexico': 'us-nm', 'Nevada': 'us-nv', 'New York': 'us-ny', 'Ohio': 'us-oh', 'Oklahoma': 'us-ok', 'Oregon': 'us-or', 'Pennsylvania': 'us-pa', 'Rhode Island': 'us-ri', 'South Carolina': 'us-sc', 'South Dakota': 'us-sd', 'Tennessee': 'us-tn', 'Texas': 'us-tx', 'Utah': 'us-ut', 'Virginia': 'us-va', 'Vermont': 'us-vt', 'Washington': 'us-wa', 'Wisconsin': 'us-wi', 'West Virginia': 'us-wv', 'Wyoming': 'us-wy', 'Uruguay': 'uy', 'Uzbekistan': 'uz', 'Vatican City (Holy See)': 'va', 'Saint Vincent and the Grenadines': 'vc', 'Venezuela': 've', 'British Virgin Islands': 'vg', 'United States Virgin Islands': 'vi', 'Vietnam': 'vn', 'Vanuatu': 'vu', 'Wallis and Futuna': 'wf', 'Samoa': 'ws', 'Kosovo': 'xk', 'Yemen': 'ye', 'Mayotte': 'yt', 'South Africa': 'za', 'Zambia': 'zm', 'Zimbabwe': 'zw'}

#database ka kaam yaha se shuru h
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="localnav",
    passwd="",
    database="minorproject"
)
#creating a cursor object using the cursor() method
mycursor = mydb.cursor()

#storing table names in a list
mycursor.execute("SHOW TABLES")
table_names = [x[0] for x in mycursor]
print(table_names)

#assigning variables to the table final_minor
finally_minor = "`final_minor - sheet1`"








# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.



# ‘/’ URL is bound with index() function.
@app.route('/')
def index():
    

    return render_template('index.html')

#get request for the country name from the user using the form in index.html
@app.route('/', methods=['GET', 'POST'])
def results():
	
	#getting the country name from the form
	
	
	if request.method == 'POST':
		country = request.form
		country = list(country.values())
		country = country[0]

		print("country name is: ",country)
      
	# mycursor.execute("select * from `final_minor - sheet1`" )
	# myresult = mycursor.fetchall()

	try:
		mycursor.execute("select * from `final_minor - sheet1` where country = %s", (country,))
		mycountryresult = mycursor.fetchall()
		
		print(type(mycountryresult))
		print(mycountryresult)
		print('a')
		country_code=country_to_code[country]
		
		flag="https://flagcdn.com/"+country_code+".svg"
	except:
		print("error")
		return render_template('index.html',error="Country not found")
	#fetching the result
	
	#['index', 'child_mort', 'exports', 'health', 'imports', 'income', 'inflation', 'life_expec', 'total_fer', 'gdpp', 'country', 'inform', 'class', 'predicted']
	#sending url of the flag of the country to the html page
	# flag="https://flagcdn.com/"+country+".svg"

	#
	

	return render_template('index.html',flag=flag,index=mycountryresult[0][0],child_mort=mycountryresult[0][1],exports=mycountryresult[0][2],health=mycountryresult[0][3],imports=mycountryresult[0][4],income=mycountryresult[0][5],inflation=mycountryresult[0][6],life_expec=mycountryresult[0][7],total_fer=mycountryresult[0][8],gdpp=mycountryresult[0][9],country=mycountryresult[0][10],inform=mycountryresult[0][11],class1=mycountryresult[0][12],predicted=mycountryresult[0][13])


# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run(debug=True)
