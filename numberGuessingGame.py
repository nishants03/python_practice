import random
import traceback

if __name__ == "__main__":
    lowerLimit = random.randint(1, 500)
    upperLimit = random.randint(501, 1000)
    numberToBeGuessed = random.randint(lowerLimit, upperLimit)

    print(
        f"Welcome\nThis is number guessing game. You will get 10 attempts to guess number correctly, Number is ranged between {lowerLimit} - {upperLimit}")
    for i in range(10):

        TrackingDict = {"Lower Value": lowerLimit, "Exact Value": None, "Greater Value": upperLimit}
        numberGuessed = None
        try:
            numberGuessed = int(input("Enter Number:"))
            if numberGuessed == numberToBeGuessed:
                print("Congratulation, You have guessed it correctly")
                TrackingDict["Exact Value"] = numberGuessed
                break
            elif numberGuessed < numberToBeGuessed:
                print("Incorrect guess, the number is smaller than entered one")
                lowerLimit = numberGuessed
                TrackingDict["Lower Value"] = numberGuessed
            else:
                print("Incorrect guess, the number is Greater than entered one")
                upperLimit = numberGuessed
                TrackingDict["Greater Value"] = numberGuessed
            print(TrackingDict)
        except Exception as ex:
            print(f"Exception in input, please enter proper digit, you have entered '{numberGuessed}'", ex)
        print(10 - i, " Attempts remaining")

        print("Sorry, You have reached your guessing limit")
        print(lowerLimit, upperLimit, "actual number", numberToBeGuessed)
