#!/usr/bin/python3
""" contains the entry point of the command interpreter"""
import cmd
#from models.base_model import BaseModel

#models = ["BaseModel"]

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "


    """def do_create(self, model):
        if model:
            new = eval("{}()".format(model)
        elif model not in models:
            print("** class doesn't exist **")
        else:
            print("** class name missing **")"""

    def do_quit(self, line):
        return True

    def help_quit(self):
        print("Quit the command interpreter")

    def help_EOF(self):
        print("Quit the command interpreter")

    def do_EOF(self, line):
        return True

    def emptyline(self):
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
