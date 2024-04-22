import re 

def highlight_code(code):
    
    styles = {
        'keyword': 'color: #0000FF;',
        'operator': 'color: #8B0000;',
        'literal': 'color: #006400;',
        'comment': 'color: #808080;',
        'identifier': 'color: #FF00FF;',
        'string': 'color: #FF8C00;',
        'builtin': 'color: #800080;'
    }

    # Define the patterns with valid Python identifiers as names
    patterns = {
        'comment': (r'(\#.*?$)|(\'\'\'[\s\S]*?\'\'\')|(\"\"\"[\s\S]*?\"\"\")', styles['comment']),
        'string': (r'(\".*?\"|\'.*?\')', styles['string']),
        'keyword': (r"\b(if|else|for|while|class|break|continue|return|try|except|finally|with|as|import|from|def|lambda|nonlocal|global|assert|yield|raise|in|pass|self|None )\b", styles['keyword']),
        'builtin': (r"\b(print|len|range|SyntaxError|IndexError)\b", styles['builtin']),
        'operator': (r"(\+|\-|\*|\/|\%|\=|\=\=|\!\=|\<|\>|\<\=|\>\=|\&|\||\~|\^|\>\>|\<\<)", styles['operator']),
        'literal': (r'(\b\d+\b|\b\d+\.\d+\b|\bTrue\b|\bFalse\b)', styles['literal']),
        'identifier': (r"\b[a-zA-Z_][a-zA-Z0-9_]*\b", styles['identifier'])
    }


    # Create a combined regex pattern with proper named groups
    combined_pattern = '|'.join(f'(?P<{name}>{pattern})' for name, (pattern, _) in patterns.items())

    # Use the named groups in the style_replacer function
    def style_replacer(match):
        for name, style in styles.items():
            value = match.group(name)
            if value:
                return f'<span style="{style}">{value}</span>'
        return match.group(0)


    highlighted_code = re.sub(combined_pattern, style_replacer, code, flags=re.MULTILINE)
    return highlighted_code

# Read input Python code from a file
with open('input.txt', 'r') as file:
    code = file.read()

# Generate the highlighted HTML content
highlighted_code = highlight_code(code)

# HTML structure for output
html_output = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Syntax Highlighted Code</title>
</head>
<body>
<pre>{highlighted_code}</pre>
</body>
</html>
"""

# Save the highlighted code as HTML
with open('out.html', 'w') as file:
    file.write(html_output)
