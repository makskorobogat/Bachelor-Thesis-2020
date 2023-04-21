from tkinter import *
import cv2
import numpy as np

def red_one():
    def findGreatesContour(contours):
        largest_area = 0
        i = 0
        total_contours = len(contours)
        while (i < total_contours):
            area = cv2.contourArea(contours[i])
            if (area > largest_area):
                largest_area = area
            i += 1
        return largest_area

    cv2.namedWindow("result")
    cap = cv2.VideoCapture(0)
    hsv_min = np.array((0, 150, 150), np.uint8)
    hsv_max = np.array((12, 255, 255), np.uint8)

    while True:
        flag, img = cap.read()
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        thresh = cv2.inRange(hsv, hsv_min, hsv_max)
        moments = cv2.moments(thresh, 1)
        dM01 = moments['m01']
        dM10 = moments['m10']
        dArea = moments['m00']
        if dArea > 100:
            x = int(dM10 / dArea)
            y = int(dM01 / dArea)
            cv2.circle(img, (x, y), 10, (0, 0, 255), -1)
            cv2.circle(thresh, (x, y), 10, (0, 0, 255), -1)
        cv2.imshow('Video', img)
        cv2.imshow('result', thresh)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        largest_area = findGreatesContour(contours)
        print(largest_area)

    cap.release()
    cv2.destroyAllWindows()

def blue_one():
    def findGreatesContour(contours):
        largest_area = 0
        i = 0
        total_contours = len(contours)
        while (i < total_contours):
            area = cv2.contourArea(contours[i])
            if (area > largest_area):
                largest_area = area
            i += 1
        return largest_area

    cv2.namedWindow("result")
    cap = cv2.VideoCapture(0)
    hsv_min = np.array((104, 139, 102), np.uint8)
    hsv_max = np.array((128, 255, 255), np.uint8)

    while True:
        flag, img = cap.read()
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        thresh = cv2.inRange(hsv, hsv_min, hsv_max)
        moments = cv2.moments(thresh, 1)
        dM01 = moments['m01']
        dM10 = moments['m10']
        dArea = moments['m00']
        if dArea > 100:
            x = int(dM10 / dArea)
            y = int(dM01 / dArea)
            cv2.circle(img, (x, y), 10, (0, 0, 255), -1)
            cv2.circle(thresh, (x, y), 10, (0, 0, 255), -1)
        cv2.imshow('Video', img)
        cv2.imshow('result', thresh)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        largest_area = findGreatesContour(contours)
        print(largest_area)

    cap.release()
    cv2.destroyAllWindows()

def green_one():
    def findGreatesContour(contours):
        largest_area = 0
        i = 0
        total_contours = len(contours)
        while (i < total_contours):
            area = cv2.contourArea(contours[i])
            if (area > largest_area):
                largest_area = area
            i += 1
        return largest_area

    cv2.namedWindow("result")
    cap = cv2.VideoCapture(0)
    hsv_min = np.array((42, 42, 97), np.uint8)
    hsv_max = np.array((84, 255, 255), np.uint8)

    while True:
        flag, img = cap.read()
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        thresh = cv2.inRange(hsv, hsv_min, hsv_max)
        moments = cv2.moments(thresh, 1)
        dM01 = moments['m01']
        dM10 = moments['m10']
        dArea = moments['m00']
        if dArea > 100:
            x = int(dM10 / dArea)
            y = int(dM01 / dArea)
            cv2.circle(img, (x, y), 10, (0, 0, 255), -1)
            cv2.circle(thresh, (x, y), 10, (0, 0, 255), -1)
        cv2.imshow('Video', img)
        cv2.imshow('result', thresh)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        largest_area = findGreatesContour(contours)
        print(largest_area)

    cap.release()
    cv2.destroyAllWindows()

def make_my_own():
    def findGreatesContour(contours):
        largest_area = 0
        i = 0
        total_contours = len(contours)
        while (i < total_contours):
            area = cv2.contourArea(contours[i])
            if (area > largest_area):
                largest_area = area
            i += 1
        return largest_area
    if __name__ == '__main__':
        def nothing(*arg):
            pass

    cv2.namedWindow("result")
    cv2.namedWindow("settings", 0)

    cap = cv2.VideoCapture(0)
    cv2.createTrackbar('h1', 'settings', 0, 255, nothing)
    cv2.createTrackbar('s1', 'settings', 0, 255, nothing)
    cv2.createTrackbar('v1', 'settings', 0, 255, nothing)
    cv2.createTrackbar('h2', 'settings', 255, 255, nothing)
    cv2.createTrackbar('s2', 'settings', 255, 255, nothing)
    cv2.createTrackbar('v2', 'settings', 255, 255, nothing)

    while True:
        flag, img = cap.read()
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        h1 = cv2.getTrackbarPos('h1', 'settings')
        s1 = cv2.getTrackbarPos('s1', 'settings')
        v1 = cv2.getTrackbarPos('v1', 'settings')
        h2 = cv2.getTrackbarPos('h2', 'settings')
        s2 = cv2.getTrackbarPos('s2', 'settings')
        v2 = cv2.getTrackbarPos('v2', 'settings')

        h_min = np.array((h1, s1, v1), np.uint8)
        h_max = np.array((h2, s2, v2), np.uint8)

        thresh = cv2.inRange(hsv, h_min, h_max)
        moments = cv2.moments(thresh, 1)
        dM01 = moments['m01']
        dM10 = moments['m10']
        dArea = moments['m00']
        if dArea > 100:
            x = int(dM10 / dArea)
            y = int(dM01 / dArea)
            cv2.circle(img, (x, y), 10, (0, 0, 255), -1)
            cv2.circle(thresh, (x, y), 10, (0, 0, 255), -1)
        cv2.imshow('Video', img)
        cv2.imshow('result', thresh)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        largest_area = findGreatesContour(contours)
        print(largest_area)

    cap.release()
    cv2.destroyAllWindows()



root = Tk()
root.title("Основное окно выбора цвета")
root.geometry("400x400")

btn1 = Button(text="Выберу сам цвет", background="#555", foreground="#ccc",
              padx="20", pady="6", font="20", command=make_my_own)

btn1.pack(side=BOTTOM)

btn2 = Button(text="Зеленый", background="#555", foreground="#ccc",
              padx="20", pady="6", font="20", command=green_one)

btn2.pack(side=RIGHT)

btn3 = Button(text="Синий", background="#555", foreground="#ccc",
              padx="20", pady="6", font="20", command=blue_one)

btn3.pack(side=LEFT)

btn4 = Button(text="Красный", background="#555", foreground="#ccc",
              padx="20", pady="6", font="20", command=red_one)

btn4.pack(side=TOP)

root.mainloop()