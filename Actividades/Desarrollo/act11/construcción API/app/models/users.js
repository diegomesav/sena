const momgoose = require('mongoose');

const UserScheme = new momgoose.Schema(
    {
        name:{
            type: String
        },
        avatar:{
            type:String,
            default: 'http://img.com'
        },
        email:{
            type:String,
            unique: true,
            require: true
        }
    }
)

module.exports = momgoose.model('users',UserScheme)