# coding=utf-8
#!/usr/bin/python
import json

parsed_json = json.loads(open('locations.json').read())

print ("""<?xml version="1.0" encoding="UTF-8"?> 
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
	<Document>
		<name> easy_currents_data_linear.kml </name>
		<Style id="sn_noicon">
			<IconStyle>
				<Icon></Icon>
			</IconStyle>
			<ListStyle></ListStyle>
			<LineStyle>
				<color> b20000ff </color>
				<width> 5 </width>
			</LineStyle>
		</Style>
		<Placemark>
			<name> easy_currents </name>
			<styleUrl> #sn_noicon </styleUrl>
			<gx:Track>
				<altitudeMode> absolute </altitudeMode>""")

for ts in parsed_json['locations']:
    print "				<when> "+ts['timeStamp'][0:10] + 'T'+ts['timeStamp'][11:19]+'Z' + " </when>"

for location in parsed_json['locations']:
	# <gx:coord>2.952437 39.360295 0.0</gx:coord>
	print "				<gx:coord>"+ location['longitude'] + " " +location['latitude']+" 0.0</gx:coord>"

print (""" 			</gx:Track>
		</Placemark>
	</Document>
</kml>
	""")
