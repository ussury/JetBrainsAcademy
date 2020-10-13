from sqlalchemy import Column, Integer, String, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    dates = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def add_task():
    """ adds the input to the task database """

    new_task = Table(task=input('\nEnter task\n'),
                     dates=datetime.strptime(input('Enter deadline\n'), '%Y-%m-%d').date())
    session.add(new_task)
    session.commit()
    print("The task has been added!\n")


def printing_today_tasks():
    """ Prints out today's tasks from the task database """

    rows = session.query(Table).filter(Table.dates == datetime.today().date()).all()

    print('\nToday ' + datetime.today().date().strftime('%d %b') + ':')
    if rows:
        print('\n'.join([str(num + 1) + '. ' + row.task for num, row in enumerate(rows)]))
    else:
        print('Nothing to do!')
    print()


def printing_all_tasks():
    """ Prints out all tasks from the task database """

    rows = session.query(Table).order_by(Table.dates).all()

    print('\nAll tasks:')
    if rows:
        print('\n'.join([f'{str(num + 1)}. {row.task}. {row.dates.day} {row.dates.strftime("%b")}'
                        for num, row in enumerate(rows)]))
    else:
        print('Nothing to do!')
    print()


def printing_week_tasks():
    """ prints all tasks for 7 days from today """

    today = datetime.today()

    for i in range(7):
        day_of_week = today + timedelta(days=i)
        rows = session.query(Table).filter(Table.dates == day_of_week.date()).all()
        print(f"\n{day_of_week.strftime('%A %d %b')}:")
        if rows:
            print('\n'.join([str(num + 1) + '. ' + row.task for num, row in enumerate(rows)]))
        else:
            print('Nothing to do!')
    print()


while True:
    menu = input("1) Today's tasks\n2) Week's tasks\n3) All tasks\n4) Add task\n0) Exit\n")
    if menu == '1':
        printing_today_tasks()
    if menu == '2':
        printing_week_tasks()
    if menu == '3':
        printing_all_tasks()
    if menu == '4':
        add_task()
    if menu == '0':
        print('\nBye!')
        exit()
