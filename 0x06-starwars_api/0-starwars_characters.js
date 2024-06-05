#!/usr/bin/node

const request = require('request');

// Function to fetch data from a given URL
function fetch (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(
          new Error(`Failed to load page, status code: ${response.statusCode}`)
        );
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

// Function to fetch characters from a movie
async function fetchCharacters (movieId) {
  try {
    const movieUrl = `https://swapi.dev/api/films/${movieId}/`;
    const movieData = await fetch(movieUrl);

    const characterPromises = movieData.characters.map((url) => fetch(url));
    const characters = await Promise.all(characterPromises);

    characters.forEach((character) => {
      console.log(character.name);
    });
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

// Check if a movie ID was provided
if (process.argv.length < 3) {
  console.error('Please provide a movie ID.');
  process.exit(1);
}

const movieId = process.argv[2];
if (isNaN(movieId)) {
  console.error('Movie ID must be a number.');
  process.exit(1);
}

// Fetch and print the characters
fetchCharacters(movieId);
