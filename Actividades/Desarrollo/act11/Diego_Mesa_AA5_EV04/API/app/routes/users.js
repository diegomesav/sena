const express = require('express');

const controller = require('../controllers/users');
const controllerLog = require('../controllers/usersLogin');
//ChatGPT
const bodyParser = require('body-parser');

const router = express.Router();

const path = 'users';
//ChatGPT
router.use(bodyParser.json())

router.get(
    `/${path}`,
    controller.getData
);
router.get(
    `/${path}/:id`,
    controller.getSomeData
);

router.post(`/${path}`,
    controllerLog.insertData
);

router.put(`/${path}/:id`,
    controller.updatedItem
);

router.delete(`/${path}/:id`,
    controller.deleteUser
)

router.post(`/${path}/login`,
    controllerLog.login
)

module.exports = router;
