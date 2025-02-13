#!/bin/bash

sudo git add .



echo "Starting code sync..."
sudo rsync -avz --exclude-from='/mnt/d/studentapi/exclude.txt' -e "ssh -i /mnt/d/studentapi/ainanbanserver.pem" /mnt/d/studentapi/ ubuntu@ec2-16-171-143-238.eu-north-1.compute.amazonaws.com:/home/ubuntu/AinanbanFastapi/

echo "Restarting FastAPI service..."
sudo ssh -i /mnt/d/studentapi/ainanbanserver.pem ubuntu@ec2-16-171-143-238.eu-north-1.compute.amazonaws.com "sudo systemctl restart fastapi.service && sudo systemctl status fastapi.service"

echo "Done!"

