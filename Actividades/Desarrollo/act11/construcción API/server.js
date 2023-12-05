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

app.use(userRouters);
app.use(itemRouters);
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