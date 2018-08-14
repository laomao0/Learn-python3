# Class Hierarchy
# * Map
#  - next_scene 功能函数
#  - opening_scene
# * Engine
#  - play
# * Scene
#  - enter
#  * Death 子类
#  * Central Corridor
#  * Laser Weapon Armory
#  * The Bridge
#  * Escape Pod
# * Human
#   - attack
#   - defend
#   * Hero
#   * Monster


from sys import exit
from random import randint
from textwrap import dedent  # dedent函数用来美观的输出 多行strings
import time
import math


# 基本的Scene类
class Scene(object):

    def enter(self, hero):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)  # python中的 exit(0):无错误退出 exit(1)：有错误退出


# 基于场景的Death场景
class Death(Scene):
    quips = [
        "You died. You kinda suck at this.",
        "Your Mom would be proud...if she were smarter.",
        "Such a loser",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
    ]

    def enter(self, hero):
        # 随机输出List中的一句对失败者的话
        print(Death.quips[randint(0, len(self.quips) - 1)])
        # 这里来验证一下 使用类名字加点和使用self是不是一样的
        print(self.quips[randint(0, len(self.quips) - 1)])
        exit(1)


# 基于场景的走廊场景
class CentralCorridor(Scene):

    def enter(self, hero):
        print(dedent("""
            The Gothons of Planet Percal #25 have invaded your ship and 
            destroyed your entire crew. You are the last surviving member 
            and your lsst mission is to get the neutron destruct bomb from 
            the weapons Armory, put it in the bridge, and blow the ship up
            after getting into an escape pod.
        
            You're running down the central corridor to the Weapons Armory when
            a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume
            flowing around his hate filled body. He's blocking the door to the Armory and
            about to pull a blast you.
            """))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                Quick on the draw you yank out your blaster and fire it at the Gothon.
                His clown costume is flowing and moving around his body, which throws
                off your aim.  Your laser hits his costume but misses him entirely.  This
                completely ruins his brand new costume his mother bought him, which
                makes him fly into an insane rage and blast you repeatedly in the face until
                you are dead.  Then he eats you.
                 """))

            return 'death'

        elif action == "dodge!":
            print(dedent("""
                Like a world class boxer you dodge, weave, slip and slide right
                as the Gothon's blaster cranks a laser past your head.
                In the middle of your artful dodge your foot slips and you
                bang your head on the metal wall and pass out.
                You wake up shortly after only to die as the Gothon stomps on
                your head and eats you.
                """))

            return 'death'

        elif action == "tell a joke":
            print(dedent("""
                Lucky for you they made you learn Gothon insults in the academy.
                You tell the one Gothon joke you know:
                Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.
                The Gothon stops, tries not to laugh, then busts out laughing and can't move.
                While he's laughing you run up and shoot him square in the head
                putting him down, then jump through the Weapon Armory door.
                """))

            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'


# 基于场景的武器基地场景
class LaserWeaponArmory(Scene):

    def enter(self, hero):
        print(dedent("""
            You do a dive roll into the Weapon Armory, crouch and scan the room
            for more Gothons that might be hiding.  It's dead quiet, too quiet.
            You stand up and run to the far side of the room and find the
            neutron bomb in its container.  There's a keypad lock on the box
            and you need the code to get the bomb out.  If you get the code
            wrong 10 times then the lock closes forever and you can't
            get the bomb.  The code is 3 digits.
            """))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"  # 随机产生三个数字
        guess = input("[keypad]> ")
        guesses = 0  # 猜测次数

        while guess != code and guesses < 10:  # python 的李哦即运算符 有 and or not
            print("BZZZEDDD!")
            guesses = guesses + 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                The container clicks open and the seal breaks, letting gas out.
                You grab the neutron bomb and run as fast as you can to the
                bridge where you must place it in the right spot.
                """))
            return 'the_bridge'
        else:
            print(dedent("""
                The lock buzzes one last time and then you hear a sickening
                melting sound as the mechanism is fused together.
                You decide to sit there, and finally the Gothons blow up the
                ship from their ship and you die.
                """))
            return 'death'


