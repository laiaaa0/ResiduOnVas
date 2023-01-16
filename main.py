import residue_bot
import time

if __name__ == "__main__":
    r = residue_bot.TelegramBotHandler()
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            break
