#!/usr/bin/python3
""" contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    classes = [
            "BaseModel",
            "User"
    ]

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

    def do_all(self, line):
        arg = parse(line)
        objects = storage.all()
        if len(arg) > 0 and arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(arg) == 0:
            print([obj.__str__() for obj in objects.values()])
        else:
            print([obj.__str__() for obj in objects.values()
                if obj.__class__.__name__ == arg[0]]) 

    def do_update(self, line):
        arg = parse(line)
        objects = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif len(arg) > 0 and arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif len(arg) > 1 and "{}.{}".format(arg[0], arg[1]) not in objects:
            print("** no instance found **")
        elif len(arg) == 2:
            print("** attribute name missing **")
        elif len(arg) == 3:
            print("** value missing **")
        else:
            obj = objects["{}.{}".format(arg[0], arg[1])]
            obj.__dict__[arg[2]] = arg[3]
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
