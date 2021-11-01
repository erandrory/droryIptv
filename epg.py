# -*- coding: utf-8 -*-
import random, json, requests, zipfile
from datetime import datetime, timezone

epgURL = ['http://bit.ly/epgfish', 'http://bit.ly/epgzip'];

url = random.choice(epgURL);
r = requests.get(url);

with open("epg.zip", "wb") as code:
    code.write(r.content);

with zipfile.ZipFile('epg.zip', 'r') as zip_ref:
    zip_ref.extractall();

f = open('epg.json','r',encoding='utf-8');
epgJson = json.load(f);

xml = """<?xml version="1.0" encoding="UTF-8"?>
<tv generator-info-name="tv">
    <channel id="Channel12.il">
        <display-name lang="he">קשת 12</display-name>
    </channel>
""";

#for channel in list(epgJson.keys()):
channel = 'Channel12.il';
for program in epgJson['12']:
    startTime = datetime.fromtimestamp( int(program['start']) ).strftime("%Y%m%d%H%M%S");
    endTime = datetime.fromtimestamp( int(program['end']) ).strftime("%Y%m%d%H%M%S");
    programStr = '<programme start="{0}" stop="{1}" channel="{2}">\n<title lang="he">{3}</title>\n<desc lang="he">{4}</desc>\n</programme>\n'.format(startTime,endTime,channel,program['name'],program['description']);
    xml += programStr;
        
xml += '</tv>';

f = open('xmltv.xml','w',encoding='utf-8');
f.write(xml);
f.close();
