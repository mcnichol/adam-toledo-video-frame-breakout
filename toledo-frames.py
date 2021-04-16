import cv2


def run():
    frameCount      = 0
    frameFolder     = "frames"
    filePrefix      = "toledo-frame-"
    bodycamVideo    = "Log  # 2021-1112 BWC 1.mp4"

    video = cv2.VideoCapture(bodycamVideo)

    success,frame = video.read()

    while success:
        frameCount +=1
        print("Writing frame: %s%s" % (filePrefix, f"{frameCount:05}"))
        cv2.imwrite("%s/%s%s.jpg" % (frameFolder, filePrefix, f"{frameCount:05}"), frame)
        success, frame = video.read()

if __name__ == "__main__":
    run()
