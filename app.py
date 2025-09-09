import os
import sys
import pickle
import streamlit as st
import numpy as np
from books_recommender.logger.log import logging
from books_recommender.config.configuration import APPConfiguration
from books_recommender.pipeline.training_pipeline import TrainingPipeline
from books_recommender.exception.exception_handler import AppException


class Recommendation():
  def __init__(self, app_config = APPConfiguration()):
    try:
      self.recommendation_config = app_config.get_model_recommendation_config()
    except Exception as e:
      raise AppException(e,sys) from e
    
  
  def fetch_poster(self, suggestions):
    try:
      book_name = []
      book_ids = []
      poster_url = []
      book_pivot = pickle.load(open(self.recommendation_config.book_pivot_serialized_object, 'rb'))
      final_rating = pickle.load(open(self.recommendation_config.final_rating_serialized_object, 'rb'))

      for book_id in suggestions[0]: # suggestions is 2D there
        name = book_pivot.index[book_id]  
        book_name.append(name)

      for name in book_name:
        id = np.where(final_rating['title'] == name)[0][0]
        book_ids.append(id)

      for id in book_ids:
        url = final_rating.iloc[id]['image_url']
        poster_url.append(url)

      return poster_url

    except Exception as e:
      raise AppException(e,sys) from e
    
  def recommend_book(self,book_name):
    try:
      book_list = []
      model = pickle.load(open(self.recommendation_config.trained_model_path, 'rb'))
      book_pivot = pickle.load(open(self.recommendation_config.book_pivot_serialized_object, 'rb'))
      book_id = np.where(book_pivot.index == book_name)[0][0]

      distance, suggestions = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=6)

      poster_url = self.fetch_poster(suggestions)

      # suggestions is 2D: (1, 6), so take the first row
      recommended_books = suggestions[0]

      for book_id in recommended_books:
        book = book_pivot.index[book_id]
        book_list.append(book)

      return book_list, poster_url
    except Exception as e:
      raise AppException(e,sys) from e
    
  def train_engine(self):
    try: 
      obj = TrainingPipeline()
      obj.start_training_pipeline()
      st.text("Training Completed.")
      logging.info("Model trained by user.")
    except Exception as e:
      raise AppException(e,sys) from e


  def recommendation_engine(self, selected_book):
    try:
      recommended_books, poster_url = self.recommend_book(selected_book)
      col1, col2, col3, col4, col5 = st.columns(5)

      with col1:
        st.text(recommended_books[1])
        st.image(poster_url[1])
      with col2:
        st.text(recommended_books[2])
        st.image(poster_url[2])
      with col3:
        st.text(recommended_books[3])
        st.image(poster_url[3])
      with col4:
        st.text(recommended_books[4])
        st.image(poster_url[4])
      with col5:
        st.text(recommended_books[5])
        st.image(poster_url[5])

    except Exception as e:
      raise AppException(e,sys) from e
    
if __name__ == "__main__":
  st.header('End to End Books Recommender System')
  st.text('This is a collaborative filtering based recommendation system!')

  # # Initialize session state
  # if 'obj' not in st.session_state:
  #   st.session_state.obj = Recommendation()

  # # Use the object from session state, don't create a new one!
  # obj = st.session_state.obj 
  obj = Recommendation()

  #Training
  if st.button('Train Recommender System'):
    obj.train_engine()

  # Check if file exists before loading
  if os.path.exists(obj.recommendation_config.book_name_serialized_object):
      book_names = pickle.load(open(obj.recommendation_config.book_name_serialized_object,'rb'))
  else:
      book_names = ["Train the system first"]
      st.warning("Please train the system first to load book names")

  selected_book = st.selectbox(
    "Type or select a book from the dropdown",
    book_names
  )

  #recommendation
  if st.button('Show Recommendation'):
    obj.recommendation_engine(selected_book)



  



