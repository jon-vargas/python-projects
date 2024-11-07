from controllers.app_controller import AppController
from views.app_view import create_main_window

def main():
    # Initialize the main window and display area with the controller
    controller = AppController(None)  # Temporarily set display_area to None
    window, display_area = create_main_window(controller)
    
    # Update the controller with the display area after it's created
    controller.display_area = display_area
    
    # Run the main Tkinter loop
    window.mainloop()

if __name__ == "__main__":
    main()
