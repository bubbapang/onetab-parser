import re

def parse_urls(file_path):
    youtube_urls = set()
    other_urls = set()

    with open(file_path, 'r') as file:
        for line in file:
            # Splitting line into potential URL segments
            parts = line.split()
            for part in parts:
                # Extracting URL from each segment
                match = re.search(r'(https?://[^\s]+)', part)
                if match:
                    url = match.group().rstrip('|,:;.')
                    if "youtube.com" in url:
                        youtube_urls.add(url)
                    else:
                        other_urls.add(url)

    # Writing the parsed URLs to separate files
    with open('youtube_urls.txt', 'w') as y_file:
        for url in youtube_urls:
            y_file.write(url + '\n')

    with open('other_urls.txt', 'w') as o_file:
        for url in other_urls:
            o_file.write(url + '\n')

    print(f"URLs parsed and saved to 'youtube_urls.txt' and 'other_urls.txt'.\nUnique YouTube URLs: {len(youtube_urls)}\nUnique Other URLs: {len(other_urls)}")

# Example usage
file_path = 'input.txt'
parse_urls(file_path)
