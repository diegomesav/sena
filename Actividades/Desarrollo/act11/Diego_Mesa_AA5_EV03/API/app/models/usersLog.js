const momgoose = require('mongoose');

const UserScheme = new momgoose.Schema(
    {
        firstName:{
            type: String
        },
        email:{
            type:String,
            unique: true,
            required: true
        },
        password:{
            type:String
        }
    }
)

module.exports = momgoose.model('users',UserScheme)