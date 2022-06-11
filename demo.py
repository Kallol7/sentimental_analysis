from turtle import end_fill
from block_print import blockPrint,enablePrint
import pandas as pd
import classify_limited
from sklearn.metrics import classification_report

csv_file="beach_review_truncate.csv"
data_f = pd.read_csv(csv_file, delimiter=',', on_bad_lines='skip')

strt=4
end=10


_reviews=data_f['review'].to_list()
_reviews=_reviews[strt:end] # 4 to 10

predictions,sentiments=classify_limited.classify(data_f,strt,end)  

input={}

total=end-strt

for i in range(total):
    
    print("{")

    print("REVIEW:\n",_reviews[i],'\n')
    print("PREDICTION:\n",predictions[i],'\n')
    print("ACTUAL SENTIMENT:\n",sentiments[i])

    print("}\n\n")

