const express = require('express');

const controller = require('../controllers/usersLogin');
//ChatGPT
const bodyParser = require('body-parser');

const router = express.Router();

const path = 'create_account';
//ChatGPT
router.use(bodyParser.json())


router.post(`/${path}`,
    controller.insertData
);

router.post(`/login`,
    controller.login
)

module.exports = router;
