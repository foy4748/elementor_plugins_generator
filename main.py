from templates import headings
from caseconverter import snakecase

THEME_NAME = 'saaslar'
LANG_DOMAIN = 'saaslar'
SECTION_NAME = input('Enter Section Name: \n')

print(headings.txt.format(
    section_name=snakecase(SECTION_NAME),
    section_name_u=SECTION_NAME,
    lang_domain=LANG_DOMAIN,
    theme_name=THEME_NAME,
    section_title_default="Fart",
    section_subtitle_default="Smelly"
))
