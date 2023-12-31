from templates import headings, paragraphs, images, repeaters, colors
from caseconverter import snakecase
#--------------------------------------------------

# Mostly Constant
THEME_NAME = 'saaslar_it'
LANG_DOMAIN = 'saaslar'
THEME_IMG_DIR_NAME = 'SAAS_THEME_IMG_DIR'
#--------------------------------------------------

# Selecting Widget Controler Type
# And Section Name
WIDGET_TYPES = ['headings','paragraphs','images','icon_repeater', 'colors']

# Printing all possible options
for idx,itm in enumerate(WIDGET_TYPES):
    print(f'({idx}) {itm}')

SELECTED_WIDGET_TYPE  = input("\nWidget Type ? :")
SECTION_NAME = input('Enter Section Name (in Title Case): \n')
#--------------------------------------------------

def writeToFile(txt):
    with open('./output.txt','a',encoding='utf-8') as file:
        file.write(txt)

match WIDGET_TYPES[int(SELECTED_WIDGET_TYPE)]:
    case "headings": 
        SECTION_TITLE_DEFAULT= input('Default Title: \n')
        SECTION_SUBTITLE_DEFAULT= input('Default SubTitle: \n')
        output = headings.txt.format(
            section_name=snakecase(SECTION_NAME),
            section_name_u=SECTION_NAME,
            lang_domain=LANG_DOMAIN,
            theme_name=THEME_NAME,
            section_title_default=SECTION_TITLE_DEFAULT,
            section_subtitle_default=SECTION_SUBTITLE_DEFAULT
        )
        writeToFile(output)
        pass
    case "paragraphs":
        SECTION_CONTENT_DEFAULT = input('Default Paragraph: \n')
        output = paragraphs.txt.format(
            section_name=snakecase(SECTION_NAME),
            section_name_u=SECTION_NAME,
            lang_domain=LANG_DOMAIN,
            theme_name=THEME_NAME,
            section_content_default=SECTION_CONTENT_DEFAULT
        )
        writeToFile(output)
        pass
    case "images":
        IMG_FILENAME = input('Enter IMG filename: \n')
        output = images.txt.format(
            section_name=snakecase(SECTION_NAME),
            section_name_u=SECTION_NAME,
            lang_domain=LANG_DOMAIN,
            theme_name=THEME_NAME,
            theme_img_dir_variable=THEME_IMG_DIR_NAME,
            img_filename=IMG_FILENAME
        )
        writeToFile(output)
        pass
    case "icon_repeater":
        IMG_FILENAME = input('Enter IMG filename: \n')
        REPEATER_TITLE = input('Enter IMG title: \n')
        REPEATER_CONTENT =  input('Enter IMG content: \n')
        output = repeaters.txt.format(
            section_name=snakecase(SECTION_NAME),
            section_name_u=SECTION_NAME,
            lang_domain=LANG_DOMAIN,
            theme_name=THEME_NAME,
            theme_img_dir_variable=THEME_IMG_DIR_NAME,
            repeater_item_icon_default=IMG_FILENAME,
            repeater_item_title_default=REPEATER_TITLE,
            repeater_item_content_default=REPEATER_CONTENT
        )
        writeToFile(output)
        pass
    case "colors":
        CLASS_NAME = input('Enter Class Name: \n')
        output = colors.txt.format(
            section_name=snakecase(SECTION_NAME),
            section_name_u=SECTION_NAME,
            lang_domain=LANG_DOMAIN,
            theme_name=THEME_NAME,
            theme_img_dir_variable=THEME_IMG_DIR_NAME,
            class_name=CLASS_NAME
        )
        writeToFile(output)
        pass

