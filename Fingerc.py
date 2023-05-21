import random
import cv2
import cvzone
import pyttsx3
import time
from cvzone.HandTrackingModule import HandDetector

speaker = pyttsx3.init()

speaker.say("Welcome to VajiX Ai. I am Artificial Intelligent Robot. I can give number of figers from your hand. You can play with me. If you want to play with me, you can press S key from your keyboard. Then I will start the game. ")
speaker.runAndWait()

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

detector = HandDetector(maxHands=1)

timer = 0
stateResult = False
start = False
skore =[0,0]

while True:
    imgBG = cv2.imread("Resources/BG.png")
    success, img = cap.read()
    imgScale = cv2.resize(img, (0, 0),None,0.875, 0.875)
    imgScale = imgScale[:,80:480]


    #find Hands 
    hands, img = detector.findHands(imgScale)

    if start:

        if stateResult is False:
            timer = time.time() - initialTime
            cv2.putText(imgBG, str(int(timer)), (605, 435), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0 , 255), 4)

            if timer>3:
                stateResult = True
                timer =0

                if hands:
                    playerMove = None
                    hand = hands[0]
                    fingers = detector.fingersUp(hand)
                    if fingers ==[0,0,0,0,0]:
                        playerMove = 0
                    if fingers ==[1,0,0,0,0] or fingers ==[0,1,0,0,0] or fingers ==[0,0,1,0,0] or fingers ==[0,0,0,1,0] or fingers ==[0,0,0,0,1]:
                        playerMove = 1
                    if fingers ==[1,1,0,0,0] or fingers ==[0,1,1,0,0] or fingers ==[0,0,1,1,0] or fingers ==[0,0,0,1,1] or fingers ==[1,0,0,0,1] or fingers ==[1,0,0,1,0] or fingers ==[0,1,0,0,1] or fingers ==[0,1,0,1,0] or fingers ==[0,0,1,0,1] or fingers ==[0,0,1,1,0] or fingers ==[1,0,1,0,0] or fingers ==[1,1,0,0,0]:
                        playerMove = 2
                    if fingers ==[1,1,1,0,0] or fingers ==[0,1,1,1,0] or fingers ==[0,0,1,1,1] or fingers ==[1,0,0,1,1] or fingers ==[1,1,0,0,1] or fingers ==[1,0,1,1,0] or fingers ==[0,1,0,1,1] or fingers ==[1,1,1,0,0] or fingers ==[1,0,1,0,1] or fingers ==[0,1,1,0,1]:
                        playerMove = 3
                    if fingers ==[1,1,1,1,0] or fingers ==[0,1,1,1,1] or fingers ==[1,0,1,1,1] or fingers ==[1,1,0,1,1] or fingers ==[1,1,1,0,1]:
                        playerMove = 4
                    if fingers ==[1,1,1,1,1]:
                        playerMove = 5
                    
                    

                    
                    imageAI = cv2.imread(f"Resources/{playerMove}.png",cv2.IMREAD_UNCHANGED) 
                    imgBG = cvzone.overlayPNG(imgBG, imageAI, [149, 310])
                    if(playerMove ==1):
                        speaker.say("I Can see 1 fingers from your hand")
                        speaker.runAndWait()
                    if(playerMove ==2):
                        speaker.say("I Can see 2 fingers from your hand")
                        speaker.runAndWait()
                    if(playerMove ==3):
                        speaker.say("I Can see 3 fingers from your hand")
                        speaker.runAndWait()
                    if(playerMove ==4):
                        speaker.say("I Can see 4 fingers from your hand")
                        speaker.runAndWait()
                    if(playerMove ==5):
                        speaker.say("I Can see 5 fingers from your hand")
                        speaker.runAndWait()
                    

                    

                    # if(playerMove ==1 and randomeNumber ==3) or (playerMove ==2 and randomeNumber ==1) or (playerMove ==3 and randomeNumber ==2):
                    #     skore[1] +=1
                    
                    # if(playerMove ==3 and randomeNumber ==1) or (playerMove ==1 and randomeNumber ==2) or (playerMove ==2 and randomeNumber ==3):
                    #     skore[0] +=1

                    # print(playerMove)


    imgBG[233:653, 795:1195] = imgScale

    if stateResult:
        imgBG = cvzone.overlayPNG(imgBG, imageAI, [149, 310])


    cv2.putText(imgBG, str(skore[0]), (410, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255 , 255), 6)
    cv2.putText(imgBG, str(skore[1]), (1112, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255 , 255), 6)


    
    #cv2.imshow("Image", img)
    cv2.imshow("BG", imgBG)
    #cv2.imshow("Scale", imgScale)


    key = cv2.waitKey(1)

    if key == ord('s'):
        start = True
        initialTime = time.time()
        stateResult = False