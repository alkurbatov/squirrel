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

import sys, os
import time, sched
import optparse

import core, config
import convert

def get(opts):
    c = config.Unit()

    c.parse(os.path.join(opts.config, config.name()))
    c.merge(opts)

    if c.is_invalid():
        return None

    return c

def serve(conf):
    t = convert.to_seconds(conf.delay)
    s = sched.scheduler(time.time, time.sleep)

    while True:
        for p in conf.path:
            s.enter(t, 1, core.compress, [p, conf.dry_run])

        s.run()

        if t == 0:
            break;

def main(opts):
    parser = optparse.OptionParser("%prog -p [time] -w [path]", version="%prog 0.22")
    parser.add_option("-p", "--period", action = "store", type = "string",
            dest="delay", help = "rotating period")
    parser.add_option("-w", "--work-dir", action = "store", type = "string",
            dest="path", help = "path to working directory")
    parser.add_option("-c", "--config", action = "store", type = "string",
            dest="config", default="", help = "path to configuration file")

    group = optparse.OptionGroup(parser, "Dev Options")
    group.add_option("-d", "--debug", action = "store_true", default = False,
            dest = "debug", help = "enables debug mode")
    group.add_option("--dry-run", action = "store_true",
            dest = "dry_run", help = "do not delete files, only compress them")
    parser.add_option_group(group)

    (opts, args) = parser.parse_args()

    try:
        c = get(opts)
        if not c:
            parser.print_usage()
            return 1

        serve(c)

    except KeyboardInterrupt:
        print >> sys.stdout, "Keyboard interrupt received, shutting down..."

    except SystemExit:
        raise

    except Exception, e:
        print >> sys.stderr, repr(e)

        if opts.debug:
            raise

        return 1

    return 0

if __name__ == "__main__" :
    sys.exit(main(sys.argv[1:]))

