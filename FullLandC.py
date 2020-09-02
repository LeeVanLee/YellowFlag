
import sensor, image, time, pyb
from pyb import UART

uart = UART(3, 38400)
stringout = ("buf.")
num = 0
snum = 0
cum = 0
lmean = 0
xmean = 0
Cmag = 0
ltheta = 0
cmean = 0
count = 0
scum = 0
cmag = 0
firstflag = 1
ledflag = 2

sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE) # grayscale is faster
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time = 2000)
clock = time.clock()


while(True):
   # clock.tick()
    img = sensor.snapshot().lens_corr(1.6)
    led = pyb.LED(ledflag)
    led.on()

    if ledflag == 2:
        ledflag = 3
    elif ledflag == 3:
        ledflag = 4
    elif ledflag == 4:
        ledflag = 2

 #   led = pyb.LED(4)
    led.on()
    for c in img.find_circles(threshold = 1400, x_margin = 5, y_margin = 5, r_margin = 5,
r_min = 1, r_max = 40, r_step = 1):
            cum = int(cum) +1

            img.draw_circle(c.x(), c.y(), c.r(), color = (255, 0, 0))

            cmean = (cmean + c.r())
            cmag = (cmag + c.magnitude())
          #  print("FPS %f" % clock.fps())
            scum =str(cum)
            xmean = str(cmean / cum)
            Cmag = str(cmag / cum)
            count = 1



    for l in img.find_line_segments(merge_distance = 4, max_theta_diff = 4):
            num = int(num) + 1
            img.draw_line(l.line(), color = (255, 0, 0))
            lmean = (int(lmean) + l.length())
            ltheta = (ltheta + l.theta())
            snum = str(num)
            count = 1
            mean = str(lmean / num)
            Ltheta = str(ltheta / num)

    led.off()

    if firstflag :
        time.sleep(0)
        firstflag = 0



    if count :
        print(stringout)
        stringout = ('Total-lines=' + snum + "," + 'Average-Line=' + mean + "," + "Circles=" + str(scum) + "," + 'AR=' + str(xmean) + "," + "CMag=" + str(Cmag) + "," 'ALA=' + str(Ltheta) + "?")
        uart.write(stringout)
        num= str(0)
        cum = str(0)
        snum = str(0)
        mean = str(0)
        lmean = str(0)
        count = str(0)
        Cmag = str(0)
        xmean = str(0)
        scum =str(0)
        Ltheta = str(0)
