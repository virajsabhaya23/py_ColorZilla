import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    cx = int(width/2)
    cy = int(height/2)

    pixel_center = hsv_frame[cy, cx]
    hue_value = pixel_center[0]

    color = "unrecognized"
    if hue_value < 5 :
        color = "RED"
    elif hue_value < 22:
        color = "ORANGE"
    elif hue_value < 33:
        color = "YELLOW"
    elif hue_value < 78:
        color = "GREEN"
    elif hue_value < 131:
        color = "BLUE"
    elif hue_value < 170:
        color = "VIOLET"
    else:
        color = "RED"

    pixel_center_bg = hsv_frame[cy, cx]
    b,g,r = int(pixel_center_bg[0]), int(pixel_center_bg[1]), int(pixel_center_bg[2])
    cv2.putText(frame, color, (10,70), 0, 2, (b,g,r), 2)
    cv2.circle(frame, (cx, cy), 5, (0,0,0), 3)

    cv2.imshow("Frame",frame)
    key = cv2.waitKey(1)
    if(key == 27):
        break

cap.release()
cv2.destroyAllWindows()