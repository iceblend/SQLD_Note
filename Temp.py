# https://gggggeun.tistory.com/77
# https://docs.sqlalchemy.org/en/14/orm/tutorial.html

from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:1234qwer@@localhost/world')

from sqlalchemy.orm import declarative_base

# SQLAlchemy 1.4 버전
# declarative_base() : 상속클래스들을 자동으로 인지하고 알아서 매핑해줌.
Base = declarative_base()

from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name, self.fullname, self.nickname)


Base.metadata.create_all(engine)


from sqlalchemy.orm import sessionmaker

session = sessionmaker()   #하나의 빈 세션 인스턴스 생성
session = sessionmaker(bind=engine)  # 엔진 넣기
