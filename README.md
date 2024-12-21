# ESPN API Parser
With a long term goal as a data pipeline for NBA, MLB, and NFL analytics application, this library is focused on building a pipeline to request data from API endpoints. The goal is to build a production application workflow on AWS

The current list of endpoints is [here](https://gist.github.com/nntrn/ee26cb2a0716de0947a0a4e9a157bc1c)

A brief description of files is below
* `Dash.ipynb` A dashboard I was originally hoping to host in python. The more I research, the more I realize what an incredibly awful idea hosting a client facing app on a server is. This should be archived for on-prem ussage, perhaps something to be packaged for client-machine use at a later date. Very badly done as is
* `drive.py`: intended to be a driver script for testing; will import and run functions of interest. Highly unstable, not to be included in prod
* `get_games_workflow.py`: this should be removed ASAP, there is good work on getting team boxscores as well as regex matching on text from scoring plays; definitely clutter, ultimately. Cannot find any references to this code
* `notes.md`: these notes are on json responses. They are to be updated continuosly and moved into an appropriate location when development matures
* `parseESPN.py`: this file is intended to house methods for parsing requests from the ESPN API. The goal is to fulfill a single-responsibility requirement for a microservice architecture. This will help when moving the app to AWS for prod
* `player_id.csv`: a csv of player ids. Used in `v0.py`
* `reqESPN.py`: this file is intended to make HTTP requests to the ESPN API endpoints. This library will need to remain clean to fulfill a single-responsibility requirement
* `team_id.csv`: a csv of team ids
* `tst.py`: same purpose as `drive.py`
* `v0.py`: a file designed to imitate the desired prod workflow. This could be considered a lazy man's DEV branch, whereas `tst.py` & `drive.py` are lazy TEST branches