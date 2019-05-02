const express = require('express');
const router = express.Router();
const interPartition = require('./src/intervalPartition');
const interSchedule = require('./src/intervalSchedule');

router.get('/intervalPartition', interPartition.intervalPartition);
router.get('/intervalSchedule', interSchedule.intervalSchedule);

module.exports = router;