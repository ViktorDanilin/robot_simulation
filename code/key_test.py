from pynput.keyboard import Key, Listener, KeyCode, Key


class Keyboard():
    def on_press(self, key):
        # print('{0} pressed'.format(key))
        if key == Key.up:
            if self.last == KeyCode(char='q'):
                print('servo 1 up')
            elif self.last == KeyCode(char='r'):
                print('servo 2 up')
        elif key == Key.down:
            if self.last == KeyCode(char='q'):
                print('servo 1 down')
            elif self.last == KeyCode(char='r'):
                print('servo 2 down')
        elif (key == KeyCode(char='w')):
            print('go forward')
        elif (key == KeyCode(char='a')):
            print('go left')
        elif (key == KeyCode(char='d')):
            print('go right')
        elif (key == KeyCode(char='s')):
            print('go back')
        elif (key == KeyCode(char='t')):
            print('stop')
        elif (key == KeyCode(char='q')):
            self.last = key
            print('servo 1')
        elif (key == KeyCode(char='e')):
            self.last = key
            print('nfs')
        elif (key == KeyCode(char='r')):
            self.last = key
            print('servo 2')
        elif (key == Key.esc):
            exit()

    def __init__(self):
        self.last = None
        with Listener(on_press=self.on_press) as listener:
            listener.join()


Keyboard()