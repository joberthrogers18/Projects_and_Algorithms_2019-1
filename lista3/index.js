const express = require('express');
const app = express();
const PORT = 3003;
const routes = require('./routes');

app.use(routes);

app.listen(PORT, () => {
    console.log('The server is on');
});

