import pygame
import pygame_gui

# Initialize PyGame
pygame.init()

# Setup the display
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Recipe Creator')

# Setup UI Manager
manager = pygame_gui.UIManager(window_size)

# Define colors
WHITE = (255, 255, 255)

# UI Components
def create_home_screen():
    """Create components for the home screen."""
    title = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(200, 50, 400, 50),
                                        text='Recipe Creator',
                                        manager=manager)
    button_filter = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(300, 150, 200, 50),
                                                 text='Filter Search',
                                                 manager=manager)
    button_recipe = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(300, 250, 200, 50),
                                                 text='Recipe Search',
                                                 manager=manager)
    return title, button_filter, button_recipe

title, button_filter, button_recipe = create_home_screen()

# Screen state
current_screen = 'home'
input_box = search_results = back_button = filter_title = recipe_title = items_text_box = None
save_button = None
item_list = []
delete_buttons = []
quantity_boxes = []
unit_dropdowns = []
ingredient_labels = []
checkboxes = []
selected_ingredients = []

def draw_filter_search_screen():
    global input_box, search_results, back_button, filter_title, items_text_box, current_screen, delete_buttons, quantity_boxes, unit_dropdowns, save_button
    title.hide()
    button_filter.hide()
    button_recipe.hide()

    filter_title = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(200, 50, 400, 50),
                                               text='List out your ingredients',
                                               manager=manager)
    back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(50, 550, 100, 40),
                                               text='Back',
                                               manager=manager)
    save_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(650, 550, 100, 40),
                                               text='Save',
                                               manager=manager)
    input_box = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(50, 100, 300, 50),
                                                    manager=manager)
    search_results = pygame_gui.elements.UIScrollingContainer(relative_rect=pygame.Rect(50, 160, 700, 380),
                                                              manager=manager)
    items_text_box = pygame_gui.elements.UITextBox(html_text='',
                                                   relative_rect=pygame.Rect(0, 0, 640, 370),
                                                   manager=manager,
                                                   container=search_results)
    input_box.focus()
    current_screen = 'filter_search'
    update_items_display()

def draw_recipe_search_screen():
    global back_button, recipe_title, checkboxes, search_results, current_screen, ingredient_labels
    title.hide()
    button_filter.hide()
    button_recipe.hide()

    recipe_title = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(200, 50, 400, 50),
                                               text='Select ingredients for your recipe',
                                               manager=manager)
    back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(50, 550, 100, 40),
                                               text='Back',
                                               manager=manager)
    search_results = pygame_gui.elements.UIScrollingContainer(relative_rect=pygame.Rect(50, 100, 700, 400),
                                                              manager=manager)
    checkboxes = []
    ingredient_labels = []

    y_offset = 0
    for idx, item in enumerate(item_list):
        checkbox = pygame_gui.elements.UISelectionList(relative_rect=pygame.Rect(10, 10 + y_offset, 200, 30),
                                                       item_list=[f'{item["name"]} ({item["quantity"]} {item["unit"]})'],
                                                       manager=manager,
                                                       container=search_results,
                                                       allow_multi_select=True,
                                                       object_id=f'checkbox_{idx}')
        checkboxes.append(checkbox)

        y_offset += 40  # Adjust y offset for next checkbox

    current_screen = 'recipe_search'

