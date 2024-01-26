const mongoose = require('mongoose')

//const DB_URI = 'mongodb+srv://crud_api:123654789@cluster0.9dukunj.mongodb.net/' //solo funciona con el DNS de google
const DB_URI = 'mongodb://127.0.0.1:27017/crud_api'


module.exports = () => {
    const connectDB = async () => {
        try {
            mongoose.set('strictQuery', false)
            mongoose.connect(DB_URI),{
            socketTimeoutMS: 45000,
            keepAlive: true,
            reconnectTries: 10}
            console.log('Mongo connected')
        } catch(error) {
            console.log(error)
            process.exit()
        }
    }

    connectDB();
}