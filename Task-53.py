import os.path


class HomeworkToDoList(object):

    def __init__(self):
        self.tasks = []

        if os.path.isfile('todo.txt'):
            with open('todo.txt') as f:
                self.tasks = list(f)
        else:
            storage = open('todo.txt', 'w')
            storage.close()
        pass

    def add_task(self, task):
        self.tasks.append(task)
        self.save()
        pass

    def remove_task(self, task):
        self.tasks.remove(task)
        self.save()
        pass

    def save(self):
        storage = open('todo.txt', 'w')
        for task in self.tasks:
            storage.write(task)
            storage.write('\n')
        storage.close()
        pass

    def display_tasks(self):
        print(' '.join(str(el) for el in self.tasks))
        pass


my_todo_list = HomeworkToDoList()
# my_todo_list.add_task("Лекция")
# my_todo_list.add_task("Работа")
# my_todo_list.add_task("Футбол")
my_todo_list.display_tasks()
