#!/usr/bin/python3.8.x
if __name__ == '__main__':
   import hidden_4

   for i in dir(hidden_4):
       if i[:2] != "__":
           print(i)
