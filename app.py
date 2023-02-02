'''
Author: Deepak Thakur
Email: deepak2009thakur@gmail.com
'''

from src.utils.all_utils import read_yaml, create_directory
import streamlit as st
import numpy as np
import os
import pickle
from PIL import Image
from src.generate_embeddings import Embeddings
from sklearn.neighbors import NearestNeighbors

config = read_yaml('config/config.yaml')
params = read_yaml('params.yaml')

artifacts = config['artifacts']
artifacts_dir = artifacts['artifacts_dir']

#upload
upload_image_dir = artifacts['upload_image_dir']
uploadn_path = os.path.join(artifacts_dir, upload_image_dir)

# pickle_format_data_dir
pickle_format_data_dir = artifacts['pickle_format_data_dir']
img_pickle_file_name = artifacts['img_pickle_file_name']

# params_path
#weight = params['base']['weight']
#include_tops = params['base']['include_top']

#loading
feature_list = np.array(pickle.load(open('artifacts/extracted_features/embedding.pkl','rb')))
filenames = pickle.load(open('artifacts/pickle_format_data/filenames.pkl','rb'))

# model
model = Embeddings.create_model()


st.title('Deep Learning Based Fashion Recommendation System')

def save_uploaded_file(uploaded_file):
    try:
        create_directory(dirs=[uploadn_path])
        with open(os.path.join(uploadn_path, uploaded_file.name),'wb') as f:
            f.write(uploaded_file.getbuffer())
        return 1
    except:
        return 0


def recommend(features, feature_list):
    neighbors = NearestNeighbors(n_neighbors=6, algorithm='brute', metric='euclidean')
    neighbors.fit(feature_list)
    distances, indices = neighbors.kneighbors([features])
    return indices


uploaded_file = st.file_uploader("Choose an image")
if uploaded_file is not None:
    if save_uploaded_file(uploaded_file):
        # display the file
        display_image = Image.open(uploaded_file)
        st.image(display_image)
        # feature extract
        normalized_result = Embeddings.extract_features(os.path.join(uploadn_path, uploaded_file.name),model)
        features = normalized_result
        #recommendation
        indices = recommend(features,feature_list)
        #show
        col1,col2,col3,col4,col5 = st.columns(5)

        with col1:
            st.image(filenames[indices[0][0]])
        with col2:
            st.image(filenames[indices[0][1]])
        with col3:
            st.image(filenames[indices[0][2]])
        with col4:
            st.image(filenames[indices[0][3]])
        with col5:
            st.image(filenames[indices[0][4]])

    else:
        st.header("some error occured in file upload")