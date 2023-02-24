#!/usr/bin/python3
""" contains the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, line):
        return True

    def help_quit(self):
        print("Quit the command interpreter")

    def help_EOF(self):
        print("Quit the command interpreter")

    def do_EOF(self, line):
        return True

    def emptyline(self):
        return cmd.Cmd.emptyline(self)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
