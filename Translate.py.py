import argparse
import requests
import json

MS_API_KEY="YOUR_API_KEY"
Google_API_KEY="YOUR_API_KEY"
MS_ENDPOINT = "YOUR_ENDPOINT"
Google_ENDPOINT = "YOUR_ENDPOINT"

def ms_translate(fromlang,tolang,category,text): 
   	headers = {"Ocp-Apim-Subscription-Key": MS_API_KEY,"Content-type": "application/json"}
   	if fromlang is not None:
   		params={'from': fromlang,'to': tolang,'category': category}
   	else:
   		params={'to': tolang,'category': category}
   	json = [{'Text': text}]
   	r = requests.post(MS_ENDPOINT, json=json,params=params,headers=headers)
   	if r.status_code != 200:
   		print('error:' + r.text)
   	else:
   		result = r.json()
   		return result[0]['translations'][0]['text']

def g_translate(fromlang,tolang,text,format):

    if fromlang is not None:
    	params = {"q": text,"target": tolang,"source":fromlang,"key":Google_API_KEY,"format":format}
    else:
    	params = {"q": text,"target": tolang,"key":Google_API_KEY,"format":format}
    r = requests.post(Google_ENDPOINT,params=params)

    if r.status_code != 200:
        print('error:' + r.text)
    else:
    	result = r.json()
    	return result['data']['translations'][0]['translatedText']

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("-f","--fromlang")
	parser.add_argument("-t","--tolang",required=True)
	parser.add_argument("-m","--method",required=True)
	parser.add_argument("-i","--input",required=True)
	args=parser.parse_args()
	texttotranslate=args.input
	fromlang=args.fromlang
	tolang=args.tolang
	method=args.method
	msresult=ms_translate(fromlang,tolang,method,texttotranslate)
	gresult=g_translate(fromlang,tolang,texttotranslate,'text')
	print()
	print("You asked for the translation of " + texttotranslate)
	print("-------THE RESULTS-------")
	print("Microsoft Translator: "+ msresult)
	print("Google Translate: "+	gresult)
	print()