import sys
import argparse


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
        nargs='+'
    )
    return parser


def main():
    parser = create_argument_object()
    parser = add_argument_object(parser)
    arguments = parser.parse_args()
    print(arguments)
    return


if __name__ == '__main__':
    main()
