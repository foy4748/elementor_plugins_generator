from templates import headings, paragraphs, images
from caseconverter import snakecase
#--------------------------------------------------

# Mostly Constant
THEME_NAME = 'saaslar_it'
LANG_DOMAIN = 'saaslar'
THEME_IMG_DIR_NAME = 'SAAS_THEME_IMG_DIR'
#--------------------------------------------------

# Selecting Widget Controler Type
# And Section Name
WIDGET_TYPES = ['headings','paragraphs','images']

# Printing all possible options
for idx,itm in enumerate(WIDGET_TYPES):
    print(f'({idx}) {itm}')

SELECTED_WIDGET_TYPE  = input("\nWidget Type ? :")
SECTION_NAME = input('Enter Section Name (in Title Case): \n')
#--------------------------------------------------


match WIDGET_TYPES[int(SELECTED_WIDGET_TYPE)]:
    case "headings": 
        SECTION_TITLE_DEFAULT= input('Default Title')
        SECTION_SUBTITLE_DEFAULT= input('Default SubTitle')
        print(headings.txt.format(
            section_name=snakecase(SECTION_NAME),
            section_name_u=SECTION_NAME,
            lang_domain=LANG_DOMAIN,
            theme_name=THEME_NAME,
            section_title_default=SECTION_TITLE_DEFAULT,
            section_subtitle_default=SECTION_SUBTITLE_DEFAULT
        ))
        pass
    case "paragraphs":
        SECTION_CONTENT_DEFAULT = input('Default Paragraph: ')
        print(paragraphs.txt.format(
            section_name=snakecase(SECTION_NAME),
            section_name_u=SECTION_NAME,
            lang_domain=LANG_DOMAIN,
            theme_name=THEME_NAME,
            section_content_default=SECTION_CONTENT_DEFAULT
        ))
        pass
    case "images":
        IMG_FILENAME = input('Enter IMG filename: \n')
        print(images.txt.format(
            section_name=snakecase(SECTION_NAME),
            section_name_u=SECTION_NAME,
            lang_domain=LANG_DOMAIN,
            theme_name=THEME_NAME,
            theme_img_dir_variable=THEME_IMG_DIR_NAME,
            img_filename=IMG_FILENAME
        ))
        pass

