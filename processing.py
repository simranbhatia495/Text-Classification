#AI PROJECT 01/05/2017  SIMRAN KAUR BHATIA simran.bhatia495@gmail.com
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from PyDictionary import PyDictionary
from nltk.stem import PorterStemmer
import nltk.tag
import goslate
import translate
from langdetect import detect
import collections, re
stop_words = set(stopwords.words('english'))
ps = PorterStemmer()
fopen = open("pos.txt","r")
# CREATE FEATURE SET WHICH WILL HAVE COUNT FOR EACH FEATURE IN EVRY SUGGESTION & ASSIGN CLASS LABEL TO EACH SUGGESTION. CLASS LABELS ARE DEFINED AS DIFFERENT MINISTRIES OF THE GOVT
feature_list=['hospitals','doctors','patients','health','medicine','education','schools','colleges','institute','english','hindi','language','technology','students','digital','army','navy','merchant','police','traffic','crimes','sanitation','water','food','cloth','fire','air','electricity','tax','aadhar','credit','cash','economy','money','bank','cashless','public','grievance','others']

class_label = {'Health': ['hospitals','doctors','patients','health','medicine'],'Education':['education','schools','colleges','institute','english','hindi','language','technology','students','digital'],'Defence/Home Affairs':['army','navy','merchant','police','traffic','crimes'],'Public Welfare':['sanitation','water','food','cloth','fire','air','electricity'],'Finance':['tax','aadhar','credit','cash','economy','money','bank','cashless'],'Public Grievances':['public','grievance','others']}
import csv
f1 = open("training_set.csv","a")
writer=csv.writer(f1, delimiter=',')
writer.writerow(feature_list+['MINISTRY'])
f1.close()

def csv_writer(temp, path):
    """
       Write data to a CSV file
       """
    with open(path, "a") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(temp)

total =0;
with open('C:\\Users\\Simran\\PycharmProjects\\AI\\pos.txt',"r") as f:
        for lines in f:
            lines = f.readline()
            lines = lines.lower()
            total = total + 1
            print(lines)
            #print(sent_tokenize(lines))
            word_tokens = word_tokenize(lines)
            filtered_sentence = [w for w in word_tokens if not w in stop_words]

            filtered_sentence = []
            for w in word_tokens:
                if w not in stop_words:
                    filtered_sentence.append(w)
            #print(word_tokens)
            #print(filtered_sentence)
            tagged = nltk.pos_tag(word_tokens)

            tagged = [word for word, pos in tagged \
                     if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS')]
            for each_word in tagged:
                each_word= ps.stem(each_word)

            print(tagged)

            """bagsofwords = [collections.Counter(re.findall(r'\w+', txt))
                           for txt in tagged]"""
            feature_count=[]
            max = 0 ;
            for i in feature_list:
                cnt = tagged.count(i)
                feature_count.append(cnt)
                #print(cnt,i)
                if(cnt>max):
                    max = cnt
                    str = i
            if(max==0):
                str = 'others'
            #print(max)
            #print(str)
            temp = []
            new = [k for k, v in class_label.items() if str in v]
            #print(new)
            temp = feature_count+ new
            path = "training_set.csv"
            print(temp)
            csv_writer(temp, path)
print(total)

