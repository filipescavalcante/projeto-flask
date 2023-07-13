const addItemBtn = document.querySelector('#add-item')
const submitBtn = document.querySelector('#submit')
const closeBtn = document.querySelector('#close')

const form = document.querySelector('form')
const addItemText = document.querySelector('p')
const inputs = [...document.querySelectorAll('input[type="text"]')]

addItemBtn.addEventListener('click', () => {
    form.style.display = 'flex'
    addItemText.style.display = 'none'
})

closeBtn.addEventListener('click', () => {
    form.style.display = 'none'
    addItemText.style.display = 'block'

    form.reset()
    }
)

submitBtn.addEventListener('click', (e) => {
    form.submit()
    e.preventDefault()
})