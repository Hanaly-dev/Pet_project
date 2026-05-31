from sqlalchemy import create_engine,select
from sqlalchemy.orm import sessionmaker,DeclarativeBase,mapped_column,Mapped

engine=create_engine(url='sqlite:///requests.db')

session=sessionmaker(engine)

class Base(DeclarativeBase):
    pass

class ChatRequests(Base):
    __tablename__='chat_requests'
    id:Mapped[int]=mapped_column(primary_key=True)
    ip_address:Mapped[str]=mapped_column(index=True)
    prompt:Mapped[str]
    response:Mapped[str]


def get_user_requests(ip_address:str) -> list[ChatRequests]:
    with session() as s:
        query=select(ChatRequests).filter_by(ip_address=ip_address)
        result=s.execute(query)
        return result.scalars().all()
    
def add_request_data(ip_address:str,prompt:str,response:str) -> None:
    with session() as s:
        new_request= ChatRequests(ip_address=ip_address,prompt=prompt,response=response)
        s.add(new_request)
        s.commit()

