import webbrowser

def open_youtube():
    """Opens youtube in the default browser."""
    url = "https://www.youtube.com"
    webbrowser.open(url)

def open_url(url):
    webbrowser.open(url)

def search(query, site):
    if site == "youtube":
        url = "https://www.youtube.com/results?search_query=" + query
        open_url(url)

    elif site == "google":
        url = "https://www.google.com/search?q=" + query
        open_url(url)


# call the function
if __name__ == "__main__":
    search("flats in delhi", "google")
