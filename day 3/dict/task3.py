library={101:{"title":"python","author":"john","copies":5},
          102:{"title":"java","author":"jane","copies":3},
          103:{"title":"c++","author":"bob","copies":7}
         }

book_id=102
library[book_id]["copies"]-=1
print(library)