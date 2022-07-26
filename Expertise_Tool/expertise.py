# Do you know the number of levels Y/n
import pandas as pd
import requests
import time
import json
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

value_of_k = 0
def question():
    i = 0
    while i < 2:
        answer = input("Do you Know the Experise Level? (yes or no)")
        if any(answer.lower() == f for f in ["yes", 'y', '1', 'ye']):
            value_of_k = int(answer)
            break

        elif any(answer.lower() == f for f in ['no', 'n', '0']):
            value_of_k = 2
            break
        else:
            i += 1
            if i < 2:
                print('Please enter yes or no')
            else:
                print("Nothing done")


# question()


# Either Python or Tensorflow ?
#import the dataset for the TENSORFLOW tags from the STACKEXCHANGE API

number_of_pages = input("Do you know the number of users you want to cluster")

question()


complete_data=[]
dfs = []
for i in range (int(number_of_pages)):
    response = requests.get("https://api.stackexchange.com/2.3/search/advanced?order=desc&sort=activity&q=tensorflow,python&site=stackoverflow&filter=!*MZqiH2P51Zpclr2&pagesize=100&page=" + str(i + 1))
    newData=json.loads(response.text)
    for item in newData['items']:
        complete_data.append(item)
        dfs.append(pd.DataFrame([item]))
    print("Processed page " + str(i + 1) + ", returned " + str(response))
    time.sleep(2) # timeout not to be rate-limited
# key=BmopG%29d9Thccirg4e%29CjOw%28%28&page="+ str(page_count) + "&pagesize=100&order=desc&sort=activity&q=" +  row + "&site=stackoverflow"

df = pd.concat(dfs, ignore_index=True, sort=False)
dataStackexchange = df.to_csv('dataStackExchange.csv', encoding='utf-8', index=False)

#import the dataset for the 150 Elements
dataset_path = "dataStackExchange.csv"
dataset = pd.read_csv(dataset_path)#, error_bad_lines=False)
#print(error_bad_lines)


# Fill missing values with mean column values in the data set
dataset.fillna(dataset.mean(), inplace=True)


#select the columns you wanna train your data with SET 2:[Upvotes, Downvotes]
x = dataset.iloc[:, [4,5]].values



# when it is not-manual it is giving me an error 
kmeans5 = KMeans(n_clusters=2)
y_kmeans5 = kmeans5.fit_predict(x)
print(y_kmeans5)
dataset['cluster'] = y_kmeans5

dataset[dataset.cluster == 0].to_csv("set1_First_Cluster_Tensorflow.csv")
dataset[dataset.cluster == 1].to_csv("set1_Second_Cluster_Tensorflow.csv")




# # Kmeans clustering

# # Output a percentage