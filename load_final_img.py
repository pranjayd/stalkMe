#e
import face_recognition
import glob
import pandas as pd
import pickle
from PIL import Image
import numpy as np
from tempfile import TemporaryFile


known_face_names=np.load('outfile.npy')
known_face_encodings=[]
dataset = pd.read_csv('second_year_thapar.csv',header=None)
person = dataset.iloc[0:,0:5].values

with open('dataset_faces.dat', 'rb') as f:
	faces_encoding = pickle.load(f)

known_face_encodings =faces_encoding


# Grab a single frame of video
frame = Image.open('prakhar_ask.jpeg')

# Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
b, g, r = frame.split()
rgb_frame= Image.merge("RGB", (r, g, b))

rgb_frame = np.array(rgb_frame)
#print(pix.shape)

# Find all the faces and face enqcodings in the frame of video
face_locations = face_recognition.face_locations(rgb_frame)
face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

# Loop through each face in this frame of video
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
  # See if the face is a match for the known face(s)
  matches = face_recognition.compare_faces(known_face_encodings, face_encoding,tolerance=0.508)


  print('MATCHES-FOUND-WITH:')

  total=0

  for i in range(0,len(matches)):
      if(matches[i]==True):
          print('Name: ',person[known_face_names[i]][1])
          print('Rollno: ',person[known_face_names[i]][0])
          name=str(person[known_face_names[i]][1])
          roll=str(person[known_face_names[i]][0])
          x_co=left
          y_co=bottom+10+total*33
          total=total+1

                

