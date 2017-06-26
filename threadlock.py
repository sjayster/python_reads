#! /usr/bin/python

import threading
import time
import random


class Parent(object):

    def __init__(self, number):
        self.number = number
        self.event = threading.Event()

    def printnums(self):
        time.sleep(1)
        for i in range(self.number * 2):
            print i
            if i >= 5 and i < 15:
                self.event.set()
            if i == 15:
                print "clearing event"
                self.event.clear()
            time.sleep(1)

    def eventing(self):
        while True:
            if not self.event.isSet():
                print "In eventing function. Event not set"
            if self.number == 20:
                print "hit 20"
                exit(0)
            time.sleep(2)

p = Parent(10)
print "Game start"
t = threading.Thread(target=p.printnums)
t.start()
time.sleep(3)
t = threading.Thread(target=p.eventing)
t.start()
