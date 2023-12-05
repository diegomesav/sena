const express = require('express');

const controller = require('../controllers/users');

const router = express.Router();

const path = 'users';

router.get(
    `/${path}`,
    controller.getData
);

module.exports = router;
