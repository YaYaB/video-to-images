# video-to-images
>Extract images from a video 


This tool helps you extract many images from a video based on a few parameters:
- step between images
- resize the output image

## Installation

OS X, Linux & Windows:

```sh
pip install git+https://github.com/YaYaB/video-to-images
```

## Usage example

```sh
usage: Split a video in several images [-h] [--path_video PATH_VIDEO]
                                       [--path_images PATH_IMAGES]
                                       [--basename BASENAME] [--step STEP]
                                       [--size SIZE [SIZE ...]]

optional arguments:
  -h, --help            show this help message and exit
  --path_video PATH_VIDEO
                        Path to the input video
  --path_images PATH_IMAGES
                        Folder path where to stored output images
  --basename BASENAME   Basename for the output images
  --step STEP           Step in ms between each image to dump (default 500ms)
  --size SIZE [SIZE ...]
                        None, max_dimension or width height, to which the
                        images must be resized (default None)
```

Please refer to [here](https://github.com/YaYaB/video-to-images/examples) for examples.


## Meta

Distributed under the Apache license v2.0. See ``LICENSE`` for more information.

[https://github.com/YaYaB/video-to-images](https://github.com/YaYaB/video-to-images)

