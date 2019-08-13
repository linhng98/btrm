import sys
import argparse
import os
import ConfigParser


def create_argument_object():
    parser = argparse.ArgumentParser(
        prog=None,
        usage=open('./resources/argument-object/usage.txt').read(),
        description=open('./resources/argument-object/description.txt').read(),
        epilog=open('./resources/argument-object/epilog.txt').read(),
        parents=[],
        formatter_class=argparse.RawDescriptionHelpFormatter,
        prefix_chars='-',
        fromfile_prefix_chars=None,
        argument_default=None,
        conflict_handler='error',
        add_help=True)
    return parser


def add_argument_object(parser):
    parser.add_argument(
        '-f', '--force',
        action='count',
        help='ignore nonexistent files and arguments, never prompt'
    )

    parser.add_argument(
        '-i',
        action='count',
        help='prompt before every removal'
    )

    parser.add_argument(
        '-I',
        action='count',
        help='''prompt once before removing more than three files, or
                when removing recursively; less intrusive than -i,
                while still giving protection against most mistakes'''
    )

    parser.add_argument(
        '--interactive',
        action='store',
        choices=['once', 'never', 'always'],
        default='always',
        help='''prompt according to WHEN: never, once (-I), or
                always (-i); without WHEN, prompt always'''
    )

    parser.add_argument(
        '--one-file-system',
        action='count',
        help='''when removing a hierarchy recursively, skip any
                directory that is on a file system different from
                that of the corresponding command line argument'''
    )

    parser.add_argument(
        '--preserve-root',
        action='store',
        choices=['yes', 'no'],
        default='yes',
        help="do not remove '/'(root directory) (default)"
    )

    parser.add_argument(
        '-r', '-R', '--recursive',
        action='count',
        help='remove directories and their contents recursively'
    )

    parser.add_argument(
        '-d', '--dir',
        action='count',
        help=' remove empty directories'
    )

    parser.add_argument(
        '--no-backup',
        action='count',
        help='remove without backup mechanism'
    )

    parser.add_argument(
        '-v', '--verbose',
        action='count',
        help='explain what is being done'
    )

    parser.add_argument(
        '--version',
        action='count',
        help='output version information and exit'
    )

    parser.add_argument(
        'filename',
        action='store',
        nargs='*'
    )
    return parser


def process_arg(arguments):

    if arguments.version is not None:   # user want to show version
        print(open('./resources/argument-object/version.txt').read())
        return

    if not arguments.filename:   # list file is empty
        print("rm: missing operand\nTry 'rm -h\--help' for more information.")
    else:
        for fname in arguments.filename:
            if not os.path.exists(fname):   # path not exist
                print(("btrm: can not remove '{0}': no such "
                       "file or directory").format(fname))


def main():
    parser = create_argument_object()
    parser = add_argument_object(parser)
    namespace_arguments = parser.parse_args()
    print(namespace_arguments)
    process_arg(namespace_arguments)
    return


if __name__ == '__main__':
    main()
