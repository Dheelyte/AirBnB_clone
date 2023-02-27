#!/usr/bin/python3
""" contains the entry point of the command interpreter"""
import cmd
import re
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    classes = [
            "BaseModel",
            "User",
            "State",
            "City",
            "Amenity",
            "Place",
            "Review"
    ]

    def do_create(self, line):
        arg = parse(line)
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new = eval(f"{arg[0]}()")
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
            
    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        argl = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

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
