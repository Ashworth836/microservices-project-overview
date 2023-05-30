const express = require('express');
const router = express.Router();
const axios = require('axios');

// POST route for creating a rating
router.post('/', async (req, res) => {
  const { title, rating } = req.body;

  try {
    // Call the Flask microservice API to submit the rating
    const response = await axios.post('http://flask-microservice/title/user-ratings', {
      title,
      rating
    });

    // Logic to handle the response from the Flask microservice
    res.redirect(`/books/${title}`);
  } catch (error) {
    console.error('Error submitting rating:', error);
    res.status(500).send('Internal Server Error');
  }
});

module.exports = router;
