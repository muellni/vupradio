 #!/bin/sh

TARGET="${1}"

# start MPD earlier
mv ${TARGET}/etc/init.d/S95mpd ${TARGET}/etc/init.d/S45mpd

exit 0
