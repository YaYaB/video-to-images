from setuptools import setup
from setuptools import find_packages


setup(name='video-to-images',
      version='0.0.1',
      description='Extract images from a video',
      author='YaYaB',
      author_email='bezzayassine@gmail.com',
      url='https://github.com/YaYaB/video-to-images',
      download_url='https://github.com/YaYaB/video-to-images',
      license='MIT',
      classifiers=['License :: MIT License',
                   'Programming Language :: Python',
                   'Operating System :: Microsoft :: Windows',
                   'Operating System :: POSIX',
                   'Operating System :: Unix',
                   'Operating System :: MacOS',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   ],
      install_requires=[],
      extras_require={},
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'video-to-images=video_to_images.video_to_images:main',
          ]},

      )

