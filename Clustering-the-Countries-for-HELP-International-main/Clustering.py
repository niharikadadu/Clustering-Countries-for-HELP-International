# Importing module
import mysql.connector
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np

# Creating connection object
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "3600"
)

cursor = mydb.cursor()

# Opening database
cursor.execute("USE minorproject")



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

"""# Data exploration
"""
cursor.execute("select * from `country-data`")
original_data = pd.DataFrame(cursor.fetchall(), columns = ['country', 'child_mort', 'exports', 'health', 'imports', 'income', 'inflation', 'life_expec', 'total_fer', 'gdpp'])

# original_data =pd.read_csv("/content/drive/MyDrive/PRML Minor Project/Country-data.csv")

original_data.info()

original_data.describe()


# Distribution of the data
original_data.hist(bins=50, figsize=(20,15))
plt.show()

#correlation matrix
corr = original_data.corr()
sns.heatmap(corr, annot=True, cmap='viridis')

# sns.pairplot(original_data)

import plotly.express as px
fig = px.choropleth(original_data, locations="country", locationmode='country names', color="gdpp", hover_name="country", color_continuous_scale=px.colors.sequential.Plasma)
fig.show()

def func(feature):
  fig = plt.subplots(nrows = 1,ncols = 3,figsize = (25,7))
  plt.subplot(1,3,1)
  ax = sns.barplot(x = 'country',y = feature, data = original_data.sort_values(ascending = False,by = 'exports').iloc[:5],edgecolor = 'black');
  plt.title(f'Countries with High {feature} (%)')
  for rect in ax.patches:
      ax.text(rect.get_x() + rect.get_width()/2, rect.get_height(), int(rect.get_height()), 
              horizontalalignment='center', fontsize = 12)

  plt.subplot(1,3,2)
  ax = sns.barplot(x = 'country',y = feature, data = original_data.sort_values(ascending = False,by = 'exports').iloc[81:86],edgecolor = 'black');
  plt.title(f'Countries with Medial {feature} (%)')
  for rect in ax.patches:
      ax.text(rect.get_x() + rect.get_width()/2, rect.get_height(), int(rect.get_height()), 
              horizontalalignment='center', fontsize = 12)

  plt.subplot(1,3,3)
  ax = sns.barplot(x = 'country',y = feature, data = original_data.sort_values(ascending = False,by = 'exports').iloc[161:166],edgecolor = 'black');
  plt.title(f'Countries with Low {feature} (%)')
  for rect in ax.patches:
      ax.text(rect.get_x() + rect.get_width()/2, rect.get_height(), int(rect.get_height()), 
              horizontalalignment='center', fontsize = 12)
  plt.show()

func('total_fer')

func('life_expec')

func('inflation')

func('income')

func('imports')

func('health')

func('child_mort')

func('exports')

func('gdpp')


country_name=original_data['country']

# delete column country from the dataset inplace
original_data.drop('country', axis=1, inplace=True)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(original_data)
scaled_features = scaler.transform(original_data)
df_scaled = pd.DataFrame(scaled_features, columns=original_data.columns)
df_scaled.head()

# apply pca to the scaled dataset
from sklearn.decomposition import PCA
pca = PCA()
pca.fit(df_scaled)
x_pca = pca.transform(df_scaled)
x_pca.shape

plt.plot(range(1,10), pca.explained_variance_ratio_.cumsum(), marker='o', linestyle='--')
plt.xlabel('Number of components')
plt.ylabel('Cumulative explained variance')
plt.show()

"""Elbow at number of components = 5"""

pca = PCA(n_components=5)
pca.fit(df_scaled)
x_pca = pca.transform(df_scaled)
x_pca.shape

"""Applying KMeans clustering on PCA reduced dataset"""

# apply kmeans clustering
from sklearn.cluster import KMeans
kmeans_pca = KMeans()
kmeans_pca.fit(x_pca)
print(kmeans_pca.cluster_centers_)

kmeans_pca.labels_

