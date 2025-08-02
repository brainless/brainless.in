import os
import re
from bs4 import BeautifulSoup
from datetime import datetime
from markdownify import markdownify as md

# Path to the Atom feed file
feed_file = 'Takeout/Blogger/Blogs/Being brainless!/feed.atom'

# Output directory
markdown_dir = 'posts'

# Create the output directory if it doesn't exist
os.makedirs(markdown_dir, exist_ok=True)

# Read the Atom feed file
with open(feed_file, 'r', encoding='utf-8') as f:
    feed_content = f.read()

# Parse the Atom feed using BeautifulSoup
soup = BeautifulSoup(feed_content, 'xml')

# Iterate over each entry
for entry in soup.find_all('entry'):
    # Extract title
    title = entry.title.text
    filename = re.sub(r'\W+', '-', title.lower()).strip('-')

    # Extract content
    content = entry.content.text if entry.content else ''

    # Convert HTML content to Markdown
    markdown_content = md(content)

    # Extract and format the published date
    published = entry.published.text
    published_date = datetime.strptime(published, '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d')

    # Create the Markdown file content
    markdown_file_content = f"""---
title: "{title}"
date: {published_date}
---

{markdown_content}
"""

    # Write to a Markdown file
    with open(os.path.join(markdown_dir, f'{filename}.md'), 'w', encoding='utf-8') as markdown_file:
        markdown_file.write(markdown_file_content)

print('Conversion to Markdown complete! Files saved in posts directory.')
