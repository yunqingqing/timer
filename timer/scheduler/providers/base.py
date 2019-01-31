import abc


class SchedulerDriveBase():

    @abc.abstractmethod
    def add_task(self, name):
        raise NotImplementedError()

    @abc.abstractmethod
    def cancle_task(self, task):
        raise NotImplementedError()

    @abc.abstractmethod
    def get_tasks(self, task):
        raise NotImplementedError()
