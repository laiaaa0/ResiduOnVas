import telepot
import logging
import residue_searcher
import os
import type_to_emoji

if not os.environ.get("TELEGRAM_BOT_TOKEN"):
    raise Exception("Please define TELEGRAM_BOT_TOKEN environment variable")


class TelegramBotHandler:
    def __init__(self):
        token = os.environ.get("TELEGRAM_BOT_TOKEN")
        self.bot = telepot.Bot(token)
        self.bot.message_loop(self.handle)
        self.searcher = residue_searcher.ResidueSearcher()

    def command_from_text(self, text):
        args_list = text.split()
        if len(args_list) < 1:
            return ""
        return args_list[0]

    def rest_of_message(self, text):
        args_list = text.split()
        if len(args_list) < 2:
            return ""
        return " ".join(args_list[1:])

    def classify_command(self, residue):
        try:
            found_residue, destination = self.searcher.search(residue)
            if destination != "":
                emoji = type_to_emoji.emoji_from_type(destination)
                return f"El residu <u> {found_residue}</u> ha d'anar a {destination} {emoji}"
        except:
            print(f"Could not find residue {residue}")
        return f"No s'ha trobat cap entrada per {residue}. <a href='https://www.residuonvas.cat/ca'>Residu On Vas?</a>"

    def handle(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type != "text":
            self.bot.sendMessage(chat_id, "This is not a command!")
            return
        chat_id = msg["chat"]["id"]
        chat_text = msg["text"]
        command = self.command_from_text(chat_text)
        logging.info(f"Got command {command} from id {chat_id}")

        if command == "/onvas":
            residue = self.rest_of_message(chat_text)

            reply = self.classify_command(residue)
            self.bot.sendMessage(chat_id, reply, parse_mode="HTML")
        else:
            reply = self.classify_command(chat_text)
            self.bot.sendMessage(chat_id, reply, parse_mode="HTML")