def update_items_display():
    global delete_buttons, quantity_boxes, unit_dropdowns
    items_text_box.html_text = ""
    items_text_box.rebuild()

    # Clear existing UI components
    for btn in delete_buttons:
        btn.kill()
    delete_buttons = []
    for box in quantity_boxes:
        box.kill()
    quantity_boxes = []
    for dropdown in unit_dropdowns:
        dropdown.kill()
    unit_dropdowns = []

    # Create new UI components for each ingredient
    y_offset = 0
    for idx, item in enumerate(item_list):
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect(10, 10 + y_offset, 200, 30),
                                    text=f'{item["name"]}',
                                    manager=manager,
                                    container=search_results)
        quantity_box = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(220, 10 + y_offset, 50, 30),
                                                           manager=manager,
                                                           container=search_results,
                                                           object_id=f'quantity_{idx}')
        quantity_box.set_text(str(item["quantity"]))
        quantity_boxes.append(quantity_box)

        unit_dropdown = pygame_gui.elements.UIDropDownMenu(options_list=["teaspoon", "tablespoon", "cup", "pint", "quart"],
                                                           starting_option=item["unit"],
                                                           relative_rect=pygame.Rect(280, 10 + y_offset, 100, 30),
                                                           manager=manager,
                                                           container=search_results,
                                                           object_id=f'unit_{idx}')
        unit_dropdowns.append(unit_dropdown)

        btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(390, 10 + y_offset, 50, 30),
                                           text='Del',
                                           manager=manager,
                                           container=search_results,
                                           object_id=f'delete_{idx}')
        delete_buttons.append(btn)
        y_offset += 40  # Adjust y offset for next button

    print(f"Updated items display: {item_list}")

def unfocus_all_text_entries():
    if input_box is not None:
        input_box.unfocus()
    for box in quantity_boxes:
        box.unfocus()

def handle_ui_events(event):
    global current_screen, item_list, selected_ingredients
    manager.process_events(event)

    if event.type == pygame.USEREVENT:
        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
            print(f"Button pressed: {event.ui_element}")  # Debug print
            if event.ui_element == button_filter:
                draw_filter_search_screen()
            elif event.ui_element == button_recipe:
                draw_recipe_search_screen()
            elif back_button and event.ui_element == back_button:
                title.show()
                button_filter.show()
                button_recipe.show()
                back_button.hide()
                if save_button:
                    save_button.hide()
                if input_box:
                    input_box.hide()
                if filter_title:
                    filter_title.hide()
                if search_results:
                    search_results.hide()
                if recipe_title:
                    recipe_title.hide()
                current_screen = 'home'
            elif save_button and event.ui_element == save_button:
                print("Save button clicked")
                title.show()
                button_filter.show()
                button_recipe.show()
                back_button.hide()
                save_button.hide()
                input_box.hide()
                filter_title.hide()
                search_results.hide()
                current_screen = 'home'
            else:
                for btn in delete_buttons:
                    if event.ui_element == btn:
                        print(f"Delete button {btn.object_id} clicked")  # Debug print
                        index = int(btn.object_id.split('_')[1])
                        item_list.pop(index)
                        update_items_display()
                        break
        elif event.user_type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
            for idx, box in enumerate(quantity_boxes):
                if event.ui_element == box:
                    try:
                        new_quantity = int(box.get_text())
                        item_list[idx]["quantity"] = new_quantity
                    except ValueError:
                        pass  # Handle non-integer input gracefully
        elif event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
            for idx, dropdown in enumerate(unit_dropdowns):
                if event.ui_element == dropdown:
                    item_list[idx]["unit"] = dropdown.selected_option
        elif event.user_type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION:
            for idx, checkbox in enumerate(checkboxes):
                if event.ui_element == checkbox:
                    if item_list[idx] not in selected_ingredients:
                        selected_ingredients.append(item_list[idx])
                    else:
                        selected_ingredients.remove(item_list[idx])
                    print(f"Selected ingredients: {selected_ingredients}")

    elif event.type == pygame.MOUSEBUTTONDOWN:
        # Ensure that clicking on a text entry box sets the focus
        clicked_on_box = False
        for box in quantity_boxes:
            if box.rect.collidepoint(event.pos):
                box.focus()
                clicked_on_box = True
                break
        if input_box and input_box.rect.collidepoint(event.pos):
            input_box.focus()
            clicked_on_box = True
        if not clicked_on_box:
            unfocus_all_text_entries()

    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN and current_screen == 'filter_search' and input_box.get_text():
            item_list.append({"name": input_box.get_text(), "quantity": 1, "unit": "teaspoon"})  # Default quantity and unit
            update_items_display()
            input_box.set_text('')


# Main loop
clock = pygame.time.Clock()
running = True

while running:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        handle_ui_events(event)

    manager.update(time_delta)

    screen.fill(WHITE)
    manager.draw_ui(screen)

    pygame.display.update()

pygame.quit()
#test