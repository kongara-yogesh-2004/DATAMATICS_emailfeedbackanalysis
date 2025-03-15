import re
def remove_html_tags(html_content):
    clean_text = re.sub('<[^<]+?>',' ', html_content)
    return clean_text
