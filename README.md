# Movie Picker 🎬

A Python application that randomly selects movies from IMDb's Top 250 list to help you decide what to watch next.

## Features

- 🎲 **Random Selection**: Get a random movie suggestion from IMDb's Top 250 movies
- 📊 **Detailed Information**: View movie title, release year, IMDb rating, and starring actors
- 🔄 **Multiple Suggestions**: Keep getting new suggestions until you find something you like
- 🌐 **Real-time Data**: Fetches the latest IMDb Top 250 list

## Prerequisites

- Python 3.6 or higher
- Internet connection (required to fetch movie data from IMDb)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/robertisaacs-hash/moviepicker.git
   cd moviepicker
   ```

2. Install the required dependencies:
   ```bash
   pip install requests beautifulsoup4
   ```

## Usage

Run the application from the command line:

```bash
python main.py
```

The application will:
1. Fetch the current IMDb Top 250 movies list
2. Display a randomly selected movie with details including:
   - Movie title
   - Release year
   - IMDb rating
   - Main starring actors
3. Ask if you want another suggestion
4. Continue until you type anything other than 'y'

### Example Output

```
The Shawshank Redemption (1994), Rating: 9.3, Starring: Frank Darabont (dir.), Tim Robbins, Morgan Freeman
Do you want another movie (y/[n])? y

The Godfather (1972), Rating: 9.2, Starring: Francis Ford Coppola (dir.), Marlon Brando, Al Pacino
Do you want another movie (y/[n])? n
```

## Dependencies

- **requests**: For making HTTP requests to IMDb
- **beautifulsoup4**: For parsing HTML content from the IMDb page

## How It Works

1. **Web Scraping**: The application sends a GET request to IMDb's Top 250 movies page
2. **HTML Parsing**: Uses BeautifulSoup to extract movie information from the HTML
3. **Data Extraction**: Parses movie titles, years, ratings, and cast information
4. **Random Selection**: Uses Python's `random` module to select movies randomly
5. **Interactive Loop**: Continues suggesting movies until the user chooses to exit

## Code Structure

- `main.py`: Main application file containing all functionality
- `get_year()`: Helper function to extract release year from movie data
- Web scraping logic using CSS selectors to target specific HTML elements

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Future Enhancements

- [ ] Add genre filtering options
- [ ] Include movie plot summaries
- [ ] Add support for different movie lists (e.g., Top movies by decade)
- [ ] Create a GUI interface
- [ ] Add movie trailer links
- [ ] Implement user ratings and watchlist functionality

## Disclaimer

This application scrapes data from IMDb for educational purposes. Please be respectful of IMDb's terms of service and consider implementing appropriate rate limiting for production use.

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

**Robert Isaacs** - [GitHub Profile](https://github.com/robertisaacs-hash)

---

*Happy movie watching! 🍿*