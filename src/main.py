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
import time
import optparse

from datetime import datetime

from zipfile import ZipFile
from zipfile import ZIP_DEFLATED

def compress(path):
    os.chdir(path)

    t = datetime.now()
    n = t.strftime("%Y%m%d-%H%M%S") + ".zip"

    with ZipFile(n, 'w') as z:
        for f in os.listdir(path):
            if os.path.islink(f) or os.path.isdir(f):
                continue

            if os.path.splitext(f)[1] in [".zip", ".tar", ".bz2", ".gz"]:
                continue

            print >> sys.stdout, "Compressing %s..." % f
            z.write(filename = f, compress_type = ZIP_DEFLATED)

            os.unlink(f)

    print >> sys.stdout, "Archive %s was created successfully" % n

def verify(opts):
    if not opts or not opts.seconds or not opts.path:
        return 1

    if not os.path.isdir(opts.path):
        print >> sys.stderr, "The specified working directory does not exists", os.linesep
        return 2

    return 0

def main(opts):
    parser = optparse.OptionParser("%prog -p [seconds] -w [path]", version="%prog 0.1")
    parser.add_option("-p", "--period", action="store", type="int",
            dest="seconds", help = "rotating period")
    parser.add_option("-w", "--work-dir", action="store", type="string",
            dest="path", help = "path to working directory")

    (opts, args) = parser.parse_args()

    e = verify(opts)
    if e:
        parser.print_usage()
        return e

    try:
        while True:
            time.sleep(opts.seconds)
            compress(opts.path)

    except KeyboardInterrupt:
        print >> sys.stdout, "Keyboard interrupt received, shutting down..."

    except SystemExit:
        raise

    except Exception, e:
        print >> sys.stderr, repr(e)

    return 0

if __name__ == "__main__" :
    sys.exit(main(sys.argv[1:]))

