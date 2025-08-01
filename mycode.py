import curses
import random
import time

def main(stdscr):
    """
    The main function for the TypeMaster game.

    Args:
        stdscr: The standard screen object provided by curses.
    """
    curses.curs_set(1)  # Make the cursor visible
    stdscr.clear()
    stdscr.refresh()

    # Set up color pairs
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    sentences = [
        "Felix, you are a big thinker, so think big, think big about everything",
        "You believe in Krishna, good vybe and growing wealth, so talk only Krishna, talk only good vybe, talk only growing wealth",
        "Felix Sindani you were a great fellow yestartday, and are going to be an even greater fellow today, no go to it Felix, go forward",
        "Felix Sindani, meet Felix Sindani, an important, a really important person",
        "Felix, You have the ability to do a first class job, so do a first class job"
    ]

    sentence = random.choice(sentences)
    typed_text = []
    start_time = time.time()

    while True:
        stdscr.clear()

        # Display the sentence to be typed
        for i, char in enumerate(sentence):
            if i < len(typed_text):
                color = curses.color_pair(1) if typed_text[i] == char else curses.color_pair(2)
                stdscr.addstr(0, i, char, color)
            else:
                stdscr.addstr(0, i, char, curses.color_pair(3))

        # Display the user's typed text
        stdscr.addstr(1, 0, "".join(typed_text))

        # Move the cursor to the correct position
        stdscr.move(1, len(typed_text))

        stdscr.refresh()

        key = stdscr.getch()

        if key == 27:  # Exit on 'ESC' key
            break

        if key in (curses.KEY_BACKSPACE, 127, 8):
            if len(typed_text) > 0:
                typed_text.pop()
        elif len(typed_text) < len(sentence):
            typed_text.append(chr(key))

        if "".join(typed_text) == sentence:
            end_time = time.time()
            time_taken = end_time - start_time
            words_per_minute = (len(sentence.split()) / time_taken) * 60

            correct_chars = 0
            for i in range(len(typed_text)):
                if typed_text[i] == sentence[i]:
                    correct_chars += 1
            accuracy = (correct_chars / len(sentence)) * 100

            stdscr.addstr(3, 0, f"Congratulations! You completed the sentence.")
            stdscr.addstr(4, 0, f"Your WPM: {words_per_minute:.2f}")
            stdscr.addstr(5, 0, f"Your Accuracy: {accuracy:.2f}%")
            stdscr.addstr(7, 0, "Press any key to play again or 'ESC' to exit.")
            stdscr.refresh()

            key = stdscr.getch()
            if key == 27:
                break
            else:
                sentence = random.choice(sentences)
                typed_text = []
                start_time = time.time()

if __name__ == "__main__":
    curses.wrapper(main)