from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.properties import ColorProperty
from kivy.utils import get_color_from_hex as hex
from kivy.clock import Clock


background_color_normal = '#F2F2F2'
background_color_clicked = "#AAAAAA"

class ToDoItemView(BoxLayout):
    title = StringProperty("<title_placeholder>")
    completed = StringProperty("<completed_placeholder>")    
    completed_ind_color = ColorProperty(hex("#DD9292"))
    id = NumericProperty(-1)

    '''
    ************************************************************************************************************
    Code to make ToDoItem clickable (so the user can click on an item to open it)
    ************************************************************************************************************
    '''
    # Define a custom color property for visual feedback
    background_color = ColorProperty(hex(background_color_normal))

    # 2. Add custom events/properties
    # Define a custom event that will be triggered when the box is clicked
    # The 'on_press' and 'on_release' events are now available in KV
    __events__ = ('on_press', 'on_release')

    def on_press(self, *args):
        # This event is dispatched and can be bound to in KV
        pass

    def on_release(self, *args):
        # This event is dispatched and can be bound to in KV
        pass

    def on_touch_down(self, touch):
        # Check if the touch position is inside the widget
        if self.collide_point(*touch.pos):
            # Record that this touch event originated on this widget
            touch.grab(self)
            
            # Change color immediately for visual feedback
            self.background_color = hex(background_color_clicked)
            
            # Dispatch the custom 'on_press' event
            self.dispatch('on_press')
            
            # Block further touch processing by other widgets below it
            return True
        
        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            # Release the touch grab
            touch.ungrab(self)
            
            # Change color back after a slight delay
            Clock.schedule_once(self.reset_color, 0.1)
            
            # Dispatch the custom 'on_release' event
            self.dispatch('on_release')
            
            return True
        return super().on_touch_up(touch)

    def reset_color(self, dt):
        # Reset the color back to the original blue/gray theme
        self.background_color = background_color_normal

    def on_click_edit(self):
        print(self.id)

