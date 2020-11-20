import numpy as np
import cv2,time,pyautogui,pyscreenshot
time.sleep(2)
pyautogui.press('f1')
pyautogui.click(button='right')

def draw_lines(img,lines):
    try:
        for line in lines:
            cords = line[0]
            cv2.line(img,(cords[0],cords[1]),(cords[2],cords[3]),[255,255,255],3)
    except:
        pass



def roi(img,vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask,vertices,255)
    masked = cv2.bitwise_and(img,mask)
    return masked

def process_img(img):
    processed_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img,threshold1=50,threshold2=150)
    processed_img = cv2.GaussianBlur(processed_img,(5,5),0)
    vertices = np.array([[10,500],[10,300], [300,200], [500,200], [800,300], [800,500]], np.int32)
    processed_img = roi(processed_img, [vertices])
    lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 180,np.array([]),100, 5)
    draw_lines(processed_img,lines)
    processed_img = cv2.cvtColor(processed_img,cv2.COLOR_GRAY2RGB)
    return processed_img
def screen_record():
    while(True):
        screen =  np.array(pyscreenshot.grab(bbox=[0,40,800,640]))
        new_screen = process_img(screen)
        #cv2.imshow('Fishing AI',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        cv2.imshow('Fishing AI',new_screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            pyautogui.press('f1')
            cv2.destroyAllWindows()
            break
screen_record()
