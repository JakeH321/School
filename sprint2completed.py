# Jacob Hicks
# This program is based on an activity in a game called Runescape that I have turned into a kind of idle game.
# https://junilearning.com/blog/coding-projects/make-countdown-timer-python/ (Source of the timer)
# the lvl variable is calculated based on the code of the game that this program is based off of
import time
import math

# this is just to fulfill the for and in requirement.
for x in range(1):
    print(
        "Hello! Please answer the question below.Enjoy: if this is your first time,enter the value 83 for total xp")

play = int(input(" Would you like to plant your tree? input 1 for yes 2 for no. "))
if play > 1:
    print("Goodbye!")
elif play < 2:
    while 1 != 10:  # this just makes it so that you don't need to keep running the code.
        experience = int(input("Total xp? "))
        if experience == 83:
            print("It seems like this is your first time playing, enjoy!")
        elif experience == 200000000:
            print("congrats you have completed the game :)")
        elif experience > 200000000:
            print("Liar? Or a typo?")
        print("Your tree has been planted, check back soon.")  # These ranges are based on values from the base game.
        if experience in range(0, 2411):
            level = 0
        if experience in range(2412, 13363):
            level = 15
        if experience in range(13364, 61512):
            level = 30
        if experience in range(61513, 273472):
            level = 45
        if experience in range(273473, 1210421):
            level = 60
        if experience in range(1210422, 13034431):
            level = 75
        if experience in range(13034432, 13034432 ** 4):
            level = 99
        else:
            level = 0

        if level == 0:
            xp = 200
            runs = ((2411 - experience) / xp)
        elif level == 15:
            xp = 481
            runs = ((13363 - experience) / xp)
        elif level == 30:
            xp = 1482
            runs = ((61512 - experience) / xp)
        elif level == 45:
            xp = 3448
            runs = ((273472 - experience) / xp)
        elif level == 60:
            xp = 7151
            runs = ((1210421 - experience) / xp)
        elif level == 75:
            xp = 13914
            runs = ((13034431 - experience) / xp)
        elif level in range(99, 101):
            xp = 22450
            runs = ((200000000 - experience) / xp)
        else:
            xp = 0
            runs = 0

        # by changing this value named "times" you change the duration of the timer, I plan to have it be
        # 900 seconds or 15 minutes.
        # for now the timer will be set to 10 for quick testing of the program.
        times = int(5)
        while times:
            minutes = times // 60
            secs = times % 60
            timer = '{:02d}:{:02d}'.format(minutes, secs)
            print(timer, end="\r")
            time.sleep(1)
            times -= 1
        lvl = int(((level + 300 * 2 ** (level / 7)) / 4 - xp))
        # the code above is a xp-remaining calc from the original game this is based off of. This would be for "true"
        # levels,
        # it does very little in this code since level is only based on milestones for this since I could not find a
        # formula for level at xp.
        # I plan to make it actually function in the finished product, but for now it is just a placeholder

        print("Your xp gained was:", xp)
        if experience < 200000000:
            print("You total xp is ", experience + xp, sep="   ")
        else:
            print("Your total xp is still 200000000, you have reached the maximum possible experience in this skill")
        if experience < 200000000:
            print("Your remaining runs until a new milestone are", runs)  # This is just the just delta experience/xp
        else:
            runs = 0
            print("What new milestones?")
        if experience < 13034432:
            print("Exp until level", lvl, sep=": ")
        else:
            print("There are no more levels to gain :(")
        if xp == 200:
            print("Enjoy the Evergreen tree")
        if xp == 481:
            print("Enjoy the Oak tree")
        if xp == 1482:
            print("Enjoy the Willow tree")
        if xp == 3448:
            print("Enjoy the Maple tree")
        if xp == 7151:
            print("Enjoy the Yew tree")
        if xp == 13914:
            print("Enjoy the Magic tree")
        if xp == 22450:
            print("Enjoy the Redwood tree")
        print("Thanks for" + " Playing" + ("!" * 2))
        # This doesn't really do that much aside from fulfill the function requirement.

        def run_count(count):

            print("You just completed", count + 1, "farm run, congratulations.")


        def main():
            total_runs = 0
            run_count(count=total_runs)


        main()
place_holder_for_else = 0
if place_holder_for_else == 1 and place_holder_for_else == 2:
    print("Hi")
else:
    print()
    # This program is just to fulfill the if-else / and requirement.
