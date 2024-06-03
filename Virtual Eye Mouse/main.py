import cv2
import pyautogui
import mediapipe as mp
sw , sh  = pyautogui.size()
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
while True : 
    _,frame = cam.read()
    frame = cv2.flip(frame,1)
    fwidth , fheight , _  = frame.shape
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmarks_points = output.multi_face_landmarks
    if landmarks_points : 
        landmarks = landmarks_points[0].landmark
        for id,landmark in enumerate(landmarks[474:478]) : 
            x = int(landmark.x*fwidth)
            y = int(landmark.y*fheight)
            if id ==1 : 
                screen_x = sw / fwidth *x
                screen_y = sh / fheight *y
                pyautogui.moveTo(screen_x,screen_y)
        left_eye = [landmarks[145],landmarks[159]]
        for landmark in left_eye : 
            x = int(landmark.x*fwidth)
            y = int(landmark.y*fheight)
            print(left_eye[0].y - left_eye[1].y)
        if left_eye[0].y - left_eye[1].y < 0.009 :
            pyautogui.click()
    cv2.imshow("Eye Mouse", frame)
    k = cv2.waitKey(100) & 0xff 
    if k==27: 
        break # press escape to close the camera
