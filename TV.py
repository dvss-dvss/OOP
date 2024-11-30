class TV:
    total = 0

    def __init__(self, channel, volume):
            self.__channel = channel
            self.__volume = volume

    @property
    def __volume(self):
        return self.__volume
    
    @property
    def __channel(self):
        return self.__channel
    
    @volume.setter
    def volume(self, volume_set):
        if volume_set >=101:
            self.__volume = 100
        elif volume_set <=0:
            self.__volume = 0
        else:
            self.__volume = volume_set
    
    @channel.setter
    def channel(self, set_channel):
        self.__channel = set_channel


    def __str__(self):
        return "Ви дивитеся канал: " + str(self.channel)+" із гучністью: " + str(self.volume)

FINISH = TV(100)
while True:
    a = input("Введіть через пробіл канал потім гучність(або нічого якщо хочете вийти):")
    if a == "":
        break
    else:
        print()
        FINISH.volume = int(a.split()[1])
        FINISH.channel = a.split()[0]
        print(FINISH)