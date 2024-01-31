const momgoose = require('mongoose');

const UserScheme = new momgoose.Schema(
    {
        firstName:{
            type: String
        },
        lastName:{
            type:String
        },
        email:{
            type:String,
            unique: true,
            required: true
        },
        lastName:{
            type:String
        }

    }
)

module.exports = momgoose.model('users',UserScheme)