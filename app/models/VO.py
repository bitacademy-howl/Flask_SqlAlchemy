from sqlalchemy import Column, Integer, String, Boolean

###############################################################################################################
# 외래키 설정의 실제 데이터베이스 쿼리
# constraint fk_id foreign key( id ) references mytable ( id ) on delete cascade
###############################################################################################################

class Music(Base):
    __tablename__ = 'Music'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    Music_ID = Column(Integer, primary_key=True, unique=True)
    Title = Column(String)
    Genre = Column(String)

    # 기타 속성들...
    Composer = Column(String)
    Lyricist = Column(String)
    Hash_Tags = Column(String, nullable=True)

    # Album Table
    FK_Album_ID = Column(Integer)
    Album = Column(String)

    # Singer Table
    FK_Singer_ID = Column(Integer)
    Singer = Column(Integer)
    IsGroup = Column(Boolean)

    def __init__(self, Music_ID, Title, Album):
        self.Music_ID = Music_ID
        self.Title = Title
        self.Album = Album

    def __repr__(self):
        return "<User('%s', '%s', '%s')>" % (self.name, self.fullname, self.password)


class Album(Base):
    __tablename__ = 'Album'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    
    # PK
    Album_ID = Column(Integer)
    
    # 속성들
    Album = Column(String)
    Release_Date = Column(Integer)

    # FK
    Singer_ID = Column(Integer)

class Singer(Base):
    __tablename__ = 'Singer'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    # PK
    Singer_ID = Column(Integer)
    Singer = Column(String)
    IsGroup = Column(Boolean)