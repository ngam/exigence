def read_lines_from_file(filename, strip=True):
    with open(filename, 'r') as fname:
        raw_lines = fname.readlines()
    return [line.strip() for line in raw_lines] if strip else raw_lines

def download_files_from_url(url, dest):
    import urllib
    import urllib.request
    urllib.request.urlretrieve(url, dest)

def download_files_from_url_batch(urls, dest_folder):
    import os
    if not os.path.exists(f"{dest_folder}"):
        os.makedirs(f"{dest_folder}", exist_ok=True)
    for url in urls:
        filename = url.split('/')[-1]
        download_files_from_url(url, os.path.join(dest_folder, filename))
