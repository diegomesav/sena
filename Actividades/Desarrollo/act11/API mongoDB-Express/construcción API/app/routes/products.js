const express = require('express');

const controller = require('../controllers/products');
//ChatGPT
const bodyParser = require('body-parser');

const router = express.Router();

const path = 'products';
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
);

module.exports = router;
