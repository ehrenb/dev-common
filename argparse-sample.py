import argparse
import sys
#-------------------------------------------------------------------------------
some_global = None
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# SDK wrappers
def utility(param):
    pass
#-------------------------------------------------------------------------------
# CLI Functions
def foo(args):
    utility(args.helloarg, args.fooarg)

def bar(args):
    utility(args.helloarg, args.bararg)

def build(args):
    utility(args.helloarg, None)
#-------------------------------------------------------------------------------
if __name__ == '__main__':
    #-------------------------------------------------------------------------------
    # Base parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', '-v', action='store_true')
    subparser = parser.add_subparsers()

    hello_parser = subparser.add_parser('hello')
    hello_parser.add_argument('--helloarg', default='val')
    hello_parser.set_defaults(func=build)

    #-------------------------------------------------------------------------------
    # Parent parser for foo/bar, with parent argument
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument('--parent', type=int)
    #-------------------------------------------------------------------------------

    #-------------------------------------------------------------------------------
    # Children parsers inheriting from parent_parser
    foo_parser = subparser.add_parser('foo', help='foo help', parent_parsers=[parent_parser])
    foo_parser.add_argument('--fooarg', default='foodef')
    foo_parser.set_defaults(func=foo)

    bar_parser = subparser.add_parser('bar', help='bar help', parent_parsers=[parent_parser])
    bar_parser.add_argument('--bararg', '-b', action='store_true')
    bar_parser.set_defaults(func=bar)
    #-------------------------------------------------------------------------------

    args = parser.parse_args()

    log_level = logging.INFO
    if args.verbose:
        log_level = logging.DEBUG
    logging.basicConfig(level=log_level, format='[*] %(message)s')
    logger = logging.getLogger(__name__)

    #---------------------------------------
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()
    #---------------------------------------
    sys.exit()