# evaluate the clusters
from sklearn.metrics import silhouette_score
print(f"The silhouette score obtained is: {silhouette_score(x_pca, kmeans_pca.labels_)}")

# davis bouldin score
from sklearn.metrics import davies_bouldin_score
print(f"The Davies Bouldin score obtained is: {davies_bouldin_score(x_pca, kmeans_pca.labels_)}")

plt.scatter(x_pca[:,0], x_pca[:,1], c=kmeans_pca.labels_, cmap='rainbow')
plt.scatter(kmeans_pca.cluster_centers_[:,0] ,kmeans_pca.cluster_centers_[:,1], color='black', marker='x', s=100, label='Centroids')
plt.legend()
plt.show()

"""Applying KMeans clustering on originally scaled data"""

kmeans = KMeans()
kmeans.fit(df_scaled)
print(kmeans.cluster_centers_)

kmeans.labels_

# evaluate the clusters
from sklearn.metrics import silhouette_score
print(f"The silhouette score obtained is: {silhouette_score(df_scaled, kmeans.labels_)}")

# davis bouldin score
from sklearn.metrics import davies_bouldin_score
print(f"The Davies Bouldin score obtained is: {davies_bouldin_score(df_scaled, kmeans.labels_)}")

plt.scatter(df_scaled.iloc[:,0], df_scaled.iloc[:,1], c=kmeans.labels_, cmap='rainbow')
plt.scatter(kmeans.cluster_centers_[:,0] ,kmeans.cluster_centers_[:,1], color='black', marker='x', s=100, label='Centroids')
plt.legend()
plt.show()




"""

# GDPP modification

This is external information 
do it on the copy
"""

cursor.execute("select * from `developed status - sheet1`")
develop_status = pd.DataFrame(cursor.fetchall(), columns = ['Country', 'Developed status'])
# develop_status =pd.read_csv("/content/drive/MyDrive/PRML Minor Project/developed status - Sheet1.csv")

develop_status

original_data['country']=country_name

dev_status=[]
not_found=0
for i in original_data['country']:
  temp=develop_status[develop_status["Country"] == i]
  if not len(temp):
    print(i ,"not found")
    not_found+=1
  dev_status.append(np.asarray(temp['Developed status'])[0])
print(not_found, "countries NOT found")

data_copy=original_data.copy()

data_copy['gdpp']=dev_status

data_copy

"""![image.png](data:image/png;base64,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)"""

import plotly.express as px
fig = px.choropleth(data_copy, locations="country", locationmode='country names', color="gdpp", hover_name="country", color_continuous_scale=px.colors.sequential.Plasma)
fig.show()

from sklearn import preprocessing



# # Import label encoder
# from sklearn import preprocessing
  
# # label_encoder object knows how to understand word labels.
# label_encoder = preprocessing.LabelEncoder()
  
# # Encode labels in column 'species'.
# data_copy['gdpp']= label_encoder.fit_transform(data_copy['gdpp'])
  
# data_copy['gdpp'].unique()

data_copy['gdpp'] = data_copy['gdpp'].replace('L', 0)
data_copy['gdpp'] = data_copy['gdpp'].replace('LM', 1)
data_copy['gdpp'] = data_copy['gdpp'].replace('UM', 2)
data_copy['gdpp'] = data_copy['gdpp'].replace('H', 3)

data_copy

from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

data_1= data_copy.drop(['country'], axis=1)

scaled_data = scale.fit_transform(data_1)
print(scaled_data)


scaled_data= pd.DataFrame(scaled_data.T)
index_ = ["child_mort",	"exports",	"health",	"imports"	,"income",	"inflation",	"life_expec"	,"total_fer"	,"gdpp"]
scaled_data.index= index_

scaled_data= scaled_data.T


df1 = pd.DataFrame()
df1['Health'] = scaled_data['child_mort']  + (scaled_data['health']) + (scaled_data['life_expec'] ) + (scaled_data['total_fer'])
df1['Trade'] = (scaled_data['imports'] ) + (scaled_data['exports'] )
df1['Finance'] = (scaled_data['income'] ) + (scaled_data['inflation'] ) + (scaled_data['gdpp'] )

