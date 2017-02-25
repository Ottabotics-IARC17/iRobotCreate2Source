import create2api
import time

bot = create2api.Create2()

bot.start()
bot.full()

bot.drive_straight(200)
time.sleep(3)
bot.turn_clockwise(200)
time.sleep(2)
bot.drive_straight(200)
time.sleep(3)

bot.drive_straight(0)
