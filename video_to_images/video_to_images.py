import os
import sys
import argparse
import cv2


def get_args():
    """
        Get arguments of the program
        :return: arguments parsed
    """
    parser = argparse.ArgumentParser(
        "Split a video in several images"
    )
    parser.add_argument("--path_video", type=str, help="Path to the input video", default="")
    parser.add_argument("--path_images", type=str, help="Folder path where to stored output images", default="./images")
    parser.add_argument("--basename", type=str, help="Basename for the output images", default="image")
    parser.add_argument("--step", type=int, help="Step in ms between each image to dump (default 500ms)", default=500)
    parser.add_argument("--size", type=int, nargs="+", help="None, max_dimension or width height, to which the images must be resized (default None)", default=None)

    args = parser.parse_args()
    return args


def dump_image(image, path_image):
    """
        Dump image to a file
        :param image: name of the image
        :param path_image: path where to store the image
    """
    cv2.imwrite(path_image, image)
    return


def parse_video(cap, base_path, step, size):
    """
        Parse a video file
        :param cap: capture of the video
        :param base_path: base path where to output images
        :param step: step between each image in ms
        :param size: size used to remap the image if wanted [none, max_dimension or width and height]
    """
    # Get nb of fps
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Compute how many images to skip to match the step
    nb_skip = int(step / 1000 * fps)
    index = 1
    count = -1
    while True:
        count += 1
        # Get next image
        success, frame = cap.read()

        # If no image to read anymore
        if not success:
            break

        # Skip images
        if count % nb_skip != 0:
            continue

        # Save current image
        suffix = '-{}.jpg'.format('0' + str(index) if index <= 9 else str(index))
        # Compute new height to keep aspect ratio
        if size is None:
            pass
        elif len(size) == 1:
            if frame.shape[0] >= frame.shape[1]:
                aspect_ratio = frame.shape[0] / frame.shape[1]
                new_h = int(size[0])
                new_w = int(size[0] / aspect_ratio)
            else:
                aspect_ratio = frame.shape[1] / frame.shape[0]
                new_w = int(size[0])
                new_h = int(size[0] / aspect_ratio)
            frame = cv2.resize(frame, (new_w, new_h))
        # Resize with width and height given
        elif len(size) == 2:
            frame = cv2.resize(frame, size)
        dump_image(frame, base_path + suffix)

        # Append index
        index += 1

    return


def main():
    """
        Main function of the program
    """
    # Parameters
    opt = get_args()

    assert os.path.exists(opt.path_video), "Video file does not exist"
    try:
        os.makedirs(opt.path_images)
    except Exception:
        print("Folder already exists. Overwriting it")
        pass

    assert opt.size is None or opt.size is not None and len(opt.size) <= 2, "Make sure the size indicated contains at maximum two numbers [none, max_dimension or width and height]"

    # Get base path
    base_path = os.path.join(opt.path_images, opt.basename)

    # Load video from file
    try:
        cap = cv2.VideoCapture(opt.path_video)
    except Exception as e:
        print('Video failed to be loaded:', e)
        sys.exit(0)

    # Parse video
    parse_video(cap, base_path, opt.step, opt.size)

    # Release capture
    cap.release()
    cv2.destroyAllWindows()
    
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        logger.info("Uncaught error waiting for scripts to finish")
        logger.info(e)
        raise
