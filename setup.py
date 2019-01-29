import setuptools

setuptools.setup(name="timer",
                 version='0.1.0',
                 description='timer',
                 author='yunqingqing',
                 author_email='zzwzfh@gmail.com',
                 data_files=[("timer/", ["timer/timer.ini", "timer/tasks.json"])],
                 entry_points={
                     "console_scripts": [
                        'timer = timer.app:run',
                     ]
                 },
                 packages=setuptools.find_packages())
