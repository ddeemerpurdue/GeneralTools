#!/Users/ddeemer/.pyenv/versions/3.9.0/bin/python
import importlib
import os
import sys
from GeneralTools import fastaTools_programs as avail_programs
from GeneralTools import main_help as main_help
from GeneralTools import warnings
# from GeneralTools.fastaTools.fastaStats import save_fa_dict as fastStats


# Put this somewhere else
def PrintHelp(program, avail_programs):
    print(f"Main help page for {program}")


def main(command):
    '''
    First thing is to test if the argument is in our dictionary
    '''

    help_flags = ['--help', '-h', '-H']
    if len(command) < 1:
        warnings.TooFewArgumentsWarning()
    else:
        program = command[0]
        if program in help_flags:
            print(main_help)
            return 0
        elif program in avail_programs:
            print(f"Found the program: {command[0]}...continuing\n")
            # print(f"Information: {avail_programs[program]}\n")
            if any(x in help_flags for x in command) or len(command) == 1:
                # Below, a potential for another class (help)
                # print(avail_programs[program][1]['help'])
                PrintHelp(program, avail_programs)
            else:  # Run parse the arguments and run!
                print('No help flags...Moving on...\n')
                imp_mod = f"GeneralTools.fastaTools.{program}"

                # Importing the current module dynamically
                # kind of as a plugin
                current_program = importlib.import_module(imp_mod)

                # Now we need a solution to feed the correct command to the program
                parser = current_program.parse_args()
                args = parser.parse_args(command[1:])
                print(f"Parser:\n{parser}\nArgs:\n{args}")
                print(current_program.main(args))
                print('Fini!')

                return 0
        else:
            warnings.InvalidArgument(program)


if __name__ == '__main__':
    arguments = sys.argv[1:]
    # print(arguments, avail_programs)
    main(arguments)
