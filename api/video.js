const fs = require('fs');
const axios = require('axios');
const path = require('path');

export default async function handler(req, res) {
  const data = JSON.parse(fs.readFileSync(path.resolve('media/video.json')));
  const url = data[Math.floor(Math.random() * data.length)];

  try {
    const response = await axios.get(url, { responseType: 'stream' });
    res.setHeader('Content-Type', 'video/mp4');
    response.data.pipe(res);
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch video.' });
  }
}
