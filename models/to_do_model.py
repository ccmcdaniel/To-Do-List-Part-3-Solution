import copy # used in Get Item operation for duplicating an object.
from datetime import datetime

class ToDoItem:
    id = 0
    title = ""
    desc = ""
    isComplete = False
    completeDate = None

    def __init__(self, id = 0, title = "", desc = ""):
        self.id = id
        self.title = title
        self.desc = desc

    # used to return a string representation of the class.
    # can be used to print a string version of the list.
    def __str__(self):
        str = f"{self.title}\n"
        str += f"-->{self.desc}\n"
        if(self.isComplete):
            str += f"-->Completed on {self.completeDate}\n"

        return str

    def MarkComplete(self):
        self.isComplete = True
        self.completeDate = datetime.now()


class ToDoModel:
    __items = [] # items is made private due to double underscore (__).
    __id_counter = 0

    def __str__(self):
        str = ""
        for item in self.__items:
            str += f"{item}\n"

        return str

    # CRUD - Create Operation
    def AddItem(self, item):
        if ToDoItem != None:
            item.id = self.__id_counter
            self.__id_counter += 1
            self.__items.append(item)

    # CRUD - Update Operation
    def UpdateItem(self, item):
        for i in range(len(self.__items)):
            if(self.__items[i].id == item.id):
                self.__items[i] = item
                return True
        
        return False

    # CRUD - Delete Operation
    def RemoveItem(self, id):
        for i in range(len(self.__items)):
            if(self.__items[i].id == id):
                del self.__items[i]
                return True
            
        return False
    
    # CRUD - Read Operation
    def GetItem(self, id):
        for i in range(len(self.__items)):
            if(self.__items[i].id == id):
                # This clones the object rather than returning
                # a reference.  This preserves the original object
                # and protects it from external modification.
                return copy.deepcopy(self.__items[i])

        return None
    
    def GetSize(self, id):
        return len(self.__items)
    
    def GetAllItems(self):
        # Return a deep copy of all items
        return copy.deepcopy(self.__items)


    def SetItemComplete(self, id):
        for i in range(len(self.__items)):
            if(self.__items[i].id == id):
                self.__items[i].MarkComplete()
                return True

        return False
    
    def GenerateTestData(self):
        self.AddItem(ToDoItem(title="Do the Laundry",desc="The laundry needs to be done by tonight!"))
        self.AddItem(ToDoItem(title="Wash the Dishes",desc="The dishes need to be cleaned!"))
        self.AddItem(ToDoItem(title="Take out the Trash",desc="The trash is full, take it out!"))
        self.SetItemComplete(2)
        self.AddItem(ToDoItem(title="Clean your Room",desc="Your room is filthy.  Get it Cleaned!"))
        self.AddItem(ToDoItem(title="Get Groceries",desc="We are running low on bread and sugar.  Go to the store!"))

# Test Bench.  Will only run if this file is directly
# executed and NOT when imported.
if __name__ == "__main__":
    list = ToDoModel()
    list.GenerateTestData()

    print(list)

    print(list.GetItem(3))

    list.RemoveItem(4)

    list.UpdateItem(ToDoItem(id=1, title="Wash the Dishes", desc="Also start the dishwasher"))
    print(list)



    