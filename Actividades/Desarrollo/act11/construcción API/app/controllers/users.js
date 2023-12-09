const model = require('../models/users')

exports.getData = (req,res) => {
    //res.send({data:'Esto viene desde USER'})
    model.find().then((docs) => {
        res.send({
            docs:docs
        })
    })
}

exports.insertData = (req, res) => {
    const data = req.body
    model.create(data)
    .then(() => {
      res.send(
        console.log('resultado')
      )
    })
    .catch((err) => {
      res.send()
    })
}