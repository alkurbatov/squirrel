# This file is a part of Squirrel project
#
# Copyright (C) 2014, Alexander Kurbatov <sir.alkurbatov@yandex.ru>
#
# Squirrel is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Squirrel is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import sys, os, os.path
import time, sched
import re
import optparse

import core, convert

def verify(opts):
    if not opts or not opts.time or not opts.path:
        return 2

    if not os.path.isdir(opts.path):
        print >> sys.stderr, "The specified working directory does not exists", os.linesep
        return 3

    if not re.search(r"(?i)[0-9][dhm]", opts.time):
        print >> sys.stderr, "Invalid time format", os.linesep
        return 4

    return 0

def main(opts):
    parser = optparse.OptionParser("%prog -p [time] -w [path]", version="%prog 0.1")
    parser.add_option("-p", "--period", action="store", type="string",
            dest="time", help = "rotating period, e.g.: 1d10h20m")
    parser.add_option("-w", "--work-dir", action="store", type="string",
            dest="path", help = "path to working directory")
    parser.add_option("--once", action = "store_true", default = False,
            dest = "once", help = "rotate only once and then exit")

    group = optparse.OptionGroup(parser, "Dev Options")
    group.add_option("-d", "--debug", action = "store_true", default = False,
            dest = "debug", help = "enables debug mode")
    group.add_option("--dry-run", action = "store_true", default = False,
            dest = "dry_run", help = "do not delete files, only compress them")
    parser.add_option_group(group)

    (opts, args) = parser.parse_args()

    e = verify(opts)
    if e:
        parser.print_usage()
        return e

    s = sched.scheduler(time.time, time.sleep)

    try:
        t = convert.to_seconds(opts.time)

        while True:
            s.enter(t, 1, core.compress, [opts.path, opts.dry_run])
            s.run()

            if opts.once:
                break

    except KeyboardInterrupt:
        print >> sys.stdout, "Keyboard interrupt received, shutting down..."

    except SystemExit:
        raise

    except Exception, e:
        print >> sys.stderr, repr(e)

        if opts.debug:
            raise

        return 1

    finally:
        for v in s.queue:
            s.cancel(v)

    return 0

if __name__ == "__main__" :
    sys.exit(main(sys.argv[1:]))

