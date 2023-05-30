const express = require('express')
const app = express()
const booksRouter = require('./routes/books')
const ratingsRouter = require('./routes/ratings')

app.use(express.urlencoded({ extened=true }))
app.use(express.json())
app.use('/books', booksRouter)
app.use('/ratings', ratingsRouter)

app.get('/', (req, res) => {
    res.render('home', { books })
})

app.listen(3000, () => {
    console.log('Express app running')
})