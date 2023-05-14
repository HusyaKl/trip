import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import random
from  sklearn.metrics.pairwise import pairwise_distances
from sklearn.metrics.pairwise import cosine_similarity
import os


cs = pd.read_csv(os.path.dirname(os.path.abspath(__file__))+'/dataset1.csv')
rs = pd.read_csv(os.path.dirname(os.path.abspath(__file__))+'/restaurants_for_model.csv')
br = pd.read_csv(os.path.dirname(os.path.abspath(__file__))+'/bars_for_model.csv')
ms = pd.read_csv(os.path.dirname(os.path.abspath(__file__))+'/museums_for_model.csv')
gl = pd.read_csv(os.path.dirname(os.path.abspath(__file__))+'/galleries_for_model.csv')

def run_up(df):
  threshold = 3
  value_counts = df['username'].value_counts() 
  to_remove = value_counts[value_counts <= threshold].index
  df['username'].replace(to_remove, np.nan, inplace=True)
  df.dropna()

  df = pd.pivot_table(df,
                index=['place'],
                columns=['username'],
                values='mark',
                fill_value=np.mean(df['mark']))
  def standardize(row):
      new_row = (row - row.mean()) / (row.max() - row.min())
      return new_row

  ratings_std = df.apply(standardize)
  return (ratings_std)

cs = run_up(cs)
rs = run_up(rs)
br = run_up(br)
ms = run_up(ms)
gl = run_up(gl)

class CoffeeshopsRecomendation(object):
  def __init__(self, df):
    self.df = df

  def fit(self, user):
    user_similarity = cosine_similarity(self.df.T)
    user_similarity_df = pd.DataFrame(user_similarity, index=self.df.columns, columns=self.df.columns)
    similar_score = user_similarity_df[user].sort_values(ascending=False)
    similar_users = similar_score[:10]
    users = similar_users.index.values.tolist()
    new_ratings = self.df.T.loc[users, :]
    new_ratings = new_ratings.fillna(0)
    item_similarity = cosine_similarity(new_ratings.T)
    item_similarity_df = pd.DataFrame(item_similarity, index=self.df.T.columns, columns=self.df.T.columns)
    return item_similarity_df

  
  def get_place_recommendation(self, method, rating, user):
    item_sim = self.fit(user)
    similar_score = item_sim[method] * (rating - 2.5)
    similar_score = similar_score.sort_values(ascending=False)
    return similar_score[:10]

  def predict(self, place_reduction_user, user):
    similar_method = pd.DataFrame()
    for method, rating in place_reduction_user:
      app = self.get_place_recommendation(method, rating, user)
      similar_method = similar_method.append(app, ignore_index=True)
    return similar_method.sum().sort_values(ascending=False)

coffee = CoffeeshopsRecomendation(cs)
rest = CoffeeshopsRecomendation(rs)
bar = CoffeeshopsRecomendation(br)
museum = CoffeeshopsRecomendation(ms)
gallery = CoffeeshopsRecomendation(gl)