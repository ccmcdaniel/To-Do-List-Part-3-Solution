import kivy
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from controllers.controllers import *
from widgets.widgets import *
from models.to_do_model import ToDoModel

Builder.load_file("views/master_list_view.kv")
Builder.load_file("views/master_list_empty_view.kv")
Builder.load_file("views/add_new_task_view.kv")
Builder.load_file("views/edit_task_view.kv")
Builder.load_file("views/delete_warning_view.kv")
Builder.load_file("views/screen_manager.kv")
Builder.load_file("widgets/ToDoItemView.kv")
Builder.load_file("style.kv")

window_scale = 1
Window.size = (412 * window_scale, 917 * window_scale)

class ToDoScreenManager(ScreenManager):
    pass

class ToDoApp(App):
    model = ToDoModel()

    def build(self):
        #self.model.GenerateTestData()
        self.sm = ToDoScreenManager()
        self.sm.current_screen.load_screen() # initiate the first screen.
        return self.sm
    
if __name__ == "__main__":
    app = ToDoApp()
    app.run()
