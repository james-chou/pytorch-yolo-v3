import cv2
from threading import Thread
import numpy as np
import pdb

class RecorderThread(Thread):
    def __init__(self, queue, path, fourcc, size):
        Thread.__init__(self)
        self.queue = queue
        self.path = path
        self.out = cv2.VideoWriter(self.path + '.avi', fourcc, 30.0, size, True)
        self.stop = False

    def run(self):
        print('im running')
        n = 0
        while not self.stop:
            frame = self.queue.get()
            # cv2.imwrite(self.path + '/' + str(n) + '.png', frame)
            #frame = (frame).astype(np.uint8)
            print('writing frame {}'.format(n))
            self.out.write(frame)
            self.queue.task_done()
            n = n+1
        self.out.release()

    def stop_thread(self):
        self.stop = True
