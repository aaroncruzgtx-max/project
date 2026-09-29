# Diamond Analytics: Baseball Stat Comparer & Rating Calculator
    #### Video Demo:  https://youtu.be/fQ0dTYX11BM
    #### Description: A way to quickly lookup a single or multiple MLB players, compare their stats, calculate an overall rating, and have that output displayed in a tabulated form.

## Features

- Uses pybaseball library
- Accepts multiple player names
- Returns statistics through a given date range
- Calculates percentile rankings for selected statistics
- Calculates a weighted batting rating
- Calculates a weighted pitching rating
- Displays results in table

## Files

### 'project.py'

Contains main program that retrieves, calculates and displays player statistics

### 'test_project.py'

Containts pytest tests for project's functions

### 'requirements.txt'

Lists Python Libraries requried to run this project

## Program Structure

### 'main()'

Houses the overall flow of the program.

Initializes by calling player_lookup(), user will be prompted to player names, those names will be stored in a list and the user is prompted if they want to add more players to the list

The function will then look up league statistics, calculate percentiles, iterate over the list of players, pulling their statistics and calculated percentiles, and then calculate an overall batting and pitching rating for those players

### 'playerlookup()'

This function prompts the user for a first and last name, stripping the input of whitespace and making it lowercase. The first and last names are then stored in separate variables.

Those variables are put into an f-string and stored as a player_name. The function then returns that player_name to main()

### 'league_stat_lookup()'

Prompts the user for a start and end date for the statistics date range they want to review

If the date format is not in YYYY-MM-DD, an exception will be raised and the user will be prompted to enter in the dates with the correct format

The function uses the following from the pybaseball library:

-'batting_stats_range()'
-'pitching_stats_range()'

These return the DataFrames containing league-wide batting and pitching statistics

This function also calculates percentile rankings for the statistics used by the rating system and adds them back into the DataFrame.

The DataFrames are then stored into a dictionary named league_stat_dict{}

### 'batting_calculation()'

This function iterates over the players stored in player_names[]

It will pull the DataFrame associated with the player name, if the data frame is empty, i.e a pitcher who does not have batting stats, the Overall Batting Rating will be automatically set to 0/100

Otherwise, if there is batting data, the function will store the following stats and their percentile rankings into a new dictionary called player_stat_dict{}

- OPS
- OBP
- SLG
- BA
- SB
- Overall Batting Rating

The Overall Batting Rating is calculated using a weighted formula. The weighted batting rating is as follows:

- OPS: 35%
- OBP: 25%
- SLG: 20%
- BA: 10%
- SB: 10%

### 'pitching_calculation()'

This function iterates over the players stored in player_names[]

It will pull the DataFrame associated with the player name, if the data frame is empty, i.e a batter who does not have pitching stats, the Overall Pitching Rating will be automatically set to 0/100

Otherwise, if there is pitching data, the function will store the following stats and their percentile rankings into a new dictionary called player_stat_dict{}

- ERA
- WHIP
- SO/9
- SO/W
- BABIP
- GB/FB
- Overall Pitching Rating

Percentile rankings are calculated differently depending on whether a higher or lower value represents better performance. For Example:

- Lower ERA is better
- Lower WHIP is better
- Higher SO/9 is better
- Higher SO/W is better

The Overall Pitching Rating is calculated using a weighted formula. The weighted pitching rating is as follows:

- ERA: 25%
- WHIP: 20%
- SO/9: 15%
- SO/W: 15%
- BABIP: 10%
- GB/FB: 10%

### 'display_table()'

Takes the statistics stored in player_stat_dict{} and prints them into a tabluated form using the 'tabulate' library.

## Installation

Required libraries include:

- pybaseball
- tabulate
- pandas

## Design Decisions

I designed the program using basic batting and pitching stats only, the popular Statcast statistics exist in another website using another function and a player_ID

I chose to pull the entire league wide statistics, and filter out the data based on the user input rather than looking up each player individually with 'batting_stats_range()' and 'pitching_stats_range()' That way, the lookup and percentile calculation would only have to be run once, rather than iterating the same functions over and over per player.

## Limitations

- Player names must match names found in Baseball Reference
- Overall Batting and Pitching Ratings are designed for this project and are not actual MLB Statistics
