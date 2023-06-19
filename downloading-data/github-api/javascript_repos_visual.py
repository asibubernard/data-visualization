import requests
import plotly.express as px


def javascript_repos_visual():
    """Make visualization of Data collected from Github to know
    which Javascript projects are being stared."""
    # Make an API call and check the response.
    url = "https://api.github.com/search/repositories"
    url += "?q=language:javascript+sort:stars+stars:>10000"

    headers = {"Accept": "application/vnd.github.v3+json"}

    try:
        r = requests.get(url, headers=headers)
    except requests.exceptions.ConnectionError:
        print("No internet connection")
    else:
        print(f"Status code: {r.status_code}")

        # Process overall results.
        # Convert the response object to a dictionary.
        response_dict = r.json()
        print(f"Complete results: {response_dict['incomplete_results']}")

        # Process repository information
        repo_dicts = response_dict['items']
        repo_names, stars = [], []
        for repo_dict in repo_dicts:
            repo_names.append(repo_dict['name'])
            stars.append(repo_dict['stargazers_count'])

        # Make Visualization.
        title = "Most-Starred Javascript Projects on GitHub"
        labels = {'x': 'Repository', 'y': 'Stars'}
        fig = px.bar(x=repo_names, y=stars, title=title, labels=labels)
        fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)

        fig.show()


# Instantiate the function
javascript_repos_visual()
