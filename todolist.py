from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import sessionmaker

# создание файла базы данных
engine = create_engine('sqlite:///todo.db?check_same_thread=False')

# создаем класс модели, описывающ. таблицу в БД
# Все классы модели наследуют от Declararive класса
Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


# создаем таблицу в БД
Base.metadata.create_all(engine)

# создаем сеанс для получения доступа к БД
Session = sessionmaker(bind=engine)
session = Session()

# создаем строку в таблице
# создаем обьект класса model и передаем его add() методу
new_row = Table(task='Nothing to do!',
                deadline=datetime.strptime('10-03-2020', '%m-%d-%Y').date())
session.add(new_row)
session.commit()

# получаем все строки из таблицы с помощью query() метода
rows = session.query(Table).all()  # all() Метод возвращает все строки из таблицы в виде списка Python.

# получаем доступ к полям строк по их именам
first_row = rows[0]  # Если список строк не пустой

# print(first_row.string_field)  # Напечатает значение string_field
# print(first_row.id)  # Напечатает идентификатор строки
# print(first_row)  # Напечатает строку, возвращенную методом __repr__

# menu
menu = input("""1) Today's tasks
2) Add task
3) Exit \n""")

while True:
    if menu == '0':
        exit()
    if menu == '1':
        print(first_row)
    if menu == '2':
        pass
