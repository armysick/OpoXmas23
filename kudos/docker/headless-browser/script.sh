#!/bin/bash

while true; do
    # Run Chrome in headless mode and make a request
    timelimit -T35 -t30 google-chrome --headless=old --disable-gpu --no-sandbox  --timeout=30000 --ignore-certificate-errors https://kudos.secsy.prd.internal/kudos/002a9ee8d4fd/ --dump-dom

    # Sleep for one minute
    sleep 60
done
