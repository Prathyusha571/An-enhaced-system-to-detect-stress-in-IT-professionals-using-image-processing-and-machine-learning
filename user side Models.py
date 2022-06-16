# Create your models here.
class UserRegistrationModel(models.Model):
    name = models.CharField(max_length=100)
    loginid = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.CharField(unique=True, max_length=100)
    email = models.CharField(unique=True, max_length=100)
    locality = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def _str_(self):
        return self.loginid

    class Meta:
        db_table = 'UserRegistrations'
class UserImagePredictinModel(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    loginid = models.CharField(max_length=100)
    filename = models.CharField(max_length=100)
    emotions = models.CharField(max_length=100000)
    file = models.FileField(upload_to='files/')
    cdate = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.loginid

    class Meta:
        db_table = "UserImageEmotions"
Image Classification:
from django.conf import settings
from PyEmotion import *
import cv2 as cv
class ImageExpressionDetect:
    def getExpression(self,imagepath):
        filepath = settings.MEDIA_ROOT + "\\" + imagepath
        PyEmotion()
        er = DetectFace(device='cpu', gpu_id=0)
        # Open you default camera
        # img = cv.imread('test.jpg')
        # cap = cv.VideoCapture(0)
        # ret, frame = cap.read()
        frame, emotion = er.predict_emotion(cv.imread(filepath))
        cv.imshow('Alex Corporation', frame)
        cv.waitKey(0)
        print("Hola Hi",filepath,"Emotion is ",emotion)
        return emotion

    def getLiveDetect(self):
        print("Streaming Started")
        PyEmotion()
        er = DetectFace(device='cpu', gpu_id=0)
        # Open you default camera
        cap = cv.VideoCapture(0)
        while (True):
            ret, frame = cap.read()
            frame, emotion = er.predict_emotion(frame)
            cv.imshow('Press Q to Exit', frame)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv.destroyAllWindows()