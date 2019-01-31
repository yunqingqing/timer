# timer

简单番茄钟实现(Pomodoro Technique),下面是使用步骤

1. clone代码

    ```bash
    git clone git@github.com:yunqingqing/timer.git
    ```

2. timer.ini文件中可以配置任务存储后端，当前只支持json文件存储,配置下你的tasks.json文件路径

    ```ini
    [tasks]
    uri = /path
    ```

3. tasks.json文件格式

    任务配置方式
    command      要执行的命令
    delay       多久之后执行(s)
    priority    delay相同时任务执行优先级
    is_period   是否为周期执行任务

    ```json
    {
        "task_name": {"command": "exo-open --launch TerminalEmulator", "delay": 10, "priority": 1, "is_period": 0}
    }
    ```

4. 安装

    ```bash
    python setup.py install
    ```

5. 启动

    ```bash
    timer
    ```
