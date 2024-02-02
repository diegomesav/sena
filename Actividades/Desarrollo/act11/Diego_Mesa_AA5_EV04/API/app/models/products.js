const momgoose = require('mongoose');

const UserScheme = new momgoose.Schema(
    {
        id:{
            type: Number
        },
        nameProduct:{
            type: String
        },
        productType:{
            type: String
        },
        price:{
            type: Number
        },
        ratin:{
            type: Number
        },
        image:{
            type: String
        },
        description:{
            type: String
        }

    }
)

module.exports = momgoose.model('products',UserScheme)