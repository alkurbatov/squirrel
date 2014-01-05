# This file is a part of Squirrel project
#
# Copyright (C) 2014, Alexander Kurbatov <sir.alkurbatov@yandex.ru>
#
# Trolls is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Trolls is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import sys, os
import time
import optparse

def rotate():
    print >> sys.stdout, "Tick"

def main(opts):
    parser = optparse.OptionParser("%prog -p [seconds] -w [path]", version="%prog 0.1")
    parser.add_option("-p", "--period", action="store", type="int",
            dest="seconds", help = "rotating period")
    parser.add_option("-w", "--work-dir", action="store", type="string",
            dest="path", help = "path to working directory")

    if not opts:
        parser.print_usage()
        return 0

    (opts, args) = parser.parse_args()

    try:
        while True:
            time.sleep(opts.seconds)
            rotate()

    except KeyboardInterrupt:
        print >> sys.stdout, "Keyboard interrupt received, shutting down..."

    except SystemExit:
        raise

    except Exception, e:
        print >> sys.stderr, repr(e)

    return 0

if __name__ == "__main__" :
    sys.exit(main(sys.argv[1:]))

