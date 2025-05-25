import fs from 'fs';
import path from 'path';
import axios from 'axios';

export default async function handler(req, res) {
  try {
    const filePath = path.resolve('media/image.json');
    const data = JSON.parse(fs.readFileSync(filePath));
    const url = data[Math.floor(Math.random() * data.length)];
    console.log('Fetching image from URL:', url);

    const response = await axios.get(url, {
      responseType: 'stream',
      headers: { 'User-Agent': 'Mozilla/5.0' }
    });

    const ext = url.split('.').pop().toLowerCase();
    const contentType = ext === 'png' ? 'image/png' : 'image/jpeg';
    res.setHeader('Content-Type', contentType);

    response.data.pipe(res);
  } catch (error) {
    console.error('Error fetching image:', error);
    res.status(500).json({ error: 'Failed to fetch image.', details: error.message });
  }
}
