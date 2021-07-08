#!/usr/bin/bash
END=$((SECONDS+30))
while [ $SECONDS -lt $END ]; do
    status=`curl -s -o /dev/null -w "%{http_code}" http://15.207.110.45:8080`
    if [ "$status" -eq 200 ]; then
        STARTED=1;
        echo "Service Started Successfully";
        break
    fi
    echo "Not started yet"
    sleep 2
done
if [ "$STARTED" = "" ]; then
    exit 1
fi
