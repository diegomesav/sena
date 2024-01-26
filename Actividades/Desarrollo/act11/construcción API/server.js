const express = require('express');
const initDB = require('./config/db');
const bodyParser = require('body-parser');
const app = express();

const port = 3001

/*
app.get('/',(req,res) => {
    res.send({
        data:'Hola mundo, esto'
    });
});
*/

const userRouters = require('./app/routes/users')
const itemRouters = require('./app/routes/items')
const userLoginRouters = require('./app/routes/usersLogin')


app.use(userRouters);
app.use(itemRouters);
app.use(userLoginRouters);
//app.use(express.json())
//para formato json
app.use(
    bodyParser.json({
        limit: '20mb'
    })
)
//para url codificada
app.use(
    bodyParser.urlencoded({
        limit: '20mb',
        extended: true
    })
)


app.listen(port, () => {
    console.log('La aplicacion esta en linea');
});

initDB();