const addItemBtn = document.querySelector('#add-item')
const submitBtn = document.querySelector('#submit')
const closeBtn = document.querySelector('#close-form')
const updateBtn = document.querySelector('#update')

const main = document.querySelector('main')
const form = document.querySelector('form')
const updateForm = document.querySelector('#update-form')
const addItemText = document.querySelector('p')
const inputs = [...document.querySelectorAll('input[type="text"]')]
const table = document.querySelector('table')

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

submitBtn.addEventListener('click', () => {
    form.submit()
})

updateBtn.addEventListener('click', () => {
    updateForm.submit()
})