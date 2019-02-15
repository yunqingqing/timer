import setuptools

setuptools.setup(name="timer",
                 version='0.1.0',
                 description='timer',
                 author='yunqingqing',
                 author_email='zzwzfh@gmail.com',
                 data_files=[("timer/", ["timer/timer.ini", "timer/tasks.json"])],
                 install_requires=[
                    'Click==7.0',
                    'Flask==1.0.2',
                    'itsdangerous==1.1.0',
                    'Jinja2==2.10',
                    'MarkupSafe==1.1.0',
                 ],
                 entry_points={
                     "console_scripts": [
                        'timer = timer.app:run',
                     ]
                 },
                 packages=setuptools.find_packages())
