const express = require('express');

const controller = require('../controllers/users');

const router = express.Router();

const path = 'users';

router.get(
    `/${path}`,
    controller.getData
);

router.post(`/${path}`,
/*(req,res) =>{
    console.log('body recibido',req.body);
    res.send()
}*/
    controller.insertData
)

module.exports = router;
