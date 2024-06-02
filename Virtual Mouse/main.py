import cv2
import mediapipe as mp
import pyautogui
hand_detector = mp.solutions.hands.Hands()
drawing = mp.solutions.drawing_utils
sw,sh = pyautogui.size()
cam = cv2.VideoCapture(0)
cam.set(3,sw+1000)
cam.set(4,sh+400)
index_y = 0
while True : 
    _,frame = cam.read()
    frame = cv2.flip(frame,1)
    fwidth , fheight , _  = frame.shape
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands : 
            drawing.draw_landmarks(frame,hand)
            landmarks = hand.landmark
            for id,landmark in enumerate(landmarks) :
                x = int(landmark.x*fwidth)
                y = int(landmark.y*fheight)
                if id == 8  : 
                    index_x = sw/fwidth*x
                    index_y = sh/fheight*y
                    pyautogui.moveTo(index_x,index_y)
                if id == 4  : 
                    thumb_x = sw/fwidth*x
                    thumb_y = sh/fheight*y
                    if abs(index_y-thumb_y) < 40 :
                        pyautogui.click()
                        pyautogui.sleep(1)
    cv2.imshow("Virtual Mouse",frame)
    k =cv2.waitKey(100) & 0xff 
    if k==27: 
        break # press escape to close the loop
