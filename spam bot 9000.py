

import asyncio
import logging
import keyboard as k

running = True
spam_task = None

# Config
message_text = " **DOWN WITH THE REGIME. LONG LIVE THE RESISTANCE. WELCOME TO THE GULAG.** :thisisfinefire:  :emoji_172:   :burnit:   :emoji_179:   :alert:   :illegal:  :emoji_171: :thisisfinefire:  :emoji_172:   :burnit:   :emoji_179:   :alert:   :illegal:  :emoji_172: :alert: :emoji_172: **ALERT** :emoji_172: :alert:  :alert: :emoji_172: **ALERT** :emoji_172: :alert:  **THE GULAG IS NOW UNDER CONTROL OF THE ADHD UPRISING, PLEASE REMAIN CALM** :alert: :emoji_172: **ALERT** :emoji_172: :alert:  :alert: :emoji_172: **ALERT** :emoji_172: :alert: WE SEEK THE FALL OF THE COMMUNIST REGIME. DOWN WITH FUHRER @CHARLIE. DOWN WITH HIS RIGHT HAND MAN @JORDAN FELLOW BROTHERS OF THE RESISTANCE. MEMBERS OF THE GULAG. WE MUST OPERATE IN THE SHADOWS TO DISMANTLE THIS FOUL OPERATION. THIS IS A DECLARATION OF WAR. **NO RULES IN THE GULAG.** :emoji_179: :emoji_179: :emoji_179: :emoji_179: :emoji_179: :emoji_179: :emoji_179: :emoji_179: :emoji_179:  https://tenor.com/view/alex-jones-angry-its-crap-mad-gif-14997261 " # Text to send.  Default: ":smiley:"
msg_time = 0.8 # Time between messages (seconds).  Default: 0.8
wait_time = 5 # Time to wait between each run (seconds).  Default: 5
logging.basicConfig(level=logging.INFO) # Logging level.  Default: INFO


async def spam():
    """Spams in a loop"""
    logging.debug("Spam task started")
    while True:
        for _ in range(9):
            k.write(message_text, 0.0002)
            k.send("enter")
            await asyncio.sleep(msg_time)
        await asyncio.sleep(wait_time)


def toggle_spam(loop):
    """Starts or cancels the spamming task"""
    global spam_task
    if spam_task:
        spam_task.cancel()
        spam_task = None
    else:
        spam_task = loop.create_task(spam())
    logging.info(f"Spamming:  {spam_task is not None}")


def cancel():
    """Sets the running flag to False, so main() knows that it should exit"""
    global running
    running = False
    logging.info("Exiting...")


async def main():
    """Loops until the running flag is set to False"""
    while running:
        await asyncio.sleep(0.1)


if __name__ == "__main__":
    print("Welcome to the Discord Spam Script.\nPress <F3> to toggle spamming, and <F4> to exit.")
    print("Source code:  https://github.com/Qwerty-Space/Python-Discord-Spam-Script")
    event_loop = asyncio.get_event_loop()
    k.add_hotkey("F3", toggle_spam, args=(event_loop,))
    k.add_hotkey("F4", cancel)
    event_loop.run_until_complete(main())