# df1["country"]= data_copy['country']




# apply kmeans clustering
from sklearn.cluster import KMeans
kmeans_feature_reduction = KMeans()
kmeans_feature_reduction.fit(df1)
print(kmeans_feature_reduction.cluster_centers_)


# evaluate the clusters
from sklearn.metrics import silhouette_score
print(f"The silhouette score obtained is: {silhouette_score(df1, kmeans_feature_reduction.labels_)}")

# davis bouldin score
from sklearn.metrics import davies_bouldin_score
print(f"The Davies Bouldin score obtained is: {davies_bouldin_score(df1, kmeans_feature_reduction.labels_)}")

plt.scatter(df1["Health"], df1["Trade"], c=kmeans_feature_reduction.labels_, cmap='rainbow')
plt.scatter(kmeans_feature_reduction.cluster_centers_[:,0] ,kmeans_feature_reduction.cluster_centers_[:,1], color='black', marker='x', s=100, label='Centroids')
plt.legend()
plt.show()

df_temp = pd.DataFrame(list(zip(list(country_name), kmeans_feature_reduction.labels_)),columns =['Country', 'Cluster'])

# !pip install geopandas
# !pip install descartes

import geopandas as gpd
import matplotlib.pyplot as plt

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

merged = world.merge(df_temp, left_on='name', right_on='Country')

fig, ax = plt.subplots(figsize=(10, 10))
merged.plot(column='Cluster', cmap='Set3', ax=ax)
plt.title('World Map with Clusters')
plt.show()

#3d plot using plotly
import plotly.express as px
fig = px.scatter_3d(df1, x='Health', y='Trade', z='Finance', color=kmeans_feature_reduction.labels_)
fig.show()

""" 
Performing DBSCAN
"""



#apply DBSCAN
from sklearn.cluster import DBSCAN
data_dimensions= df1.shape[1]
dbscan_min_samples=2*data_dimensions

#using min_samples=2*data_dimensions as suggested in the link below
#http://sefidian.com/2020/12/18/how-to-determine-epsilon-and-minpts-parameters-of-dbscan-clustering/
dbscan_feature_reduction = DBSCAN(eps=0.5, min_samples=dbscan_min_samples)
dbscan_feature_reduction.fit(df1)
print(dbscan_feature_reduction.labels_)

#plotting scatter plot
fig, ax = plt.subplots(1, 3, figsize=(15, 5))
ax[0].scatter(df1["Health"], df1["Trade"], c=dbscan_feature_reduction.labels_, cmap='rainbow')
ax[0].set_title("Health vs Trade")
ax[1].scatter(df1["Health"], df1["Finance"], c=dbscan_feature_reduction.labels_, cmap='rainbow')
ax[1].set_title("Health vs Finance")
ax[2].scatter(df1["Trade"], df1["Finance"], c=dbscan_feature_reduction.labels_, cmap='rainbow')
ax[2].set_title("Trade vs Finance")
plt.show()

#3d plot using plotly
import plotly.express as px
fig = px.scatter_3d(df1, x='Health', y='Trade', z='Finance', color=dbscan_feature_reduction.labels_)
fig.show()

#evaluate the clusters
from sklearn.metrics import silhouette_score
print(f"The silhouette score obtained is: {silhouette_score(df1, dbscan_feature_reduction.labels_)}")

# davis bouldin score
from sklearn.metrics import davies_bouldin_score
print(f"The Davies Bouldin score obtained is: {davies_bouldin_score(df1, dbscan_feature_reduction.labels_)}")

#the model above is not performing well that's why we are required to refine it

#k distance graph to find optimal eps value for our dbscan
#epsilon (ε): The value for ε can then be chosen by using a k-distance graph, plotting the distance to the k = MinPts-1 
from sklearn.neighbors import NearestNeighbors
neigh = NearestNeighbors(n_neighbors=dbscan_min_samples-1)
nbrs = neigh.fit(df1)
distances, indices = nbrs.kneighbors(df1)
distances = np.sort(distances, axis=0)
distances = distances[:,1]
plt.plot(distances)
plt.ylabel(str(dbscan_min_samples-1)+"-NN distance")
plt.xlabel("Points")
plt.show()

