import cv2
import sys
import mediapipe as mp
import time

class poseDetector():
    def __init__(self, mode=False,
               model_complexity=1,
               smooth_landmarks=True,
               enable_segmentation=False,
               smooth_segmentation=True,
               min_detection_confidence=0.5,
               min_tracking_confidence=0.5):
        # mediapipe的pose函数参数有改变，原视频的代码需要修改
        self.mode = mode
        self.smooth = smooth_landmarks
        self.segmentation = enable_segmentation
        self.modelCom = model_complexity
        self.smoothSeg = smooth_segmentation
        self.detectionCon = min_detection_confidence
        self.trackCon = min_tracking_confidence

        self.mPose = mp.solutions.pose
        self.pose = self.mPose.Pose(self.mode, self.smooth, self.segmentation, self.smoothSeg, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
    
    def findPose(self, img, draw=True):

        imgRGB= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.pose.process(imgRGB)
        
            
        if results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, results.pose_landmarks, self.mPose.POSE_CONNECTIONS)
        return img
            # for id, lm in enumerate(results.pose_landmarks.landmark):
            #     h, w, c = img.shape
            #     print(id, lm)
            #     cx, cy = int(lm.x*w), int(lm.y*h)
            #     cv2.circle(img, (cx,cy), 10, (255,0,0), cv2.FILLED)


def main():
    cap = cv2.VideoCapture(sys.path[0]+"/PoseVideos/2.mp4")
    #这里用相对路径"/PoseVideos/2.mp4"会找不到视频
    pTime = 0
    detector = poseDetector()

    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (70,50), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1) 
if __name__ == '__main__':
    main()