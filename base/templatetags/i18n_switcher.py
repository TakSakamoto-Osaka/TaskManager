from django import template
from django.template.defaultfilters import stringfilter
from config import settings
 

def switch_lang_code(path, language):
 
    # Get the supported language codes
    lang_codes = [code for code, name in settings.LANGUAGES]
 
    # Validate the inputs
    if path == '':
        raise Exception('URL path for language switch is empty')
    elif path[0] != '/':
        raise Exception('URL path for language switch does not start with "/"')
    elif language not in lang_codes:
        raise Exception('%s is not a supported language code' % language)
 
    # Split the parts of the path
    parts = path.split('/')
 
    # Add or substitute the new language prefix
    if parts[1] in lang_codes:
        parts[1] = language
    else:
        parts[0] = "/" + language
 
    # Return the full new path
    return '/'.join(parts)

 
register = template.Library()
 
@register.filter
@stringfilter
def switch_i18n_prefix(path, language):
    """文字列パスを受け取る"""
    return switch_lang_code(path, language)
 
@register.filter
def switch_i18n(request, language):
    """リクエストオブジェクトを受け取り、そこからパスを取得"""
    return switch_lang_code(request.get_full_path(), language)

