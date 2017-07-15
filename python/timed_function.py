import sched, time

scheduler = sched.scheduler(time.time, time.sleep)

def new_timed_call(calls_per_second, callback, *args, **kw):
    period = 1.0 / calls_per_second
    def reload():
        callback(*args, **kw)
        scheduler.enter(period, 0, reload, ())
    scheduler.enter(period, 0, reload, ())

#### example code ####

def p(c):
    "print the specified character"
    print(c)
new_timed_call(3, p, '3')  # print '3' three times per second
#new_timed_call(6, p, '6')  # print '6' six times per second
#snew_timed_call(9, p, '9')  # print '9' nine times per second
scheduler.run()
