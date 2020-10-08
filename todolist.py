from sqlalchemy import Column, Integer, String, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def add_task():
    """ adds the input to the task database """

    new_row = Table(task=input('Enter task\n'))
    session.add(new_row)
    session.commit()
    print("The task has been added!\n")


def printing_tasks():
    """ Prints out all tasks from the task database """

    rows = session.query(Table).all()

    print('Today:')
    if rows:
        print('\n'.join([str(row.id) + '. ' + row.task for row in rows]))
    else:
        print('Nothing to do!')
    print()


while True:
    menu = input("1) Today's tasks\n2) Add task\n0) Exit\n")
    if menu == '1':
        printing_tasks()
    if menu == '2':
        add_task()
    if menu == '0':
        print('\nBye!')
        exit()
