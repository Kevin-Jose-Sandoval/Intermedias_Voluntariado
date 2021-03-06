const express = require('express');
const app = express();

app.use(express.json());

// routes
app.use(require('./routes/users'));

app.listen('4000', () => {
    console.log("Server running on port 4000")
});