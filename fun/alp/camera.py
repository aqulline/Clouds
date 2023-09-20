import os
import cv2
import firebase_admin
from firebase_admin import credentials, storage

# Initialize Firebase app and storage client
cred = credentials.Certificate('/home/alpha/PycharmProjects/Clouds/fun/alp/medics-inventorry-firebase-adminsdk-jgzwk-6aec367f7e.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'gs://medics-inventorry.appspot.com'
})
bucket = storage.bucket()

# Open the camera
cap = cv2.VideoCapture(0)

# Capture a frame from the camera
ret, frame = cap.read()

# Save the image to a file
cv2.imwrite('capture.jpg', frame)

# Upload the image to Firebase Storage
blob = bucket.blob('images/capture.jpg')
blob.upload_from_filename('capture.jpg')

# Delete the local copy of the image
os.remove('capture.jpg')

# Release the camera
cap.release()
cv2.destroyAllWindows()
