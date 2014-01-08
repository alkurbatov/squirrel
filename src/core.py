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

from datetime import datetime

from zipfile import ZipFile
from zipfile import ZIP_DEFLATED

def compress(path, dry_run):
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

            if not dry_run:
                print >> sys.stdout, "Removing %s..." % f
                os.unlink(f)

    print >> sys.stdout, "Archive %s was created successfully" % n

