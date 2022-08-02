from app import db, Message

all_messages = Message.query.all()
print(all_messages)

#  [Jonas - jonas@mail.com, Antanas - antanas@mail.lt, Juozas - juozukas@friends.lt, Bronius - bronka@yahoo.com]