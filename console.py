#!/usr/bin/python3
""" cmd module for AirBnB"""

import cmd


class HBNBCommand(cmd.Cmd):
    """cmd class"""
    prompt = '(hbnb)'

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """ Overrides the emptyline method of CMD """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
