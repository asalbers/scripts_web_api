Contains scripts for a web api

docker_container.sh - runs the container

main.tf - used for standing up the compute instance on gcp compute

requst_script.py - used for querying the api

run_request.sh - used for running the request_script.py 

I used a nginx container from docker hub and bind mounted the included web_api.conf config file to /etc/nginx/conf.d/ to work as the load balancer for the web_api containers and just proxied the traffic between.

docker kill -s HUP nginx - used to reload the nginx config