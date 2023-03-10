from robot import Robot


def start():
    robot = Robot(robot="my_robot_name")
    robot.say_hello()
    print("hello")


if __name__ == '__main__':
    start()
