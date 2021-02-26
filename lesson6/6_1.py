class TrafficLight:
    __color = 0
    __time_color = 0
    __stop = 0

    def running(self):
        while True:
            TrafficLight.__stop += 1
            if TrafficLight.__time_color <= 7:
                self.__color = 'red'
                print('red')
                TrafficLight.__time_color += 1
                if TrafficLight.__time_color <= 9:
                    self.__color = 'yellow'
                    print('yellow')
                    TrafficLight.__time_color += 1
                    if TrafficLight.__time_color <= 18:
                        self.__color = 'green'
                        print('green')
                        TrafficLight.__time_color += 1
                        TrafficLight.__time_color = 0
                        if TrafficLight.__stop == 5:
                            break


tl = TrafficLight()
tl.running()
