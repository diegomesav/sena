const momgoose = require('mongoose');

const UserScheme = new momgoose.Schema(
    {
        id:{
            type: Number
        },
        firstName:{
            type: String
        },
        lastName:{
            type: String
        },
        address:{
            type: Number
        },
        phone:{
            type: Number
        },
        city:{
            type: String
        },
        email:{
            type: String
        }

    }
)

module.exports = momgoose.model('shippingAddress',UserScheme)