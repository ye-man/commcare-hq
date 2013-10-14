from gevent import monkey; monkey.patch_all()
from optparse import make_option
import sys
from django.conf import settings
from pillowtop.utils import import_pillow_string
from django.core.management.base import NoArgsCommand
from pillowtop.run_pillowtop import start_pillows


class Command(NoArgsCommand):
    help = "Run pillows pillows listed in settings."
    option_list = NoArgsCommand.option_list + (
        make_option('--all',
                    action='store_true',
                    dest='run_all',
                    default=False,
                    help="Run all pillows from settings - use for local dev"),

        make_option('--pillow-key',
                    action='store',
                    dest='pillow_key',
                    default=None,
                    help="Run a specific key's pillows from the PILLOWS dict"),
    )
    def handle_noargs(self, **options):
        run_all = options['run_all']
        pillow_key = options['pillow_key']

        if not run_all and not pillow_key:
            print "\n\tError, not running all. Please specify a key from settings.PILLOWTOPS:"
            print "\t%s" % settings.PILLOWTOPS.keys()
            sys.exit()
        elif run_all:
            pillows_to_run = []
            pillows_to_run = [v for group in settings.PILLOWTOPS for k, v in group.items()]
        else:
            if pillow_key not in settings.PILLOWTOPS:
                print "\n\tError, key %s is not in settings.PILLOWTOPS, legal keys are: %s" % \
                      (pillow_key, settings.PILLOWTOPS.keys())
                sys.exit()
            else:
                pillows_to_run = settings.PILLOWTOPS[pillow_key]

        start_pillows(pillows=[import_pillow_string(x) for x in pillows_to_run])




