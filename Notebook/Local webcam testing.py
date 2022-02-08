{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "00ada066",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "from keras.models import load_model\n",
    "from time import sleep\n",
    "from keras.preprocessing.image import img_to_array\n",
    "from keras.preprocessing import image\n",
    "import cv2\n",
    "import numpy as np\n",
    "\n",
    "face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') # Face Detection\n",
    "classifier =load_model('CNN_model.h5')  #Load model\n",
    "\n",
    "emotion_labels = ['Angry','Disgust','Fear','Happy','Neutral', 'Sad', 'Surprise']  # Emotion that will be predicted\n",
    "\n",
    "cap = cv2.VideoCapture(0)  ## Opening webcam\n",
    "\n",
    "\n",
    "\n",
    "while True:\n",
    "    _, frame = cap.read()\n",
    "    labels = []\n",
    "    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)\n",
    "    faces = face_classifier.detectMultiScale(gray)\n",
    "\n",
    "    for (x,y,w,h) in faces:\n",
    "        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)\n",
    "        roi_gray = gray[y:y+h,x:x+w]\n",
    "        roi_gray = cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)  ##Face Cropping for prediction\n",
    "\n",
    "\n",
    "\n",
    "        if np.sum([roi_gray])!=0:\n",
    "            roi = roi_gray.astype('float')/255.0\n",
    "            roi = img_to_array(roi)\n",
    "            roi = np.expand_dims(roi,axis=0) ## reshaping the cropped face image for prediction\n",
    "\n",
    "            prediction = classifier.predict(roi)[0]   #Prediction\n",
    "            label=emotion_labels[prediction.argmax()]\n",
    "            label_position = (x,y)\n",
    "            cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)   # Text Adding\n",
    "        else:\n",
    "            cv2.putText(frame,'No Faces',(30,80),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)\n",
    "    cv2.imshow('Emotion Detector',frame)\n",
    "    if cv2.waitKey(1) & 0xFF == ord('q'):\n",
    "        break\n",
    "\n",
    "cap.release()\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6bc2c8d6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
