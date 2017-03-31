class SoccerPlayer(object):
    def __init__(self, name , position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number

    def __str__(self):
        return("Hello %s %s %s" %(self.name, self.position, self.back_number))

    def change_back_number(self, new_backnumber):
        self.back_number = new_backnumber

jinhyun = SoccerPlayer("jin","MF","10")
print(jinhyun)
jinhyun.change_back_number("20")
print(jinhyun)

names=["jin","kim","pack"]
positions=["MF","DF","GK"]
numbers=["10","15","20"]
obj_player = [SoccerPlayer(name,position,number) for name, position, number
            in zip(names, positions, numbers)]
print("Class Player:", obj_player[1])            
