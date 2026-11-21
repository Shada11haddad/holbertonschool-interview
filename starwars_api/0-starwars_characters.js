#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

const fetchJson = (targetUrl) => {
  return new Promise((resolve, reject) => {
    request(targetUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
};

const printCharacters = async () => {
  if (!movieId) {
    return;
  }
  try {
    const film = await fetchJson(url);
    const promises = film.characters.map((charUrl) => fetchJson(charUrl));
    const characters = await Promise.all(promises);
    characters.forEach((character) => {
      console.log(character.name);
    });
  } catch (err) {
    console.error(err);
  }
};

printCharacters();
