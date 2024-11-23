from bs4 import BeautifulSoup

# Example HTML content
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Example Page</title>
</head>
<body>
    <h1>Welcome to the Example Page</h1>
    <p class="intro">This is an introduction paragraph.</p>
    <p class="info">Here is some information.</p>
    <a href="https://example.com/page1">Link to Page 1</a>
    <a href="https://example.com/page2">Link to Page 2</a>
</body>
</html>
"""

# Parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Use find_all to get all paragraph (<p>) tags
paragraphs = soup.find_all("p")
print("All paragraph tags:")
for p in paragraphs:
    print(p.text)

# Use find_all to get all anchor (<a>) tags
links = soup.find_all("a")
print("\nAll links:")
for link in links:
    print(f"Text: {link.text}, URL: {link['href']}")

# Use find_all with a class filter
intro_paragraphs = soup.find_all("p", class_="intro")
print("\nParagraphs with class 'intro':")
for intro in intro_paragraphs:
    print(intro.text)