#running a for loop to find the optimal eps value between 1 and 2 with step size 0.05
davies_bouldin_score_list = []
silhouette_score_list = []

for i in np.arange(1,2,0.05):
    dbscan_feature_reduction = DBSCAN(eps=i, min_samples=2*data_dimensions)
    dbscan_feature_reduction.fit(df1)
    davies_bouldin_score_list.append(davies_bouldin_score(df1, dbscan_feature_reduction.labels_))
    silhouette_score_list.append(silhouette_score(df1, dbscan_feature_reduction.labels_))

#plotting the davies bouldin score
plt.plot(np.arange(1,2,0.05), davies_bouldin_score_list,color='red', linestyle='dashed', marker='o', )
plt.xlabel("eps")
plt.ylabel("davies bouldin score")
plt.show()

#plotting the silhouette score
plt.plot(np.arange(1,2,0.05), silhouette_score_list,color='blue', linestyle='dashed', marker='o', )
plt.xlabel("eps")
plt.ylabel("silhouette score")
plt.show()

#best eps value is 1.55 as it has low davies bouldin score and high silhouette score
#making the final model
dbscan_feature_reduction = DBSCAN(eps=1.55, min_samples=dbscan_min_samples)
dbscan_feature_reduction.fit(df1)
print(dbscan_feature_reduction.labels_)
#evaluate the clusters

print(f"The silhouette score obtained is: {silhouette_score(df1, dbscan_feature_reduction.labels_)}")
print(f"The Davies Bouldin score obtained is: {davies_bouldin_score(df1, dbscan_feature_reduction.labels_)}")

#plotting scatter plot
fig, ax = plt.subplots(1, 3, figsize=(15, 5))
ax[0].scatter(df1["Health"], df1["Trade"], c=dbscan_feature_reduction.labels_, cmap='rainbow')
ax[0].set_title("Health vs Trade")
ax[1].scatter(df1["Health"], df1["Finance"], c=dbscan_feature_reduction.labels_, cmap='rainbow')
ax[1].set_title("Health vs Finance")
ax[2].scatter(df1["Trade"], df1["Finance"], c=dbscan_feature_reduction.labels_, cmap='rainbow')
ax[2].set_title("Trade vs Finance")
plt.show()

#3d plot using plotly
import plotly.express as px
fig = px.scatter_3d(df1, x='Health', y='Trade', z='Finance', color=dbscan_feature_reduction.labels_)
fig.show()

"""# Performing hirerchical clustering"""

#performing hierarchical clustering
from sklearn.cluster import AgglomerativeClustering
hierarchical_clustering_feature_reduction = AgglomerativeClustering(n_clusters=3)
hierarchical_clustering_feature_reduction.fit(df1)
print(hierarchical_clustering_feature_reduction.labels_)
#evaluate the clusters
print(f"The silhouette score obtained is: {silhouette_score(df1, hierarchical_clustering_feature_reduction.labels_)}")
# davis bouldin score
print(f"The Davies Bouldin score obtained is: {davies_bouldin_score(df1, hierarchical_clustering_feature_reduction.labels_)}")

#plotting scatter plots

fig, ax = plt.subplots(1, 3, figsize=(15, 5))
ax[0].scatter(df1["Health"], df1["Trade"], c=hierarchical_clustering_feature_reduction.labels_, cmap='rainbow')
ax[0].set_title("Health vs Trade")
ax[1].scatter(df1["Health"], df1["Finance"], c=hierarchical_clustering_feature_reduction.labels_, cmap='rainbow')
ax[1].set_title("Health vs Finance")
ax[2].scatter(df1["Trade"], df1["Finance"], c=hierarchical_clustering_feature_reduction.labels_, cmap='rainbow')
ax[2].set_title("Trade vs Finance")
plt.show()

