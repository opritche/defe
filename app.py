from flask import Flask, render_template, request
from core import feedcore


app = Flask(__name__)


@app.route("/", methods=["GET"])
def feed():
    filter_feed = request.args.get("filter", default="*", type=str)
    data_keys = feedcore.read_data("general")
    data_keys = [item["name"] for item in data_keys]
    if filter_feed == "*":
        data = feedcore.all_feed(True)
        return render_template("general.html", allfeed=data, feeder_sites=data_keys)
    else:
        for item in feedcore.read_data("general"):
            if item["name"] == filter_feed:
                data = feedcore.feed(item["link"])
                return render_template(
                    "general.html",
                    allfeed=data,
                    filterfeed=filter_feed,
                    feeder_sites=data_keys,
                )


@app.route("/news", methods=["GET"])
def news_feed():
    filter_feed = request.args.get("filter", default="*", type=str)
    data_keys = feedcore.read_data("news")
    data_keys = [item["name"] for item in data_keys]
    if filter_feed == "*":
        data = feedcore.news_feed(True)
        return render_template("news.html", news_feed_data=data, feeder_sites=data_keys)
    else:
        for item in data_keys:
            if item["name"] == filter_feed:
                data = feedcore.feed(item["link"])
                return render_template(
                    "news.html",
                    news_feed_data=data,
                    feeder_sites=data_keys,
                    filterfeed=filter_feed,
                )


@app.route("/podcasts", methods=["GET"])
def podcast():
    filter_feed = request.args.get("filter", default="*", type=str)

    data_keys = feedcore.read_data("podcasts")
    data_keys = [item["name"] for item in data_keys]

    if filter_feed == "*":
        data = feedcore.podcasts_feeds(True)
        return render_template(
            "podcast.html", podcast_feed=data, feeder_sites=data_keys
        )
    else:
        for item in data_keys:
            if item["name"] == filter_feed:
                data = feedcore.feed(item["link"])
                return render_template(
                    "podcast.html",
                    podcast_feed=data,
                    feeder_sites=data_keys,
                    filterfeed=filter_feed,
                )


@app.route("/newsletters", methods=["GET"])
def newsletter():
    filter_feed = request.args.get("filter", default="*", type=str)

    data_keys = feedcore.read_data("newsletters")
    data_keys = [item["name"] for item in data_keys]

    if filter_feed == "*":
        data = feedcore.newsletters_feeds(True)
        return render_template(
            "newsletter.html", newsletter_feed=data, feeder_sites=data_keys
        )
    else:
        for item in data_keys:
            if item["name"] == filter_feed:
                data = feedcore.feed(item["link"])
                return render_template(
                    "newsletter.html",
                    newsletter_feed=data,
                    feeder_sites=data_keys,
                    filterfeed=filter_feed,
                )


@app.route("/feeders")
def feeder_sites_info():
    feed_sites = feedcore.read_data("general")
    news_sites = feedcore.read_data("news")
    podcasts_sites = feedcore.read_data("podcasts")
    newsletter_feeds = feedcore.read_data("newsletters")
    return render_template(
        "feeders.html",
        feed_sites=feed_sites,
        news_sites=news_sites,
        podcasts_sites=podcasts_sites,
        newsletter_feeds=newsletter_feeds,
        total=len(feed_sites)
        + len(podcasts_sites)
        + len(newsletter_feeds)
        + len(news_sites),
    )


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/support")
def support():
    return render_template("support.html")


@app.route("/feedback")
def feedback():
    return render_template("feedback.html")


if __name__ == "__main__":
    app.run()
