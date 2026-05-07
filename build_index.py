import sys

content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Shanthi Wellness - Ancient Wisdom. Modern Healing.</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Raleway:wght@300;400;500;600;700&family=Lato:wght@300;400;700&display=swap" rel="stylesheet">
</head>
<body>
<p>placeholder</p>
</body>
</html>"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('done')
