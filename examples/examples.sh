# Dl a free open sourced video
wget -nc  https://gcs-vimeo.akamaized.net/exp=1573099965~acl=%2A%2F1481216989.mp4%2A~hmac=cb7ab0aa557d62ebc55dcda60de9569f4d30b489a517b4b5b2961713aff198bf/vimeo-prod-skyfire-std-us/01/2218/14/361092071/1481216989.mp4

# By default the step is 0.5s
video-to-images --path_video "1481216989.mp4" --basename image --path_images "./example_0"

# Here we take an image each 0.1s
video-to-images --path_video "1481216989.mp4" --step 100 --basename image --path_images "./example_1"

# Here we resize the image in 900x600
video-to-images --path_video "1481216989.mp4" --size 900 600 --basename image --path_images "./example_2"

# Here we resize the image by 900 for the biggest dimension and keeping the same aspect ratio
video-to-images --path_video "1481216989.mp4" --size 900 --basename image --path_images "./example_3"

