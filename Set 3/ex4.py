# 4. Fie functia build_xml_element care primeste urmatorii parametri:
# tag, content si elemente cheie-valoare date ca parametri cu nume. Sa se
# construiasca si sa se returneze un string care reprezinta elementul
# XML aferent.
# Exemplu: build_xml_element("a", "Hello there", href="http://python.org",
# class_="my-link", id="someid")
# => '<a href="http://python.org" class="my-link" id="someid">Hello there</a>'

def build_xml_element(tag: str, content: str, **attributes) -> str:
    """Build an XML element string from a tag, its content and its attributes."""
    parts = []
    for key, value in attributes.items():
        # Allows using names like "class_" for attributes that clash with
        # Python keywords (e.g. "class").
        attr_name = key[:-1] if key.endswith('_') else key
        parts.append(f'{attr_name}="{value}"')

    attrs_str = (' ' + ' '.join(parts)) if parts else ''
    return f'<{tag}{attrs_str}>{content}</{tag}>'


print('\n Exercise 4')
result = build_xml_element("a", "Hello there", href="http://python.org", class_="my-link", id="someid")
print(f' {result}')