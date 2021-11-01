# -*- coding: utf-8 -*-
import random, json, requests, zipfile

epgURL = ['http://bit.ly/epgfish', 'http://bit.ly/epgzip'];

url = random.choice(epgURL);
r = requests.get(url);

with open("epg.zip", "wb") as code:
    code.write(r.content);

with zipfile.ZipFile('epg.zip', 'r') as zip_ref:
    zip_ref.extractall();

f = open('epg.json','r',encoding='utf-8');
epgJson = json.load(f);

xml = '<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE tv SYSTEM "xmltv.dtd"><tv>';

#for channel in list(epgJson.keys()):
channel = '12';
for program in epgJson[channel]:
    programStr = '<programme start="{0}" stop="{1}" channel="{2}"><title lang="he">{3}</title><desc lang="he">{4}</desc></programme>'.format(program['start'],program['end'],channel,program['name'],program['description']);
    xml += programStr;
        
xml += '</tv>';

f = open('xmltv.xml','w',encoding='utf-8');
f.write(xml);
f.close();
