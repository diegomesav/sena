const express = require('express');

const controller = require('../controllers/users');
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
    controller.insertData
);

router.put(`/${path}/:id`,
    controller.updatedItem
);

router.delete(`/${path}/:id`,
    controller.deleteUser
)



module.exports = router;
