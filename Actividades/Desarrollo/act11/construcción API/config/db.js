const mongoose = require('mongoose')

const DB_URI = 'mongodb+srv://crud_api:123654789@cluster0.9dukunj.mongodb.net/'

module.exports = () => {
    const connectDB = async () => {
        try {
            mongoose.set('strictQuery', false)
            mongoose.connect(DB_URI) 
            console.log('Mongo connected')
        } catch(error) {
            console.log(error)
            process.exit()
        }
    }

    connectDB();
}