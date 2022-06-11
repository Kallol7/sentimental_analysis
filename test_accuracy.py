from block_print import blockPrint,enablePrint
import pandas as pd
import classify_limited
from sklearn.metrics import classification_report

csv_file="beach_review_truncate.csv"
data_f = pd.read_csv(csv_file, delimiter=',', on_bad_lines='skip')

strt=0
end=0
length=data_f.size

all_predictions =[]
all_sentiments = []

for i in range(0,length,10):
  strt=i
  end=i+10
  if strt==length-1:
    end=length
  if end>length: #to prevent index error
    end=length

  # cohere allows maximum 32 input at a time & more than 10 calls sometimes causes
  # internal server error, so I limited to 10 calls at time
  predictions,sentiments=classify_limited.classify(data_f,strt,end)
  
  all_predictions.extend(predictions)
  all_sentiments.extend(sentiments)
  
print(classification_report(all_sentiments, all_predictions))