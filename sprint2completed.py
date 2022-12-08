"""" time is used for the timer built below and math for the sqrt function
"""
import math
import time


# Jacob Hicks
# This program is based on an activity in a game called Runescape that I have turned into a kind of idle game.
# https://junilearning.com/blog/coding-projects/make-countdown-timer-python/ (Source of the timer)
# the lvl variable is calculated based on the code of the game that this program is based off of
# https://stackoverflow.com/questions/63437196/how-to-re-ask-for-user-input-if-user-inputted-a-non-integer-in-python
# source of the way to generate error messages rather than just breaking.
# this is just to fulfill the for and in requirement.


def main():
    """ Runs the whole game.
    """
    for x in range(1):
        print("Hello! if this is your first time,enter the value 83 for total xp, otherwise put in your total xp.")
    play = 1
    while play == 1:
        try:
            play = int(input(" Would you like to plant your tree? input 1 for yes or 2 for no: "))
        except ValueError:
            print("Invalid input, please try again.")
            continue
        else:
            if play == 2:
                print("Goodbye!")
            if play == 1:
                while play == 1:  # this just makes it so that you don't need to keep running the code.
                    while True:  # This allows the question to be repeated on improper input rather than breaking.
                        try:
                            experience = int(input("Total xp? "))
                        except ValueError:
                            print("Invalid input, please try again.")
                            continue
                        else:
                            if experience == 83:
                                print("It seems like this is your first time playing, enjoy!")
                            elif experience == 73:
                                print("One of the most iconic numbers in Runescape...")
                            elif experience == 200000000:
                                print("congrats you have completed the game :) no further experience can be gained...")
                            elif experience == 2147483647:
                                print("Liar? Or a typo? 200 Million was the limit, but here's a little easter egg, "
                                      "this is the maximum possible value in the game of runescape... kind of.")
                            elif experience <= 83:
                                print("This doesn't seem quite right, but it isn't a bug, it's just a feature.")
                            elif experience == 4600000000:
                                print("This maximum total xp possible in Old School Runescape.")
                            print("Your tree has been planted, check back soon.")
                            # These ranges are based on values from the base game.
                            level = 0
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
                            # This part is just extra to fulfill the not function requirement..
                            comparison_a = 1
                            comparison_b = 0

                            truth = not comparison_a > comparison_b
                            if not truth:
                                print("Hope you're having fun!")
                            elif Truth:
                                print("Enjoy!")
                            # by changing this value named "times" you change the duration of the timer,
                            # I plan to have it be
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
                            # the code above is a xp-remaining calc from the original game this is based off of.
                            # This would be for true levels,
                            # it does very little in this code since level is only based on milestones for this since
                            # I could not find a formula for level at xp.
                            # I plan to make it actually function in the finished product,
                            # but for now it is just a placeholder
                            print("Your xp gained was:", xp)
                            if experience < 200000000:
                                print("You total xp is: ", experience + xp, sep="  ")
                            else:
                                print("Your total xp is still 200000000,you have reached "
                                      "the maximum possible experience in this skill")
                            if experience < 200000000:
                                print("Nice!")
                                # This is just the just delta experience/xp
                            else:
                                print("What new milestones?")
                            if experience < 13034432:
                                print("Exp until level", lvl, sep=": ")
                            if lvl < 0:
                                print("Congratulations, you have gained a level")
                            else:
                                print("There are no more levels to gain :(")
                            if xp == 200:
                                print("Enjoy the Evergreen tree")
                            elif xp == 481:
                                print("Enjoy the Oak tree")
                            elif xp == 1482:
                                print("Enjoy the Willow tree")
                            elif xp == 3448:
                                print("Enjoy the Maple tree")
                            elif xp == 7151:
                                print("Enjoy the Yew tree")
                            elif xp == 13914:
                                print("Enjoy the Magic tree")
                            elif xp == 22450:
                                print("Enjoy the Redwood tree")
                            print("Hope you're having" + " fun" + ("!" * 2))
                            total_runs = math.ceil(runs)
                            run_count(count=total_runs)
                            try:
                                play = int(
                                    input(" Would you like to continue playing? Press anything but 2 for yes or 2 "
                                          "for no."
                                          " "))
                            except ValueError:
                                print("Error, improper input, I suppose we'll continue for now")
                            if play != 1:
                                print("Thank you for playing :)")
                                break


def run_count(count):
    """" Uses the parameter count
    """
    print("You only need", count, "more "
                                  "runs until a milestone,congratulations")


main()
