"""
    Commands:
        api get_users
        api retrieve_user <user_id>
        api delete_user <user_id>
        api update_user <user_id> <first_name> <last_name> <email> <nick_name>
        api create_user <first_name> <last_name> <email> <nick_name>
        api (-i | --interactive)
        api (-h | --help | --version)

    Options:
        -i, --interactive  Interactive Mode
        -h, --help  Show this screen and exit.
        --baud=<n>  Baudrate [default: 9600]
"""


from docopt import docopt, DocoptExit
import cmd
import os
from functions import API
api = API()


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match
            # We print a message to the user and the usage block
            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


def intro():
    os.system("clear")
    print(__doc__)


class MyAPI(cmd.Cmd):
    prompt = 'myapi>>>'

    @docopt_cmd
    def do_get_users(self, arg):
        """Usage: get_users"""
        api.get_all_users()

    @docopt_cmd
    def do_retrieve_user(self, arg):
        """Usage: retrieve_user <user_id>"""
        user_id = arg["<user_id>"]
        api.retrieve_user(user_id)

    @docopt_cmd
    def do_delete_user(self, arg):
        """Usage: delete_user <user_id>"""
        user_id = arg["<user_id>"]
        api.delete_user(user_id)

    @docopt_cmd
    def do_update_users(self, arg):
        """Usage: update_user <user_id> <first_name> <last_name> <email> <nick_name>"""
        user_id = arg["<user_id>"]
        name = arg["<first_name>"] + " " + arg["<last_name>"]
        email = arg["<email>"]
        nickname = arg["<nick_name>"]
        data = {'name': name, 'email': email,
                'name': name, 'username': nickname}
        api.update_user(user_id, data)

    @docopt_cmd
    def do_create_user(self, arg):
        """Usage: create_user <first_name> <last_name> <email> <nick_name>"""
        name = arg["<first_name>"] + " " + arg["<last_name>"]
        email = arg["<email>"]
        nickname = arg["<nick_name>"]
        data = {'name': name, 'email': email,
                'name': name, 'username': nickname}
        api.create_user(data)

    @docopt_cmd
    def do_quit(self, arg):
        """Usage: quit"""
        os.system('clear')
        print ('Application Exiting')
        exit()


if __name__ == "__main__":
    try:
        intro()
        MyAPI().cmdloop()
    except KeyboardInterrupt:
        os.system("clear")
        print('Application Exiting')
