from redvid import Downloader

reddit = Downloader(max_q=True)
reddit.url = 'https://www.reddit.com/r/Whatcouldgowrong/comments/iaf07q/put_an_electric_cable_behind_the_grapes/'
reddit.download()

