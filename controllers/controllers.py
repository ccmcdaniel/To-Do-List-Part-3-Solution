from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty
from kivy.properties import StringProperty
from kivy.utils import get_color_from_hex as hex
from kivy.app import App
from functools import partial
from models.to_do_model import ToDoItem

class MasterListView(Screen):
    to_do_items_view = ListProperty([])

    def load_screen(self):
        app = App.get_running_app()

        self.to_do_items_view = []
        items = app.model.GetAllItems()
        
        if(len(items) == 0):
            self.manager.current = "master_list_empty"
            return

        for item in items:
            conv_item = {}
            conv_item['id'] = item.id
            conv_item['title'] =  item.title
            # partial "packages" a function with a return value to be binded to on_release for each particular item.
            conv_item['on_release'] = partial(self.on_click_edit_item, item.id)

            if(item.isComplete):
                datetime_str = item.completeDate.strftime("Completed on %b %d, %Y at %H:%M:%S")
                conv_item['completed'] = datetime_str
                conv_item['completed_ind_color'] = hex("#92DD92")
            else:
                conv_item['completed'] = "Not Completed"
                conv_item['completed_ind_color'] = hex("#DD9292")

            self.to_do_items_view.append(conv_item)

        return
    
    def on_click_edit_item(self, id):
        self.manager.current = "edit_task"
        self.manager.current_screen.load_screen(id)

class MasterListEmptyView(Screen):
    pass
        
class AddNewTaskView(Screen):
    def on_press_add_task(self):
        app = App.get_running_app()
        new_item = ToDoItem()
        new_item.title = self.ids.txtTitle.text
        new_item.desc = self.ids.txtDesc.text
        app.model.AddItem(new_item)
        self.manager.current = "master_list"
        self.manager.current_screen.load_screen()

    def on_press_cancel(self):
        self.manager.current = "master_list"
        self.manager.current_screen.load_screen()

        
class EditTaskView(Screen):
    id = -1
    title = StringProperty()
    desc = StringProperty()
    item = None

    def load_screen(self, id):
        self.id = id
        
        app = App.get_running_app()
        self.item = app.model.GetItem(id)
        self.title = self.item.title
        self.desc = self.item.desc

    def on_press_save(self):
        self.item.title = self.title
        self.item.desc = self.desc

        app = App.get_running_app()
        app.model.UpdateItem(self.item)

        self.manager.current = "master_list"
        self.manager.current_screen.load_screen()

    def on_press_delete(self):
        self.manager.current = "delete_warning"
        self.manager.current_screen.load_screen(self.id)

    def on_press_mark_complete(self):
        app = App.get_running_app()
        app.model.SetItemComplete(self.id)
        self.manager.current = "master_list"
        self.manager.current_screen.load_screen()


class DeleteWarningView(Screen):
    id = -1

    def load_screen(self, id):
        self.id = id

    def on_click_confirm(self):
        app = App.get_running_app()
        result = app.model.RemoveItem(self.id)

        self.manager.current = "master_list"
        self.manager.current_screen.load_screen()