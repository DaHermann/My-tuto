```
const mongoose = require('mongoose');
const uri = "mongodb+srv://user:Paswword@url/dbname";

const connectToDB = async () => {
    try {
        await mongoose.connect(uri, {
            autoIndex: true
        })
        console.log('Connected to Mongodb');
    } catch (error) {
        console.error(error);
    }
}
connectToDB();
```