class TheBridge(Scene):

    def enter(self, hero):
        print(dedent("""
            You burst onto the Bridge with the netron destruct bomb
            under your arm and surprise 5 Gothons who are trying to
            take control of the ship.  Each of them has an even uglier
            clown costume than the last.  They haven't pulled their
            weapons out yet, as they see the active bomb under your
            arm and don't want to set it off.
            """))

        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
                In a panic you throw the bomb at the group of Gothons
                and make a leap for the door.  Right as you drop it a
                Gothon shoots you right in the back killing you.
                As you die you see another Gothon frantically try to disarm
                the bomb. You die knowing they will probably blow up when
                it goes off.
                """))
            return 'death'  # 这里是在当前场景下进行选择之后，返回的是string类型的对象，如何
            # 将strings对象和 class关联起来？ 是由Map类完成
        elif action == "slowly place the bomb":
            print(dedent("""
                You point your blaster at the bomb under your arm
                and the Gothons put their hands up and start to sweat.
                You inch backward to the door, open it, and then carefully
                place the bomb on the floor, pointing your blaster at it.
                You then jump back through the door, punch the close button
                and blast the lock so the Gothons can't get out.
                Now that the bomb is placed you run to the escape pod to
                get off this tin can.
                """))
            return 'escape_pod'

        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"


class EscapePod(Scene):

    def enter(self, hero):
        print(dedent("""
            You rush through the ship desperately trying to make it to
            the escape pod before the whole ship explodes.  It seems like
            hardly any Gothons are on the ship, so your run is clear of
            interference.  You get to the chamber with the escape pods, and
            now need to pick one to take.  Some of them could be damaged
            but you don't have time to look.  There's 5 pods, which one
            do you take?
            """))

        good_pod = randint(1, 5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent(f"""
                You jump into pod {guess} and hit the eject button.
                The pod escapes out into the void of space, then
                implodes as the hull ruptures, crushing your body
                into jam jelly.
                """))

            return 'death'
        else:
            print(dedent(f"""    
                You jump into pod {guess} and hit the eject button.
                The pod easily slides out into space heading to
                the planet below.  As it flies to the planet, you look
                back and see your ship implode then explode like a
                bright star, taking out the Gothon ship at the same
                time.  You won!
                """))
            return 'finished'


class Win(Scene):
    """ Win """

    def enter(self, hero):
        print("You win! Good Job!")

        exit(0)


class Final(Scene):
    """ final fight """

    def enter(self, hero):
        # initialize a monster
        monster = Monster("Gothon")

        print(f"{hero.name}, You now came across the final boss {monster.name}")

        a_combat = Combat()

        next_stage = a_combat.combat(hero, monster)

        return next_stage


class Combat(object):

    #@staticmethod
    def combat(hero, monster):
        """ combat between two roles"""

        round = 1

        while True:
            print(dedent(f"""
                =====================================
                round : {round}
                =====================================
                Your HP: {hero.hp}
                {monster.name}'s HP: {monster.hp}
                Which action do you want to take?
                -------------------------------------
                1. attack - Attack the enemy
                2. defend - Defend from being attacked, also will recover a bit
                """))

            # 使用try来输入一个值
            try:
                action = int(input('> '))
            except ValueError:
                print("Please enter a number!")
                continue  # 如果输入的值发生了值错误类型，则再次执行输入

            # defending should be done before attacking
            if action == 2:
                hero.defend()

            # action of monster, 1/5 possibility it will defends
            monster_action = randint(1, 6)
            if monster_action == 5:
                monster.defend()

            if action == 1:
                hero.attack(monster)
            elif action == 2:
                pass
            else:
                print("No such actions!")

            # whether win or die
            if hero.hp <= 0:
                return 'death'

            if monster.hp <= 0:
                return 'win'

            hero.rest()
            monster.rest()

            round += 1


# class Engine
class Engine(object):

    def __init__(self, scene_map, hero):
        self.scene_map = scene_map
        self.hero = hero

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('win')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter(self.hero)
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()


class Map(object):
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'final_fight': Final(),
        'win': Win()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


class Human(object):
    """ class for human """

    defending = 0

    def __init__(self, name, power, hp, rate):
        self.name = name
        self.power = power
        self.hp = hp
        self.rate = rate

    def attack(self, target):

        """ attack the target """

        percent = 0
        time.sleep(1)

        if target.defending == 1:
            percent = float(self.power) / 10.0 + randint(0, 10)
            target.hp = math.floor(target.hp - percent)
        else:
            percent = float(self.power) / 5.0 + randint(0, 10)
            target.hp = math.floor(target.hp - percent)

        print(f"{self.name} attack {target.name}. {target.name}'s Hp decreased by {percent} points")

    def defend(self):
        """ be in the defending state"""
        self.defending = 1
        print(f"{self.name} is trying to defend.")

    def rest(self):

        if self.defending == 1:
            percent = self.rate * 10 + randint(0, 10)
        else:
            percent = self.rate * 2 + randint(0, 10)
        self.hp += percent
        print(f"{self.name}'s Hp increased by {percent} after rest")
        self.defending = 0


class Hero(Human):
    """ class for hero """

    def __init__(self, name):
        super(Hero, self).__init__(name, power=200, hp=1000, rate=5)


class Monster(Human):
    """ class for monster"""

    def __init__(self, name):
        super(Monster, self).__init__(name, power=250, hp=5000, rate=5)


a_map = Map('central_corridor')
a_hero = Hero('Joe')
a_game = Engine(a_map, a_hero)
a_game.play()
