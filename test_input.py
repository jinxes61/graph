import pygame
import pygame.locals as pl

pygame.font.init()

def getNum(key):
    if key[pl.K_SPACE]:
        return ' '

    zer = ord('0')
    for i in range (pl.K_0, pl.K_9 + 1):
        if key[i] == True:
            return chr(zer + i - pl.K_0)
    return ''

class TextInput:
    """
    This class lets the user input a piece of text, e.g. a name or a message.
    This class let's the user input a short, one-lines piece of text at a blinking cursor
    that can be moved using the arrow-keys. Delete, home and end work as well.
    """
    def __init__(
            self,
            initial_string="",
            font_family="font/comic.ttf",
            font_size=28,
            antialias=True,
            text_color=(220, 220, 220),
            cursor_color=(220, 220, 220),
            repeat_keys_initial_ms=400,
            repeat_keys_interval_ms=35,
            max_string_length=-1,
            password=False):
        """
        :param initial_string: Initial text to be displayed
        :param font_family: name or list of names for font (see pygame.font.match_font for precise format)
        :param font_size:  Size of font in pixels
        :param antialias: Determines if antialias is applied to font (uses more processing power)
        :param text_color: Color of text (duh)
        :param cursor_color: Color of cursor
        :param repeat_keys_initial_ms: Time in ms before keys are repeated when held
        :param repeat_keys_interval_ms: Interval between key press repetition when held
        :param max_string_length: Allowed length of text
        """

        # Text related vars:
        self.antialias = antialias
        self.text_color = text_color
        self.font_size = font_size
        self.max_string_length = max_string_length
        self.password = password
        self.input_string = initial_string  # Inputted text

        self.font_object = pygame.font.Font(font_family, font_size)

        # Text-surface will be created during the first update call:
        self.surface = pygame.Surface((1, 1))
        self.surface.set_alpha(0)

        # Vars to make keydowns repeat after user pressed a key for some time:
        self.keyrepeat_counters = {}  # {event.key: (counter_int, event.unicode)} (look for "***")
        self.keyrepeat_intial_interval_ms = repeat_keys_initial_ms
        self.keyrepeat_interval_ms = repeat_keys_interval_ms

        # Things cursor:
        self.cursor_surface = pygame.Surface((int(self.font_size / 20 + 1), self.font_size))
        self.cursor_surface.fill(cursor_color)
        self.cursor_position = len(initial_string)  # Inside text
        self.cursor_visible = True  # Switches every self.cursor_switch_ms ms
        self.cursor_switch_ms = 500  # /|\
        self.cursor_ms_counter = 0

        self.clock = pygame.time.Clock()
        self.key_clock = pygame.time.Clock()
        self.key_interval = 10
        self.key_counter = 0

    def update(self, events):
        if self.key_counter < self.key_interval:
            self.key_counter += 1
        else:
            self.key_counter = 0

            key = pygame.key.get_pressed()
            # If none exist, create counter for that key:
            # if event.key not in self.keyrepeat_counters:
            #     if not event.key == pl.K_RETURN: # Filters out return key, others can be added as necessary
            #         self.keyrepeat_counters[event.key] = [0, event.unicode]

            if key[pl.K_BACKSPACE] == True:
                self.input_string = (
                    self.input_string[:max(self.cursor_position - 1, 0)]
                    + self.input_string[self.cursor_position:]
                )

                # Subtract one from cursor_pos, but do not go below zero:
                self.cursor_position = max(self.cursor_position - 1, 0)

            elif key[pl.K_RETURN] == True:
                return True

            elif key[pl.K_RIGHT] == True:
                # Add one to cursor_pos, but do not exceed len(input_string)
                self.cursor_position = min(self.cursor_position + 1, len(self.input_string))

            elif key[pl.K_LEFT] == True:
                # Subtract one from cursor_pos, but do not go below zero:
                self.cursor_position = max(self.cursor_position - 1, 0)

            elif len(self.input_string) < self.max_string_length or self.max_string_length == -1:
                # If no special key is pressed, add unicode of key to input_string
                s = getNum(key)
                if (len(s) > 0):
                    self.input_string = (
                        self.input_string[:self.cursor_position]
                        + s
                        + self.input_string[self.cursor_position:]
                    )
                    self.cursor_position += len(s)  # Some are empty, e.g. K_UP
                else:
                    self.key_counter = self.key_interval



        # Update key counters:
        # for key in self.keyrepeat_counters:
        #     self.keyrepeat_counters[key][0] += self.clock.get_time()  # Update clock

        #     # Generate new key events if enough time has passed:
        #     if self.keyrepeat_counters[key][0] >= self.keyrepeat_intial_interval_ms:
        #         self.keyrepeat_counters[key][0] = (
        #             self.keyrepeat_intial_interval_ms
        #             - self.keyrepeat_interval_ms
        #         )

        #         event_key, event_unicode = key, self.keyrepeat_counters[key][1]
        #         pygame.event.post(pygame.event.Event(pl.KEYDOWN, key=event_key, unicode=event_unicode))

        # Re-render text surface:
        string = self.input_string

        self.surface = self.font_object.render(string, self.antialias, self.text_color)

        # Update self.cursor_visible
        self.cursor_ms_counter += self.clock.get_time()
        if self.cursor_ms_counter >= self.cursor_switch_ms:
            self.cursor_ms_counter %= self.cursor_switch_ms
            self.cursor_visible = not self.cursor_visible

        if self.cursor_visible:
            cursor_y_pos = self.font_object.size(self.input_string[:self.cursor_position])[0]
            # Without this, the cursor is invisible when self.cursor_position > 0:
            if self.cursor_position > 0:
                cursor_y_pos -= self.cursor_surface.get_width()
            self.surface.blit(self.cursor_surface, (cursor_y_pos, 0))

        self.clock.tick()
        return False

    def get_surface(self):
        return self.surface

    def get_text(self):
        return self.input_string

    def get_cursor_position(self):
        return self.cursor_position

    def set_text_color(self, color):
        self.text_color = color

    def set_cursor_color(self, color):
        self.cursor_surface.fill(color)

    def clear_text(self):
        self.input_string = ""
        self.cursor_position = 0



if __name__ == "__main__":
    pygame.init()

    # Create TextInput-object
    textinput = TextInput()

    screen = pygame.display.set_mode((1000, 200))
    clock = pygame.time.Clock()

    while True:
        screen.fill((225, 225, 225))

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        # Feed it with events every frame
        textinput.update(events)
        # Blit its surface onto the screen
        screen.blit(textinput.get_surface(), (10, 10))

        pygame.display.update()
        clock.tick(30)