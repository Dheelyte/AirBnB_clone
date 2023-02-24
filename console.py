#!/usr/bin/python3
""" contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    
    classes = ["BaseModel"]

    def do_create(self, line):
        arg = parse(line)
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new = eval(f"{line}()")
            print(new.id)
            storage.save()
            

    def do_show(self, line):
        arg = parse(line)
        objects = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in objects:
            print("** no instance found **")
        else:
            print(objects["{}.{}".format(arg[0], arg[1])])

    def do_destroy(self, line):
        arg = parse(line)
        objects = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in objects:
            print("** no instance found **")
        else:
            del objects["{}.{}".format(arg[0], arg[1])]
            storage.save()

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

def parse(arg):
    # Convert line argument(s) to a tuple
    return tuple(map(lambda i: i, arg.split()))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
