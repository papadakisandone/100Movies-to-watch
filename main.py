from bs4 import BeautifulSoup
import requests

url = "https://stacker.com/stories/1587/100-best-movies-all-time"

responce = requests.get(url)
website_html = responce.text

soup = BeautifulSoup(website_html, "html.parser")
all_titles = [line.getText().split("\n")[1].split(".") for line in
              soup.find_all(name="h2", class_="ct-slideshow__slide__text-container__caption")]
# print(all_titles)

print(f"{''.join(all_titles[0])}\n")  # list to string
titlos = [all_titles[title][1] for title in range(len(all_titles)) if title > 0]
order = [all_titles[title][0] for title in range(len(all_titles)) if title > 0]

# reverse lists
titlos.reverse()
order.reverse()

movies = [f"{order[name].split('#')[1]} {titlos[name]}" for name in range(len(titlos))]
print(movies)
with open("movies.txt", "w") as f:
    [f.write(line+"\n") for line in movies]
