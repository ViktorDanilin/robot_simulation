from pynput.keyboard import Key, Listener, KeyCode, Key

class Keyboard():
    def on_press(self, key):
        #print('{0} pressed'.format(key))
        if (key == KeyCode(char='w')):
            print('go forward')
        elif (key == KeyCode(char='a')):
            print('go left')
        elif (key == KeyCode(char='d')):
            print('go right')
        elif (key == KeyCode(char='s')):
            print('go back')
        elif (key == KeyCode(char='t')):
            print('stop')  
        elif (key == Key.esc):
            exit()
    def __init__(self):
        with Listener(on_press=self.on_press) as listener:
            listener.join()
       

Keyboard()
