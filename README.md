# Twitter-Scrap-IoT-Platform
Script to scrap and analyze (LDA analysis) twitter data on industrial IoT platforms

1. Step
The used approach is totally relying on the **twitterscraper script, provided by taspinar**: https://github.com/taspinar/twitterscraper

Please use the following command in your **CLI** to get the data in the same format, as we did:

```
pip install twitterscraper
twitterscraper #PlatformName --lang en -bd 2015-01-01 -p 100 --csv --output=PlatformName.csv
```
