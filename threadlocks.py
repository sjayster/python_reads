#!/usr/bin/python
import time
import threading


class testclass(object):

    def __init__(self, name):
        self.name = name
        print self.name
        self.lock = threading.Event()

    def foo1(self):
        while True:
            print "foo1 is speaking. Acquiring lock in 10 sec by %s" % self.name
            time.sleep(10)

            # Acquiring the lock
            self.lock.set()
            print "lock acquired by foo1 object %s" % self.name
            print "I am gonna sleep for 15s. zzzzz"
            time.sleep(15)
            print "releasing lock - object %s" % self.name
            # Clear the lock. Make sure other threads can work
            self.lock.clear()

    def foo2(self):
        while True:
            if not self.lock.isSet():
                time.sleep(2)
                print "foo2 has spoken after 2 seconds by %s" % self.name
            else:
                print "locked out. foo2 unable to work. Retry after 2s"
                time.sleep(2)

    def foo3(self):
        while True:
            if not self.lock.isSet():
                time.sleep(3)
                print "foo3 has spoken after 3 seconds by %s" % self.name
            else:
                print "locked out. foo3 unable to work.. Retry after 2s"
                time.sleep(2)


if __name__ == "__main__":
    lock = threading.Lock()
    obj1 = testclass("object1")

    t1 = threading.Thread(target=obj1.foo1)
    t2 = threading.Thread(target=obj1.foo2)
    t3 = threading.Thread(target=obj1.foo3)

    t1.start()
    t2.start()
    t3.start()


"""
python threadlocks.py 

object1
foo1 is speaking. Acquiring lock in 10 sec by object1
foo2 has spoken after 2 seconds by object1
foo3 has spoken after 3 seconds by object1
foo2 has spoken after 2 seconds by object1
foo3 has spoken after 3 seconds by object1
foo2 has spoken after 2 seconds by object1
foo2 has spoken after 2 seconds by object1
foo3 has spoken after 3 seconds by object1
lock acquired by foo1 object object1
I am gonna sleep for 15s. zzzzz
foo2 has spoken after 2 seconds by object1
locked out. foo2 unable to work. Retry after 2s
foo3 has spoken after 3 seconds by object1
locked out. foo3 unable to work.. Retry after 2s
locked out. foo2 unable to work. Retry after 2s
locked out. foo3 unable to work.. Retry after 2s
locked out. foo2 unable to work. Retry after 2s
locked out. foo3 unable to work.. Retry after 2s
locked out. foo2 unable to work. Retry after 2s
locked out. foo3 unable to work.. Retry after 2s
locked out. foo2 unable to work. Retry after 2s
locked out. foo3 unable to work.. Retry after 2s
locked out. foo2 unable to work. Retry after 2s
locked out. foo3 unable to work.. Retry after 2s
locked out. foo2 unable to work. Retry after 2s
locked out. foo3 unable to work.. Retry after 2s
locked out. foo2 unable to work. Retry after 2s
releasing lock - object object1
foo1 is speaking. Acquiring lock in 10 sec by object1
foo2 has spoken after 2 seconds by object1
foo3 has spoken after 3 seconds by object1
foo2 has spoken after 2 seconds by object1
foo3 has spoken after 3 seconds by object1
foo2 has spoken after 2 seconds by object1
foo2 has spoken after 2 seconds by object1
lock acquired by foo1 object object1
I am gonna sleep for 15s. zzzzz
foo3 has spoken after 3 seconds by object1
locked out. foo3 unable to work.. Retry after 2s
foo2 has spoken after 2 seconds by object1
locked out. foo2 unable to work. Retry after 2s
locked out. foo3 unable to work.. Retry after 2s
locked out. foo2 unable to work. Retry after 2s
"""
