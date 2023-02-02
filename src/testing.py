import pickle
import numpy as np
from src.generate_embeddings import Embeddings
from sklearn.neighbors import NearestNeighbors
import cv2


feature_list = np.array(pickle.load(open('artifacts/extracted_features/embedding.pkl','rb')))
filenames = pickle.load(open('artifacts/pickle_format_data/filenames.pkl','rb'))


# calling model
model = Embeddings.create_model()

#extracting features
normalized_result = Embeddings.extract_features('samples/bag.jpg',model)


neighbors = NearestNeighbors(n_neighbors=6, algorithm='brute',metric='euclidean')
neighbors.fit(feature_list)

distance, indices = neighbors.kneighbors([normalized_result])

print(indices)

for file in indices[0][1:6]:
    temp_img = cv2.imread(filenames[file])
    cv2.imshow('output', cv2.resize(temp_img,(150,150)))
    cv2.waitKey(0)