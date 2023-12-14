const momgoose = require('mongoose');

const UserScheme = new momgoose.Schema(
    {
        name:{
            type: String
        },
        avatar:{
            type:String,
            default: 'img.com'
        },
        email:{
            type:String,
            unique: true,
            required: true
        }

    }
)

module.exports = momgoose.model('users',UserScheme)