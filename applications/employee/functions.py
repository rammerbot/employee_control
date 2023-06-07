import datetime



def timetable():
    #variables para la vallidacion del horario de entrada, almuerzo y salida.
    enter_time_start = datetime.time(7,0)
    enter_time_end = datetime.time(11,59)
    lunch_time_start = datetime.time(12,0)
    lunch_time_end = datetime.time(16, 59)
    exit_time_start = datetime.time(17, 0)
    exit_time_end = datetime.time(23,0)
    register = None
    # validacion del horario

    if  datetime.datetime.now().time() >= enter_time_start and datetime.datetime.now().time() <= enter_time_end:
        register = "entry"
    elif datetime.datetime.now().time() >= lunch_time_start and datetime.datetime.now().time() <= lunch_time_end:
        register = "lunch"
    elif datetime.datetime.now().time() >= exit_time_start and datetime.datetime.now().time() <= exit_time_end:
        register = "exit"


    return register