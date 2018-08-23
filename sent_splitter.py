
from pycorenlp import StanfordCoreNLP
import os,sys

def recur_split(arr,start,prefix):
	bracket_active = 1
	senten = prefix
	i = start
	# print str(start) + ' ' + prefix
	o_brac = 0
	while i<len(arr):
		if arr[i]==None:
			return len(arr)
		if arr[i].strip()=='(':
			bracket_active+=1
			brac_o = 1
		elif arr[i].strip()==')':
			bracket_active = bracket_active - 1
			brac_o = 0
		elif arr[i].strip().islower() or arr[i].strip().isnumeric() :
			senten = senten + ' ' + arr[i]
			brac_o = 0
		elif arr[i].strip()=='S' or arr[i].strip()=='SQ':
			brac_o = 0
			# print 'clausal sentence: ' + arr[i]
			i = recur_split(arr,i+1,senten)
			# print i
			if i==None: return len(arr)
			senten = ''
		elif arr[i].strip()=='SBAR' or arr[i].strip()=='SBARQ':
			brac_o = 0
			if len(senten)>0:
				# sent_arr = sent_arr + senten.strip() + '\n'
				sent_arr.append(senten.strip())
			senten = ''
			i=recur_split(arr,i+1,senten)
			if i==None: return len(arr)
		else:
			if brac_o==1:
				# print arr[i]
				brac_o = 0
			else:
				# print "punct: " + arr[i]
				if len(senten)>0:
					senten = senten + ' ' + arr[i]
				else:
					# print len(sent_arr)
					if len(sent_arr)>0:
						sent_arr[len(sent_arr)-1] = sent_arr[len(sent_arr)-1]+' '+arr[i]

		if bracket_active==0:
			# print 'sentence: ' + senten
			if len(senten)>0:
				# sent_arr = sent_arr + senten.strip() + '\n'
				sent_arr.append(senten.strip())
				senten = ''
			return i
		if i==len(arr)-1:
			if len(senten)>0:
				sent_arr.append(senten.strip())
				senten = ''
				return i
		i=i+1

def sent_splt(text):
	nlp = StanfordCoreNLP('http://localhost:9000')

	## needed for caseless
	text = text.lower()

	##-------## Replacing Does to Do if the question starts from Does
	##-----## Replacing based on latest rules:
	text = text.replace('like to','likes to')
	text = text.replace('love to','loves to')

	## caseless not generating constituency graph correctly so default one is preferred
	output = nlp.annotate(text, properties={
		'annotators': 'tokenize,ssplit,pos,depparse,parse',
		'outputFormat': 'json'
		# 'pos.model': 'edu/stanford/nlp/models/pos-tagger/english-caseless-left3words-distsim.tagger',
		# 'parse.model': 'edu/stanford/nlp/models/lexparser/englishPCFG.caseless.ser.gz',
		# 'ner.model': 'edu/stanford/nlp/models/ner/english.all.3class.caseless.distsim.crf.ser.gz,edu/stanford/nlp/models/ner/english.muc.7class.caseless.distsim.crf.ser.gz,edu/stanford/nlp/models/ner/english.conll.4class.caseless.distsim.crf.ser.gz'
	})

	# print "len of sentences: " + str(len(output['sentences']))

	for index in range(0,len(output['sentences'])):
		parse = output['sentences'][index]['parse']

		# print 'parse' + ": "	 + str(parse)

		parse = parse.replace('\n','')
		parse = parse.replace('(',' ( ')
		parse = parse.replace(')',' ) ')
		# parse = parse.replace('\t',' ')
		# parse = parse.replace('\r',' ')

		parse_arr = parse.split()
		# for prs in parse_arr:
		# 	print prs

		# sent_arr = ''
		last = recur_split(parse_arr,0,'') ## parse_arr = arr with all the tags, 0 = position to start parsing the input array, third argument=left over array to be added to the first array

	# print last
	# print sent_arr
	# for i in range(0,len(sent_arr)):
		# print sent_arr[i]

if __name__ == "__main__":
	# text = sys.argv[1]
	# global sent_arr
	# sent_arr = []
	# sent_splt(text)
	# app.run(host='0.0.0.0', port=8019)
    global sent_arr
    text = "hi vinay! i did respond on december 9 , 2017"
    sent_arr = []
    sent_splt(str(text).strip())
    sent = ''
    print (sent_arr)
    text = "unfortunately our situation has not changed since then , but if it does i will make sure to reach out !"
    sent_arr = []
    sent_splt(str(text).strip())
    sent = ''
    print(sent_arr)
    # text = ""
    # sent_arr = []
    # sent_splt(str(text).strip())
    # sent = ''
    # print (sent_arr)