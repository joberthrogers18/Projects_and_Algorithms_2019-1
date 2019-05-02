const express = require('express');
const router = express.Router();
const Partition = require('./intervalPartition');

router.get('/intervalPartition', Partition.intervalPartition);

module.exports = router;