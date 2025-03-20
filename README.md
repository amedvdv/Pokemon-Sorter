# Pokemon-Sorter

Project Summary
  This project aims to create a comprehensive Pokémon Trading Card Game (TCG) database by extracting detailed card information, including stats, moves, damage, HP, weaknesses, and abilities. Additionally, the project      analyzes and compares card values to help collectors and traders assess price trends and market fluctuations. Using Python, we developed a web scraper with BeautifulSoup and requests to gather structured data from     
  online sources, storing it in JSON and CSV formats for easy retrieval, analysis, and integration.

Sort Pokemon card value in following fashion:
  - Oldest Card to Newest Card
  - Highest Value to Lowest Value
  - Highest old card value to lowest old card value [1996 - 2009]
    - Same for Newer releases [2010 - Present Date]
  - Highest value card of a certain pokemon to lowest value of said pokemon.

Tech Stack & Tools Used
 - Python – Core programming language
 - Flask – Web framework for API and user interface (optional for data serving)
 - BeautifulSoup – Web scraping tool to parse HTML content
 - Requests – HTTP library for fetching webpage data
 - Pandas – Data processing and transformation into structured formats (CSV, JSON)
 - Matplotlib/Seaborn – Data visualization for price trends and comparisons
 - Git & GitHub – Version control and project collaboration
   
Key Features
 - Scrapes Pokémon TCG card details, including attack power, type, evolution, and rarity.
 - Tracks and compares Pokémon card values by integrating market price data from external sources.
 - Stores data efficiently in JSON and CSV formats for easy analysis.
 - Implements robust error handling and request management to ensure efficient and reliable data collection.
 - Future expansion includes integrating a web-based search and filter functionality using Flask and providing price history visualization.

This project serves as a valuable tool for Pokémon TCG collectors, traders, and data analysts, offering a structured and easily accessible Pokémon card database while enabling price trend analysis and market value comparisons.
