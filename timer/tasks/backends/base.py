import abc


class TaskDriveBase():

    @abc.abstractmethod
    def create_collection(self, name):
        raise NotImplementedError()

    @abc.abstractmethod
    def create_task(self, task):
        raise NotImplementedError()

    @abc.abstractmethod
    def get_tasks(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def delete_task(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def update_task(self):
        raise NotImplementedError()