#3d plot using plotly
import plotly.express as px
fig = px.scatter_3d(df1, x='Health', y='Trade', z='Finance', color=hierarchical_clustering_feature_reduction.labels_)
fig.show()

#dendogram
plt.figure(figsize=(15,15))
import scipy.cluster.hierarchy as sch
dendrogram = sch.dendrogram(sch.linkage(df1, method = 'ward'))
plt.title('Dendrogram')
plt.xlabel('Countries')
plt.ylabel('Euclidean distances')
plt.show()

#silhouette score and davies bouldin score for hierarchical clustering
silhouette_score_list = []
davies_bouldin_score_list = []
for i in range(2,10):
    hierarchical_clustering_feature_reduction = AgglomerativeClustering(n_clusters=i)
    hierarchical_clustering_feature_reduction.fit(df1)
    silhouette_score_list.append(silhouette_score(df1, hierarchical_clustering_feature_reduction.labels_))
    davies_bouldin_score_list.append(davies_bouldin_score(df1, hierarchical_clustering_feature_reduction.labels_))
#plotting the silhouette score
plt.plot(range(2,10), silhouette_score_list, color='red', linestyle='dashed', marker='o',)
plt.xlabel("number of clusters")
plt.ylabel("silhouette score")
plt.show()
#plotting the davies bouldin score
plt.plot(range(2,10), davies_bouldin_score_list, color='blue', linestyle='dashed', marker='o',)
plt.xlabel("number of clusters")
plt.ylabel("davies bouldin score")
plt.show()

#with number of clusters as 8
hierarchical_clustering_feature_reduction = AgglomerativeClustering(n_clusters=8)
hierarchical_clustering_feature_reduction.fit(df1)
print(hierarchical_clustering_feature_reduction.labels_)
#plotting scatter plot
fig, ax = plt.subplots(1, 3, figsize=(15, 5))
ax[0].scatter(df1["Health"], df1["Trade"], c=hierarchical_clustering_feature_reduction.labels_, cmap='rainbow')
ax[0].set_title("Health vs Trade")
ax[1].scatter(df1["Health"], df1["Finance"], c=hierarchical_clustering_feature_reduction.labels_, cmap='rainbow')
ax[1].set_title("Health vs Finance")
ax[2].scatter(df1["Trade"], df1["Finance"], c=hierarchical_clustering_feature_reduction.labels_, cmap='rainbow')
ax[2].set_title("Trade vs Finance")
plt.show()

#3d plot using plotly
import plotly.express as px
fig = px.scatter_3d(df1, x='Health', y='Trade', z='Finance', color=hierarchical_clustering_feature_reduction.labels_)
fig.show()



cursor.execute("select * from `inform index - sheet1`")
inform_index = pd.DataFrame(cursor.fetchall(), columns = ['Iso3', 'CountryName', 'HA', 'VU', 'CC', 'INFORM'])

# inform_index =pd.read_csv("/content/drive/MyDrive/PRML Minor Project/Inform Index - Sheet1.csv")


inform=[]
not_found=0
for i in original_data['country']:
  temp=inform_index[inform_index["CountryName"] == i]
  if not len(temp):
    print(i ,"not found")
    not_found+=1
  inform.append(np.asarray(temp['INFORM'])[0])
print(not_found, "countries NOT found")

original_data['inform']=inform


class_inform=[]
for i in range(len(original_data)):
  if(original_data['inform'][i]>5.5):
    class_inform.append(1)
  else:
    class_inform.append(0)

original_data['class']= class_inform


label_poor= kmeans_feature_reduction.labels_[0]



label_kmeans=[]
for i in kmeans_feature_reduction.labels_:
  if (i==label_poor):
    label_kmeans.append(1)
  else:
    label_kmeans.append(0)

original_data['predicted']= label_kmeans


accuracy=0
for i in range(len(original_data)):
  if (original_data['class'][i]==original_data['predicted'][i]):
    accuracy+=1

accuracy= accuracy/ len(original_data)
print("Accuracy:", accuracy )

   
mydb.commit()
